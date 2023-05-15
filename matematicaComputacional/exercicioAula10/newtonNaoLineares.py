import numpy as np
from buscadorDePrecisao import buscadorDePrecisao


def eliminacaoDeGauss(A, b):
  for k in range(1, len(A)):
    # PIVOTEAMENTO PARCIAL
    for i in range(k+1, len(A)+1):
      if (abs(A[i-1][k-1]) > abs(A[k-1][k-1])):
        [A[k-1], A[i-1]] = [A[i-1], A[k-1]]
        [b[k-1], b[i-1]] = [b[i-1], b[k-1]]
    # ELIMINAÇÃO
    for i in range(k+1, len(A)+1):
      if (A[i-1][k-1] != 0):
        m = A[i-1][k-1]/A[k-1][k-1]
        A[i-1][k-1] = 0
        for j in range(k+1, len(A)+1):
          A[i-1][j-1] = A[i-1][j-1] - m * A[k-1][j-1]
        b[i-1] = b[i-1] - m * b[k-1]
  # RESOLUÇÃO DO SISTEMA
  x = [None for _ in range(0, len(b))]
  xn = b[-1]/A[-1][-1]
  x[-1] = xn
  for k in range(len(b) - 2, -1, -1):
    s = 0
    for j in range(k+1, len(b)):
      s = s + A[k][j]*x[j]
    x[k] = (b[k] - s)/A[k][k]

  return x


def verificar(mat, e):
    flag = False
    for i in range(0, len(mat)):
        if mat[i] < e:
            flag = flag or False
        else:
            return True
   
    return flag

def F(x):
    return np.matrix([
            x[0] + x[1] - 3,
            x[0]**2 + x[1]**2 - 9
         ])


def J(x):
    return np.matrix([
            [1, 1],
            [2*x[0], 2*x[1]]
         ])


def newtonNaoLinear(F, J, x0, e1=0.00000001, e2=0.00000001, it_max=100000000):
    k = 0
    Fx = F(x0)
    
    if not(verificar(abs(Fx).tolist()[0], e1)):
        return x0
    
    Fx = -Fx
    s = eliminacaoDeGauss(J(x0).tolist(), Fx.tolist()[0])
    x = np.matrix(x0) + s
    
    while (verificar(F(x.tolist()[0]).tolist()[0], e1) and verificar(abs(x-np.matrix(x0)).tolist()[0], e2) and k < it_max):
        x0 = x        
        x = np.matrix(x0) + s 
        Fx = -F(x.tolist()[0])
        s = eliminacaoDeGauss(J(x.tolist()[0]).tolist(), Fx.tolist()[0])            
        k += 1
    return (x.tolist()[0], k)

precisao = buscadorDePrecisao()
print(newtonNaoLinear(F, J, [1, 5], precisao, precisao))    
