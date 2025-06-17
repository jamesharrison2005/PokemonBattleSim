import requests
import os
import random
from colorama import init, Fore, Back, Style
from pokemonClass import Pokemon
from movesClass import Move

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
    
    os.system("PAUSE")
    BattleSimulation(p1, p2)

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
    os.system('cls')
    p1_index = 0
    p2_index = 0

    p1_pokemon = p1_team[p1_index]
    p2_pokemon = p2_team[p2_index]

    #Establish who goes first
    if p1_pokemon.speed > p2_pokemon.speed:
        turn = 1
    elif p2_pokemon.speed > p1_pokemon.speed:
        turn = 2
    else:
        turn = random.randint(1,2)

    # battle runs while until one of the pokemon have fainted
    while not AllFainted(p1_team) and not AllFainted(p2_team):
        #decides based on which pokemon was faster
        errorValue = False
        if turn == 1:
            attacker = p1_pokemon
            defender = p2_pokemon
        else:
            attacker = p2_pokemon
            defender = p1_pokemon

        while errorValue == False:     
            print(f"\n{attacker.name.capitalize()}'s Turn (HP: {attacker.cHp}) ")
            print("Choose an Action:")
            print("1. Use Move")
            print(f"2. Use Potion - Potions left ({attacker.potions})")
            print("3. Switch Pokemon")
            try:
                choice = int(input("What will you do?\nInput Choice: "))
                match choice:
                    case 1:
                        print("\nMoves:")
                        for i, move in enumerate(attacker.moves, start=1):
                            print(f" {i} - {move}")
                        move_choice = int(input("Please select the number of move you'd like to use: ")) - 1
                        if move_choice >= 0 and move_choice < 4:
                            selected_move = Move(attacker.moves[move_choice])
                            if selected_move.MoveHits:
                                #simple damage calculation
                                damage = int(((attacker.attack / defender.defense) * selected_move.power) / 2)
                                print(f"{attacker.name.capitalize()} has used the move {selected_move.name}!")
                                print(f"It has done {damage} damage! to {defender.name.capitalize()}")
                                defender.Take_Damage(damage)
                                
                            else:
                                print(Fore.RED + "The move missed!")
                                print(Style.RESET_ALL) 
                            errorValue = True
                        else:
                            print(Fore.RED + "incorrect value entered, please try again")
                            os.system("PAUSE")
                            os.system('cls')  
                    case 2:
                        heal = 30
                        attacker.potions -= 1
                        if attacker.cHp + heal > attacker.mHp:
                            diff = attacker.mHp - attacker.cHp
                            attacker.cHp += diff
                            print(Fore.GREEN + f"{attacker.name.capitalize()} has been healed by {diff} points")
                        else:
                            attacker.cHp += heal
                            print(Fore.GREEN + f"{attacker.name.capitalize()} has been healed by {heal} points")
                        print(Style.RESET_ALL) 
                        print(f"You have {attacker.potions} potions left")
                        errorValue = True
                    case 3:
                        if turn == 1:
                            p1_index, p1_pokemon = Switch_pokemon(turn, p1_team, p2_team, p1_index, p2_index)
                        else:
                            p2_index, p2_pokemon = Switch_pokemon(turn, p1_team, p2_team, p1_index, p2_index) 
                        errorValue = True
                    case _:
                        print("please enter a valid input")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")
                print(Style.RESET_ALL)
                os.system("PAUSE")
                os.system('cls')  

        #Checking if the defender / team has fainted
        if AllFainted(p1_team):
            print(Fore.RED + "Player 2 wins! All of Player 1's Pokémon have fainted!")
            print(Style.RESET_ALL)
            return 
        elif AllFainted(p2_team):
            print(Fore.GREEN + "Player 1 wins! All of Player 2's Pokémon have fainted!")
            print(Style.RESET_ALL)

        print(f"{defender.name.capitalize()} has {defender.cHp} HP remaining")

        
        if defender.Is_Fainted():
            print(Fore.RED + f"{defender.name.capitalize()} has fainted!")
            print(Style.RESET_ALL)
            if turn == 1:
                p2_index, p2_pokemon = Switch_pokemon(2, p1_team, p2_team, p1_index, p2_index)
            else:
                p1_index, p1_pokemon = Switch_pokemon(1, p1_team, p2_team, p1_index, p2_index)
        
        turn = 2 if turn == 1 else 1

def Switch_pokemon(turn, p1_team, p2_team, p1_index, p2_index):
    if turn == 1:
        team = p1_team
        current_index = p1_index
    else:
        team = p2_team
        current_index = p2_index    

    print(f"Which Pokémon would you like to switch to:")
    for i, pokemon in enumerate(team, start=1):
        print(f"{i} - {pokemon.name.capitalize()} (HP: {pokemon.cHp}/{pokemon.mHp})")

    try:
        new_index = int(input("Please select the Pokémon you wish to switch to: ")) - 1

        if new_index == current_index:
            print(Fore.YELLOW + "You're already using this Pokémon.")
            print(Style.RESET_ALL)
            return current_index, team[current_index]

        if 0 <= new_index < len(team):
            if team[new_index].Is_Fainted():
                print(Fore.RED + f"{team[new_index].name.capitalize()} has fainted! Please select another Pokémon")
                return current_index, team[current_index]
            else:
                print(f"{team[current_index].name.capitalize()} has switched to {team[new_index].name.capitalize()}")
                return new_index, team[new_index]
        else:
            print(Fore.RED + "Invalid selection.")
            print(Style.RESET_ALL)
            return current_index, team[current_index]
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")
        print(Style.RESET_ALL)
        os.system("PAUSE")
        os.system('cls')  
        return current_index, team[current_index]

def AllFainted(team):
    return all(pokemon.Is_Fainted() for pokemon in team)
MainMenu()





