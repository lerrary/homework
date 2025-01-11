from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def get_main_page():
    return "Главная страница"


@app.get("/user/{user_id}")
async def get_user(
        user_id: Annotated[int, Path(gt=0,
                                     le=100,
                                     description="Enter User ID'")]):
    return {'message': f'Вы вошли как пользователь №{user_id}'}

@app.get("user/{username}/{age}")
async def get_user_by_username(
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      description="Enter username")],
        age: Annotated[int, Path(ge=18,le=120,description="Enter age")]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
