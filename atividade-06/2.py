# Gerador de Usuarios aleatórios

import requests
import random

try:
  response = requests.get('https://randomuser.me/api/?nat=br')
except requests.RequestException as e:
    print(f'Erro na requisição: {e}')


if response.status_code == 200:

  dados = response.json()['results']
  
  usuario_aleatorio = random.choice(dados)

  nome = f"{usuario_aleatorio['name']['first']} {usuario_aleatorio['name']['last']}"
  email = f"{usuario_aleatorio['email']}"
  pais = f"{usuario_aleatorio['location']['country']}"

  print(f"Nome -> {nome}\nE-mail -> {email}\nPaís -> {pais}")

else:
  print("Erro externo , consulte o programador")  