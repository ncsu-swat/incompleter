# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1118183/how-to-debug-in-django-the-good-way
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_a_(63116, _n_(63115, "register", lambda: register), "filter") 
def pdb(element):
    _l_(63124)

    try:
        import pdb; 
        _l_(63121)

    except ImportError:
        pass
    aux = _n_(63122, "element", lambda: element)
    _l_(63123)
    return aux

