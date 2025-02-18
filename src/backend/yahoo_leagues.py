import requests
from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/yahoo/leagues")
def fetch_yahoo_leagues(access_token: str = Query(..., alias="access_token")):
    if not access_token:
        return {"error": "Missing access token"}

    yahoo_api_url = f"https://fantasysports.yahooapis.com/fantasy/v2/game/nfl?access_token={access_token}&format=json"

    response = requests.get(yahoo_api_url)
    print(response)
    return response.json()