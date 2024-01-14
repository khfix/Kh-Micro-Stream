import requests
from fastapi import APIRouter

router = APIRouter()

aspnet_service_url = "http://localhost:5232/"


@router.get("/api/Billing")
async def get_billing():
    response = requests.get(aspnet_service_url + "api/Billing")
    return response.json()


@router.get("/api/Billing/{id}")
async def get_billing_by_id(id: int):
    response = requests.get(aspnet_service_url + f"api/Billing/{id}")
    return response.json()


@router.post("/api/Billing")
async def post_billing(billingId: int, userId: int, amount: float, timestamp: str):
    response = requests.post(
        aspnet_service_url + "api/Billing",
        json={
            "billingId": billingId,
            "userId": userId,
            "amount": amount,
            "timestamp": timestamp,
        },
    )
    return response.json()


@router.delete("/api/Billing/{id}")
async def delete_billing(id: int):
    response = requests.delete(aspnet_service_url + f"api/Billing/{id}")
    return response.json()


@router.get("/api/Subscription")
async def get_subscription():
    response = requests.get(aspnet_service_url + "api/Subscription")
    return response.json()


@router.get("/api/Subscription/{id}")
async def get_subscription_by_id(id: int):
    response = requests.get(aspnet_service_url + f"api/Subscription/{id}")
    return response.json()


@router.post("/api/Subscription")
async def post_subscription(
    subscriptionId: int, userId: int, planType: str, startDate: str, endDate: str
):
    response = requests.post(
        aspnet_service_url + "api/Subscription",
        json={
            "subscriptionId": subscriptionId,
            "userId": userId,
            "planType": planType,
            "startDate": startDate,
            "endDate": endDate,
        },
    )
    return response.json()


@router.delete("/api/Subscription/{id}")
async def delete_subscription(id: int):
    response = requests.delete(aspnet_service_url + f"api/Subscription/{id}")
    return response.json()
