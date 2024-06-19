from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    placa = Column(String, unique=True, index=True)
    price = Column(Float)

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    seller_id = Column(Integer, ForeignKey("sellers.id"))
    discount = Column(Float, default=0.0)
    sale_date = Column(Date)

    car = relationship("Car")
    customer = relationship("Customer")
    seller = relationship("Seller")

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    rental_date = Column(Date)
    return_date = Column(Date)
    daily_rate = Column(Float)
    insurance = Column(Boolean, default=False)

    car = relationship("Car")
    customer = relationship("Customer")
