from fastapi import APIRouter
from ..models.product_models import Product, ProductAdd, ProductPublic
from ..database import engine, Session, select

router = APIRouter()

@router.post("/add_product", response_model=ProductPublic)
async def product(product: ProductAdd):
    with Session(engine) as session:
        db_product =Product.model_validate(product)
        session.add(db_product)
        session.commit()
        session.refresh(db_product)
        return db_product

@router.get("/products")
def get_products():
    with Session(engine) as session:
        products = session.exec(select(Product)).all()
        return products