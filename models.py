from typing import Optional
from beanie import Document, Indexed
from schema import Category
from datetime import datetime


class Product(Document):
    # You can use normal types just like in pydantic
    name: str  # Indexed(str, unique=True)
    description: Optional[str] = None
    # You can also specify that a field should correspond to an index
    price: Indexed(float)
    category: Category

    class Settings:
        name = "product_collection"


class ProductReview(Document):
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    class Settings:
        name = "product_review"
