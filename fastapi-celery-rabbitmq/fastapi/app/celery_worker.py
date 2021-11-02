from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger
from model import CryptoDetails

# Initialize celery
celery = Celery('tasks', broker='amqp://guest:guest@rabbitmq:5672//')

# Create logger
celery_log = get_task_logger(__name__)

@celery.task
def check_strategy(strategy: str, crypto_details: CryptoDetails)-> bool:
    
    sleep(10)
    # Display log
    celery_log.info(f"{strategy} Strategy Validated")
    return True