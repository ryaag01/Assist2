# app/main.py
import uvicorn
from fastapi import FastAPI, WebSocket, BackgroundTasks
from pydantic import BaseModel
from app.admin_ai import AdminAI
from app.auth import router as auth_router
from app.admin_panel import router as admin_router

app = FastAPI(title="ASSIST AI", version="2.0")

# Include authentication and admin routes
app.include_router(auth_router)
app.include_router(admin_router)

admin_ai = AdminAI()

# REST endpoint for processing AI commands
class CommandRequest(BaseModel):
    command: str

@app.post("/command")
async def process_command(request: CommandRequest):
    response = admin_ai.interpret_command(request.command)
    return {"response": response}

# WebSocket endpoint for real-time interaction
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        response = admin_ai.interpret_command(data)
        await websocket.send_text(response)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
