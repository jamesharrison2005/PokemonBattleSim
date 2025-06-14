import requests
import os
from pokemonClass import Pokemon

base_url = "https://pokeapi.co/api/v2/"

def Get_Poke_Data(name):
    n = name
    while True:
        url = f"{base_url}pokemon/{n.lower()}"
        response = requests.get(url)

        if response.status_code == 200:
            poke_Info = response.json()
            break
            
        else:
            print(f"There was a problem retrieving data! Error Code: {response.status_code}")
            n = input("Please enter the pokemons name again: ")
    return poke_Info
    
def MainMenu():

    print("\n-----Welcome to the Pokemon Battle Sim!-----\n")
    print("Player 1 please select your pokemon:")
    p1 = selectPokemon()
    print("Player 2 please select your pokemon:")
    p2 = selectPokemon()
    os.system('cls')

    print("\n\n-------Player 1-------")
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
            player.append(pokemon) 

    return player        

def BattleSimulation(p1_team, p2_team):
    p1_index = 0
    p2_index = 0

    p1_pokemon = p1_team[p1_index]
    p2_pokemon = p2_team[p2_index]

MainMenu()





