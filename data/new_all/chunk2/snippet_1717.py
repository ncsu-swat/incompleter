# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54620191/list-comprehension-returntypeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(475558, _n_(475557, "open", lambda: open), '/Users/Weindependent/Desktop/dataset/albumlist.csv', encoding='cp1252') as case0:
    _l_(475572)

    reader = _c_(475562, _a_(475560, _n_(475559, "csv", lambda: csv), "DictReader"), _n_(475561, "case0", lambda: case0)) #the file is coded with single-byte coding
    _l_(475563) #the file is coded with single-byte coding
    album = []
    _l_(475564)
    for row in _n_(475565, "reader", lambda: reader):
        _l_(475571)

        _c_(475569, _a_(475567, _n_(475566, "album", lambda: album), "append"), _n_(475568, "row", lambda: row))
        _l_(475570)
_c_(475577, _n_(475573, "print", lambda: print), _c_(475576, _n_(475574, "len", lambda: len), _n_(475575, "album", lambda: album)))
_l_(475578)