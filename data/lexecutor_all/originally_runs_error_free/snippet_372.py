# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def print_msg(msg):
    _l_(1543852)

    # This is the outer enclosing function

    def printer():
        _l_(1543849)

        # This is the nested function
        _c_(1543847, _n_(1543845, "print", lambda: print), _n_(1543846, "msg", lambda: msg))
        _l_(1543848)
    aux = _n_(1543850, "printer", lambda: printer)  # returns the nested function
    _l_(1543851)  # returns the nested function

    return aux  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = _c_(1543854, _n_(1543853, "print_msg", lambda: print_msg), "Hello")
_l_(1543855)
_c_(1543857, _n_(1543856, "another", lambda: another))
_l_(1543858)

