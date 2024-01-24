# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65603054/typeerror-while-using-pool-from-multiprocessing-python-3-7
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(626790)

except ImportError:
    pass
try:
    from multiprocessing import Pool
    _l_(626792)

except ImportError:
    pass

def _count(self, path):
    _l_(626855)

    stats = _c_(626797, _a_(626794, _n_(626793, "dict", lambda: dict), "fromkeys"), _a_(626796, _n_(626795, "self", lambda: self), "_categories"), 0)
    _l_(626798)
    try:
        _l_(626807)

        dir_list = _c_(626802, _a_(626800, _n_(626799, "os", lambda: os), "listdir"), _n_(626801, "path", lambda: path))
        _l_(626803)
    except:
        _l_(626806)

        aux = _n_(626804, "stats", lambda: stats)
        _l_(626805)
        # I do some warning here, but removed it for SSCCE
        return aux

    for element in _n_(626808, "dir_list", lambda: dir_list):
        _l_(626852)

        new_path = _c_(626814, _a_(626811, _a_(626810, _n_(626809, "os", lambda: os), "path"), "join"), _n_(626812, "path", lambda: path), _n_(626813, "element", lambda: element))
        _l_(626815)

        if _c_(626820, _a_(626818, _a_(626817, _n_(626816, "os", lambda: os), "path"), "isdir"), _n_(626819, "new_path", lambda: new_path)):
            _l_(626851)

            add_stats = _c_(626824, _a_(626822, _n_(626821, "self", lambda: self), "_count"), _n_(626823, "new_path", lambda: new_path))
            _l_(626825)
            stats = _c_(626830, _a_(626827, _n_(626826, "self", lambda: self), "_sum_dicts"), [_n_(626828, "stats", lambda: stats), _n_(626829, "add_stats", lambda: add_stats)])
            _l_(626831)
        else:
            file_type = _c_(626835, _a_(626833, _n_(626832, "self", lambda: self), "_get_file_type"), _n_(626834, "element", lambda: element))
            _l_(626836)
            try:
                _l_(626846)

                size = _c_(626841, _a_(626839, _a_(626838, _n_(626837, "os", lambda: os), "path"), "getsize"), _n_(626840, "new_path", lambda: new_path))
                _l_(626842)
            except _n_(626843, "Exception", lambda: Exception) as e:
                _l_(626845)

                # I do some warning here, but removed it for SSCCE
                continue
                _l_(626844)

            _n_(626847, "stats", lambda: stats)[_n_(626848, "file_type", lambda: file_type)] += _n_(626849, "size", lambda: size)
            _l_(626850)
    aux = _n_(626853, "stats", lambda: stats)
    _l_(626854)

    return aux

files = []
_l_(626856)
dirs = []
_l_(626857)
for e in _n_(626858, "dir_list", lambda: dir_list):
    _l_(626882)

    new_name = _c_(626864, _a_(626861, _a_(626860, _n_(626859, "os", lambda: os), "path"), "join"), _n_(626862, "path", lambda: path), _n_(626863, "e", lambda: e))
    _l_(626865)
    if _c_(626870, _a_(626868, _a_(626867, _n_(626866, "os", lambda: os), "path"), "isdir"), _n_(626869, "new_name", lambda: new_name)):
        _l_(626881)

        _c_(626874, _a_(626872, _n_(626871, "dirs", lambda: dirs), "append"), _n_(626873, "new_name", lambda: new_name))
        _l_(626875)
    else:
        _c_(626879, _a_(626877, _n_(626876, "files", lambda: files), "append"), _n_(626878, "new_name", lambda: new_name))
        _l_(626880)

with _c_(626885, _n_(626883, "Pool", lambda: Pool), processes=_n_(626884, "number_of_threats", lambda: number_of_threats)) as pool:
    _l_(626893)

    res = _c_(626891, _a_(626887, _n_(626886, "pool", lambda: pool), "map"), _a_(626889, _n_(626888, "self", lambda: self), "_count"), _n_(626890, "dirs", lambda: dirs))
    _l_(626892)

_n_(626894, "self", lambda: self)._stats = _c_(626898, _a_(626896, _n_(626895, "self", lambda: self), "_sum_dicts"), _n_(626897, "res", lambda: res))
_l_(626899)