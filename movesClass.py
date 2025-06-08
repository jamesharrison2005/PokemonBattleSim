import requests

class Move:
    
    def __init__(self, name):
        self.name = name.lower()
        url = f"https://pokeapi.co/api/v2/move/{self.name}"
        response = requests.get(url)

        if response.status_code == 200:
            pass