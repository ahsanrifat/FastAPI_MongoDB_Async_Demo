from fastapi import FastAPI
from typing import List
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models import Product, ProductReview
from schema import ProductSchema, ProductReviewSchema, ProductReviewSchemaResponse, ProductSchemaResponse, ProductUpdateSchema
from beanie import PydanticObjectId


app = FastAPI()


async def init_db():
    client = AsyncIOMotorClient(
        "localhost:1000",
        maxPoolSize=10,
        minPoolSize=10)

    db = client.test_db
    await init_beanie(database=db, document_models=[Product, ProductReview])


@app.on_event("startup")
async def start_db():
    await init_db()


@app.post("/product/", response_model=ProductSchemaResponse)
async def create_product(payload: ProductSchema):
    product = Product(**payload.dict())
    await product.insert()
    return product


@app.get("/product/", response_model=List[ProductSchemaResponse])
async def get_list_product():
    product = await Product.find().to_list()
    return product


@app.get("/product/{id}", response_model=ProductSchemaResponse)
async def get_product(id: PydanticObjectId):
    product = await Product.get(id)
    return product


@app.post("/product/{id}", response_model=ProductSchemaResponse)
async def update_product(id: PydanticObjectId, payload: ProductUpdateSchema):
    product = await Product.get(id)
    await product.update({"$set": payload.dict()})
    return product


@app.delete("/product/{id}", response_model=ProductSchemaResponse)
async def get_product(id: PydanticObjectId):
    product = await Product.get(id)
    await product.delete()


@app.post("/review/", response_model=ProductReviewSchemaResponse)
async def create_product_review(payload: ProductReviewSchema):
    review = ProductReview(
        **payload.dict())
    await review.insert()
    return review


@app.get("/review/", response_model=List[ProductReviewSchemaResponse])
async def get_product_review_list():
    review = await ProductReview.find().to_list()
    return review


@app.get("/review/{id}", response_model=ProductReviewSchemaResponse)
async def get_product_review(id: PydanticObjectId):
    review = await ProductReview.get(id)
    return review
 