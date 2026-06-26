import requests
import json

url = "http://127.0.0.1:5000/clientes"

payload = json.dumps({
  "nombre": " Pepe toño",
  "saldo": 200
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)