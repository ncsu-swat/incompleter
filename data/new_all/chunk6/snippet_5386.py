# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59626524/typeerror-a-class-meth-missing-1-required-positional-argument-a-class-meth
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class A():
    _l_(364288)

    def __init__(self,init_var):
        _l_(364283)

        _n_(364280, "self", lambda: self).init_var = _n_(364281, "init_var", lambda: init_var)
        _l_(364282)

    def A_class_meth(self, A_class_meth_var1):
        _l_(364287)

        _c_(364285, _n_(364284, "print", lambda: print), "run")
        _l_(364286)

class B():
    _l_(364300)

    def Start(self):
        _l_(364299)

        _n_(364289, "self", lambda: self).B_class_var = _c_(364291, _n_(364290, "A", lambda: A), "NAME")
        _l_(364292)
        _c_(364297, _a_(364294, _n_(364293, "A", lambda: A), "A_class_meth"), _a_(364296, _n_(364295, "self", lambda: self), "B_class_var"))
        _l_(364298)

var = _c_(364302, _n_(364301, "B", lambda: B))
_l_(364303)
_c_(364306, _a_(364305, _n_(364304, "var", lambda: var), "Start"))
_l_(364307)