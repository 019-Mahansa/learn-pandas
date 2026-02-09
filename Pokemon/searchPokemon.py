import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")

pokemon = input("Ketik nama pokemon yang ingin anda cari: ")
upper = pokemon.capitalize()

try:
    print(df.loc[upper])
except KeyError:
    print(f" {upper} tidak di temukan!")
