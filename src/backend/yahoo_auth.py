import os
import requests
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

YAHOO_CLIENT_ID = os.getenv("YAHOO_CLIENT_ID")
YAHOO_CLIENT_SECRET = os.getenv("YAHOO_CLIENT_SECRET")
YAHOO_REDIRECT_URI = os.getenv("YAHOO_REDIRECT_URI")

if not YAHOO_CLIENT_ID or not YAHOO_CLIENT_SECRET or not YAHOO_REDIRECT_URI:
    raise ValueError("Missing YAHOO_CLIENT_ID, YAHOO_CLIENT_SECRET, or YAHOO_REDIRECT_URI")

@router.get("/yahoo/login")
def yahoo_login():
    yahoo_auth_url = (
      f"https://api.login.yahoo.com/oauth2/request_auth?"
      f"client_id={YAHOO_CLIENT_ID}&redirect_uri={YAHOO_REDIRECT_URI}&"
      f"response_type=code"
    )
    return RedirectResponse(yahoo_auth_url)

@router.get("/yahoo/callback")
def yahoo_callback(code: str):
    token_url = "https://api.login.yahoo.com/oauth2/get_token"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = {
        "client_id": YAHOO_CLIENT_ID,
        "client_secret": YAHOO_CLIENT_SECRET,
        "redirect_uri": YAHOO_REDIRECT_URI,
        "code": code,
        "grant_type": "authorization_code",
    }

    response = requests.post(token_url, headers=headers, data=data)
    return response.json()