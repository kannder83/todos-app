# install:

pip install pymongo "pymongo[srv]" python-decouple uvicorn fastapi pydantic

## 1. File .env

Create a file with URL to access a MongoDb Atlas

## 2. Config DB access

Use db.py file to connect to DB.

## 3. Main file:

Import FastAPI to create de application server.

## 4. Models

## 5. Schemas

## 6. Routes

## 7. Server

uvicorn app:app --reload
