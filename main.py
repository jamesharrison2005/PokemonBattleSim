import requests
import os
import random
from colorama import init, Fore, Back, Style
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

    #Establish who goes first
    if p1_pokemon.speed > p2_index.speed:
        turn = 1
    elif p2_pokemon.speed > p1_pokemon.speed:
        turn = 2
    else:
        turn = random.randint(1,2)

    # battle runs while until one of the pokemon have fainted
    while not p1_pokemon.IsFainted() and not p2_pokemon.IsFainted():
        #decides based on which pokemon was faster
        if turn == 1:
            attacker = p1_pokemon
            defender = p2_pokemon
        else:
            attacker = p2_pokemon
            defender = p1_pokemon
        

        
        

MainMenu()





