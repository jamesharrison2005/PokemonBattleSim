import requests

class Move:
    
    def __init__(self, name):
        self.name = name.lower()
        url = f"https://pokeapi.co/api/v2/move/{self.name}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.type = data["type"]["name"]
            self.power = data["power"] or 0
            self.accuracy = data["accuracy"] or 100
            self.damage_class = data["damage_class"]["name"]
        else:
            print(f"There was a problem retrieving data! Error Code: {response.status_code}")
    
    