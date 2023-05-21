from matplotlib import pyplot as plt
import numpy as np


def generate_points(a, b, num_points):
    X = np.linspace(0.1, 1, num_points)  # Valores de X no intervalo [0.1, 1]
    Y = 1 / (a + b * X) * np.random.randint(-100, 30) + np.random.randint(0, 30)   # Calcula os valores de Y usando a função 1/(a+bx)
    return X, Y

X, Y = generate_points(np.random.randint(-50,10), np.random.randint(-1,20), 20)
print(2+3 == 1/(1/(2+3)))
print('X1 =', list(X))
print('Y1 =', list(Y))
plt.plot(X, Y, 'bo')
plt.show()