from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    hello_world = "Hello World!"
    return hello_world
