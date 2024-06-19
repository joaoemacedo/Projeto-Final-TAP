from sqlalchemy.orm import Session
from app import models, schemas

def get_car(db: Session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).first()

def get_cars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Car).offset(skip).limit(limit).all()

def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def update_car(db: Session, car_id: int, car_update: schemas.CarUpdate):
    db_car = get_car(db, car_id)
    if db_car:
        for key, value in car_update.dict().items():
            setattr(db_car, key, value)
        db.commit()
        db.refresh(db_car)
    return db_car

def delete_car(db: Session, car_id: int):
    db_car = get_car(db, car_id)
    if db_car:
        db.delete(db_car)
        db.commit()
    return db_car

def delete_cars(db: Session, car_ids: list[int]):
    db.query(models.Car).filter(models.Car.id.in_(car_ids)).delete(synchronize_session=False)
    db.commit()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def get_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def update_customer(db: Session, customer_id: int, customer_update: schemas.CustomerUpdate):
    db_customer = get_customer(db, customer_id)
    if db_customer:
        for key, value in customer_update.dict().items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
    return db_customer

def create_seller(db: Session, seller: schemas.SellerCreate):
    db_seller = models.Seller(**seller.dict())
    db.add(db_seller)
    db.commit()
    db.refresh(db_seller)
    return db_seller

def get_seller(db: Session, seller_id: int):
    return db.query(models.Seller).filter(models.Seller.id == seller_id).first()

def get_sellers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Seller).offset(skip).limit(limit).all()

def update_seller(db: Session, seller_id: int, seller_update: schemas.SellerUpdate):
    db_seller = get_seller(db, seller_id)
    if db_seller:
        for key, value in seller_update.dict().items():
            setattr(db_seller, key, value)
        db.commit()
        db.refresh(db_seller)
    return db_seller

def create_sale(db: Session, sale: schemas.SaleCreate):
    if sale.discount > 10.0:
        sale.discount = 10.0
    db_sale = models.Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def get_sale(db: Session, sale_id: int):
    return db.query(models.Sale).filter(models.Sale.id == sale_id).first()

def get_sales(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Sale).offset(skip).limit(limit).all()

def create_rental(db: Session, rental: schemas.RentalCreate):
    db_rental = models.Rental(**rental.dict())
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    return db_rental

def get_rental(db: Session, rental_id: int):
    return db.query(models.Rental).filter(models.Rental.id == rental_id).first()

def get_rentals(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Rental).offset(skip).limit(limit).all()
