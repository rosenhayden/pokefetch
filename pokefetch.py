import json
import urllib.request
import urllib.parse
from colorama import Fore
import argparse
def getUserPokemon():
    parser = argparse.ArgumentParser(description='Fetch Pokemon')
    parser.add_argument("pokemon", metavar="pokemon", type = str, help="Enter the name of a Gen 1 Pokemon, use - for multi word names...")
    args = parser.parse_args()
    return args.pokemon

def createApiString(userInput):
    return "https://pokeapi.co/api/v2/pokemon/" + userInput

def getPokemonStats(url):
    req = urllib.request.Request(url, headers={ "User-Agent": "Mozilla/5.0" })
    resp = urllib.request.urlopen(req)
    raw = resp.read()
    data = json.loads(raw)
    data = data["stats"] 
    print(Fore.RED +"HP: " + str(data[0].get("base_stat")))
    print(Fore.BLUE +"Attack: " + str(data[1].get("base_stat")))
    print(Fore.YELLOW +"Defence: " + str(data[2].get("base_stat")))
    print(Fore.GREEN +"Sp. Attack: " + str(data[3].get("base_stat")))
    print(Fore.MAGENTA +"Sp. Defence: " + str(data[4].get("base_stat")))
    print(Fore.WHITE +"Speed: " + str(data[5].get("base_stat")))


def pokemonPrinter(userInput):
    f = open(userInput, "r")
    print(f.read())


def main():
    userInput = getUserPokemon()
    pokemonPrinter(userInput)
    getPokemonStats(createApiString(userInput))
       




if __name__ == "__main__":
    main()
