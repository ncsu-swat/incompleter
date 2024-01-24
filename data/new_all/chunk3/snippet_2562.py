# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71609574/my-code-is-not-working-typeerror-int-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
neword = '100115'
_l_(547570)
val=0
_l_(547571)
neword2=''
_l_(547572)
for n in _c_(547577, _n_(547573, "range", lambda: range), 0,_c_(547576, _n_(547574, "len", lambda: len), _n_(547575, "neword", lambda: neword)),3):
  _l_(547594)

  neword2 = _c_(547591, _n_(547578, "chr", lambda: chr), _c_(547581, _n_(547579, "int", lambda: int), _n_(547580, "neword", lambda: neword))[_n_(547582, "val", lambda: val)]+_c_(547585, _n_(547583, "int", lambda: int), _n_(547584, "neword", lambda: neword))[_n_(547586, "val", lambda: val)+1]+_c_(547589, _n_(547587, "int", lambda: int), _n_(547588, "neword", lambda: neword))[_n_(547590, "val", lambda: val)+2])
  _l_(547592)
  val+=3
  _l_(547593)
_c_(547597, _n_(547595, "print", lambda: print), _n_(547596, "neword2", lambda: neword2))
_l_(547598)