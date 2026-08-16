import matplotlib.pyplot as plt
import numpy as np

mu = 3
sigma = 0.5
n = 2500
vals = np.random.normal(loc=mu, scale=sigma, size=n)
print(vals)

# 1. Crear el histograma con 30 barras
plt.hist(vals, bins=30, edgecolor="black", color="skyblue", density=True)

# 2. Agregar títulos y etiquetas a los ejes
plt.title("Distribución Normal (Campana de Gauss)")
plt.xlabel("Valores")
plt.ylabel("Densidad de probabilidad")

# 3. Mostrar el gráfico en pantalla
plt.show()
