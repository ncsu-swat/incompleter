# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43356922/attributeerror-gzipfile-object-has-no-attribute-next
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import gzip
    _l_(444709)

except ImportError:
    pass
try:
    import numpy as np
    _l_(444711)

except ImportError:
    pass

"""
Read in a SOFT format data file.  The following values can be exported:

GID : A list of gene identifiers of length d
SID : A list of sample identifiers of length n
STP : A list of sample descriptions of length d
X   : A dxn array of gene expression values
"""

fname = "../Anchang Charles/GDS1615_full.soft.gz"
_l_(444712)
with _c_(444716, _a_(444714, _n_(444713, "gzip", lambda: gzip), "open"), _n_(444715, "fname", lambda: fname)) as fid:
    _l_(444781)

    SIF = {}
    _l_(444717)
    for line in _n_(444718, "fid", lambda: fid):
        _l_(444758)

        if _c_(444724, _a_(444720, _n_(444719, "line", lambda: line), "startswith"), _n_(444721, "line", lambda: line), _c_(444723, _n_(444722, "len", lambda: len), "!dataset_table_begin")):
            _l_(444757)

            break
            _l_(444725)
        elif _c_(444731, _a_(444727, _n_(444726, "line", lambda: line), "startswith"), _n_(444728, "line", lambda: line), _c_(444730, _n_(444729, "len", lambda: len), "!subject_description")):
            _l_(444756)

            subset_description = _c_(444736, _a_(444735, _c_(444734, _a_(444733, _n_(444732, "line", lambda: line), "split"), "=")[1], "strip"))
            _l_(444737)
        elif _c_(444743, _a_(444739, _n_(444738, "line", lambda: line), "startswith"), _n_(444740, "line", lambda: line), _c_(444742, _n_(444741, "len", lambda: len), "!subset_sample_id")):
            _l_(444755)

            subset_ids = [_c_(444746, _a_(444745, _n_(444744, "x", lambda: x), "strip")) for x in _n_(444747, "subset_ids", lambda: subset_ids)]
            _l_(444748)
            for k in _n_(444749, "subset_ids", lambda: subset_ids):
                _l_(444754)

                _n_(444750, "SIF", lambda: SIF)[_n_(444751, "k", lambda: k)] = _n_(444752, "subset_description", lambda: subset_description)
                _l_(444753)
    SID = _c_(444763, _a_(444762, _c_(444761, _a_(444760, _n_(444759, "fid", lambda: fid), "next")), "split"), "\t")
    _l_(444764)
    I = [_n_(444765, "i", lambda: i) for i,x in _c_(444768, _n_(444766, "enumerate", lambda: enumerate), _n_(444767, "SID", lambda: SID)) if _c_(444771, _a_(444770, _n_(444769, "x", lambda: x), "startswith"), "GSM")]
    _l_(444772)
    SID = [_n_(444773, "SID", lambda: SID)[_n_(444774, "i", lambda: i)] for i in _n_(444775, "I", lambda: I)]
    _l_(444776)
    STP = [_n_(444777, "SIF", lambda: SIF)[_n_(444778, "k", lambda: k)] for k in _n_(444779, "SID", lambda: SID)]
    _l_(444780)