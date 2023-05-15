"""
Polinômio de grau n = 10
11 pontos xi = -1 + 2i/n, i =0,1,...,n
pontos igualmente espaçados → Fenômeno de Runge
para não ocorrer o fenômeno de Runge usa-se os pontos (nós) de Chebyshev:
x'i = cos(((2i + 1)*pi)/((n+1)*2))
"""

import numpy as np
import matplotlib.pyplot as plt
from interpolacaoNewton import InterpoladorNewton


def runge(x):
    return 1/(1+25*x**2)

def cheby_nodes(x0, x1, n):
    return (x1-x0)*(np.cos((2*np.arange(1, n+1)-1)/(2*n)*np.pi)+1)/2+x0

x0 = -1
x1 = 1
x = np.linspace(x0, x1, 500)
t1 = np.linspace(x0,x1,11)
t2 = cheby_nodes(x0,x1,11)

IN = InterpoladorNewton(t1, runge(t1))
IN.construirTabelaDiferencaDividida()

IN2 = InterpoladorNewton(t2, runge(t2))
IN2.construirTabelaDiferencaDividida()

yt1 = [ IN.interpolarEm(i) for i in x ] 
yt2 = [ IN2.interpolarEm(i) for i in x ] 
# print(yt2)
fig = plt.figure(figsize=(10,10))
fig.suptitle('Gráficos de Runge')

fig.add_subplot(311)
plt.plot(x, runge(x), 'y-', label='1/(1+25*x**2)')
plt.legend()
plt.title('função original')

fig.add_subplot(312)
plt.plot(x, runge(x), 'y-', label='1/(1+25*x**2)')
plt.legend()
plt.plot(x, yt1, 'k-', label='função Igual')
plt.legend()
plt.plot(t1, runge(t1), 'bo', label='Igual')
plt.legend()
plt.title('pontos igualmente espaçados')

fig.add_subplot(313)
plt.plot(x, runge(x), 'y-', label='1/(1+25*x**2)')
plt.legend()
plt.plot(t1, runge(t1), 'bo', label='Igual')
plt.legend()
plt.plot(t2, runge(t2), 'ro', label='Cheby')
plt.legend()
plt.plot(x, yt2, 'g-', label="função Cheby")
plt.legend()
plt.title('nós de cheby')
plt.plot()

plt.show()