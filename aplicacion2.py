import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def SA(n):
    return 0.1 * n + 30

def SB(n):
    return 0.05 * n**2 + 10 * n + 40

def difference_function(n):
    return SB(n) - SA(n)

n_valor = np.arange(0, 1001, 1)

Exito_SA = SA(n_valor)
Exito_SB = SB(n_valor)

area, _ = integrate.quad(difference_function, 0, 1000)

area_aproximada = round(area, 3)
print(f"Área entre las curvas (aproximada): {area_aproximada}")

plt.figure(figsize=(10, 6))
plt.plot(n_valor, Exito_SA, label='SA(n) = 0.1n + 30')
plt.plot(n_valor, Exito_SB, label='SB(n) = 0.05n^2 + 10n + 40')

plt.fill_between(n_valor, Exito_SA, Exito_SB, color='lightblue', alpha=0.5, label='Área entre curvas')

plt.title('Tasas de éxito de los algoritmos SA y SB con Área entre curvas')
plt.xlabel('Tamaño del conjunto (n)')
plt.ylabel('Tasa de éxito')
plt.legend()

plt.text(500, 10000, f'Área = {area_aproximada}', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.grid(True)
plt.show()