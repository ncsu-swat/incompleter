# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45216000/python-max-function-asks-for-src2-typeerror-required-argument-src2-pos-2-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _c_(597992, _n_(597985, "any", lambda: any), [_n_(597986, "img", lambda: img)[0:3] == _n_(597987, "imgs_type", lambda: imgs_type) for img in _c_(597991, _a_(597989, _n_(597988, "os", lambda: os), "listdir"), _n_(597990, "imgs_path", lambda: imgs_path))]):
        _l_(598026)

        current_imgs = _c_(598002, _n_(597993, "list", lambda: list), _c_(598001, _n_(597994, "filter", lambda: filter), lambda x: _n_(597995, "x", lambda: x)[0:3] == _n_(597996, "imgs_type", lambda: imgs_type), _c_(598000, _a_(597998, _n_(597997, "os", lambda: os), "listdir"), _n_(597999, "imgs_path", lambda: imgs_path))))
        _l_(598003)
        name_index = _c_(598013, _n_(598004, "max", lambda: max), _c_(598012, _n_(598005, "list", lambda: list), _c_(598011, _n_(598006, "map", lambda: map), lambda x: _c_(598009, _n_(598007, "int", lambda: int), _n_(598008, "x", lambda: x)[4:-4]), _n_(598010, "current_imgs", lambda: current_imgs))))
        _l_(598014)
        imgs = _c_(598024, _n_(598015, "list", lambda: list), _c_(598023, _n_(598016, "filter", lambda: filter), lambda x: _n_(598017, "x", lambda: x)[0:3] != _n_(598018, "imgs_type", lambda: imgs_type), _c_(598022, _a_(598020, _n_(598019, "os", lambda: os), "listdir"), _n_(598021, "imgs_path", lambda: imgs_path))))
        _l_(598025)