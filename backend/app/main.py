# backend/app/main.py

from fastapi import FastAPI
from app.routers import base_router

app: FastAPI = FastAPI(
    title="MyChatBot",
    version="1.0.0",
    description="This is my first ChatBot Project"
)

app.include_router(base_router)