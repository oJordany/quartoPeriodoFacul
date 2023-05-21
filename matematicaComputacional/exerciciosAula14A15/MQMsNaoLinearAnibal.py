import matplotlib.pyplot as plt
import numpy as np


def construirSistemaAumentado(x,y, dimensao):
    """
    :param x: list abscissas tabeladas.
    :param y: list ordenadas tabeladas.
    :param dimensao: quantidade de alphas/coeficientes usados → grau + 1.
    """
    m = len(x)
    A = np.empty((dimensao, dimensao))
    b = np.empty((dimensao))
    soma = []
    for i in range(0, dimensao+2):
        aux = 0
        for k in range(0,m):
            aux = aux + x[k]**i
        soma.append(aux)

    for i in range(0, dimensao):
        for j in range(i, dimensao):
            A[i,j] = soma[i+j]
            if (i != j):
                A[j,i] = A[i,j]

    for i in range(0,dimensao):
        aux = 0
        for k in range(0,m):
            aux = aux + y[k]*(x[k]**i)
        b[i] = aux

    return A, b

def p(coef, x):
    y = np.exp(coef[0]) * np.exp(coef[1] * x)
    return y

x  = [-1.0, -0.7, -0.4,	-0.1,	0.2, 0.5, 0.8, 1.0]
y  = [36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246]
ly = np.log(y)
A, b = construirSistemaAumentado(x,ly,2)
coef = np.linalg.solve(A,b)
print('A = ', A)
print('b = ', b)
print('coef=', coef)

plt.plot(x, y, 'ro')
data = np.linspace(min(x), max(x), 100)
plt.plot(data, p(coef, data), 'b-')
plt.grid()
plt.show()