from fastapi import FastAPI
from celery_worker import check_strategy
from model import CryptoDetails

# Create FastAPI app
app = FastAPI()

# Create order endpoint
@app.post('/check_strategy')
def process_strategy(crypto_details: CryptoDetails):
    strategy = "BBRSI"
    check_strategy.delay(strategy, crypto_details.json())

    return {"message": "Validation in-progress."}