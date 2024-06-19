# tests/test_crud.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import main, models, schemas
from app.database import Base

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
    
    main.app.dependency_overrides[main.get_db] = override_get_db
    with TestClient(main.app) as c:
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

# Implemente mais testes para as demais operações do CRUD e casos de erro
