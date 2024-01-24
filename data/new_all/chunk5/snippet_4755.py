# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49304400/python-a-type-error-caused-by-what
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import maya.cmds as mc
    _l_(674838)

except ImportError:
    pass

attributes = ['.t', '.r', '.s']
_l_(674839)

controllers = _c_(674842, _a_(674841, _n_(674840, "mc", lambda: mc), "ls"), 'ctrl_Lip*')
_l_(674843)

def corresponding_proxy(controller):
    _l_(674851)

    corresponding_proxy = _c_(674847, _a_(674845, _n_(674844, "mc", lambda: mc), "ls"), _n_(674846, "controller", lambda: controller)+'_proxy')
    _l_(674848)
    aux = _n_(674849, "corresponding_proxy", lambda: corresponding_proxy)
    _l_(674850)
    return aux

for controller in _n_(674852, "controllers", lambda: controllers) :
    _l_(674865)

    for attr in _n_(674853, "attributes", lambda: attributes) :
        _l_(674864)

        _c_(674862, _a_(674855, _n_(674854, "mc", lambda: mc), "connectAttr"), _n_(674856, "controller", lambda: controller)+_n_(674857, "attr", lambda: attr), _c_(674860, _n_(674858, "corresponding_proxy", lambda: corresponding_proxy), _n_(674859, "controller", lambda: controller))+_n_(674861, "attr", lambda: attr))
        _l_(674863)