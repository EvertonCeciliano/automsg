import requests

# Preencha com seus dados do UltraMsg
instance_id = "instance124585"
token = "ra8tip9t9dj61ipc"
numero = "5514998780481" # Exemplo: 5511999999999 (sem o +)
mensagem = "Bom dia, amor! ❤️ Tenha um dia maravilhoso!"

url = f"https://api.ultramsg.com/{instance_id}/messages/chat"
payload = {
    "token": token,
    "to": numero,
    "body": mensagem
}

response = requests.post(url, data=payload)
print(response.json()) 