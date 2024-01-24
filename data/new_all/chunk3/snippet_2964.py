# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56846939/why-am-i-getting-typeerror-for-device-function-in-pennylane
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pennylane import numpy as np
    _l_(558633)

except ImportError:
    pass
try:
    import pennylane as qml
    _l_(558635)

except ImportError:
    pass

dev1 = _c_(558638, _a_(558637, _n_(558636, "qml", lambda: qml), "Device"), 'default.qubit', wires=1)
_l_(558639)