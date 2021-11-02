from pydantic import BaseModel

class CryptoDetails(BaseModel):
    pair: str
    bid_price: float
    ask_price: float