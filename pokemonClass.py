class Pokemon:

    def __init__(self, data):

        #Getting all the stats ftom the json

        self.name = data["name"]
        self.potions = 2
        info + 2
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

    def Display_Stats(self):
        print(f"Name: {self.name.capitalize()}")      
        print(f"Hp: {self.mHp}")
        print(f"Attack dmg: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed stat: {self.speed}")
        print("Type:", end=" ")
        for i in self.types:
            print(i, end = ", ")


        