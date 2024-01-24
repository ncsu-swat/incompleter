# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28272322/typeerror-slice-indices-must-be-integers-or-none-or-have-an-index-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import deque
    _l_(379326)

except ImportError:
    pass

m = []
_l_(379327)
f = _c_(379329, _n_(379328, "open", lambda: open), "IntegerArray.txt")
_l_(379330)
for line in _n_(379331, "f", lambda: f):
    _l_(379339)

    _c_(379337, _a_(379333, _n_(379332, "m", lambda: m), "append"), _c_(379336, _n_(379334, "int", lambda: int), _n_(379335, "line", lambda: line)))
    _l_(379338)

class InversionCount:
    _l_(379457)


    def __init__(self, n):
        _l_(379343)

        _n_(379340, "self", lambda: self).n = _n_(379341, "n", lambda: n)
        _l_(379342)
    def inversionMergeSort(self, m):
        _l_(379376)

        if _c_(379346, _n_(379344, "len", lambda: len), _n_(379345, "m", lambda: m)) <= 1:
            _l_(379349)

            aux = _n_(379347, "m", lambda: m)
            _l_(379348)
            return aux
        half = _c_(379352, _n_(379350, "len", lambda: len), _n_(379351, "m", lambda: m))/2
        _l_(379353)
        left = _n_(379354, "m", lambda: m)[0:_n_(379355, "half", lambda: half)]
        _l_(379356)
        right = _n_(379357, "m", lambda: m)[_n_(379358, "half", lambda: half):]
        _l_(379359)
        left = _c_(379363, _a_(379361, _n_(379360, "self", lambda: self), "inversionMergeSort"), _n_(379362, "left", lambda: left))
        _l_(379364)
        right = _c_(379368, _a_(379366, _n_(379365, "self", lambda: self), "inversionMergeSort"), _n_(379367, "right", lambda: right))
        _l_(379369)
        aux = _c_(379374, _a_(379371, _n_(379370, "self", lambda: self), "inversionSort"), _n_(379372, "left", lambda: left), _n_(379373, "right", lambda: right))
        _l_(379375)
        return aux

    def inversionSort(self, left, right):
        _l_(379456)

        leftQueue = _c_(379380, _n_(379377, "deque", lambda: deque), (_n_(379378, "i", lambda: i) for i in _n_(379379, "left", lambda: left)))
        _l_(379381)
        rightQueue = _c_(379385, _n_(379382, "deque", lambda: deque), (_n_(379383, "j", lambda: j) for j in _n_(379384, "right", lambda: right)))
        _l_(379386)
        orderedList = []
        _l_(379387)
        while _c_(379390, _n_(379388, "len", lambda: len), _n_(379389, "leftQueue", lambda: leftQueue)) > 0 or _c_(379393, _n_(379391, "len", lambda: len), _n_(379392, "rightQueue", lambda: rightQueue)) > 0:
            _l_(379453)

            if _c_(379396, _n_(379394, "len", lambda: len), _n_(379395, "leftQueue", lambda: leftQueue)) > 0 and _c_(379399, _n_(379397, "len", lambda: len), _n_(379398, "rightQueue", lambda: rightQueue)) > 0:
                _l_(379452)

                if _n_(379400, "leftQueue", lambda: leftQueue)[0] <= _n_(379401, "rightQueue", lambda: rightQueue)[0]:
                    _l_(379425)

                    _c_(379405, _a_(379403, _n_(379402, "orderedList", lambda: orderedList), "append"), _n_(379404, "leftQueue", lambda: leftQueue)[0])
                    _l_(379406)
                    _c_(379409, _a_(379408, _n_(379407, "leftQueue", lambda: leftQueue), "popleft"))
                    _l_(379410)
                else:
                    _c_(379414, _a_(379412, _n_(379411, "orderedList", lambda: orderedList), "append"), _n_(379413, "rightQueue", lambda: rightQueue)[0])
                    _l_(379415)
                    _n_(379416, "self", lambda: self).n += _c_(379419, _n_(379417, "len", lambda: len), _n_(379418, "leftQueue", lambda: leftQueue))
                    _l_(379420)
                    _c_(379423, _a_(379422, _n_(379421, "rightQueue", lambda: rightQueue), "popleft"))
                    _l_(379424)
            elif _c_(379428, _n_(379426, "len", lambda: len), _n_(379427, "leftQueue", lambda: leftQueue)) > 0:
                _l_(379451)

                _c_(379432, _a_(379430, _n_(379429, "orderedList", lambda: orderedList), "append"), _n_(379431, "leftQueue", lambda: leftQueue)[0])
                _l_(379433)
                _c_(379436, _a_(379435, _n_(379434, "leftQueue", lambda: leftQueue), "popleft"))
                _l_(379437)
            elif _c_(379440, _n_(379438, "len", lambda: len), _n_(379439, "rightQueue", lambda: rightQueue)) > 0:
                _l_(379450)

                _c_(379444, _a_(379442, _n_(379441, "orderedList", lambda: orderedList), "append"), _n_(379443, "rightQueue", lambda: rightQueue)[0])
                _l_(379445)
                _c_(379448, _a_(379447, _n_(379446, "rightQueue", lambda: rightQueue), "popleft"))
                _l_(379449)
        aux = _n_(379454, "orderedList", lambda: orderedList)
        _l_(379455)
        return aux

nInversions = _c_(379459, _n_(379458, "InversionCount", lambda: InversionCount), 0)
_l_(379460)
_c_(379464, _a_(379462, _n_(379461, "nInversions", lambda: nInversions), "inversionMergeSort"), _n_(379463, "m", lambda: m))
_l_(379465)
_c_(379469, _n_(379466, "print", lambda: print), _a_(379468, _n_(379467, "nInversions", lambda: nInversions), "n"))
_l_(379470)