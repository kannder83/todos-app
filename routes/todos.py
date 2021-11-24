from fastapi import APIRouter
from config.db import conn
from models.todos import Todo
from schemas.todos import todo_serializer, todos_serializer
from bson import ObjectId

todo_router = APIRouter()


@todo_router.get("/")
async def get_todos():
    todos = todos_serializer(conn.todos_app.todos.find())
    return {"status": "Ok", "data": todos}


@todo_router.get("/{id}")
async def get_todo(id: str):
    todo = todo_serializer(
        conn.todos_app.todos.find_one({"_id": ObjectId(id)}))
    return {"status": "Ok", "data": todo}


@todo_router.post("/")
async def post_todo(todo: Todo):
    _id = conn.todos_app.todos.insert_one(dict(todo))
    todo = todo_serializer(
        conn.todos_app.todos.find_one({"_id": _id.inserted_id}))
    return {"status": "Ok", "data": todo}
