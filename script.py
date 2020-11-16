import requests

r = requests.get("https://www.johnlewis.com")
print(r.status_code)
