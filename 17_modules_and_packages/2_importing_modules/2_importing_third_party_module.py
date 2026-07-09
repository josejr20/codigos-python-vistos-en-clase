# 3_importing_third_party_module.py
# Version de Python: Puedes instalar y importar modulos externos usando
# pip.

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()

print('Response Data:', data)
