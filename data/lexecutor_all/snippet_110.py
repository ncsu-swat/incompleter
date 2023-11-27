# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/931092/how-do-i-reverse-a-string-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
string = "python"
_l_(1548929)
rev_string = _n_(1548930, "string", lambda: string)[::-1]
_l_(1548931)
_c_(1548934, _n_(1548932, "print", lambda: print), _n_(1548933, "rev_string", lambda: rev_string))
_l_(1548935)

string = "python"
_l_(1548936)
rev= _c_(1548939, _n_(1548937, "reversed", lambda: reversed), _n_(1548938, "string", lambda: string)) 
_l_(1548940) 
rev_string = _c_(1548943, _a_(1548941, "", "join"), _n_(1548942, "rev", lambda: rev)) 
_l_(1548944) 
_c_(1548947, _n_(1548945, "print", lambda: print), _n_(1548946, "rev_string", lambda: rev_string))
_l_(1548948)

string = "python"
_l_(1548949)
def reverse(string):
  _l_(1548961)

  if _c_(1548952, _n_(1548950, "len", lambda: len), _n_(1548951, "string", lambda: string))==0:
    _l_(1548960)

    aux = _n_(1548953, "string", lambda: string)
    _l_(1548954)
    return aux
  else:
    aux = _c_(1548957, _n_(1548955, "reverse", lambda: reverse), _n_(1548956, "string", lambda: string)[1:])+_n_(1548958, "string", lambda: string)[0]
    _l_(1548959)
    return aux
_c_(1548966, _n_(1548962, "print", lambda: print), _c_(1548965, _n_(1548963, "reverse", lambda: reverse), _n_(1548964, "string", lambda: string)))
_l_(1548967)

string = "python"
_l_(1548968)
rev_string =""
_l_(1548969)
for s in _n_(1548970, "string", lambda: string):
  _l_(1548974)

  rev_string = _n_(1548971, "s", lambda: s)+ _n_(1548972, "rev_string", lambda: rev_string)
  _l_(1548973)
_c_(1548977, _n_(1548975, "print", lambda: print), _n_(1548976, "rev_string", lambda: rev_string))
_l_(1548978)

string = "python"
_l_(1548979)
rev_str =""
_l_(1548980)
length = _c_(1548983, _n_(1548981, "len", lambda: len), _n_(1548982, "string", lambda: string))-1
_l_(1548984)
while _n_(1548985, "length", lambda: length) >=0:
  _l_(1548990)

  rev_str += _n_(1548986, "string", lambda: string)[_n_(1548987, "length", lambda: length)]
  _l_(1548988)
  length -= 1
  _l_(1548989)
_c_(1548993, _n_(1548991, "print", lambda: print), _n_(1548992, "rev_str", lambda: rev_str))
_l_(1548994)

