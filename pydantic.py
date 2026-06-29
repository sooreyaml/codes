# pydantic is used for data validation
from pydantic import BaseModel
from typing import list


class User(BaseModel):
    id: int
    name: str
    age: int
    friends: list[str]
    

external_data =  {
    "id": "1",
    "name": "moyo",
    "age": 20,
    "friends": ["daniel", "goodness"]
}

# ** is the standard way to “spread” the dict into those named parameters
user = User(**external_data)

print(user)