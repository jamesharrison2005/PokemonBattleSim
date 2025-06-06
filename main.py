import requests

base_url = "https://pokeapi.co/api/v2/"

def Get_Poke_Data(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        poke_Info = response.json()
        return poke_Info
    else:
        print(f"There was a problem retrieving data! Error Code: {response.status_code}")
    
    

poke_Name = input("Please enter the name of a pokemon: ").lower()
poke_Data = Get_Poke_Data(poke_Name)
print(poke_Data)