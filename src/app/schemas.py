from pydantic import BaseModel,Field
from datetime import time
from typing import List



class Item(BaseModel):
    shortDescription: str = Field(...,pattern="^[\\w\\s\\-&]+$")
    price: str = Field(...,pattern="^\\d+\\.\\d{2}$")


class Receipt(BaseModel):
    retailer: str = Field(...,pattern="^[\\w\\s\\-&]+$")
    purchaseDate: str = Field(...) 
    purchaseTime: time 
    items: List[Item]
    total: str = Field(...,pattern="^\\d+\\.\\d{2}$")
