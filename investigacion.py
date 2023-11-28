#Importacion de librerias usadas
import sympy as sp
#-----------Item 2----------------------
#a)
x = sp.Symbol('x')#variable simbolica referencias a x

sp.init_printing(use_latex='mathjax')#uso de latex para imprimir

fx = sp.tan(5*x)**2#variable de la funcion
resultado = sp.integrate(fx, x)# se integra con sympy
print("El resultado de la integral Indefinida es: ")
sp.pprint(resultado)#se impreme el resultado

#b)
x= sp.symbols('x')#variable simbolica referencias a x
fx2 = sp.cos(2*x)#variable de la funcion
resultado2 = sp.integrate(fx2, (x, 0, sp.pi))# se integra con sympy
print("\n\nEl resultado de la integral Definida es: ")
sp.pprint(resultado2)#resultados
#---------------------------------------
#-----------Item 3----------------------
import numpy as np
import matplotlib.pyplot as plt

#funciones
def f(x):
    return x**2

def g(x):
    return np.sin(x)

# Generar datos para x
x = np.linspace(-2, 2, 1000)

# Evaluar las funciones en los datos de x
y_f = f(x)
y_g = g(x)

# Encontrar puntos de intersección
intersecciones = np.where(np.abs(y_f - y_g) < 0.01)[0]

# Crea la gráfica
plt.plot(x, y_f, label='$f(x) = x^2$')#etiquetas
plt.plot(x, y_g, label='$g(x) = \sin(x)$')
plt.fill_between(x, np.minimum(y_f, y_g), np.maximum(y_f, y_g),
                where=(x >= x[intersecciones[0]]) & (x <= x[intersecciones[-1]]),
                color='gray', alpha=0.5, label='Área entre funciones')
plt.scatter(x[intersecciones], y_f[intersecciones], color='red')  # Marcar puntos de intersección
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)#activa la grilla
plt.show()#mostrar grafico
#---------------------------------------
#ejercicio 3 solido de revolucion
#librerias usadas
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Se define la funcion a graficar
def f(x):
    return x**2

#Genera datos para la función
x = np.linspace(0, 2, 100)
y = f(x)

# Genera datos para la rotación en 3D del grafico
theta = np.linspace(0, 2*np.pi, 100)
x_3d = np.outer(x, np.cos(theta))
y_3d = np.outer(x, np.sin(theta))
z_3d = np.outer(np.ones_like(x), y)

fig = plt.figure()#crea la figura
ax = fig.add_subplot(111, projection='3d')#y la rotacion en 3D

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