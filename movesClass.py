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

    def Get_Type_Multiplier(self, defender_type):
        url = f"https://pokeapi.co/api/v2/type/{self.type}"
        response = requests.get(url)
        multiplier = 1.0

        if response.status_code == 200:
            data = response.json()
            double = [t['name'] for t in data['damage_relations']['double_damage_to']]
            half = [t['name'] for t in data['damage_relations']['half_damage_to']]
            zero = [t['name'] for t in data['damage_relations']['no_damage_to']]

            for t in defender_type:
                if t in double:
                    multiplier *= 2.0
                elif t in half:
                    multiplier *= 0.5
                elif t in zero:
                    multiplier *= 0.0
            
        return multiplier