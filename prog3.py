from fastapi import FastAPI
app= FastAPI()

food_items= {
    "indian":["samosa","dosa"],
    "american":["pizza","burger"]
}

@app.get("/get_food/{cuisine}")
async def getFood(cuisine):
    return food_items.get(cuisine)
