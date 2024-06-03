import requests

resp = requests.post("http://localhost:5000/", files={'file': open('sample.JPG', 'rb')})

result = resp.json()

print(result)
print(result.get("Grade"))
print(result.get("Gula/100ml(g)"))
print(result.get("Gula/Sajian(g)"))
print(result.get("Product"))

ml=int(200)#input user volume air
countsug = float(result.get("Gula/100ml(g)"))*(ml/100)
print(countsug)