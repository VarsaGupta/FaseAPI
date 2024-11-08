from fastapi import FastAPI
from typing import Optional
app = FastAPI()

# Using query parameter (single parameter)
# @app.get("/blog")
# def blog(limit):
#     return {"data":f"{limit} all blog list"}

# Using query parameters (two parameter)
@app.get("/blog")
def blog(limit,published):
    if published:
        return {"data":f"{limit} published blog list"}
    return {"data":f"{limit} blog list"}


# query parameter with default values
@app.get("/blog/unpublished")
def unpublished(limit=10 , published:bool = False):
    if published != True:
        return {"data":f"{limit} unpublished blog"}
    else:
        return f"no blog"  
    

@app.get("/blog/sorted")
def blog(limit=10, sort: Optional[str]= None):
    return {"data":f"{limit} all sorted blog list"}    

