from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import investigations, ai

app = FastAPI(title="IGNIS API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(investigations.router, prefix="/api/investigations", tags=["Investigations"])
app.include_router(ai.router, prefix="/api/ai", tags=["SI Analyst"])

@app.get("/")
def health_check():
    return {"status": "online", "service": "IGNIS Spacecraft Fire Safety Intelligence"}
