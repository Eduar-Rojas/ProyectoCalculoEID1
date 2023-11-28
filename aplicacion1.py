import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def f(x):
    return 0.1 * x**2 + 0.5 * x + 0.625


def parabola(x, a, b, c):
    return a * x**2 + b * x + c


def encontrar_vertice(param):
    a, b, c = param
    h = -b / (2 * a)
    k = parabola(h, a, b, c)
    return k


parametros = [0.1, 0.5, 0.625]
resultado = minimize(encontrar_vertice, parametros)
a_optimo, b_optimo, c_optimo = resultado.x

x = np.linspace(0, 5, 100)
y = f(x)

x_parabola = np.linspace(-5, 7.5, 100)
y_parabola = parabola(x_parabola, a_optimo, b_optimo, c_optimo)

h_optimo = -b_optimo / (2 * a_optimo)
k_optimo = parabola(h_optimo, a_optimo, b_optimo, c_optimo)

plt.plot(x_parabola, y_parabola, label="Parábola generada", linestyle="--")
plt.plot(x, y, label="Curva original")
plt.scatter(h_optimo, k_optimo, color="red", label="Punto Focal")
plt.title("Antena Parabólica")
plt.xlabel("Distancia desde el centro (metros)")
plt.ylabel("Altura (metros)")
plt.legend()
plt.grid(True)
plt.show()
