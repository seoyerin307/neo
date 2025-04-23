from fastapi import FastAPI, Request, HTTPException
import pandas as pd

app = FastAPI()
df = pd.read_csv("data_filled.csv")

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

    if quality_life not in [750000000, 1500000000]:
        raise HTTPException(status_code=400)

    start_year = 2025 + (65 - age)
    pension = dict(zip(df['year'], df['amount_per_person']))
    monthly = pension.get(start_year, pension[max(pension)])
    total_received = monthly * 12 * 25
    gap = quality_life - total_received

    return {
        "gap": gap
    }