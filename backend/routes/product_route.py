from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models import Product
from ..database import get_async_session

router = APIRouter()

@router.get("/products", response_model=List[Product])
async def get_products(db: AsyncSession = Depends(get_async_session)):
    async with db.begin():
        query = db.query(select(Product))
        products = query.scalars().all()
        return products



@router.post("/add_product", response_model=Product)
async def create_product(product: Product, db: AsyncSession = Depends(get_async_session)):
    async with db.begin():
        db.add(product)
        print(product)
        await db.commit()
        await db.refresh(product)
        return product