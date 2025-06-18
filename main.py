from fastapi import FastAPI, Query
import httpx

app = FastAPI()

@app.get("/servers")
async def search_servers(name: str = Query(...)):
    url = f"https://api.battlemetrics.com/servers?filter[search]={name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()
