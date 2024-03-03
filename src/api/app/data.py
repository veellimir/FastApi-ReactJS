from httpx import AsyncClient


DATA_TOKEN = "f6a9a866459c01b795a269a625ec105816477ff1"
DATA_API_URL = "https://suggestions.dadata.ru/suggestions/api/4_1/rs"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Token {DATA_TOKEN}"
}


async def data_suggest(query: str):
    async with AsyncClient() as client:
        response = await client.post(
            f"{DATA_API_URL}/suggest/currency",
            json={"query": query},
            headers=headers
        )
        return response.json()