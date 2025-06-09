import requests
import os

# Preencha com seus dados do UltraMsg
instance_id = os.environ["ULTRAMSG_INSTANCE_ID"]
token = os.environ["ULTRAMSG_TOKEN"]
numero = os.environ["WHATSAPP_NUMBER"]
mensagem = "se fude"

url = f"https://api.ultramsg.com/{instance_id}/messages/chat"
payload = {
    "token": token,
    "to": numero,
    "body": mensagem
}

response = requests.post(url, data=payload)
print(response.json()) 
