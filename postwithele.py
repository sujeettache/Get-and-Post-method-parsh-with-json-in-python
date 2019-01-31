import requests
import json

data ={"email": "anand@tache.in", "password": "tachee"}
r = requests.post("http://13.233.186.205/rest-auth/login/", data)
print(r.text)
print(r.status_code)
if r.status_code != 200:
    print("Bad Status")
elif r.status_code !=400:
    print("OK Status") 
a= r.json()
#print(a.text)
#print(a['user']['name'])
#print(a['user']['mobile'])

headers = {
 'Authorization':'Token df60cad8f46658cdc1a03938aafdacebbef44f9c', 
 'Content-Type':'application/json'
}
r = requests.get("http://13.233.186.205/links/missions/", headers=headers)

print(r.text)
print(r.status_code)

