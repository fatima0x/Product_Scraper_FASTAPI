from fastapi import FastAPI
from models import Base
from database import engine
from app.routes import router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Create tables on startup
Base.metadata.create_all(bind=engine)

# Serve the frontend folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS setup
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)





@app.get("/")
def serve_frontend():
    file_path = os.path.join("static", "index.html")
    return FileResponse(file_path)
