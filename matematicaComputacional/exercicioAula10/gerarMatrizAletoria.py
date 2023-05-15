import numpy as np


def mudancaAleatoria(matriz):
    n = matriz.shape[0]
    linha = np.random.randint(n)
    if (np.random.rand() > 0.25):
        matriz[linha, :] += np.random.rand()* 10 ** -10 * matriz[np.random.randint(n), :]
    else:
        matriz[linha, :] -= np.random.rand()* 10 ** -10 * matriz[np.random.randint(n), :]


def gerarSistema(n):
    matriz = np.zeros((n, n+1))
    b = np.random.rand(n)
    matriz[:, n] = b
    matriz[:,:-1] = np.identity(n)
    matriz * np.random.randint(400,600)
    rounds = np.random.randint(8000, 10000)
    while rounds > 0:
        mudancaAleatoria(matriz)
        rounds -= 1

    A = matriz[:, :-1].tolist()
    x = b.tolist()
    newb = [element[0] for element in matriz[:, -1:].tolist()]
    
    return [A, x, newb]

s = gerarSistema(4)
print('A = ', s[0])
print('x = ', s[1])
print('b = ', s[2])