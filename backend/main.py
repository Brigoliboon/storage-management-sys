from fastapi import FastAPI
from .routes.product_route import router


app = FastAPI()

# Include the router in your FastAPI application
app.include_router(router)

