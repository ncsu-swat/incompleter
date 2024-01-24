# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65603054/typeerror-while-using-pool-from-multiprocessing-python-3-7
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(589951)

except ImportError:
    pass
try:
    from multiprocessing import Pool
    _l_(589953)

except ImportError:
    pass

def _count(self, path):
    _l_(590016)

    stats = _c_(589958, _a_(589955, _n_(589954, "dict", lambda: dict), "fromkeys"), _a_(589957, _n_(589956, "self", lambda: self), "_categories"), 0)
    _l_(589959)
    try:
        _l_(589968)

        dir_list = _c_(589963, _a_(589961, _n_(589960, "os", lambda: os), "listdir"), _n_(589962, "path", lambda: path))
        _l_(589964)
    except:
        _l_(589967)

        aux = _n_(589965, "stats", lambda: stats)
        _l_(589966)
        # I do some warning here, but removed it for SSCCE
        return aux

    for element in _n_(589969, "dir_list", lambda: dir_list):
        _l_(590013)

        new_path = _c_(589975, _a_(589972, _a_(589971, _n_(589970, "os", lambda: os), "path"), "join"), _n_(589973, "path", lambda: path), _n_(589974, "element", lambda: element))
        _l_(589976)

        if _c_(589981, _a_(589979, _a_(589978, _n_(589977, "os", lambda: os), "path"), "isdir"), _n_(589980, "new_path", lambda: new_path)):
            _l_(590012)

            add_stats = _c_(589985, _a_(589983, _n_(589982, "self", lambda: self), "_count"), _n_(589984, "new_path", lambda: new_path))
            _l_(589986)
            stats = _c_(589991, _a_(589988, _n_(589987, "self", lambda: self), "_sum_dicts"), [_n_(589989, "stats", lambda: stats), _n_(589990, "add_stats", lambda: add_stats)])
            _l_(589992)
        else:
            file_type = _c_(589996, _a_(589994, _n_(589993, "self", lambda: self), "_get_file_type"), _n_(589995, "element", lambda: element))
            _l_(589997)
            try:
                _l_(590007)

                size = _c_(590002, _a_(590000, _a_(589999, _n_(589998, "os", lambda: os), "path"), "getsize"), _n_(590001, "new_path", lambda: new_path))
                _l_(590003)
            except _n_(590004, "Exception", lambda: Exception) as e:
                _l_(590006)

                # I do some warning here, but removed it for SSCCE
                continue
                _l_(590005)

            _n_(590008, "stats", lambda: stats)[_n_(590009, "file_type", lambda: file_type)] += _n_(590010, "size", lambda: size)
            _l_(590011)
    aux = _n_(590014, "stats", lambda: stats)
    _l_(590015)

    return aux

files = []
_l_(590017)
dirs = []
_l_(590018)
for e in _n_(590019, "dir_list", lambda: dir_list):
    _l_(590043)

    new_name = _c_(590025, _a_(590022, _a_(590021, _n_(590020, "os", lambda: os), "path"), "join"), _n_(590023, "path", lambda: path), _n_(590024, "e", lambda: e))
    _l_(590026)
    if _c_(590031, _a_(590029, _a_(590028, _n_(590027, "os", lambda: os), "path"), "isdir"), _n_(590030, "new_name", lambda: new_name)):
        _l_(590042)

        _c_(590035, _a_(590033, _n_(590032, "dirs", lambda: dirs), "append"), _n_(590034, "new_name", lambda: new_name))
        _l_(590036)
    else:
        _c_(590040, _a_(590038, _n_(590037, "files", lambda: files), "append"), _n_(590039, "new_name", lambda: new_name))
        _l_(590041)

with _c_(590046, _n_(590044, "Pool", lambda: Pool), processes=_n_(590045, "number_of_threats", lambda: number_of_threats)) as pool:
    _l_(590054)

    res = _c_(590052, _a_(590048, _n_(590047, "pool", lambda: pool), "map"), _a_(590050, _n_(590049, "self", lambda: self), "_count"), _n_(590051, "dirs", lambda: dirs))
    _l_(590053)

_n_(590055, "self", lambda: self)._stats = _c_(590059, _a_(590057, _n_(590056, "self", lambda: self), "_sum_dicts"), _n_(590058, "res", lambda: res))
_l_(590060)