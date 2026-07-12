# grouped = df.groupby("Column Name")
# for name , group in grouped:
#     print(name)
#     print(group)
# grouped.sum()
#
# df = groupby("Column Name")["Numeric_col"].mean()
# df.groupby("Column Name").agg({"Numeric_col": ["Mean"]})
#
# pivot = df.pivot_table(
#     values="Numeric_col",
#     index="Column Name",
#     aggfunc="mean"
# )
#
# def ranege_fun(x):
#     return x.max() - x.min()
#
# df.groupby("Column Name")["Numeric_col"].agg(ranege_fun)
# df.groupby("Column Name")["Numeric_col"].mean()
# df.groupby("Column Name")["Numeric_col"].max()
# df.groupby("Column Name")["Numeric_col"].min()
#
# df.groupby("Column Name").agg({"Numeric_col": ["Mean","max","min"]})


# Excercise
import pandas as pd
import numpy as np

data = {
    "Class" : ["A","B","C","D","E","F"],
    "Score" : [85,90,90,90,44,33],
    "Age" : [1,2,3,4,5,6],
}
df = pd.DataFrame(data)
print(df)

grouped = df.groupby("Class").mean()
print(grouped)

# Calculating summary statistical
stas = df.groupby("Class").agg({
    "Score" :["mean","std" , "min","max"],
    "Age" :["min","max" , "mean"]
})
print(stas)