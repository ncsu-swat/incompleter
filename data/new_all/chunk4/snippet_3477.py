# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73756417/nameerror-name-load-is-not-defined-after-importing-spyrmsd
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from spyrmsd import io,rmsd
    _l_(594293)

except ImportError:
    pass
ref = _c_(594296, _a_(594295, _n_(594294, "io", lambda: io), "loadmol"), "tempref.pdb")
_l_(594297)