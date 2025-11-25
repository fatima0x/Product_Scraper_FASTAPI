from fastapi import FastAPI
from models import Base
from database import engine
from app.routes import router

app = FastAPI()

# Create tables on startup
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Data Extraction API is running!"}
