from random import sample

import pandas as pd
# s = pd.Series([10,20,30] , index=['a','b','c'])
# print(s)

# data = {"Name": ["A", "N", "V"],
#         "Age": [45, 55, 65], }
# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv('data.csv')
# print(df)
# df = pd.read_excel('data1.xlsx')
# print(df)
# df.to_excel('data1.xlsx' , index=False)
#

# df.head() -> first three row
# df.tail() -> last three row
#  df.info()
#  df.describe()
# print(df(["name"]))
# df.iloc[0]
# df.iloc[:,0]
#
# df.loc[0]
# df.loc[:"name"]

# Load and explore sample dataset
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv
# load data set
# df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# select_col = df[["species", "sepal_length"]]
# print(select_col)
# filter_row = df[(df["sepal_length"] > 5.0) & (df["species"]=="setosa")]
# print(filter_row)