# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60989557/typeerror-can-only-concatenate-str-not-float-to-str-when-there-is-no-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for x in _c_(366326, _n_(366322, "range", lambda: range), _c_(366325, _n_(366323, "len", lambda: len), _n_(366324, "nums", lambda: nums))):
    _l_(366343)

    file = _c_(366331, _n_(366327, "open", lambda: open), "updates" + _c_(366330, _n_(366328, "str", lambda: str), _n_(366329, "x", lambda: x)) + ".txt", "a")
    _l_(366332)
    data2 = '{"Percent":"' + \
            _n_(366333, "element", lambda: element)[_n_(366334, "x", lambda: x)] + '", "diff":"' + _n_(366335, "diff", lambda: diff) + '"}'
    _l_(366336)
    text = _c_(366341, _a_(366338, _n_(366337, "json", lambda: json), "dump"), _n_(366339, "data2", lambda: data2) + '\n', _n_(366340, "file", lambda: file))
    _l_(366342)