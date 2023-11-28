import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def f(x):
    return 0.1 * x**2 + 0.5 * x + 0.625

def parabola(x, a, b, c):
    return a * x**2 + b * x + c

<<<<<<< HEAD
def encontrar_vertice(params):
    a, b, c = params
=======
def encontrar_vertice(param):
    a, b, c = param
>>>>>>> c8352385a637fd55e9cfc08915cf7fa9c8e1fdae
    h = -b / (2 * a)
    k = parabola(h, a, b, c)
    return k

<<<<<<< HEAD
params_iniciales = [0.1, 0.5, 0.625]
resultado = minimize(encontrar_vertice, params_iniciales)
=======
parametros = [0.1, 0.5, 0.625]
resultado = minimize(encontrar_vertice, parametros)
>>>>>>> c8352385a637fd55e9cfc08915cf7fa9c8e1fdae
a_optimo, b_optimo, c_optimo = resultado.x

x = np.linspace(0, 5, 100)
y = f(x)

x_parabola = np.linspace(-5, 7.5, 100)
y_parabola = parabola(x_parabola, a_optimo, b_optimo, c_optimo)

h_optimo = -b_optimo / (2 * a_optimo)
k_optimo = parabola(h_optimo, a_optimo, b_optimo, c_optimo)

plt.plot(x_parabola, y_parabola, label='Parábola generada', linestyle='--')
plt.plot(x, y, label='Curva original')
plt.scatter(h_optimo, k_optimo, color='red', label='Punto Focal')
plt.title('Antena Parabólica')
plt.xlabel('Distancia desde el centro (metros)')
plt.ylabel('Altura (metros)')
plt.legend()
plt.grid(True)
plt.show()