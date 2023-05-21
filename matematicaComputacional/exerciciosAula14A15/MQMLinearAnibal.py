from ..exercicioAula11A13.interpolacaoNewton import InterpoladorNewton
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


x = [-1.0, -0.75, -0.6,	-0.5, -0.3, 0, 0.2, 0.4, 0.5, 0.7, 1]
y = [2.05, 1.153, 0.45,	0.4, 0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05]
A, b = construirSistemaAumentado(x,y,3)
coef = np.linalg.solve(A,b)

print('A = ', A)
print('b = ', b)
print('coef=', coef)

plt.plot(x, y, 'ro')
data = np.linspace(min(x), max(x), 100)
c = coef[::-1].copy() # invertendo a lista de coeficientes/alphas
IN = InterpoladorNewton()
p = np.poly1d(c)
plt.plot(data, p(data))
plt.grid()
plt.show()