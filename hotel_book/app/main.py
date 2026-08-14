from fastapi import FastAPI
from app.config import settings
from app.api.v1.router import api_router
from app.core.database import Base, engine

# สร้างตารางใน Database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Include Router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Clean Architecture Service"}