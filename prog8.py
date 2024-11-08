# post method

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Blog( BaseModel):
    title : str
    body : str
    id : int
    published : Optional[bool]

@app.post('/blog')
def blog(request : Blog):
    return{'message': f'Blog with title {request.title} is created'}


