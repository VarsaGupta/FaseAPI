from fastapi import FastAPI
app= FastAPI()

coupon_codes={
    1 : "10%",  # it works 
    "2" : "20%" # doesnot work
}

@app.get("/get_coupon/{coupon}")
async def getCoupon(coupon:int):
    return coupon_codes.get(coupon)
