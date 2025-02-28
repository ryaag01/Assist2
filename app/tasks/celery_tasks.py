# app/tasks/celery_tasks.py
from celery import Celery
from app.config import REDIS_URL

celery = Celery("assist_tasks", broker=REDIS_URL)

@celery.task
def web_scrape_task():
    print("Web scraping initiated.")
    return "Web scraping completed."

@celery.task
def retrain_models_task():
    print("Retraining models with new data.")
    return "Retraining completed."
