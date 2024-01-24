# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58800137/rpy2-typeerror-parameter-categories-must-be-list-like
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import rpy2, rpy2.robjects as robjects, rpy2.robjects.packages as rpackages
    _l_(543237)

except ImportError:
    pass
try:
    from rpy2.robjects.vectors import StrVector
    _l_(543239)

except ImportError:
    pass
try:
    import os
    _l_(543241)

except ImportError:
    pass
try:
    from rpy2.robjects.packages import importr
    _l_(543243)

except ImportError:
    pass
base = _c_(543245, _n_(543244, "importr", lambda: importr), 'base')
_l_(543246)
_c_(543251, _n_(543247, "print", lambda: print), _c_(543250, _a_(543249, _n_(543248, "base", lambda: base), "R_home")))
_l_(543252)

# install packages in r from python

packageNames  = ('ggplot2', 'hexbin', 'MVN','afex', 'emmeans')
_l_(543253)
utils = _c_(543256, _a_(543255, _n_(543254, "rpackages", lambda: rpackages), "importr"), 'utils')
_l_(543257)
_c_(543260, _a_(543259, _n_(543258, "utils", lambda: utils), "chooseCRANmirror"), ind=1)
_l_(543261)

packnames_to_install = [_n_(543262, "x", lambda: x) for x in _n_(543263, "packageNames", lambda: packageNames) if not _c_(543267, _a_(543265, _n_(543264, "rpackages", lambda: rpackages), "isinstalled"), _n_(543266, "x", lambda: x))]
_l_(543268)

if _c_(543271, _n_(543269, "len", lambda: len), _n_(543270, "packnames_to_install", lambda: packnames_to_install)) > 0:
    _l_(543279)

    _c_(543277, _a_(543273, _n_(543272, "utils", lambda: utils), "install_packages"), _c_(543276, _n_(543274, "StrVector", lambda: StrVector), _n_(543275, "packnames_to_install", lambda: packnames_to_install)))
    _l_(543278)


# Read table function in r to python dataframe
data = _c_(543282, _a_(543281, _n_(543280, "robjects", lambda: robjects), "r"), 'read.table(file =' \
       '"http://personality-project.org/r/datasets/R.appendix3.data", header = T)')
_l_(543283)

_c_(543286, _a_(543285, _n_(543284, "data", lambda: data), "head"))
_l_(543287)