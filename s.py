import sympy as sp

#Se define la variable simbólica t
t = sp.symbols('t')
#la función de tasa de transferencia
T_t = 4 * t

#Se Define la integral para encontrar la cantidad total de datos transferidos
D = sp.integrate(T_t, (t, 0, 6))

# Se imprime el resultado
print(f"La cantidad total de datos transferidos en los primeros 6 segundos es: {D} kilobits.")
