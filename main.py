from fastapi import FastAPI
from fastapi import HTTPException
import requests

app = FastAPI()

@app.get("/server-info/{server_id}")
def get_server_info(server_id: str):
    url = f"https://api.battlemetrics.com/servers/{server_id}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Server not found")
    
    return response.json()