import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def parabola(x):
    return np.sqrt(10 * x)

x_valores = np.linspace(0, 5, 400)

valorpositivo = parabola(x_valores)
y_valornegativo = -parabola(x_valores)

x, theta = np.meshgrid(x_valores, np.linspace(0, 2*np.pi, 100))

X = x
Y = valorpositivo * np.cos(theta)
Z = valorpositivo * np.sin(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.5, cmap='inferno')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Sólido de revolución de la parábola $y^2 = 10x$')

plt.show()