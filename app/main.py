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
async def users():
    return users_db