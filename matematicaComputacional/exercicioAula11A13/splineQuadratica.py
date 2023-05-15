import numpy as np
import matplotlib.pyplot as plt


def splineQuadratica(Xs, Ys, x):
    from interpolacaoNewton import InterpoladorNewton
    IN = InterpoladorNewton(Xs, Ys)
    IN.construirTabelaDiferencaDividida()
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
    for i in range(0,len(x)-2, 2):
        ti = np.linspace(x[i], x[i+2], 100)
        Xs = [x[i], x[i+1], x[i+2]]
        Ys = [y[i], y[i+1], y[i+2]]
        si = geraSplineQuadraticaNosPontos(Xs, Ys, ti)
        splinesTotal.append([ti, si])
        XsTotal = [*XsTotal[:], *Xs[:]]
        YsTotal = [*YsTotal[:], *Ys[:]]

    return XsTotal, YsTotal, splinesTotal


def plotarGraficoDasSplines(Xs, Ys, splines):
    # cores = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    cores = ['r']
    splineX = [*splines[0][0]]
    splineY = [*splines[0][1]]
    for spline in splines[1:]:
        splineX += [*spline[0][1:]]
        splineY += [*spline[1][1:]]
    
    plt.plot(Xs, Ys, 'go', label="11 pts igualmente espaçados")
    
    # for cor, spline in enumerate(splines):
        # plt.plot(spline[0], spline[1], f'{cores[cor%7]}-', label="função com spline quadrática")
    plt.plot(splineX, splineY, f'{cores[1%1]}-', label="função com spline quadrática")
    plt.legend()
    plt.show()


# x = np.linspace(0,10, num=11, endpoint=True)
# fx = np.cos(-x**2/9.0)

# XsTotal, YsTotal, sTotal = geraSplineQuadratica(x, fx)
# # print(sTotal)
# plotarGraficoDasSplines(XsTotal, YsTotal, sTotal)
