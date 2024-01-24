# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63563886/type-error-a-def-that-works-only-with-str-but-not-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def tiene_uno(expresion):
    _l_(558969)

    n = _c_(558954, _n_(558950, "str", lambda: str), _c_(558953, _n_(558951, "len", lambda: len), _n_(558952, "expresion", lambda: expresion)))
    _l_(558955)
    i = 0
    _l_(558956)
    tiene = False
    _l_(558957)
    while (_n_(558958, "i", lambda: i)<_n_(558959, "n", lambda: n)) and not _n_(558960, "tiene", lambda: tiene):
        _l_(558966)

        if _n_(558961, "expresion", lambda: expresion)[_n_(558962, "i", lambda: i)] == '1':
            _l_(558964)

            tiene = True
            _l_(558963)
        i += 1
        _l_(558965)
    aux = _n_(558967, "tiene", lambda: tiene)
    _l_(558968)
    return aux


_c_(558971, _n_(558970, "tiene_uno", lambda: tiene_uno), 'UNSAM 2020')
_l_(558972)
_c_(558974, _n_(558973, "tiene_uno", lambda: tiene_uno), 'La novela 1984 de George Orwell')
_l_(558975)
_c_(558977, _n_(558976, "tiene_uno", lambda: tiene_uno), 1984)
_l_(558978)