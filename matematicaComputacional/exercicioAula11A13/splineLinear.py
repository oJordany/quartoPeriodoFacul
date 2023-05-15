import numpy as np
import matplotlib.pyplot as plt


def splineLinear(xi, xiant, fxi, fxiant, x):
    from interpolacaoNewton import InterpoladorNewton
    _x = [xiant, xi]
    _y = [fxiant, fxi]
    IN = InterpoladorNewton(_x, _y)
    IN.construirTabelaDiferencaDividida()
    # si = (fxiant*(xi - x)/(xi - xiant)) + (fxi*(x - xiant)/(xi - xiant))
    si = IN.interpolarEm(x)
    return si


def geraSplineLinearNoIntervalo(xi, xiant, fxi, fxiant, t):
    yt = []
    for i in t:
        yt.append(splineLinear(xi, xiant, fxi, fxiant, i))
    return yt 


def geraSplineLinear(x, y):
    splinesTotal = []
    XsTotal = []
    YsTotal = []
    for i in range(len(x)-1):
        ti = np.linspace(x[i], x[i+1], 10)
        si = geraSplineLinearNoIntervalo(x[i+1], x[i], y[i+1], y[i], ti)
        splinesTotal.append([ti, si])
        XsTotal.append(x)
        YsTotal.append(y)

    return XsTotal, YsTotal, splinesTotal


def plotarGraficoDasSplines(XsTotal, YsTotal, splines):
    cores = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    plt.plot(XsTotal, YsTotal, 'bo')
    
    for cor, spline in enumerate(splines):
        plt.plot(spline[0], spline[1], f'{cores[cor%7]}-')

    plt.show()


x = np.linspace(0,10, num=11, endpoint=True)
fx = np.cos(-x**2/9.0)

XsTotal, YsTotal, sTotal = geraSplineLinear(x, fx)
# print(sTotal)
plotarGraficoDasSplines(XsTotal, YsTotal, sTotal)
