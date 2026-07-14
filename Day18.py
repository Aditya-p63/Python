import sympy as sp
import numpy as np
# x = sp.symbols('x')
# f = x**2
# definite = sp.integrate(f, (x,0,2))
# print(definite)
# indef = sp.integrate(f,x)
# print(indef)

# excercise
# 1)simple integrals
# x = sp.Symbol('x')
# f = sp.exp(-x)
# indef = sp.integrate(f, x)
# print(indef)
# defin = sp.integrate(f, (x,0,2))
# print(defin)

# 2)implement sgd
import numpy as np

np.random.seed(42)

x = 2 * np.random.randn(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)
x_b = np.c_[np.ones((100, 1)), x]

def sgd(x, y, theta, learning, iterations):
    m = len(y)

    for epoch in range(iterations):
        for i in range(m):
            random_index = np.random.randint(m)

            xi = x[random_index:random_index+1]
            yi = y[random_index:random_index+1]

            gradient = 2 * xi.T @ (xi @ theta - yi)
            theta -= learning * gradient

    return theta

theta = np.random.randn(2, 1)

learning = 0.01
iterations = 1000

theta = sgd(x_b, y, theta, learning, iterations)

print(theta)