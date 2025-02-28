# app/agent_manager.py
class AgentManager:
    def __init__(self, agents: dict):
        self.agents = agents

    def route_command(self, interpretation: str) -> str:
        """
        Delegate the interpreted command to the appropriate agent using keyword-based routing.
        """
        interpretation_lower = interpretation.lower()
        if "code" in interpretation_lower:
            return self.agents["developer"].process(interpretation)
        elif "test" in interpretation_lower:
            return self.agents["tester"].process(interpretation)
        elif "research" in interpretation_lower:
            return self.agents["researcher"].process(interpretation)
        elif "data" in interpretation_lower:
            return self.agents["data_manager"].process(interpretation)
        elif "e-commerce" in interpretation_lower:
            return self.agents["ecommerce"].process(interpretation)
        elif "marketing" in interpretation_lower:
            return self.agents["marketing"].process(interpretation)
        elif "business" in interpretation_lower:
            return self.agents["biz_dev"].process(interpretation)
        else:
            return "AdminAI: Command not recognized. Please clarify."
