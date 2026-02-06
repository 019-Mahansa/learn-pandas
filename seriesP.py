import pandas as pd

information = {
    'day 1' : 1000,
    'day 2' : 1200
}

conv = pd.Series(information, index=["hari 1","hari 2"])

print(conv)

info = [10,20,30]

series = pd.Series(info,index=["hari 1", "hari 2","hari 3"])

print(series)