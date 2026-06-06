from flask import Flask, request
import requests
import urllib.parse

app = Flask(__name__)

CLIENT_KEY = "sbaw2pswnx9isr4rjo"
CLIENT_SECRET = "21GDyc1aOWBFRy03Weathl3DG9YPwUh8"
REDIRECT_URI = "https://asesabd.github.io/KommentTiktok/callback.html"

@app.route("/")
def login():
    params = {
        "client_key": CLIENT_KEY,
        "scope": "user.info.basic,video.list",
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "state": "teszt123"
    }

    url = "https://www.tiktok.com/v2/auth/authorize/?" + urllib.parse.urlencode(params)
    return f'<a href="{url}">Login with TikTok</a>'

@app.route("/token")
def token():
    code = request.args.get("code")
    return f"Code: {code}"

app.run(port=8000, debug=True)
