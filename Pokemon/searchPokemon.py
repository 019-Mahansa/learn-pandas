import pandas as pd
df = pd.read_csv("data.csv", index_col="Type1")


def mainMenu():
    print("Welcome to Pokemon menu!")
    print("1. Type of Pokemon")
    print("2. Nama Pokemon")
    print("3. Legendary Character \n")
    pokemon = int(input("Pilih menu yang anda inginkan : "))
    if pokemon == 1:
        pokemonType()
    elif pokemon == 2:
        pokemonName()
    elif pokemon == 3:
        pokemonLegendary()
    else:
        print("Pencarian anda gagal!")

def pokemonType():

    print("Welcome to type of pokemon!")
    ine = input("typing type pokemon that you want: ")
    print(df["Rock"])
    print("That is all type of pokemon!")

def pokemonName():
    print("1")

def pokemonLegendary():
    print("1")

mainMenu()

# try:
#     print(df.loc[upper])
# except KeyError:
#     print(f" {upper} tidak di temukan!")
