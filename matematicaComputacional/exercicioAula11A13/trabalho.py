import numpy as np
import matplotlib.pyplot as plt
from interpolacaoNewton import InterpoladorNewton
import splineQuadratica

def poli15(x):
    """
    polinômio de grau 15
    :param x: int
    """
    return np.sin(np.pi*x**15)/np.pi*x + 1/(1+25*x**2)


def poli18(x):
    """
    polinômio de grau 18
    :param x: int
    """
    return (x**18 - 2**18 - x**8) * 1/(1+25*x**2)

# PONTOS IGUALMENTE ESPAÇADOS
x5pts = np.linspace(-1, 1, 5)
x8pts = np.linspace(-1, 1, 8)
x10pts = np.linspace(-1, 1, 11)
# PARA UM POLINÔMIO DE GRAU 15
y5ptsPoli15 = [poli15(x) for x in x5pts]
y8ptsPoli15 = [poli15(x) for x in x8pts]
y10ptsPoli15 = [poli15(x) for x in x10pts]

IN5pts = InterpoladorNewton(x5pts, y5ptsPoli15)
IN5pts.construirTabelaDiferencaDividida()
IN8pts = InterpoladorNewton(x8pts, y8ptsPoli15)
IN8pts.construirTabelaDiferencaDividida()
IN10pts = InterpoladorNewton(x10pts, y10ptsPoli15)
IN10pts.construirTabelaDiferencaDividida()

x100Poli15 = np.linspace(-1, 1, 100)
y5funcPoli15 = [poli15(x) for x in x100Poli15]
y5interpPoli15 = [IN5pts.interpolarEm(x) for x in x100Poli15]
y8interpPoli15 = [IN8pts.interpolarEm(x) for x in x100Poli15]
y10interpPoli15 = [IN10pts.interpolarEm(x) for x in x100Poli15]

# fig = plt.figure(figsize=(20,15))
# fig.suptitle('Interpolação para o polinômio de grau 15')
# fig.add_subplot(221)
# plt.plot(x100Poli15, y5funcPoli15, 'k-', label='polinômio de grau 15')
# plt.plot(x5pts,y5ptsPoli15,'bo', label='5 pts igualmente espaçados')
# plt.plot(x100Poli15, y5interpPoli15, 'm-', label='função interpoladora para os 5 pts')
# plt.title('Gráfico com os 5 pontos igualmente espaçados')
# plt.grid() 
# plt.legend()
# fig.add_subplot(222)
# plt.plot(x100Poli15, y5funcPoli15, 'k-', label='polinômio de grau 15')
# plt.plot(x8pts,y8ptsPoli15,'ro', label='8 pts igualmente espaçados')
# plt.plot(x100Poli15, y8interpPoli15, 'y-', label='função interpoladora para os 8 pts')
# plt.title('Gráfico com os 8 pontos igualmente espaçados')
# plt.grid() 
# plt.legend()
# fig.add_subplot(223)
# plt.plot(x100Poli15, y5funcPoli15, 'k-', label='polinômio de grau 15')
# plt.plot(x10pts,y10ptsPoli15,'go', label='11 pts igualmente espaçados')
# plt.plot(x100Poli15, y10interpPoli15, 'c-', label='função interpoladora para os 11 pts')
# plt.title('Gráfico com os 11 pontos igualmente espaçados')
# plt.grid() 
# plt.legend()
# # plt.show()
# XsTotal, YsTotal, sTotal = splineQuadratica.geraSplineQuadratica(x10pts, y10ptsPoli15)
# fig.add_subplot(224)
# plt.plot(x100Poli15, y5funcPoli15, 'k-', label='polinômio de grau 15')
# plt.plot(x100Poli15, y10interpPoli15, 'c-', label='func interpoladora para os 11 pts')
# plt.title('Gráfico comparando func de 11pts com a spline quadrática')
# plt.grid()
# splineQuadratica.plotarGraficoDasSplines(XsTotal, YsTotal, sTotal)

# PARA UM POLINÔMIO DE GRAU 18
# y5ptsPoli18 = [poli18(x) for x in x5pts]
# y8ptsPoli18 = [poli18(x) for x in x8pts]
# y10ptsPoli18 = [poli18(x) for x in x10pts]

# IN5pts = InterpoladorNewton(x5pts, y5ptsPoli18)
# IN5pts.construirTabelaDiferencaDividida()
# IN8pts = InterpoladorNewton(x8pts, y8ptsPoli18)
# IN8pts.construirTabelaDiferencaDividida()
# IN10pts = InterpoladorNewton(x10pts, y10ptsPoli18)
# IN10pts.construirTabelaDiferencaDividida()

# x100Poli18 = np.linspace(-1, 1, 100)
# y5funcPoli18 = [poli18(x) for x in x100Poli18]
# y5interpPoli18 = [IN5pts.interpolarEm(x) for x in x100Poli18]
# y8interpPoli18 = [IN8pts.interpolarEm(x) for x in x100Poli18]
# y10interpPoli18 = [IN10pts.interpolarEm(x) for x in x100Poli18]

# fig = plt.figure(figsize=(20,15))
# fig.suptitle('Interpolação para o polinômio de grau 18')
# fig.add_subplot(221)
# plt.plot(x100Poli18, y5funcPoli18, 'k-', label='polinômio de grau 18')
# plt.plot(x5pts,y5ptsPoli18,'bo', label='5 pts igualmente espaçados')
# plt.plot(x100Poli18, y5interpPoli18, 'm-', label='função interpoladora para os 5 pts')
# plt.title('Gráfico com os 5 pontos igualmente espaçados')
# plt.grid() 
# plt.legend()
# fig.add_subplot(222)
# plt.plot(x100Poli18, y5funcPoli18, 'k-', label='polinômio de grau 18')
# plt.plot(x8pts,y8ptsPoli18,'ro', label='8 pts igualmente espaçados')
# plt.plot(x100Poli18, y8interpPoli18, 'y-', label='função interpoladora para os 8 pts')
# plt.title('Gráfico com os 8 pontos igualmente espaçados')
# plt.grid() 
# plt.legend()
# fig.add_subplot(223)
# plt.plot(x100Poli18, y5funcPoli18, 'k-', label='polinômio de grau 18')
# plt.plot(x10pts,y10ptsPoli18,'go', label='11 pts igualmente espaçados')
# plt.plot(x100Poli18, y10interpPoli18, 'c-', label='função interpoladora para os 11 pts')
# plt.title('Gráfico com os 11 pontos igualmente espaçados')
# plt.grid() 
# plt.legend()
# # plt.show()
# XsTotal2, YsTotal2, sTotal2 = splineQuadratica.geraSplineQuadratica(x10pts, y10ptsPoli18)
# fig.add_subplot(224)
# plt.plot(x100Poli18, y5funcPoli18, 'k-', label='polinômio de grau 18')
# plt.plot(x100Poli18, y10interpPoli18, 'c-', label='func interpoladora para os 11 pts')
# plt.title('Gráfico comparando func de 11pts com a spline quadrática')
# plt.grid()
# splineQuadratica.plotarGraficoDasSplines(XsTotal2, YsTotal2, sTotal2)
