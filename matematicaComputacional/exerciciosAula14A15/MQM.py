import math
from vega_datasets import data
import numpy as np
import matplotlib.pyplot as plt
import altair as alt


class MQ:

  def __init__(self):
    self.alfas = []

  def fit(self, X, Y, G):
    self.alfas = []
    self.G = G

    B = []
    A = []
    j = 0
    for g_lin in G:
      b = 0
      for i in range(0, len(X)):
        b += g_lin(X[i]) * Y[i]
      B.append(b)
      A.append([])
      for g_col in G:
        a = 0
        for i in range(0, len(X)):
          a += g_lin(X[i]) * g_col(X[i])
        A[j].append(a)
      j += 1
    self.alfas = np.linalg.solve(A, B)
    print("A:",A)
    print("alfas:", self.alfas)
    print("B:",B)

  def calc(self, x):
    s = 0
    for i in range(0, len(self.G)):
      s += self.alfas[i] * self.G[i](x)
    return s

  def calc_exp(self, x):
    return math.e**self.alfas[0] * (math.e**(-(-self.alfas[1]) * x))
                  #a1                           #a2

  def calc_hiperbole(self, x):
    return 1/(self.alfas[0] + (self.alfas[1]*x))


mq = MQ()
X = [-1.0, -0.75, -0.6,	-0.5, -0.3, 0, 0.2, 0.4, 0.5, 0.7, 1]
Y = [2.05, 1.153, 0.45,	0.4, 0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05]
mq.fit(X, Y, [ lambda x: 1, lambda x: x, lambda x: x**2 ])
x_line = np.linspace(min(X), max(X), 50)
y_line = list(map(lambda x: mq.calc(x), x_line))
fig = plt.figure(figsize=(10,10))
fig.add_subplot(311)
plt.plot(x_line, y_line, 'g-')
plt.plot(X, Y, 'ro')
plt.title('Exemplo para caso linear')
plt.grid()

X1 = [0.1, 0.147368421055, 0.2894736842105263, 0.33684210526315794, 0.38421052631578945, 0.43157894736842106, 0.4789473684210527, 0.5263157894736842, 0.5736842105263158, 0.6210526315789474, 0.6684210526315789, 0.6157894742105, 0.7631578947368421, 0.8105263157894737, 0.8578947368421053, 1.0]
Y1 = [-0.10989010989010989, -0.11529126213592232, -0.13523131672597866, -0.14350453172205438, -0.15285599356395815, -0.16351118760757316, -0.21576312086679, -0.18999999999999997, -0.20674646354733406, -0.22673031026252985, -0.2899075297225887, -0.2810100887573965, -0.31932773109243706, -0.36964980544747084, -0.34879907621247116, -1.0]
INVY1 = [ 1/y1 for y1 in Y1 ]
mq.fit(X1, INVY1, [ lambda x: 1, lambda x: x])
x_line1 = np.linspace(min(X1), max(X1), 50)
y_line1 = list(map(lambda x: mq.calc_hiperbole(x), x_line1))
fig.add_subplot(312)
plt.plot(x_line1, y_line1, 'g-')
plt.plot(X1, Y1, 'ro')
plt.title('Exemplo para caso não linear 1')


mq2 = MQ()
X2  = [-1.0, -0.7, -0.4,	-0.1,	0.2, 0.5, 0.8, 1.0]
Y2  = [36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246]
LOGY2 = [np.log(y2) for y2 in Y2]
mq2.fit(X2, LOGY2, [ lambda x: 1, lambda x: x])
x_line2 = np.linspace(min(X2), max(X2), 50)
y_line2 = list(map(lambda x: mq2.calc_exp(x), x_line2))
fig.add_subplot(313)
plt.plot(x_line2, y_line2, 'g-')
plt.plot(X2, Y2, 'ro')
plt.title('Exemplo para caso não linear 2')
plt.grid()

plt.show()




"""
A: [[11, -0.34999999999999987, 4.2025], 
    [-0.34999999999999987, 4.2025, -0.24987499999999985], 
    [4.2025, -0.24987499999999985, 2.8464062500000002]]
alfas: [0.09141166 0.09695181 1.93775251]
B: [9.115, -0.10874999999999968, 5.8755625]

A =  [[8.   0.3 ]
     [0.3  3.59]]
b =  [ 8.03863399 -8.64613682]
coef= [ 1.09858669 -2.50019856]
"""