from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status
from typing import List, Optional

def get_car(db: Session, car_id: int) -> Optional[models.Car]:
    return db.query(models.Car).filter(models.Car.id == car_id).first()

def get_cars(db: Session, skip: int = 0, limit: int = 10) -> List[models.Car]:
    return db.query(models.Car).offset(skip).limit(limit).all()

def create_car(db: Session, car: schemas.CarCreate) -> models.Car:
    db_car = models.Car(**car.dict())
    db.add(db_car)
    try:
        db.commit()
        db.refresh(db_car)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    return db_car

def update_car(db: Session, car_id: int, car_update: schemas.CarUpdate) -> Optional[models.Car]:
    db_car = get_car(db, car_id)
    if db_car:
        for key, value in car_update.dict(exclude_unset=True).items():
            setattr(db_car, key, value)
        try:
            db.commit()
            db.refresh(db_car)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Car not found")
    return db_car

def delete_car(db: Session, car_id: int) -> Optional[models.Car]:
    db_car = get_car(db, car_id)
    if db_car:
        db.delete(db_car)
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Car not found")
    return db_car

def delete_cars(db: Session, car_ids: List[int]) -> None:
    try:
        db.query(models.Car).filter(models.Car.id.in_(car_ids)).delete(synchronize_session=False)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))

def create_customer(db: Session, customer: schemas.CustomerCreate) -> models.Customer:
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    try:
        db.commit()
        db.refresh(db_customer)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    return db_customer

def get_customer(db: Session, customer_id: int) -> Optional[models.Customer]:
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def get_customers(db: Session, skip: int = 0, limit: int = 10) -> List[models.Customer]:
    return db.query(models.Customer).offset(skip).limit(limit).all()

def update_customer(db: Session, customer_id: int, customer_update: schemas.CustomerUpdate) -> Optional[models.Customer]:
    db_customer = get_customer(db, customer_id)
    if db_customer:
        for key, value in customer_update.dict(exclude_unset=True).items():
            setattr(db_customer, key, value)
        try:
            db.commit()
            db.refresh(db_customer)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return db_customer

def delete_customer(db: Session, customer_id: int) -> Optional[models.Customer]:
    db_customer = get_customer(db, customer_id)
    if db_customer:
        db.delete(db_customer)
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return db_customer

def create_seller(db: Session, seller: schemas.SellerCreate) -> models.Seller:
    db_seller = models.Seller(**seller.dict())
    db.add(db_seller)
    try:
        db.commit()
        db.refresh(db_seller)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    return db_seller

def get_seller(db: Session, seller_id: int) -> Optional[models.Seller]:
    return db.query(models.Seller).filter(models.Seller.id == seller_id).first()

def get_sellers(db: Session, skip: int = 0, limit: int = 10) -> List[models.Seller]:
    return db.query(models.Seller).offset(skip).limit(limit).all()

def update_seller(db: Session, seller_id: int, seller_update: schemas.SellerUpdate) -> Optional[models.Seller]:
    db_seller = get_seller(db, seller_id)
    if db_seller:
        for key, value in seller_update.dict(exclude_unset=True).items():
            setattr(db_seller, key, value)
        try:
            db.commit()
            db.refresh(db_seller)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seller not found")
    return db_seller

def delete_seller(db: Session, seller_id: int) -> Optional[models.Seller]:
    db_seller = get_seller(db, seller_id)
    if db_seller:
        db.delete(db_seller)
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seller not found")
    return db_seller

def create_sale(db: Session, sale: schemas.SaleCreate) -> models.Sale:
    if sale.discount > 10.0:
        sale.discount = 10.0
    db_sale = models.Sale(**sale.dict())
    db.add(db_sale)
    try:
        db.commit()
        db.refresh(db_sale)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    return db_sale

def get_sale(db: Session, sale_id: int) -> Optional[models.Sale]:
    return db.query(models.Sale).filter(models.Sale.id == sale_id).first()

def get_sales(db: Session, skip: int = 0, limit: int = 10) -> List[models.Sale]:
    return db.query(models.Sale).offset(skip).limit(limit).all()

def update_sale(db: Session, sale_id: int, sale_update: schemas.SaleUpdate) -> Optional[models.Sale]:
    db_sale = get_sale(db, sale_id)
    if db_sale:
        for key, value in sale_update.dict(exclude_unset=True).items():
            setattr(db_sale, key, value)
        try:
            db.commit()
            db.refresh(db_sale)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale not found")
    return db_sale

def delete_sale(db: Session, sale_id: int) -> Optional[models.Sale]:
    db_sale = get_sale(db, sale_id)
    if db_sale:
        db.delete(db_sale)
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale not found")
    return db_sale

def create_rental(db: Session, rental: schemas.RentalCreate) -> models.Rental:
    db_rental = models.Rental(**rental.dict())
    db.add(db_rental)
    try:
        db.commit()
        db.refresh(db_rental)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    return db_rental

def get_rental(db: Session, rental_id: int) -> Optional[models.Rental]:
    return db.query(models.Rental).filter(models.Rental.id == rental_id).first()

def get_rentals(db: Session, skip: int = 0, limit: int = 10) -> List[models.Rental]:
    return db.query(models.Rental).offset(skip).limit(limit).all()

def update_rental(db: Session, rental_id: int, rental_update: schemas.RentalUpdate) -> Optional[models.Rental]:
    db_rental = get_rental(db, rental_id)
    if db_rental:
        for key, value in rental_update.dict(exclude_unset=True).items():
            setattr(db_rental, key, value)
        try:
            db.commit()
            db.refresh(db_rental)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rental not found")
    return db_rental

def delete_rental(db: Session, rental_id: int) -> Optional[models.Rental]:
    db_rental = get_rental(db, rental_id)
    if db_rental:
        db.delete(db_rental)
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rental not found")
    return db_rental
