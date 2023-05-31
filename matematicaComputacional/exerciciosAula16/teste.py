import numpy as np
import matplotlib.pyplot as plt

# Definir a função
def f(x):
    return x**2

# Definir os limites inferior e superior do gráfico
x_min = -2
x_max = 2

# Definir os limites inferior e superior para preenchimento da área
x_start = -1
x_end = 1

# Gerar uma série de pontos para traçar a função
x = np.linspace(x_min, x_max, 100)
y = f(x)

# Plotar a função
plt.plot(x, y)

# Obter os índices correspondentes aos limites de preenchimento da área
idx_start = np.argmin(np.abs(x - x_start))
idx_end = np.argmin(np.abs(x - x_end))

# Preencher a área entre os limites definidos
plt.fill_between(x[idx_start:idx_end+1], y[idx_start:idx_end+1], color='gray', alpha=0.5)

# Exibir o gráfico
plt.show()