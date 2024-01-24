# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49304400/python-a-type-error-caused-by-what
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import maya.cmds as mc
    _l_(676733)

except ImportError:
    pass

attributes = ['.t', '.r', '.s']
_l_(676734)

controllers = _c_(676737, _a_(676736, _n_(676735, "mc", lambda: mc), "ls"), 'ctrl_Lip*')
_l_(676738)

def corresponding_proxy(controller):
    _l_(676746)

    corresponding_proxy = _c_(676742, _a_(676740, _n_(676739, "mc", lambda: mc), "ls"), _n_(676741, "controller", lambda: controller)+'_proxy')
    _l_(676743)
    aux = _n_(676744, "corresponding_proxy", lambda: corresponding_proxy)
    _l_(676745)
    return aux

for controller in _n_(676747, "controllers", lambda: controllers) :
    _l_(676760)

    for attr in _n_(676748, "attributes", lambda: attributes) :
        _l_(676759)

        _c_(676757, _a_(676750, _n_(676749, "mc", lambda: mc), "connectAttr"), _n_(676751, "controller", lambda: controller)+_n_(676752, "attr", lambda: attr), _c_(676755, _n_(676753, "corresponding_proxy", lambda: corresponding_proxy), _n_(676754, "controller", lambda: controller))+_n_(676756, "attr", lambda: attr))
        _l_(676758)