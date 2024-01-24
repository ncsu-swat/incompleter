# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37191263/how-to-find-integer-representing-code-point-of-special-character-typeerror-ord
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
characters = ['Č', 'č', 'Š', 'š', 'Ž', 'ž']
_l_(523821)
codecs = ['iso8859_2', 'cp1250', 'mac_latin2', 'utf-8', 'utf_16_le', 'utf_16_be']
_l_(523822)

for letter in _n_(523823, "characters", lambda: characters):
    _l_(523839)

    for code in _n_(523824, "codecs", lambda: codecs):
        _l_(523838)

        _c_(523836, _n_(523825, "print", lambda: print), _n_(523826, "letter", lambda: letter) + ' ' + _n_(523827, "code", lambda: code) + ' ' + _c_(523835, _n_(523828, "str", lambda: str), _c_(523834, _n_(523829, "ord", lambda: ord), _c_(523833, _a_(523831, _n_(523830, "letter", lambda: letter), "encode"), _n_(523832, "code", lambda: code)))))
        _l_(523837)