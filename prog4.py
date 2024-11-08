# using data validation (error statements)

from fastapi import FastAPI
app= FastAPI()

food_items= {
    "indian":["samosa","dosa"],
    "american":["pizza","burger"]
}
valid_cuisine= food_items.keys()

@app.get("/get_food/{cuisine}")
async def getFood(cuisine):
    if cuisine not in valid_cuisine:
        return f"Supported cuisines are {valid_cuisine}"
    return food_items.get(cuisine)
