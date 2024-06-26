from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship, backref
from app.database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), index=True)
    model = Column(String(50), index=True)
    year = Column(Integer)
    placa = Column(String(10), unique=True, index=True)
    price = Column(Float)

    rentals = relationship("Rental", back_populates="car")
    sales = relationship("Sale", back_populates="car")

    def __repr__(self):
        return f"<Car(id={self.id}, brand={self.brand}, model={self.model}, year={self.year}, placa={self.placa}, price={self.price})>"

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)

    rentals = relationship("Rental", back_populates="customer")
    sales = relationship("Sale", back_populates="customer")

    def __repr__(self):
        return f"<Customer(id={self.id}, name={self.name}, email={self.email})>"

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)

    sales = relationship("Sale", back_populates="seller")

    def __repr__(self):
        return f"<Seller(id={self.id}, name={self.name}, email={self.email})>"

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    seller_id = Column(Integer, ForeignKey("sellers.id"))
    discount = Column(Float, default=0.0)
    sale_date = Column(Date)

    car = relationship("Car", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")
    seller = relationship("Seller", back_populates="sales")

    def __repr__(self):
        return f"<Sale(id={self.id}, car_id={self.car_id}, customer_id={self.customer_id}, seller_id={self.seller_id}, discount={self.discount}, sale_date={self.sale_date})>"

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    rental_date = Column(Date)
    return_date = Column(Date)
    daily_rate = Column(Float)
    insurance = Column(Boolean, default=False)

    car = relationship("Car", back_populates="rentals")
    customer = relationship("Customer", back_populates="rentals")

    def __repr__(self):
        return f"<Rental(id={self.id}, car_id={self.car_id}, customer_id={self.customer_id}, rental_date={self.rental_date}, return_date={self.return_date}, daily_rate={self.daily_rate}, insurance={self.insurance})>"
