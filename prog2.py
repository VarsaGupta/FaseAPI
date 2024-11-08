
from fastapi import FastAPI
app= FastAPI()

@app.get('/hello/{name}')
async def hello(name):
    return f"Welcome to channel {name}"
