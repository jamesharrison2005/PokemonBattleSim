import requests
import random

class Move:
    
    def __init__(self, name):
        self.name = name.lower()
        url = f"https://pokeapi.co/api/v2/move/{self.name}"
        response = requests.get(url)

        #reads the json file and stores all the important info in variables such as power, accuracy and so on
        if response.status_code == 200:
            data = response.json()
            self.type = data["type"]["name"]
            self.power = data["power"] or 0
            self.accuracy = data["accuracy"] or 100
            self.damage_class = data["damage_class"]["name"]
        else: # returns status code if there was an error returning data
            print(f"There was a problem retrieving data! Error Code: {response.status_code}")
    
    #generates a random number if the accuracy is greater or equal to the move will land
    def MoveHits(self):
        num = random.randint(1,99)
        if self.accuracy >= num:
            return True
        else:
            return False
            
