import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_data(pokemon_name):
    url = f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"failed to retrieve data for {pokemon_name}.")


pokemon_name = 'ditto'
pokemon_data = get_pokemon_data(pokemon_name)

if pokemon_data:
    print(f"Name: {pokemon_data['name']}")
    print(f"abilities: {pokemon_data['abilities']}")
