
from typing import Optional
from sqlmodel import Field, SQLModel

class Product(SQLModel, table= True):
    product_id: Optional[int] = Field(primary_key=True,unique= True, default=None)
    product_name:str = Field(index=True)
    price: float
    description: str
    available : bool
    quantity: int

class ProductAdd(SQLModel):
    product_name:str
    price: float
    description: Optional[str]
    available : bool
    quantity: int

class ProductPublic(SQLModel):
    product_id: int
    product_name:set
    price: float
    description: str
    available: bool
    quantity : int