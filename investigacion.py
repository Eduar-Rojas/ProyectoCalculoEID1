import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
#-----------Item 2----------------------
#a)
x = sp.Symbol('x')

sp.init_printing(use_latex='mathjax')

fx = sp.tan(5*x)**2
resultado = sp.integrate(fx, x)
print("El resultado de la integral Indefinida es: ")
sp.pprint(resultado)

#b)
x= sp.symbols('x')
fx2 = sp.cos(2*x)
resultado2 = sp.integrate(fx2, (x, 0, sp.pi))
print("\n\nEl resultado de la integral Definida es: ")
sp.pprint(resultado2)
#---------------------------------------
#-----------Item 3----------------------

# Definir las funciones
def f(x):
    return x**2

def g(x):
    return np.sin(x)

# Crear valores x
x_values = np.linspace(-2, 2, 100)

# Calcular los valores y para cada función
y1_values = f(x_values)
y2_values = g(x_values)

# Graficar las funciones
plt.plot(x_values, y1_values, label='x^2')
plt.plot(x_values, y2_values, label='sin(x)')

# Rellenar el área entre las funciones
plt.fill_between(x_values, y1_values, y2_values, where=(y1_values > y2_values), color='gray', alpha=0.3, interpolate=True, label='Área entre funciones')

# Configuración adicional
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Intersección de Funciones y Área Entre Ellas')
plt.grid(True)
plt.show()
#---------------------------------------


# Definir la función para el sólido de revolución
def f(x):
    return x**2

# Crear valores x
x_values = np.linspace(0, 2, 100)

# Calcular los valores y para la función
y_values = f(x_values)

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar el sólido de revolución
ax.plot(x_values, y_values, zs=0, zdir='z', label='Sólido de Revolución')

# Configuración adicional
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title('Sólido de Revolución en 3D')

plt.show()

