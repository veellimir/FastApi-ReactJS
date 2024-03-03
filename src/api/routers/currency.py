from fastapi import APIRouter, HTTPException

from src.api.app.data import data_suggest

router = APIRouter()


@router.get("/currency/suggest/")
async def suggest_currency(query: str):
    try:
        suggestions = await data_suggest(query)
        return suggestions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

