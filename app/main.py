from fastapi import FastAPI

app = FastAPI(
    title="KPT48 Theater Ticketing API",
    description="Backend service for FP SBD 2026",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to KPT48 Ticketing System! Ready for the war."}