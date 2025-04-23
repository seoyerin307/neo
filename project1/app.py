from fastapi import FastAPI, Form, Request, status
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from datetime import datetime
import pandas as pd


app = FastAPI()
df = pd.read_csv("data_filled.csv")

client = MongoClient("mongodb://192.168.1.41:27017")
db = client["pension_calculation"]
collection = db["pension"] 

@app.post(
    path="/api/pension_calculation",
    description="연금 조회",
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
)
async def get_pension(request: Request):
    content_type = request.headers.get("Content-Type", "")
    
    if "application/json" in content_type:
        data = await request.json()
    elif "application/x-www-form-urlencoded" in content_type:
        form = await request.form()
        data = dict(form)
    else:
        return JSONResponse(
            status_code=415,
            content={"error": "error"}
        )

    try:
        age = int(data.get("age"))
    except (TypeError, ValueError):
        return JSONResponse(
            status_code=400,
            content={"error": "error"}
        )

    current_year = datetime.now().year
    birth_year = current_year - age
    pension_year = birth_year + 65

    result = collection.find_one({"year": pension_year})
    if result:
        return {"saving_pension": result["amount_per_person"]}

    return {"message": f"{pension_year}년도에 대한 연금 데이터가 없습니다."}

@app.post("/pension_gap")
async def pension_gap(request: Request):
    content_type = request.headers.get("content-type", "")

    if "application/json" in content_type:
        data = await request.json()
    elif "application/x-www-form-urlencoded" in content_type:
        form = await request.form()
        data = dict(form)
    else:
        raise HTTPException(status_code=415)

    try:
        age = int(data.get("age"))
        quality_life = int(data.get("quality_life"))
    except (TypeError, ValueError):
        raise HTTPException(status_code=400)

    if quality_life not in [750000000, 1200000000]:
        raise HTTPException(status_code=400)

    start_year = 2025 + (65 - age)
    pension = dict(zip(df['year'], df['amount_per_person']))
    monthly = pension.get(start_year, pension[max(pension)])
    total_received = monthly * 12 * 25
    gap = quality_life - total_received

    return {
        "gap": gap
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
    