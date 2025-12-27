# In a separate test file or interactive cell:
import requests
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
data = response.json()

print(data['stats'])
