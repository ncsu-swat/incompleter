# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49304400/python-a-type-error-caused-by-what
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import maya.cmds as mc
    _l_(687359)

except ImportError:
    pass

attributes = ['.t', '.r', '.s']
_l_(687360)

controllers = _c_(687363, _a_(687362, _n_(687361, "mc", lambda: mc), "ls"), 'ctrl_Lip*', tr=True)
_l_(687364)

for controller in _n_(687365, "controllers", lambda: controllers):
    _l_(687372)

    _c_(687370, _a_(687367, _n_(687366, "mc", lambda: mc), "duplicate"), _n_(687368, "controller", lambda: controller), n=_n_(687369, "controller", lambda: controller)+'_proxy')
    _l_(687371)

def corresponding_proxy(controller):
    _l_(687375)

    aux = _n_(687373, "controller", lambda: controller)+'_proxy'
    _l_(687374)
    return aux

for controller in _n_(687376, "controllers", lambda: controllers):
    _l_(687389)

    for attr in _n_(687377, "attributes", lambda: attributes):
        _l_(687388)

        _c_(687386, _a_(687379, _n_(687378, "mc", lambda: mc), "connectAttr"), _n_(687380, "controller", lambda: controller)+_n_(687381, "attr", lambda: attr), _c_(687384, _n_(687382, "corresponding_proxy", lambda: corresponding_proxy), _n_(687383, "controller", lambda: controller))+_n_(687385, "attr", lambda: attr))
        _l_(687387)