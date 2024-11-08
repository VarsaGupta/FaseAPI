#  using fastapi built-in validation functionality

from fastapi import FastAPI
from enum import Enum
app= FastAPI()

class Availablecuisines(str, Enum):
    indian = "indian"
    american = "american"

food_items= {
    "indian":["samosa","dosa"],
    "american":["pizza","burger"]
}

@app.get("/get_food/{cuisine}")
async def getFood(cuisine:Availablecuisines):
    return food_items.get(cuisine)
