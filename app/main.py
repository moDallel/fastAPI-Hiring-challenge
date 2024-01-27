from fastapi import FastAPI
from app.api.endpoints import user
from databases import Database

DATABASE_URL = "postgresql://postgres:123456@localhost/usershiringchallenge"

app = FastAPI()

# Connect to the database
database = Database(DATABASE_URL)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user.router)

@app.get("/")
async def root():
    return {"message":"main root"}
