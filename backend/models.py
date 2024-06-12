from pydantic import BaseModel

class Product(BaseModel):
    product_name:str
    price: float
    description: str
    available : bool
    quantity: int