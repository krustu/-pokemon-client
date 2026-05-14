import requests


class PokemonClient:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon"

    def get_pokemon(self, name):
        response = requests.get(f"{self.BASE_URL}/{name}")
        if response.status_code != 200:
            raise ValueError(f"Pokemon '{name}' not found.")
        return response.json()


class Pokemon:
    def __init__(self, data):
        self.name = data["name"]
        self.height = data["height"]
        self.weight = data["weight"]
        self.types = [t["type"]["name"] for t in data["types"]]
        self.abilities = [a["ability"]["name"] for a in data["abilities"]]

    def display(self):
        print(f"Name:      {self.name.capitalize()}")
        print(f"Height:    {self.height}")
        print(f"Weight:    {self.weight}")
        print(f"Types:     {', '.join(self.types)}")
        print(f"Abilities: {', '.join(self.abilities)}")


if __name__ == "main":
    client = PokemonClient()

    pokemons = ["pikachu", "bulbasaur", "charmander"]

    for name in pokemons:
        print(f"\n--- {name.upper()} ---")
        data = client.get_pokemon(name)
        pokemon = Pokemon(data)
        pokemon.display()