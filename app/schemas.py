from pydantic import BaseModel, Field, EmailStr, validator
from datetime import date
from typing import Optional

class CarBase(BaseModel):
    brand: str = Field(..., example="Toyota")
    model: str = Field(..., example="Corolla")
    year: int = Field(..., example=2022)
    placa: str = Field(..., example="XYZ-1234")
    price: float = Field(..., example=15000.00)

    class Config:
        orm_mode = True

class CarCreate(CarBase):
    pass

class CarUpdate(CarBase):
    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    placa: Optional[str] = None
    price: Optional[float] = None

class Car(CarBase):
    id: int

    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    name: str = Field(..., example="John Doe")
    email: EmailStr = Field(..., example="john.doe@example.com")

    class Config:
        orm_mode = True

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True

class SellerBase(BaseModel):
    name: str = Field(..., example="Jane Doe")
    email: EmailStr = Field(..., example="jane.doe@example.com")

    class Config:
        orm_mode = True

class SellerCreate(SellerBase):
    pass

class SellerUpdate(SellerBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

class Seller(SellerBase):
    id: int

    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    car_id: int
    customer_id: int
    seller_id: int
    discount: Optional[float] = Field(0.0, example=0.0)
    sale_date: date

    class Config:
        orm_mode = True

class SaleCreate(SaleBase):
    pass

class SaleUpdate(SaleBase):
    car_id: Optional[int] = None
    customer_id: Optional[int] = None
    seller_id: Optional[int] = None
    discount: Optional[float] = None
    sale_date: Optional[date] = None

class Sale(SaleBase):
    id: int

    class Config:
        orm_mode = True

class RentalBase(BaseModel):
    car_id: int
    customer_id: int
    rental_date: date
    return_date: date
    daily_rate: float
    insurance: bool = Field(False, example=False)

    class Config:
        orm_mode = True

    @validator('return_date')
    def check_return_date(cls, v, values):
        if 'rental_date' in values and v < values['rental_date']:
            raise ValueError('return_date must be after rental_date')
        return v

class RentalCreate(RentalBase):
    pass

class RentalUpdate(RentalBase):
    car_id: Optional[int] = None
    customer_id: Optional[int] = None
    rental_date: Optional[date] = None
    return_date: Optional[date] = None
    daily_rate: Optional[float] = None
    insurance: Optional[bool] = None

class Rental(RentalBase):
    id: int

    class Config:
        orm_mode = True
