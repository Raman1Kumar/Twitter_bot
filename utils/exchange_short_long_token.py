import requests
import json
import credential


short_lived_access_token=credential.INSTAGRAM_ACCESS_TOKEN
instagram_app_secret=credential.INSTAGRAM_APP_SECRET

url = f"https://graph.instagram.com/access_token?grant_type=ig_exchange_token&client_secret={instagram_app_secret}&access_token={short_lived_access_token}"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()
print(data)
long_lived_token=data["access_token"]
print(long_lived_token)
