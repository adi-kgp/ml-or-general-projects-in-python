import sympy as sp

x, y, z, l1, l2 = sp.symbols('x y z l1 l2')

f = 3*x - y -3*z
g = x + y - z
h = x**2 + 2*z**2 - 1


F = f + l1*g + l2*h

Fx = sp.diff(F, x)
Fy = sp.diff(F, y)
Fz = sp.diff(F, z)
Fl1 = sp.diff(F, l1)
Fl2 = sp.diff(F, l2)

solutions = sp.solve([Fx, Fy, Fz, Fl1, Fl2], [x, y, z, l1, l2])

print(solutions)