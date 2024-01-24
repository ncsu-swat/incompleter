# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65533434/python-setattr-causes-attribute-error-on-a-defined-variable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame as pg
    _l_(444889)

except ImportError:
    pass


class Block:
    _l_(444972)

    blocks = {}
    _l_(444890)
    id_ = 1
    _l_(444891)

    def __init__(self, surface, name=None, color=[0] * 3, width=0):
        _l_(444934)

        _n_(444892, "self", lambda: self).surface = _n_(444893, "surface", lambda: surface)
        _l_(444894)
        _n_(444895, "self", lambda: self).name = (_n_(444896, "name", lambda: name) if _n_(444897, "name", lambda: name) else _a_(444899, _n_(444898, "Block", lambda: Block), "id_"))
        _l_(444900)
        _n_(444901, "self", lambda: self).color = _n_(444902, "color", lambda: color)
        _l_(444903)
        _n_(444904, "self", lambda: self).width = _n_(444905, "width", lambda: width)
        _l_(444906)

        _n_(444907, "self", lambda: self).rect = _c_(444910, _a_(444909, _n_(444908, "pg", lambda: pg), "Rect"), (0, 0), [20] * 2)
        _l_(444911)
        _n_(444912, "self", lambda: self).block = _c_(444915, _a_(444914, _n_(444913, "self", lambda: self), "make_block"))
        _l_(444916)

        _c_(444922, _a_(444919, _a_(444918, _n_(444917, "pg", lambda: pg), "draw"), "polygon"), *_a_(444921, _n_(444920, "self", lambda: self), "block"))
        _l_(444923)

        _a_(444925, _n_(444924, "Block", lambda: Block), "blocks")[_a_(444927, _n_(444926, "self", lambda: self), "name")] = _n_(444928, "self", lambda: self)
        _l_(444929)

        if not _n_(444930, "name", lambda: name):
            _l_(444933)

            _n_(444931, "Block", lambda: Block).id_ += 1
            _l_(444932)

    def make_block(self):
        _l_(444969)

        point_1 = _a_(444937, _a_(444936, _n_(444935, "self", lambda: self), "rect"), "topleft")
        _l_(444938)
        point_2 = (_a_(444941, _a_(444940, _n_(444939, "self", lambda: self), "rect"), "topleft")[0], _a_(444944, _a_(444943, _n_(444942, "self", lambda: self), "rect"), "topleft")[1] + _a_(444947, _a_(444946, _n_(444945, "self", lambda: self), "rect"), "size")[1])
        _l_(444948)
        point_3 = (_n_(444949, "point_2", lambda: point_2)[0] + _a_(444952, _a_(444951, _n_(444950, "self", lambda: self), "rect"), "size")[0], _n_(444953, "point_2", lambda: point_2)[1])
        _l_(444954)
        point_4 = (_n_(444955, "point_3", lambda: point_3)[0], _n_(444956, "point_1", lambda: point_1)[0])
        _l_(444957)
        aux = [_a_(444959, _n_(444958, "self", lambda: self), "surface"), _a_(444961, _n_(444960, "self", lambda: self), "color"), (_n_(444962, "point_1", lambda: point_1), _n_(444963, "point_2", lambda: point_2), _n_(444964, "point_3", lambda: point_3), _n_(444965, "point_4", lambda: point_4)), _a_(444967, _n_(444966, "self", lambda: self), "width")]
        _l_(444968)

        return aux

    def __setattr__(self, name, value):
        _l_(444971)

        pass
        _l_(444970)


_c_(444977, _n_(444973, "Block", lambda: Block), _c_(444976, _a_(444975, _n_(444974, "pg", lambda: pg), "Surface"), (20, 20)))
_l_(444978)