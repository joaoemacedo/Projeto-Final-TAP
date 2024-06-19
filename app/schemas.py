from pydantic import BaseModel
from datetime import date
from typing import Optional

class CarBase(BaseModel):
    brand: str
    model: str
    year: int
    placa: str
    price: float

    class Config:
        from_attributes = True

class CarCreate(CarBase):
    pass

class CarUpdate(CarBase):
    pass

class Car(CarBase):
    id: int

    class Config:
        from_attributes = True

class CustomerBase(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        from_attributes = True

class SellerBase(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True

class SellerCreate(SellerBase):
    pass

class SellerUpdate(SellerBase):
    pass

class Seller(SellerBase):
    id: int

    class Config:
        from_attributes = True

class SaleBase(BaseModel):
    car_id: int
    customer_id: int
    seller_id: int
    discount: Optional[float] = 0.0
    sale_date: date

    class Config:
        from_attributes = True

class SaleCreate(SaleBase):
    pass

class SaleUpdate(SaleBase):
    pass

class Sale(SaleBase):
    id: int

    class Config:
        from_attributes = True

class RentalBase(BaseModel):
    car_id: int
    customer_id: int
    rental_date: date
    return_date: date
    daily_rate: float
    insurance: bool = False

    class Config:
        from_attributes = True

class RentalCreate(RentalBase):
    pass

class RentalUpdate(RentalBase):
    pass

class Rental(RentalBase):
    id: int

    class Config:
        from_attributes = True
