from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()

@app.post("/api/pension_calculation")
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
            content={"error": "지원하지 않는 Content-Type입니다. JSON 또는 Form으로 요청해주세요."}
        )

    try:
        age = int(data.get("age"))
    except (TypeError, ValueError):
        return JSONResponse(
            status_code=400,
            content={"error": "나이(age)를 정확히 입력해 주세요. 숫자 형태여야 합니다."}
        )

    current_year = datetime.now().year
    birth_year = current_year - age
    pension_year = birth_year + 65

    return {"pension_year": pension_year}