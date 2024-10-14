import requests

base_url = "https://httpbin.org"

# params = {
#    "name": "Mike",
#    "age": 30,
# }

payload = {
    "name": "Mike",
    "age": 30,
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Accept": "image/png"
}

# response = requests.get(f"{base_url}/get", params=params)
# response = requests.post(f"{base_url}/post", data=payload)
# response = requests.get(f"{base_url}/user-agent", headers=headers)
response = requests.get(f"{base_url}/image", headers=headers)

if response.status_code == requests.codes.not_found:
    print("not found 404")
else:
    print(response.status_code)

with open("myimage.png", "wb") as f:
    f.write(response.content)

# data = response.json()
print(response.text)
# print(data)
# print(response.url)
