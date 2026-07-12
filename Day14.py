# project
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
print(df.info())
print(df.describe())
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df = df.drop_duplicates()
first_class = df[df["Pclass"] == 1]
print(first_class)

# survival_by_class = df.groupby("Pclass")["Survived"].mean()
# survival_by_class.plot(kind="bar",color="blue")
# plt.show()

# sns.histplot(df["Age"],kde=True,bins=20,color="blue")
# plt.show()
#
# plt.scatter(df["Age"],df["Fare"],alpha=0.5,color="red")
# plt.title("Fare vs Age")
# plt.xlabel("Age")
# plt.ylabel("Fare")
# plt.show()


