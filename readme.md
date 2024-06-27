# Projeto Final - TAP

Este projeto é uma aplicação de gerenciamento de vendas e aluguéis de carros, desenvolvida como parte do Projeto Final para a disciplina de Tópicos Avançados de Programação.

##Versão Final -- Branch: final-version

## Tecnologias Utilizadas

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite

## Instalação e Execução

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/joaoemacedo/Projeto-Final-TAP.git
   cd Projeto-Final-TAP
   ```

2. **Crie e Ative o Ambiente Virtual (opcional, mas recomendado)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # no Windows use `venv\Scripts\activate`
    ```

3. **Instale as Dependências**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configuração do Banco de Dados**

    Certifique-se de configurar corretamente o banco de dados no arquivo database.py.

5. **Executar o Servidor**

    ```bash
    uvicorn app.main:app --reload #Acesse http://localhost:8000/docs
    ```


6. **Diagrama de classes**

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

