import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def SA(n):
    return 0.1 * n + 30

def SB(n):
    return 0.05 * n**2 + 10 * n + 40

def difference_function(n):
    return SB(n) - SA(n)

# Crear un rango de valores de n en el intervalo [0, 1000]
n_values = np.arange(0, 1001, 1)

# Calcular las tasas de éxito para cada valor de n
success_rate_SA = SA(n_values)
success_rate_SB = SB(n_values)

# Calcular el área bajo la curva de la diferencia entre SA(n) y SB(n)

area, _ = integrate.quad(difference_function, 0, 1000)
area_aproximada = round(area, 2)
print(f"Área entre las curvas (aproximada): {area_aproximada}")

# Graficar las tasas de éxito
plt.figure(figsize=(10, 6))
plt.plot(n_values, success_rate_SA, label='SA(n) = 0.1n + 30')
plt.plot(n_values, success_rate_SB, label='SB(n) = 0.05n^2 + 10n + 40')

# Agregar etiquetas y leyenda
plt.title('Tasas de éxito de los algoritmos SA y SB con Área entre curvas')
plt.xlabel('Tamaño del conjunto (n)')
plt.ylabel('Tasa de éxito')
plt.legend()
plt.text(500, 10000, f'Área = {area_aproximada}', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

# Mostrar la gráfica
plt.grid(True)
plt.show()