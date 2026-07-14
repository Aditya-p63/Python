import sympy as sp
import numpy as np
# x = sp.Symbol('x')
# f = x**2;
# der = sp.diff(f,x)
# print(der)

# x , y = sp.symbols('x y')
# f = x**2 + y**2
# gradx = sp.diff(f,x)
# grady = sp.diff(f,y)
# print(gradx)
# print(grady)

# Excericise
# x = sp.symbols("x")
# f = x**3-5*x+7
# derivative = sp.diff(f,x)
# print(derivative)


# 2)computing gradient
# x , y = sp.symbols("x y")
# f = x**2+3*y**2-4*x*y
# gradx = sp.diff(f,x)
# grady = sp.diff(f,y)
# print(gradx, grady)

# implement gradient decent
def grad(x, y, theta, learning, iterations):
    x = np.array(x)
    y = np.array(y)
    theta = np.array(theta, dtype=float)

    m = len(y)

    for _ in range(iterations):
        prediction = np.dot(x, theta)
        error = prediction - y
        gradient = (1 / m) * np.dot(x.T, error)
        theta -= learning * gradient

    return theta

x = [[2, 3], [4, 5]]
y = [2, 3.4]
theta = [0.1, 0.1]
learning = 0.1
iterations = 10

optimized = grad(x, y, theta, learning, iterations)
print(optimized)