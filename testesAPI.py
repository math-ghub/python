import requests

resp = requests.get("https://api.github.com/users/math-ghub/repos")

if resp.status_code == 200:
    print(resp.json())
    if type(resp.json()) is not int:
        for i in range(len(resp.json())):
            print(resp.json()[i]["name"])