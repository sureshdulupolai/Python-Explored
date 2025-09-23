from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from slugify import slugify   # for auto slug

# Category Model
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    slug = Column(String, unique=True, index=True)

    # One-to-many relationship
    products = relationship("Product", back_populates="category")


# Product Model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, index=True)
    image = Column(String)
    price = Column(Float)
    desc = Column(String)
    status = Column(String)

    # Relation back to category
    category = relationship("Category", back_populates="products")

    # Slug generate
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.name:
            self.slug = slugify(self.name)
