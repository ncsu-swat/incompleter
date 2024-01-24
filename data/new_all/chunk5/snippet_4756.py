# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49304400/python-a-type-error-caused-by-what
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import maya.cmds as mc
    _l_(686465)

except ImportError:
    pass

attributes = ['.t', '.r', '.s']
_l_(686466)

controllers = _c_(686469, _a_(686468, _n_(686467, "mc", lambda: mc), "ls"), 'ctrl_Lip*', tr=True)
_l_(686470)

for controller in _n_(686471, "controllers", lambda: controllers):
    _l_(686478)

    _c_(686476, _a_(686473, _n_(686472, "mc", lambda: mc), "duplicate"), _n_(686474, "controller", lambda: controller), n=_n_(686475, "controller", lambda: controller)+'_proxy')
    _l_(686477)

def corresponding_proxy(controller):
    _l_(686481)

    aux = _n_(686479, "controller", lambda: controller)+'_proxy'
    _l_(686480)
    return aux

for controller in _n_(686482, "controllers", lambda: controllers):
    _l_(686495)

    for attr in _n_(686483, "attributes", lambda: attributes):
        _l_(686494)

        _c_(686492, _a_(686485, _n_(686484, "mc", lambda: mc), "connectAttr"), _n_(686486, "controller", lambda: controller)+_n_(686487, "attr", lambda: attr), _c_(686490, _n_(686488, "corresponding_proxy", lambda: corresponding_proxy), _n_(686489, "controller", lambda: controller))+_n_(686491, "attr", lambda: attr))
        _l_(686493)