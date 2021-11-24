# install:

pip install pymongo "pymongo[srv]" python-decouple uvicorn fastapi pydantic

## 1. File .env

Create a file with URL to access a MongoDb Atlas

## 2. Config DB access

Use db.py file to connect to DB.

## 3. Main file:

Import FastAPI to create de application server.

## 4. Models

Models for detarminate a type of data.

## 5. Schemas

Schemas for determinate a organization of data.

## 6. Routes

It's use for determinate path in app.

## 7. Server

uvicorn app:app --reload

## 8. Exception

Using exception.

## 9. Tutorial:

[Tutorial] https://www.youtube.com/watch?v=MXwcUrI-iss
