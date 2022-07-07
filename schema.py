from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from beanie import Document
from beanie import PydanticObjectId


class Category(BaseModel):
    name: str
    description: str


class ProductSchema(BaseModel):
    name: str
    description: Optional[str]
    price: float
    category: Category


class ProductUpdateSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    category: Optional[Category]


class ProductSchemaResponse(ProductSchema):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")


class ProductReviewSchema(BaseModel):
    name: str
    product: str
    rating: float
    review: str


class ProductReviewSchemaResponse(ProductReviewSchema):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
