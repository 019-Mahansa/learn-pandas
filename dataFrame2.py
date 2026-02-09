import pandas as pd

df = pd.read_csv("data.csv",index_col="Name")

# print(df.to_string())
# print(df[["Name","Legendary"]].to_string())

#select by row
# print(df.loc[1])
print(df.loc["Charizard",["Height","Weight"]]) #call only by the object that in the charizard