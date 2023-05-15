import numpy as np


def newtonRaphson(f, derivada, x0, e1=0.000001, e2=0.000001, it_max=100000000):
    if (abs(f(x0)) < e1):
        return x0
    
    k = 1
    x = x0 - (f(x0)/derivada(x0))
    while (abs(f(x)) > e1 and abs(x - x0) > e2 and k < it_max):
        print(f'x={x}, f(x)={f(x)}, k={k}')
        x0 = x
        x = x - (f(x)/derivada(x))
        k += 1

    return (x, f(x), k)

res = newtonRaphson(lambda x: x**np.sin(x) - 1, lambda x: x*np.sin(x)*(np.log(x)*np.cos(x) + np.sin(x)/x), 0.5, 5*10**-4, 5*10**-4)
print(res)