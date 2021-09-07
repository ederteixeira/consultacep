import requests
import json

cep = input("Informe o seu CEP: ")

try:
    req = requests.get('https://cep.awesomeapi.com.br/json/' + cep)
    formatado = json.loads(req.text)
    print(formatado['address'])
    print(formatado['district'])
    print(formatado['city'], "/", formatado['state'])
except:
    print("Erro: Valor inválido!")
