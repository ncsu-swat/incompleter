# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55735777/typeerror-not-supported-between-instances-of-str-and-int-in-version-num
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from distutils.version import LooseVersion
    _l_(395126)

except ImportError:
    pass
versions_list = ['2.5.6.RC02', '2.0.8', '2.0-m2']
_l_(395127)
_c_(395131, _a_(395129, _n_(395128, "versions_list", lambda: versions_list), "sort"), key=_n_(395130, "LooseVersion", lambda: LooseVersion), reverse=False)
_l_(395132)

_c_(395135, _n_(395133, "print", lambda: print), _n_(395134, "versions_list", lambda: versions_list)) 
_l_(395136) 