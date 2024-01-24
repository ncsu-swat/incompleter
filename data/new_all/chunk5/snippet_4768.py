# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49259443/im-overlooking-something-typeerror-create-got-unexpected-keyword-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class SystemManager(_a_(701916, _n_(701915, "models", lambda: models), "Manager")):
    _l_(701936)

    """"""
    def create(self, project, system_name):
        _l_(701935)

        system = _c_(701921, _a_(701918, _n_(701917, "super", lambda: super)(), "create"), project=_n_(701919, "project", lambda: project), system_name=_n_(701920, "system_name", lambda: system_name))
        _l_(701922)
        _c_(701925, _a_(701924, _n_(701923, "system", lambda: system), "save"))
        _l_(701926)

        _c_(701931, _a_(701929, _a_(701928, _n_(701927, "Circuit", lambda: Circuit), "objects"), "create"), system=_n_(701930, "system", lambda: system), circuit_name="Primary circuit")
        _l_(701932)
        aux = _n_(701933, "system", lambda: system)
        _l_(701934)
        return aux

class System(_a_(701938, _n_(701937, "models", lambda: models), "Model")):
    _l_(701961)

    objects = _c_(701940, _n_(701939, "SystemManager", lambda: SystemManager))
    _l_(701941)

    project     = _c_(701944, _a_(701942, models, "ForeignKey"), 'solgeo.Project', related_name='systems', on_delete=_a_(701943, models, "CASCADE"))
    _l_(701945)
    system_name = _c_(701947, _a_(701946, models, "CharField"), max_length=200)
    _l_(701948)

    @_n_(701949, "classmethod", lambda: classmethod)
    def create(cls, project):
        _l_(701954)

        system = _c_(701952, _n_(701950, "cls", lambda: cls), project=_n_(701951, "project", lambda: project))
        _l_(701953)

    def __str__(self):
        _l_(701960)

        aux = "system name: " + _c_(701958, _n_(701955, "str", lambda: str), _a_(701957, _n_(701956, "self", lambda: self), "system_name"))
        _l_(701959)
        return aux

class CircuitManager(_a_(701963, _n_(701962, "models", lambda: models), "Manager")):
    _l_(701977)

    """"""
    def create(self, project, system_name):
        _l_(701976)

        circuit = _c_(701968, _a_(701965, _n_(701964, "super", lambda: super)(), "create"), system=_n_(701966, "system", lambda: system), circuit_name=_n_(701967, "circuit_name", lambda: circuit_name))
        _l_(701969)
        _c_(701972, _a_(701971, _n_(701970, "circuit", lambda: circuit), "save"))
        _l_(701973)
        aux = _n_(701974, "circuit", lambda: circuit)
        _l_(701975)
        return aux


class Circuit(_a_(701979, _n_(701978, "models", lambda: models), "Model")):
    _l_(701991)

    """Models a hydraulic circuit"""
    objects = _c_(701981, _n_(701980, "CircuitManager", lambda: CircuitManager))
    _l_(701982)

    system = _c_(701986, _a_(701983, models, "ForeignKey"), _n_(701984, "System", lambda: System), related_name='circuits', on_delete=_a_(701985, models, "CASCADE"))
    _l_(701987)
    circuit_name = _c_(701989, _a_(701988, models, "CharField"), max_length=200)
    _l_(701990)