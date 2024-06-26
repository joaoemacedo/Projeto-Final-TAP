import dotenv
import os

dotenv.load_dotenv()

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import models, schemas
from app.database import Base
from app.main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c

def test_create_car(client):
    car_data = {"brand": "Toyota", "model": "Corolla", "year": 2020}
    response = client.post("/cars/", json=car_data)
    assert response.status_code == 200
    created_car = response.json()
    assert created_car["brand"] == car_data["brand"]
    assert created_car["model"] == car_data["model"]
    assert created_car["year"] == car_data["year"]
    assert created_car["available"] is True
    assert "id" in created_car

def test_read_car(client):
    response = client.get("/cars/1")
    assert response.status_code == 200
    car = response.json()
    assert car["id"] == 1
    assert car["brand"] == "Toyota"
    assert car["model"] == "Corolla"
    assert car["year"] == 2020
    assert car["available"] is True

def test_update_car(client):
    car_update_data = {"brand": "Toyota", "model": "Camry", "year": 2021, "available": False}
    response = client.put("/cars/1", json=car_update_data)
    assert response.status_code == 200
    updated_car = response.json()
    assert updated_car["brand"] == car_update_data["brand"]
    assert updated_car["model"] == car_update_data["model"]
    assert updated_car["year"] == car_update_data["year"]
    assert updated_car["available"] is car_update_data["available"]

def test_delete_car(client):
    response = client.delete("/cars/1")
    assert response.status_code == 200
    deleted_car = response.json()
    assert deleted_car["id"] == 1

    response = client.get("/cars/1")
    assert response.status_code == 404

def test_create_customer(client):
    customer_data = {"name": "John Doe", "email": "john.doe@example.com"}
    response = client.post("/customers/", json=customer_data)
    assert response.status_code == 200
    created_customer = response.json()
    assert created_customer["name"] == customer_data["name"]
    assert created_customer["email"] == customer_data["email"]
    assert "id" in created_customer

def test_read_customer(client):
    response = client.get("/customers/1")
    assert response.status_code == 200
    customer = response.json()
    assert customer["id"] == 1
    assert customer["name"] == "John Doe"
    assert customer["email"] == "john.doe@example.com"

def test_update_customer(client):
    customer_update_data = {"name": "Jane Doe", "email": "jane.doe@example.com"}
    response = client.put("/customers/1", json=customer_update_data)
    assert response.status_code == 200
    updated_customer = response.json()
    assert updated_customer["name"] == customer_update_data["name"]
    assert updated_customer["email"] == customer_update_data["email"]

def test_delete_customer(client):
    response = client.delete("/customers/1")
    assert response.status_code == 200
    deleted_customer = response.json()
    assert deleted_customer["id"] == 1

    response = client.get("/customers/1")
    assert response.status_code == 404

def test_create_seller(client):
    seller_data = {"name": "Seller One"}
    response = client.post("/sellers/", json=seller_data)
    assert response.status_code == 200
    created_seller = response.json()
    assert created_seller["name"] == seller_data["name"]
    assert "id" in created_seller

def test_read_seller(client):
    response = client.get("/sellers/1")
    assert response.status_code == 200
    seller = response.json()
    assert seller["id"] == 1
    assert seller["name"] == "Seller One"

def test_update_seller(client):
    seller_update_data = {"name": "Seller Two"}
    response = client.put("/sellers/1", json=seller_update_data)
    assert response.status_code == 200
    updated_seller = response.json()
    assert updated_seller["name"] == seller_update_data["name"]

def test_delete_seller(client):
    response = client.delete("/sellers/1")
    assert response.status_code == 200
    deleted_seller = response.json()
    assert deleted_seller["id"] == 1

    response = client.get("/sellers/1")
    assert response.status_code == 404

def test_create_sale(client):
    sale_data = {"car_id": 1, "customer_id": 1, "price": 20000}
    response = client.post("/sales/", json=sale_data)
    assert response.status_code == 200
    created_sale = response.json()
    assert created_sale["car_id"] == sale_data["car_id"]
    assert created_sale["customer_id"] == sale_data["customer_id"]
    assert created_sale["price"] == sale_data["price"]
    assert "id" in created_sale

def test_read_sale(client):
    response = client.get("/sales/1")
    assert response.status_code == 200
    sale = response.json()
    assert sale["id"] == 1
    assert sale["car_id"] == 1
    assert sale["customer_id"] == 1
    assert sale["price"] == 20000

def test_update_sale(client):
    sale_update_data = {"car_id": 1, "customer_id": 1, "price": 25000}
    response = client.put("/sales/1", json=sale_update_data)
    assert response.status_code == 200
    updated_sale = response.json()
    assert updated_sale["car_id"] == sale_update_data["car_id"]
    assert updated_sale["customer_id"] == sale_update_data["customer_id"]
    assert updated_sale["price"] == sale_update_data["price"]

def test_delete_sale(client):
    response = client.delete("/sales/1")
    assert response.status_code == 200
    deleted_sale = response.json()
    assert deleted_sale["id"] == 1

    response = client.get("/sales/1")
    assert response.status_code == 404

def test_create_rental(client):
    rental_data = {"car_id": 1, "customer_id": 1, "rental_date": "2023-01-01", "return_date": "2023-01-10"}
    response = client.post("/rentals/", json=rental_data)
    assert response.status_code == 200
    created_rental = response.json()
    assert created_rental["car_id"] == rental_data["car_id"]
    assert created_rental["customer_id"] == rental_data["customer_id"]
    assert created_rental["rental_date"] == rental_data["rental_date"]
    assert created_rental["return_date"] == rental_data["return_date"]
    assert "id" in created_rental

def test_read_rental(client):
    response = client.get("/rentals/1")
    assert response.status_code == 200
    rental = response.json()
    assert rental["id"] == 1
    assert rental["car_id"] == 1
    assert rental["customer_id"] == 1
    assert rental["rental_date"] == "2023-01-01"
    assert rental["return_date"] == "2023-01-10"

def test_update_rental(client):
    rental_update_data = {"car_id": 1, "customer_id": 1, "rental_date": "2023-01-01", "return_date": "2023-01-15"}
    response = client.put("/rentals/1", json=rental_update_data)
    assert response.status_code == 200
    updated_rental = response.json()
    assert updated_rental["car_id"] == rental_update_data["car_id"]
    assert updated_rental["customer_id"] == rental_update_data["customer_id"]
    assert updated_rental["rental_date"] == rental_update_data["rental_date"]
    assert updated_rental["return_date"] == rental_update_data["return_date"]

def test_delete_rental(client):
    response = client.delete("/rentals/1")
    assert response.status_code == 200
    deleted_rental = response.json()
    assert deleted_rental["id"] == 1

    response = client.get("/rentals/1")
    assert response.status_code == 404
