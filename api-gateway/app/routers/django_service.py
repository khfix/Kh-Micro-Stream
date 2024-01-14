import requests
from fastapi import APIRouter, UploadFile

router = APIRouter()


django_service_url = "http://127.0.0.1:8000/"


@router.post("/register/user", tags=["register"])
async def register(email: str, password: str):
    response = requests.post(
        django_service_url + "account/register/user",
        json={"email": email, "password": password},
    )
    return response.json()


@router.post("/register/streamer", tags=["register"])
async def register(email: str, password: str):
    response = requests.post(
        django_service_url + "account/register/streamer",
        json={"email": email, "password": password},
    )
    return response.json()


@router.post("/login/", tags=["login"])
async def login(email: str, password: str):
    response = requests.post(
        django_service_url + "account/login/",
        json={"email": email, "password": password},
    )
    return response.json()


@router.get("/users/", tags=["users"])
async def users(token: str):
    response = requests.get(
        django_service_url + "account/users/", headers={"token": token}
    )
    return response.json()


@router.get("/user/{user_id}", tags=["user"])
async def user(user_id: int, token: str):
    response = requests.get(
        django_service_url + f"account/user/{user_id}/", headers={"token": token}
    )
    return response.json()


@router.post("streamer/{user_id}/stream/create", tags=["stream"])
async def stream_create(
    user_id: int,
    title: str,
    description: str,
    file: UploadFile,
    hashtags: str,
    token: str,
):
    response = requests.post(
        django_service_url + "stream/create/",
        json={
            "title": title,
            "description": description,
            "hashtags": hashtags,
            "file_path": file,
            "uploader": user_id,
        },
        headers={"token": token},
    )
    return response.json()


@router.get("/streamer/{user_id}/streams", tags=["stream"])
async def user_streams(user_id: int, token: str):
    response = requests.get(
        django_service_url + f"stream/video/uploader/{user_id}/",
        headers={"token": token},
    )
    return response.json()


@router.get("/{hashtag}/streames/", tags=["stream"])
async def hashtag_streams(hashtag: str, token: str):
    response = requests.get(
        django_service_url + f"stream/video/hashtag/value/{hashtag}/",
        headers={"token": token},
    )
    return response.json()


@router.get("/hashtags/", tags=["hashtags"])
async def hashtags(token: str):
    response = requests.get(
        django_service_url + "stream/hashtags/", headers={"token": token}
    )
    return response.json()


@router.get("/hashtag/{hashtag}", tags=["hashtag"])
async def hashtag(hashtag: str, token: str):
    response = requests.get(
        django_service_url + f"stream/hashtag/value/{hashtag}/",
        headers={"token": token},
    )
    return response.json()
