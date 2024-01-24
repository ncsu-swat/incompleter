# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51720526/how-to-remove-the-type-error-associated-with-elements-of-a-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
pyramidlist = [[_c_(367465, _n_(367463, "int", lambda: int), _n_(367464, "x", lambda: x)) for x in _c_(367468, _a_(367467, _n_(367466, "y", lambda: y), "split"), ' ')] for y in _c_(367471, _a_(367470, _n_(367469, "number", lambda: number), "split"), '\n')]
_l_(367472)

for i in _c_(367477, _n_(367473, "range", lambda: range), _c_(367476, _n_(367474, "len", lambda: len), _n_(367475, "pyramidlist", lambda: pyramidlist)) - 2, -1, -1):
    _l_(367494)

    for j in _c_(367480, _n_(367478, "range", lambda: range), _n_(367479, "i", lambda: i)+1):
        _l_(367493)

        _n_(367481, "pyramidlist", lambda: pyramidlist)[_n_(367482, "i", lambda: i)][_n_(367483, "j", lambda: j)] += _c_(367491, _n_(367484, "max", lambda: max), _n_(367485, "pyramidlist", lambda: pyramidlist)[_n_(367486, "i", lambda: i)+1][_n_(367487, "j", lambda: j)], _n_(367488, "pyramidlist", lambda: pyramidlist)[_n_(367489, "i", lambda: i)+1][_n_(367490, "j", lambda: j)+1])
        _l_(367492)