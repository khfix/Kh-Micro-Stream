import io

import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse

app = FastAPI()


def get_video_path(video_id: int) -> str:
    api_url = f"http://127.0.0.1:8000/api/video/id/{video_id}/"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()["file_path"]
    else:
        raise HTTPException(
            status_code=response.status_code, detail="Failed to fetch video path"
        )


@app.get("/video/{video_id}")
async def stream_video(video_id: int):
    try:
        video_path = get_video_path(video_id)
        video_content = requests.get(video_path).content
    except HTTPException as e:
        raise e

    return StreamingResponse(io.BytesIO(video_content), media_type="video/mp4")
