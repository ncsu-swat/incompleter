# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64509096/typeerror-not-supported-between-instances-of-numpy-ndarray-and-str-when
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
maxcoord = [0,0,0,0,0,0]
_l_(644371)
mincoord = [0,0,0,0,0,0]
_l_(644372)
for i in _c_(644375, _n_(644373, "range", lambda: range), _n_(644374, "num_atoms", lambda: num_atoms)):
    _l_(644448)

    if(_n_(644376, "coord_array", lambda: coord_array)[_n_(644377, "i", lambda: i)][0] > _n_(644378, "maxcoord", lambda: maxcoord)[0]):
        _l_(644387)

        _n_(644379, "maxcoord", lambda: maxcoord)[0] = _n_(644380, "coord_array", lambda: coord_array)[_n_(644381, "i", lambda: i)][0]
        _l_(644382)
        _n_(644383, "maxcoord", lambda: maxcoord)[1] = _n_(644384, "names", lambda: names)[_n_(644385, "i", lambda: i)]
        _l_(644386)
    if(_n_(644388, "coord_array", lambda: coord_array)[_n_(644389, "i", lambda: i)][0] < _n_(644390, "mincoord", lambda: mincoord)[0]):
        _l_(644399)

        _n_(644391, "mincoord", lambda: mincoord)[0] = _n_(644392, "coord_array", lambda: coord_array)[_n_(644393, "i", lambda: i)][0]
        _l_(644394)
        _n_(644395, "mincoord", lambda: mincoord)[1] = _n_(644396, "names", lambda: names)[_n_(644397, "i", lambda: i)]
        _l_(644398)
    if(_n_(644400, "coord_array", lambda: coord_array)[_n_(644401, "i", lambda: i)][1] > _n_(644402, "maxcoord", lambda: maxcoord)[2]):
        _l_(644411)

        _n_(644403, "maxcoord", lambda: maxcoord)[2] = _n_(644404, "coord_array", lambda: coord_array)[_n_(644405, "i", lambda: i)][1]
        _l_(644406)
        _n_(644407, "maxcoord", lambda: maxcoord)[2] = _n_(644408, "names", lambda: names)[_n_(644409, "i", lambda: i)]
        _l_(644410)
    if(_n_(644412, "coord_array", lambda: coord_array)[_n_(644413, "i", lambda: i)][1] < _n_(644414, "mincoord", lambda: mincoord)[2]):
        _l_(644423)

        _n_(644415, "mincoord", lambda: mincoord)[2] = _n_(644416, "coord_array", lambda: coord_array)[_n_(644417, "i", lambda: i)][1]
        _l_(644418)
        _n_(644419, "mincoord", lambda: mincoord)[2] = _n_(644420, "names", lambda: names)[_n_(644421, "i", lambda: i)]
        _l_(644422)
    if(_n_(644424, "coord_array", lambda: coord_array)[_n_(644425, "i", lambda: i)][2] > _n_(644426, "maxcoord", lambda: maxcoord)[4]):
        _l_(644435)

        _n_(644427, "maxcoord", lambda: maxcoord)[4] = _n_(644428, "coord_array", lambda: coord_array)[_n_(644429, "i", lambda: i)][2]
        _l_(644430)
        _n_(644431, "maxcoord", lambda: maxcoord)[5] = _n_(644432, "names", lambda: names)[_n_(644433, "i", lambda: i)]
        _l_(644434)
    if(_n_(644436, "coord_array", lambda: coord_array)[_n_(644437, "i", lambda: i)][2] < _n_(644438, "mincoord", lambda: mincoord)[4]):
        _l_(644447)

        _n_(644439, "mincoord", lambda: mincoord)[4] = _n_(644440, "coord_array", lambda: coord_array)[_n_(644441, "i", lambda: i)][2]
        _l_(644442)
        _n_(644443, "mincoord", lambda: mincoord)[5] = _n_(644444, "names", lambda: names)[_n_(644445, "i", lambda: i)]
        _l_(644446)