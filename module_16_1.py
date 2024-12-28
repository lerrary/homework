from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_main():
    return "Главная страница"

@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return f"Вы вошли как пользователь №{user_id}"

@app.get("/user")
async def get_user_info(username: str = 'Lera', age: int = 44):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
