from pydantic import BaseModel
from pydantic import Field


class Todo(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )
    description: str
    completed: bool
    date: str

    class Config:
        schema_extra = {
            "examples": [
                {
                    "name": "Activity ToDo",
                    "description": "Information about ToDo",
                    "completed": False,
                    "date": "14/nov/2021"
                }
            ]
        }
