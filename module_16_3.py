from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def add_user(username: str, age: int) -> str:
    new_id = str(int(max(users, key = int))+ 1)
    users[new_id] = f'Имя: {username}, возраст: {age}'
    #new_user = {"id": new_id, "description": description}
    #users.append(new_user)
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, description: str):
    users[user_id] = description
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    users.pop(user_id)
    return f"The user {user_id} is deleted"
