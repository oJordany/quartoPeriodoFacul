from decimal import Decimal

def buscadorDePrecisao(valorDeReferencia):
  A = 1
  s = valorDeReferencia + A

  while s > valorDeReferencia: # 11 > 10
    A = A/2 # 0.5 → 0.25
    s = valorDeReferencia + A # 10.5 → 10.25

  prec = A*2

  print(f'precisão com variável de precisão simples: {prec}')
  print(f'precisão com variável de precisão dupla: {Decimal(prec)}')

while (True):
  valorDeReferencia = float(input("Insira o valor de referência [Digite 0 para parar]: "))
  if valorDeReferencia == 0:
    break
  buscadorDePrecisao(valorDeReferencia)
