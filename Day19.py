# def bayes(prior,likelood,evidence):
#     return (likelood*prior)/evidence

import numpy as np
import matplotlib.pyplot as plt

# mu, sig = 0, 1
#
# x = np.linspace(-4, 4, 100)
#
# y = (1 / (np.sqrt(2 * np.pi * sig**2))) * np.exp(-0.5 * ((x - mu) / sig) ** 2)
# plt.plot(x, y)
# plt.xlabel("x")
# plt.ylabel("Probability Density")
# plt.title("Normal Distribution")
# plt.grid(True)
# plt.show()

# p = 0.6
# plt.bar([0,1],[1-p,p])
# plt.xticks([0,1] , labels=['0','1'])
# plt.show()

# binomian dis
from scipy.stats import binom
# n , p = 10,0.5
# x = np.arange(0,n+1)
# y = binom.pmf(x,n,p)
# plt.bar(x,y)
# plt.plot(x,y)
# plt.show()

from scipy.stats import poisson

# possion dis
lam = 3
x = np.arange(0,10)
y = poisson.pmf(x,lam)
plt.bar(x,y)
plt.show()
