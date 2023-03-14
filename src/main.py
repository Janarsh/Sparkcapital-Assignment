from fastapi import FastAPI
from pydantic import BaseModel

from crud import Crud

app = FastAPI()

class User(BaseModel):
    user_id: str = None
    name: str
    address: str

@app.post("/create-user/")
async def create_user(user: User):
    user_id = Crud().create(user)
    return {"user_id": user_id}


@app.get("/get-user/{user_id}")
async def get_user(user_id: int):
    return Crud().read(user_id)


@app.put("/update-user/")
async def update_user(user: User):
    status = Crud().update(user)
    return {"message": "update successful" if status else "update failed"}


@app.delete("/delete-user/{user_id}")
async def delete_user(user_id: int):
    status = Crud().delete(user_id)
    return {"message": "deleted successful" if status else "deletion failed"}
