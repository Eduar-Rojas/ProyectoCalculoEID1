import numpy as np
import matplotlib.pyplot as plt

def SA(n):
    return 0.1 * n + 30

def SB(n):
    return 0.05 * n**2 + 10 * n + 40

n_values = np.arange(0, 1001, 1)

success_rate_SA = SA(n_values)
success_rate_SB = SB(n_values)

plt.figure(figsize=(10, 6))
plt.plot(n_values, success_rate_SA, label='SA(n) = 0.1n + 30')
plt.plot(n_values, success_rate_SB, label='SB(n) = 0.05n^2 + 10n + 40')

plt.title('Tasas de éxito de los algoritmos SA y SB')
plt.xlabel('Tamaño del conjunto (n)')
plt.ylabel('Tasa de éxito')
plt.legend()

plt.grid(True)
plt.show()