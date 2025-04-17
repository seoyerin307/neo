from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def HealthCheck():
    return {"status": "ok"}

@app.get('/hello')
async def Hello():
    return {"message": "Hello World~!!"}

@app.get('/random')
@app.post('/random')
async def Random(max=None):
    import random

    if max is None:
        max = 10
    else:
        max = int(max)
    return {"random number": random.randint(1, max)}