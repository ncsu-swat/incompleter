# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56812810/sympy-physics-units-substitution-gives-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sympy.parsing.sympy_parser import parse_expr
    _l_(426337)

except ImportError:
    pass
try:
    from sympy.physics import units
    _l_(426339)

except ImportError:
    pass

_c_(426343, _n_(426340, "type", lambda: type), _a_(426342, _n_(426341, "units", lambda: units), "newton")) # -> sympy.physics.units.quantities.Quantity
_l_(426344) # -> sympy.physics.units.quantities.Quantity

_c_(426350, _a_(426347, _c_(426346, _n_(426345, "parse_expr", lambda: parse_expr), '2*Newton'), "subs"), {'Newton':_a_(426349, _n_(426348, "units", lambda: units), "newton")}) # -> 2N
_l_(426351) # -> 2N
_c_(426357, _a_(426354, _c_(426353, _n_(426352, "parse_expr", lambda: parse_expr), '2*newton'), "subs"), {'newton':_a_(426356, _n_(426355, "units", lambda: units), "newton")}) # -> 2N
_l_(426358) # -> 2N
_c_(426364, _a_(426361, _c_(426360, _n_(426359, "parse_expr", lambda: parse_expr), '2*n'), "subs"), {'n':_a_(426363, _n_(426362, "units", lambda: units), "newton")}) # -> 2N
_l_(426365) # -> 2N
_c_(426371, _a_(426368, _c_(426367, _n_(426366, "parse_expr", lambda: parse_expr), '2*N'), "subs"), {'N':_a_(426370, _n_(426369, "units", lambda: units), "newton")}) # -> raises TypeError below
_l_(426372) # -> raises TypeError below
_c_(426376, _a_(426375, _c_(426374, _n_(426373, "parse_expr", lambda: parse_expr), 'N'), "subs")) # -> raises AttributeError below
_l_(426377) # -> raises AttributeError below
_c_(426379, _n_(426378, "parse_expr", lambda: parse_expr), 'N') # -> <function sympy.core.evalf.N(x, n=15, **options)>
_l_(426380) # -> <function sympy.core.evalf.N(x, n=15, **options)>