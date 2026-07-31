from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas
from auth import get_current_user
from database import get_db

router = APIRouter(
    prefix="/products",
    tags=["products"],
)


# Create a new product
@router.post("/", response_model=schemas.Product, status_code=status.HTTP_201_CREATED)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Create a new product. Requires authentication."""
    # Anyone logged in can create a product
    db_product = models.Product(**product.dict(), owner_id=current_user.id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Get a list of all products
@router.get("/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve all products with optional pagination."""
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products


# Get a single product by its ID
@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    """Retrieve a single product by its ID."""
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


# Update an existing product
@router.put("/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int,
    product_update: schemas.ProductUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Update a product. Requires authentication."""
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    # For a real app, you might want to check if current_user.id == db_product.owner_id

    update_data = product_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Delete a product
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Delete a product. Requires authentication."""
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    # Again, you might want to add an ownership check here

    db.delete(db_product)
    db.commit()
    # No content is returned for a 204 response
    return
