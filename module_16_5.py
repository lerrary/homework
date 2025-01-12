from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List

app = FastAPI()

templates = Jinja2Templates(directory="templates")
users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/")
async def get_page(request: Request):
    return templates.TemplateResponse("users.html", {'request': request, 'users': users})

@app.get("user/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html",
                                              {"request": request, "user": user, "title": f"User {user_id}"})
    raise HTTPException(status_code=404, detail="User was not found")

@app.post("/user/{username}/{age}")
async def add_user(user: User, username: str, age: int):
    user.id = 1 if len(users) == 0 else len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
