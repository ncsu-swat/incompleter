# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50021737/detecting-type-errors-using-mypy-without-type-annotations
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def foo(x, y):
    _l_(383821)

    _c_(383819, _n_(383816, "print", lambda: print), _n_(383817, "x", lambda: x)[:_n_(383818, "y", lambda: y)])
    _l_(383820)

def main():
    _l_(383825)

    _c_(383823, _n_(383822, "foo", lambda: foo), 'abcde', '2')
    _l_(383824)

if _n_(383826, "__name__", lambda: __name__) == "__main__":
    _l_(383830)

    _c_(383828, _n_(383827, "main", lambda: main))
    _l_(383829)