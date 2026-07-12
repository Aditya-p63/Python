import matplotlib
import matplotlib.pyplot as plt
from unicodedata import category

# x = [1,2,3,4,5,6,7,8,9]
# y = [10,20,30,40,50,60,70,80,90]
# plt.plot(x,y)
# plt.show()

# line plot
# plt.plot([1,2,3],[4,5,6],label="A")
# plt.title("Plot 1")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.legend()
# plt.show()

# Bar Chart
# Categories = ["A","B","C","D","E","F","G"]
# values = [10,25,4,3,4,5,5]
# plt.bar(Categories,values,color="red")
# plt.show()

# Histogram
# data = [1,2,3,4,5,5,5,6,6,6]
# plt.hist(data,bins=4,color="red",edgecolor="black")
# plt.show()

# Scatter Plot
# x = [1,2,3,4,5]
# y = [10,20,30,40,50]
# plt.scatter(x,y,color="red")
# plt.show()

# Customizing plot
# x = [1,2,3,4,5,6,7,8,9]
# y = [10,20,30,40,50,60,70,80,90]
# plt.scatter(x,y,color="red")
# plt.xlabel("x-axis label")
# plt.ylabel("y-axis label")
# plt.legend("Dataset")
# plt.show()


# import seaborn as sns
# import pandas as pd
# import numpy as np
# # Heat Map
# data = np.random.rand(5,5)
# sns.heatmap(data,annot=True,cmap="coolwarm")
# plt.show()
#
# # Pair Plot
# df = pd.DataFrame(data)
# sns.pairplot(df)
# plt.show()


# Create a basic plots with matplotlib.
# years = [2010 , 2020 , 2030 , 2040]
# sales = [100,230,33,44]
# plt.plot(years,sales , label="sales" , color="blue" , marker="o")
# plt.xlabel("years")
# plt.ylabel("sales")
# plt.legend()
# plt.show()
# # bar chart
# categorys = ["Electornics" , "clothing"]
# revenue = [250 , 400]
# plt.bar(categorys,revenue,color="green")
# plt.xlabel("category")
# plt.ylabel("revenue")
# plt.show()
# # scatter plot
# hour = [1,23,4,5]
# exam = [50,22,44,50]
# plt.scatter(hour,exam,color="red")
# plt.xlabel("hour")
# plt.ylabel("exam")
# plt.show()


# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# df = sns.load_dataset("iris")
#
# # Remove the categorical column
# df = df.drop(columns=["species"])
#
# correlation = df.corr()
#
# sns.heatmap(correlation, annot=True, cmap="coolwarm")
# plt.show()