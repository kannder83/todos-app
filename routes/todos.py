from fastapi import APIRouter, HTTPException
from config.db import conn
from models.todos import Todo
from schemas.todos import todo_serializer, todos_serializer
from bson import ObjectId

todo_router = APIRouter()


@todo_router.get("/")
async def get_todos():
    try:
        todos = todos_serializer(conn.todos_app.todos.find())
        return {"status": "Ok", "data": todos}
    except:
        raise HTTPException(status_code=500, detail="Posts can not be found")


@todo_router.get("/{id}")
async def get_todo(id: str):
    try:
        todo = todo_serializer(
            conn.todos_app.todos.find_one({"_id": ObjectId(id)}))
        return {"status": "Ok", "data": todo}
    except:
        raise HTTPException(status_code=404, detail="Post not found.")


@todo_router.post("/")
async def post_todo(todo: Todo):
    try:
        _id = conn.todos_app.todos.insert_one(dict(todo))
        todo = todo_serializer(
            conn.todos_app.todos.find_one({"_id": _id.inserted_id}))
        return {"status": "Ok", "data": todo}
    except:
        raise HTTPException(status_code=500, detail="Post can not send.")


@todo_router.put("/{id}")
async def update_todo(id: str, todo: Todo):
    try:
        conn.todos_app.todos.find_one_and_update(
            {
                "_id": ObjectId(id)
            },
            {
                "$set": dict(todo)
            }
        )
        todo = todo_serializer(
            conn.todos_app.todos.find_one({"_id": ObjectId(id)}))
        return {"message": "Ok", "data": todo}
    except:
        raise HTTPException(status_code=404, detail="Post not found.")


@todo_router.delete("/{id}")
async def delete_todo(id: str):
    try:
        todo_serializer(
            conn.todos_app.todos.find_one_and_delete({"_id": ObjectId(id)}))
        return {"message": "Ok", "data": []}
    except:
        raise HTTPException(status_code=404, detail="Post not found.")
