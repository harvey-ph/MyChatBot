# backend/app/routers/base_router.py

from fastapi import APIRouter

base_router: APIRouter = APIRouter()

@base_router.get("/", summary="Root endpoint", response_description="Welcome Message")
async def root() -> dict:
    """
        Root endpoint that returns a welcome message.

        Returns:
            dict: A dictionary with a welcome message.
    """
    return {"message": "Welcome to MyChatBot, enjoy!"}