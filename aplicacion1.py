# 1. Se te encarga la creacion de un proyecto de diseno de antenas destinado a una red inalambrica
# de alta velocidad. Tu objetivo es crear una antena parabolica que logre concentrar las senales
# de manera eficiente. La curva que describe la seccion transversal de la antena es f(x) en el
# intervalo [0, 5] metros, donde x representa la distancia desde el centro de la antena en metros,
# y f(x) representa la altura en metros. La funcion que modela esta curva es la siguiente:
# f(x) = 0, 1(x) **2 + 0, 5x + a, con a el numero de su equipo.
# a) Representa graficamente la antena parabolica generada al realizar un solido de revolucion
# con esta curva a traves de Python
# b) ¿Cual es el volumen de la antena? Deja expresado en terminos de π.

import numpy as np
import matplotlib.pyplot as plt


# Definir la función de la curva
def f(x, a):
    return 0.1 * x**2 + 0.5 * x + a


# Definir el intervalo [0, 5]
x_values = np.linspace(0, 5, 100)

# Elegir un valor para 'a'
a_value = 2

# Calcular los valores de la función en el intervalo
y_values = f(x_values, a_value)

# Crear la figura y el eje
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Representar la curva 2D
ax.plot(x_values, y_values, zs=0, zdir="z", label="Curva 2D")

# Generar las coordenadas de la superficie de revolución
X, Y = np.meshgrid(x_values, y_values)
Z = np.zeros_like(X)

# Crear la superficie de revolución
ax.plot_surface(X, Y, Z, color="c", alpha=0.5)

# Configurar etiquetas y título
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Antena Parabólica")

# Mostrar la gráfica
plt.show()


from scipy.integrate import quad
import numpy as np


# Definir la función de la curva
def f(x, a):
    return 0.1 * x**2 + 0.5 * x + a


# Función para la integración numérica
def integrando(x, a):
    return np.pi * f(x, a) ** 2


# Elegir un valor para 'a'
a_value = 2

# Calcular el volumen utilizando la integración numérica
volumen, error = quad(integrando, 0, 5, args=(a_value,))

# Mostrar el resultado
print(f"El volumen de la antena es: {volumen}π unidades cúbicas")
