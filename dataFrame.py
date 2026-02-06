import pandas as pd

spogbob = {
    "Karakter" : ["Spongbob","Mr Krab", "Squidword"],
    "Umur" : [30,32,36]
}

dataframe = pd.DataFrame(spogbob)

#add kolom baru
dataframe["Posisi"] = ["Chef","Owner","Cashier"]

#add row baru
row = pd.DataFrame([{"Karakter" : "Sandy", "Umur" : 28, "Posisi" : "Waiters"}, {"Karakter" : "Puko", "Umur" : 48, "Posisi" : "Janitor"}])
dataframe = pd.concat([dataframe, row])

dataframe.index = [f"Karyawan {i+1} " for i in range(len(dataframe))] #number karyawan nya looping



print(dataframe)


# print(dataframe.loc["Karyawan 1"])
# print(dataframe.iloc[0])