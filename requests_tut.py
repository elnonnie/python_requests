import requests

#download a photo from a website
r = requests.get("https://netstorage-legit.akamaized.net/images/b9a95bf856f5a91d.jpg?imwidth=720")
with open ("comic.png", "wb") as f:
    f.write(r.content)

#site status check
r = requests.get("https://netstorage-legit.akamaized.net/images/b9a95bf856f5a91d.jpg?imwidth=720")
print(r.status_code)

r = requests.get("https://netstorage-legit.akamaized.net/images/b9a95bf856f5a91d.jpg?imwidth=720")
print(r.ok)

r = requests.get("https://netstorage-legit.akamaized.net/images/b9a95bf856f5a91d.jpg?imwidth=720")
print(r.headers)