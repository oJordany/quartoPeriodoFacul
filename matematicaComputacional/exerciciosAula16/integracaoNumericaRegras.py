import numpy as np
import math

# FUNÇÃO QUE A GENTE VAI INTEGRAR
def f(x):
  # y = np.exp(x) → Isso pra quado for função
  # qunado for valor tabelado a gente passa em um dicionário e vai dando return
  d = {0.0:1.5, 0.5:2.0, 1.0:2.0, 1.5:1.6364, 2.0:1.25, 2.5:0.9565}
  y = d[x]
  return y


def trapezio(x):
  h = x[1] - x[0]
  baseMedia = (f(x[0])+f(x[1]))/2
  y = h * baseMedia
  return y


def trapeziosRepetidos(x):
  n = len(x)
  h = x[1] - x[0]
  soma = (f(x[0])+f(x[n-1]))
  for e in x[1:n-1]:
    soma = soma + 2*f(e)
  y = soma * h/2
  return y


def simpsonRepetido(x):
  n = len(x)
  h = x[1] - x[0]
  soma = (f(x[0])+f(x[n-1]))
  for i in range(1, n-1):
    if (i % 2 == 1):
      soma = soma + 4*f(x[i])
    else:
      soma = soma + 2*f(x[i])
    
  y = soma * h/3
  return y


xT = [0, 2.5]                 # Caso seja a regra do trapézio

print(f"It = {trapezio(xT)}")

xTR = np.arange(0, 2.6, 0.5)  # Caso seja a regra dos trapézios repetidos 

print(f"Itr = {trapeziosRepetidos(xTR)}")

xSR = np.arange(0, 2.1, 0.5)  # Caso seja a regra do Simpson Repetida e não dê pra dividir todos os intervalos

I1 = simpsonRepetido(xSR)

xT = [2.0, 2.5]                # O que sobrar eu aplico trapézio
I2 = trapezio(xT)
print(f"I1 = {I1}, I2 = {I2}, IT = {I1 + I2}")
print(f"ISr = {simpsonRepetido(xSR)}")

# prec = float(input("Entre com a precisão: "))
# maximo = max(f(xTR))
# h = (12*prec/maximo)**(0.5)
# n = 1/h

# print("Número de subintevalos: ", math.ceil(n))