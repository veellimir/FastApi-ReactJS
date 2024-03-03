from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter(
    prefix='/currency',
    tags=['currency']
)

API_KEY = "9de480a4cf9fa09365b29010"
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"


@router.get("/exchange-rate/{base_currency}")
async def get_exchange_rate(base_currency: str):
    try:
        url = f"{API_URL}/{base_currency.upper()}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return data
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))