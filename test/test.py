import requests

resp = requests.post("http://localhost:5000/", files={'file': open('sample.JPG', 'rb')})

result = resp.json()
print(result)
print(result.get("Grade"))
print(result.get("Gula/100ml(g)"))
print(result.get("Gula/Sajian(g)"))
print(result.get("Product"))