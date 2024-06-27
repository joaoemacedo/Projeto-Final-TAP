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
