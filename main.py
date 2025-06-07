import requests
import os
from pokemonClass import Pokemon

base_url = "https://pokeapi.co/api/v2/"

def Get_Poke_Data(name):
    url = f"{base_url}pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        poke_Info = response.json()
        return poke_Info
    else:
        print(f"There was a problem retrieving data! Error Code: {response.status_code}")
    
    
def MainMenu():

    print("\n-----Welcome to the Pokemon Battle Sim!-----\n")
    print("Player 1 please select your pokemon:")
    p1 = selectPokemon()
    os.system('cls')
    print("Player 2 please select your pokemon:")
    p2 = selectPokemon()
         
        
    for pokemon in p1:
        print("\n")
        pokemon.Display_Stats()
    print("\n\n-------Player 2-------")
    for pokemon in p2:
        print("\n")
        pokemon.Display_Stats()
        
def selectPokemon():
    player = []
    ctr = 1
    for i in range(2):
        print(f"Please enter the name of Pokemon {ctr} you want to use: ")
        ctr += 1
        name = input()
        poke_Data = Get_Poke_Data(name)
        if poke_Data:
            pokemon = Pokemon(poke_Data)
            player.append(pokemon)  # Correct: Append to the player list   

    return player        

MainMenu()





