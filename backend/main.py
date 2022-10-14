import os
from urllib import request
import requests  # use httpx instead
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SessionMiddleware, secret_key="123")

@app.get("/")
async def root():
    return {"message": "Connection with fastapi container works fine"}


github_client_id = os.environ["github_client_id"]
github_client_secret = os.environ["github_client_secret"]


def get_user_attributes(github_access_token: str):
    email_url = "https://api.github.com/user/emails"
    email_response = requests.get(
        email_url, headers={"Authorization": f"Bearer {github_access_token}"}
    )
    email = ""
    for val in email_response.json():
        if val["primary"] == True:
            email = val["email"]
    user = {"email": email}
    return user


@app.get("/github")
async def callback(response: Response, code: str):
    """After GitHub successful authentication, the user is sent to this endpoint
    with the `code` url parameter. code is a temporary token issued by GitHub, we
    verify this token using the GitHub `client_id` and `client_secret` that are 
    available **only** on the server.
    After successful verification the user is redirected to a Svelte HTML page, the 
    HTML response includes an Authrization cookie. On the frontend side we can fetch 
    the cookie with javascript, this way we retrieve the token on the client.
    """

    client_id = f"?client_id={github_client_id}"
    client_secret = f"&client_secret={github_client_secret}"
    client_code = f"&code={code}"
    token_request_url = f"https://github.com/login/oauth/access_token{client_id}{client_secret}{client_code}"
    github_access_token = requests.post(
        token_request_url, headers={"Accept": "application/json"}
    ).json()["access_token"]
    user = get_user_attributes(github_access_token)
    response = RedirectResponse("https://localhost:81/logged")
    response.set_cookie(key="Authorization", value=user["email"], httponly=False)
    return response