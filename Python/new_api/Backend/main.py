from fastapi import FastAPI, UploadFile, File, Form, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models.prod_model as models
import schemas.prod_schemas as schemas
import shutil, os, uuid

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Media folder
MEDIA_DIR = os.path.join(os.path.dirname(__file__), "media")
os.makedirs(MEDIA_DIR, exist_ok=True)
app.mount("/media", StaticFiles(directory=MEDIA_DIR), name="media")

# DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Categories ---
@app.post("/categories/", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = models.Category(
        name=category.name,
        slug=category.name.lower().replace(" ", "-")
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@app.get("/categories/", response_model=list[schemas.CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()

# --- Products ---
@app.post("/products/", response_model=schemas.ProductResponse)
async def create_product(
    name: str = Form(...),
    price: float = Form(...),
    desc: str = Form(...),
    status: str = Form(...),
    category_id: int = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Save image to media
    filename = f"{uuid.uuid4().hex}_{image.filename}"
    filepath = os.path.join(MEDIA_DIR, filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    db_product = models.Product(
        name=name,
        price=price,
        desc=desc,
        status=status,
        category_id=category_id,
        image=f"/media/{filename}"
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()
