
import numpy as np
import matplotlib.pyplot as plt

#funciones
def f(x):#funcion 1
    return x**2


def g(x):#funcion 2
    return np.sin(x)


valor_x = np.linspace(-2, 2, 100)# Crear valores x


# Calcular los valores y para cada función de prueba
valor_y1 = f(valor_x)
valor_y2 = g(valor_x)


# Graficar las funciones con matplotlib
plt.plot(valor_x, valor_y1, label='x^2')
plt.plot(valor_x, valor_y2, label='sin(x)')


# Rellenar el área entre las funciones
plt.fill_between(valor_x, valor_y1, valor_y2, where=(valor_y1 > valor_y2), color='gray', alpha=0.3, interpolate=True, label='Área entre funciones')
#configuración del gráfico(visual)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=1)  # Línea horizontal del eje y 
plt.axvline(0, color='black', linewidth=1)  # Línea vertical del eje x en x=0

plt.legend()
plt.title('Intersección de Funciones y Área Entre Ellas')
plt.grid(True)#activa la grilla
plt.show()# muestra el gráfico

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la función a graficar
def f(x):
    return x**2

# Generar datos para la función
x = np.linspace(0, 2, 100)
y = f(x)

# Generar datos para la rotación en 3D
theta = np.linspace(0, 2*np.pi, 100)
x_3d = np.outer(x, np.cos(theta))
y_3d = np.outer(x, np.sin(theta))
z_3d = np.outer(np.ones_like(x), y)

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar el sólido de revolución
ax.plot_surface(x_3d, y_3d, z_3d, color='lightblue', alpha=0.8)

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título del gráfico
ax.set_title('Sólido de Revolución')

# Mostrar el gráfico
plt.show()



#_----
