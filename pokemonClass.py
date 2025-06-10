from random import choices
from movesClass import Move

class Pokemon:

    def __init__(self, data):

        #Getting all the stats ftom the json

        self.name = data["name"]
        self.potions = 2
        
        stats = data['stats']
        #loop through stats dictionary until desired stat is found
        for stat in stats:
            if stat['stat']['name'] == 'hp':
                self.cHp = stat['base_stat']
                self.mHp = stat['base_stat']
            elif stat['stat']['name'] == 'attack':
                self.attack = stat['base_stat']
            elif stat['stat']['name'] == 'defense':
                self.defense = stat['base_stat']
            elif stat['stat']['name'] == 'speed':
                self.speed = stat['base_stat']

        #get the pokemon types
        self.types = []
        for i in range (len(data['types'])):
            type = data['types'][i]
            self.types.append(type['type']['name'])

        self.moves = self.Get_Moves(data)

    def Get_Moves(self, data):
        moves_list = []
        
        for i in data["moves"]:
            for j in i["version_group_details"]:
                if j["move_learn_method"]["name"] == "level-up":
                    moves_list.append(i["move"]["name"])
                    break
        while True:

            print("\nMoves:")
            for i, move in enumerate(moves_list, start=1):
                print(f" {i} - {move}")

            selection = input("Please select the number of the moves you would like to use e.g 2,6,9,11: ")
            try:
                choices = [int(num.strip()) for num in selection.split(',')]
                if len(choices) != 4 or any(i < 1 or i > len(moves_list) for i in choices):
                    print("Invalid selection. Please enter 3 valid numbers between 1 and", len(moves_list))
                else:
                    poke_moves = [moves_list[i - 1] for i in choices]
                    break
            except ValueError:
                print("Thats not an integer please enter again")
            
        return poke_moves    
                

        


    def Display_Stats(self):
        print(f"Name: {self.name.capitalize()}")      
        print(f"Hp: {self.mHp}")
        print(f"Attack dmg: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed stat: {self.speed}")
        print("Type:", end=" ")
        for i in self.types:
            print(i, end = ", ")

        print("\nMoves:")
        for i, move in enumerate(self.moves, start=1):
            print(f" {i} - {move}")



        