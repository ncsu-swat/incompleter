#Source: https://stackoverflow.com/questions/47872010/attributeerror-module-sympy-has-no-attribute-polys
from sympy import integrate as inter
import sympy as sp
from sympy import symbols 

def f(x):
    f1 = (sp.exp(-x ** 2)) / (1 + x ** 2)
    f2 = (2 * (sp.cos(x)) ** 2) / (1 + (x - 4) ** 2)
    f = f1 + f2
    return(f)

def integrate_f_from0(b):
    x = symbols('x')
    a = inter(f(x), (x, 0, b))
    return(a)