from fastapi import FastAPI

app = FastAPI()
users_db = [{"id": "1", "name": "andrew"}]

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    return {"status": "OK"}

@app.get("/users")
async def get_users():
    return users_db

@app.post("/users")
async def post_users(id: int, name: str):
    new_user = {"id": id, "name": name}
    users_db.append(new_user)
    return users_db