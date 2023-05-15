import numpy as np
import matplotlib.pyplot as plt


def splineQuadratica(Xs, Ys, x):
    from interpolacaoNewton import InterpoladorNewton
    IN = InterpoladorNewton(Xs, Ys)
    IN.construirTabelaDiferencaDividida()
    # si = (fxiant*(xi - x)/(xi - xiant)) + (fxi*(x - xiant)/(xi - xiant))
    si = IN.interpolarEm(x)
    return si


def geraSplineQuadraticaNosPontos(Xs, Ys, t):
    yt = []
    for i in t:
        yt.append(splineQuadratica(Xs, Ys, i))
    return yt 


def geraSplineQuadratica(x, y):
    splinesTotal = []
    XsTotal = []
    YsTotal = []
    for i in range(0,len(x)-3, 2):
        ti = np.linspace(x[i], x[i+2], 100)
        Xs = [x[i], x[i+1], x[i+2], x[i+3]]
        Ys = [y[i], y[i+1], y[i+2], y[i+3]]
        si = geraSplineQuadraticaNosPontos(Xs, Ys, ti)
        splinesTotal.append([ti, si])
        XsTotal = [*XsTotal[:], *Xs[:]]
        YsTotal = [*YsTotal[:], *Ys[:]]

    return XsTotal, YsTotal, splinesTotal


def plotarGraficoDasSplines(XsTotal, YsTotal, splines):
    cores = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    plt.plot(XsTotal, YsTotal, 'bo')
    for cor, spline in enumerate(splines):
        plt.plot(spline[0], spline[1], f'{cores[cor%7]}-')

    plt.show()


x = np.linspace(0,10, num=11, endpoint=True)
fx = np.cos(-x**2/9.0)

XsTotal, YsTotal, sTotal = geraSplineQuadratica(x, fx)
# print(sTotal)
plotarGraficoDasSplines(XsTotal, YsTotal, sTotal)