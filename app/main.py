from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine
import app.logging_config as logging_config

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Car endpoints
@app.post("/cars/", response_model=schemas.Car)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    logging_config.logger.info("Creating a new car")
    return crud.create_car(db=db, car=car)

@app.get("/cars/", response_model=list[schemas.Car])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logging_config.logger.info("Fetching all cars")
    cars = crud.get_cars(db=db, skip=skip, limit=limit)
    return cars

@app.get("/cars/{car_id}", response_model=schemas.Car)
def read_car(car_id: int, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Fetching car with id {car_id}")
    db_car = crud.get_car(db=db, car_id=car_id)
    if db_car is None:
        logging_config.logger.error(f"Car with id {car_id} not found")
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@app.put("/cars/{car_id}", response_model=schemas.Car)
def update_car(car_id: int, car_update: schemas.CarUpdate, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Updating car with id {car_id}")
    db_car = crud.update_car(db=db, car_id=car_id, car_update=car_update)
    if db_car is None:
        logging_config.logger.error(f"Car with id {car_id} not found")
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@app.delete("/cars/{car_id}", response_model=schemas.Car)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Deleting car with id {car_id}")
    db_car = crud.delete_car(db=db, car_id=car_id)
    if db_car is None:
        logging_config.logger.error(f"Car with id {car_id} not found")
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@app.delete("/cars/", response_model=dict)
def delete_multiple_cars(car_ids: list[int], db: Session = Depends(get_db)):
    logging_config.logger.info(f"Deleting multiple cars with ids {car_ids}")
    crud.delete_cars(db=db, car_ids=car_ids)
    return {"message": f"Deleted cars with ids {car_ids}"}

# Customer endpoints
@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    logging_config.logger.info("Creating a new customer")
    return crud.create_customer(db=db, customer=customer)

@app.get("/customers/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Fetching customer with id {customer_id}")
    db_customer = crud.get_customer(db=db, customer_id=customer_id)
    if db_customer is None:
        logging_config.logger.error(f"Customer with id {customer_id} not found")
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@app.get("/customers/", response_model=list[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logging_config.logger.info("Fetching all customers")
    customers = crud.get_customers(db=db, skip=skip, limit=limit)
    return customers

@app.put("/customers/{customer_id}", response_model=schemas.Customer)
def update_customer(customer_id: int, customer_update: schemas.CustomerUpdate, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Updating customer with id {customer_id}")
    db_customer = crud.update_customer(db=db, customer_id=customer_id, customer_update=customer_update)
    if db_customer is None:
        logging_config.logger.error(f"Customer with id {customer_id} not found")
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@app.delete("/customers/{customer_id}", response_model=schemas.Customer)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Deleting customer with id {customer_id}")
    db_customer = crud.delete_customer(db=db, customer_id=customer_id)
    if db_customer is None:
        logging_config.logger.error(f"Customer with id {customer_id} not found")
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

# Seller endpoints
@app.post("/sellers/", response_model=schemas.Seller)
def create_seller(seller: schemas.SellerCreate, db: Session = Depends(get_db)):
    logging_config.logger.info("Creating a new seller")
    return crud.create_seller(db=db, seller=seller)

@app.get("/sellers/{seller_id}", response_model=schemas.Seller)
def read_seller(seller_id: int, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Fetching seller with id {seller_id}")
    db_seller = crud.get_seller(db=db, seller_id=seller_id)
    if db_seller is None:
        logging_config.logger.error(f"Seller with id {seller_id} not found")
        raise HTTPException(status_code=404, detail="Seller not found")
    return db_seller

@app.get("/sellers/", response_model=list[schemas.Seller])
def read_sellers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logging_config.logger.info("Fetching all sellers")
    sellers = crud.get_sellers(db=db, skip=skip, limit=limit)
    return sellers

@app.put("/sellers/{seller_id}", response_model=schemas.Seller)
def update_seller(seller_id: int, seller_update: schemas.SellerUpdate, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Updating seller with id {seller_id}")
    db_seller = crud.update_seller(db=db, seller_id=seller_id, seller_update=seller_update)
    if db_seller is None:
        logging_config.logger.error(f"Seller with id {seller_id} not found")
        raise HTTPException(status_code=404, detail="Seller not found")
    return db_seller

@app.delete("/sellers/{seller_id}", response_model=schemas.Seller)
def delete_seller(seller_id: int, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Deleting seller with id {seller_id}")
    db_seller = crud.delete_seller(db=db, seller_id=seller_id)
    if db_seller is None:
        logging_config.logger.error(f"Seller with id {seller_id} not found")
        raise HTTPException(status_code=404, detail="Seller not found")
    return db_seller

# Sale endpoints
@app.post("/sales/", response_model=schemas.Sale)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    logging_config.logger.info("Creating a new sale")
    return crud.create_sale(db=db, sale=sale)

@app.get("/sales/{sale_id}", response_model=schemas.Sale)
def read_sale(sale_id: int, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Fetching sale with id {sale_id}")
    db_sale = crud.get_sale(db=db, sale_id=sale_id)
    if db_sale is None:
        logging_config.logger.error(f"Sale with id {sale_id} not found")
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale

@app.get("/sales/", response_model=list[schemas.Sale])
def read_sales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logging_config.logger.info("Fetching all sales")
    sales = crud.get_sales(db=db, skip=skip, limit=limit)
    return sales

@app.put("/sales/{sale_id}", response_model=schemas.Sale)
def update_sale(sale_id: int, sale_update: schemas.SaleUpdate, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Updating sale with id {sale_id}")
    db_sale = crud.update_sale(db=db, sale_id=sale_id, sale_update=sale_update)
    if db_sale is None:
        logging_config.logger.error(f"Sale with id {sale_id} not found")
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale

@app.delete("/sales/{sale_id}", response_model=schemas.Sale)
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Deleting sale with id {sale_id}")
    db_sale = crud.delete_sale(db=db, sale_id=sale_id)
    if db_sale is None:
        logging_config.logger.error(f"Sale with id {sale_id} not found")
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale

# Rental endpoints
@app.post("/rentals/", response_model=schemas.Rental)
def create_rental(rental: schemas.RentalCreate, db: Session = Depends(get_db)):
    logging_config.logger.info("Creating a new rental")
    return crud.create_rental(db=db, rental=rental)

@app.get("/rentals/{rental_id}", response_model=schemas.Rental)
def read_rental(rental_id: int, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Fetching rental with id {rental_id}")
    db_rental = crud.get_rental(db=db, rental_id=rental_id)
    if db_rental is None:
        logging_config.logger.error(f"Rental with id {rental_id} not found")
        raise HTTPException(status_code=404, detail="Rental not found")
    return db_rental

@app.get("/rentals/", response_model=list[schemas.Rental])
def read_rentals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logging_config.logger.info("Fetching all rentals")
    rentals = crud.get_rentals(db=db, skip=skip, limit=limit)
    return rentals

@app.put("/rentals/{rental_id}", response_model=schemas.Rental)
def update_rental(rental_id: int, rental_update: schemas.RentalUpdate, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Updating rental with id {rental_id}")
    db_rental = crud.update_rental(db=db, rental_id=rental_id, rental_update=rental_update)
    if db_rental is None:
        logging_config.logger.error(f"Rental with id {rental_id} not found")
        raise HTTPException(status_code=404, detail="Rental not found")
    return db_rental

@app.delete("/rentals/{rental_id}", response_model=schemas.Rental)
def delete_rental(rental_id: int, db: Session = Depends(get_db)):
    logging_config.logger.info(f"Deleting rental with id {rental_id}")
    db_rental = crud.delete_rental(db=db, rental_id=rental_id)
    if db_rental is None:
        logging_config.logger.error(f"Rental with id {rental_id} not found")
        raise HTTPException(status_code=404, detail="Rental not found")
    return db_rental
