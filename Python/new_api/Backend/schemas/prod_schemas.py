from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    image: Optional[str] = None
    price: float
    desc: Optional[str] = None
    status: str

class ProductCreate(ProductBase):
    category_id: int

class ProductResponse(ProductBase):
    id: int
    slug: str

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    slug: str
    products: List[ProductResponse] = []

    class Config:
        orm_mode = True
