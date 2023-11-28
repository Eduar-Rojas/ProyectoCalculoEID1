# ---------Área del sólido de revolución----------------------

import sympy as sp

x = sp.symbols("x")  # variable simbólica referencias a x
fx2 = sp.pi * 10 * x  # variable de la función
resultado2 = sp.integrate(fx2, (x, 0, 5))  # se integra con sympy
print("\n\nEl resultado de la integral Definida es: ")
sp.pprint(resultado2)  # resultados
