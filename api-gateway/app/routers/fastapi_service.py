import requests
from fastapi import APIRouter

router = APIRouter()

fastapi_service_url = "http://localhost:8080/"


@router.get("/video/{video_id}")
async def stream_video(video_id: int):
    try:
        response = requests.get(fastapi_service_url + f"video/{video_id}")
    except requests.exceptions.ConnectionError:
        return "Failed to fetch video"

    return response.content
