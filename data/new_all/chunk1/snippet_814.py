# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32943002/python-3-x-attributeerror-str-object-has-no-attribute-append
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def enc(input, output, seq, str_int):
     _l_(387790)

     input = _c_(387765, _a_(387764, _n_(387763, "input", lambda: input), "lower"))
     _l_(387766)
     output = []
     _l_(387767)
     for char in _n_(387768, "input", lambda: input):
          _l_(387787)

          num = _c_(387771, _n_(387769, "ord", lambda: ord), _n_(387770, "char", lambda: char)) + 5
          _l_(387772)
          str_int = _c_(387775, _n_(387773, "str", lambda: str), _n_(387774, "num", lambda: num))
          _l_(387776)
          _c_(387780, _a_(387778, _n_(387777, "output", lambda: output), "append"), _n_(387779, "str_int", lambda: str_int))
          _l_(387781)
          output = _c_(387785, _a_(387783, _n_(387782, "seq", lambda: seq), "join"), _n_(387784, "output", lambda: output))
          _l_(387786)
     aux = _n_(387788, "output", lambda: output)
     _l_(387789)
     return aux
_c_(387794, _n_(387791, "print", lambda: print), _c_(387793, _n_(387792, "enc", lambda: enc), "hello", [], ' ', ' '))
_l_(387795)