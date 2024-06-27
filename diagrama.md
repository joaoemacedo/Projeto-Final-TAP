```mermaid
classDiagram
    class Car {
        Integer id
        String brand
        String model
        Integer year
        String placa
        Float price
        + __repr__(): String
    }

    class Customer {
        Integer id
        String name
        String email
        + __repr__(): String
    }

    class Seller {
        Integer id
        String name
        String email
        + __repr__(): String
    }

    class Sale {
        Integer id
        Integer car_id
        Integer customer_id
        Integer seller_id
        Float discount
        Date sale_date
        + __repr__(): String
    }

    class Rental {
        Integer id
        Integer car_id
        Integer customer_id
        Date rental_date
        Date return_date
        Float daily_rate
        Boolean insurance
        + __repr__(): String
    }

    Car "1" --o "*" Rental : "rentals"
    Car "1" --o "*" Sale : "sales"
    Customer "1" --o "*" Rental : "rentals"
    Customer "1" --o "*" Sale : "sales"
    Seller "1" --o "*" Sale : "sales"
