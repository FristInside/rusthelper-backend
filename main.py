from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/search")
def search_servers(name: str = Query(...)):
    url = f"https://api.battlemetrics.com/servers?filter[search]={name}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "API error"}

    data = response.json()["data"]

    result = []
    for server in data:
        result.append({
            "id": server["id"],
            "name": server["attributes"]["name"],
            "players": server["attributes"]["players"],
            "maxPlayers": server["attributes"]["maxPlayers"]
        })

    return result
