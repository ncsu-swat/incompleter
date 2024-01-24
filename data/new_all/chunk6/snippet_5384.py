# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59697444/typeerror-unsupported-operand-types-for-str-and-int-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import datetime
  _l_(357435)

except ImportError:
  pass


q= _c_(357438, _a_(357437, _n_(357436, "datetime", lambda: datetime), "date"), 2004,12,25)
_l_(357439)

e= _c_(357442, _a_(357441, _n_(357440, "datetime", lambda: datetime), "date"), 2019,11,23) 
_l_(357443) 

f= _c_(357446, _a_(357445, _n_(357444, "datetime", lambda: datetime), "date"), 2019,11,26)
_l_(357447)

p= _c_(357450, _a_(357449, _n_(357448, "datetime", lambda: datetime), "date"), 2004,12,13)
_l_(357451)

nam=[["attack on titan",10,"completed",_n_(357452, "p", lambda: p),_n_(357453, "q", lambda: q)],["one punch man",10,"WATCHING",_n_(357454, "e", lambda: e),_n_(357455, "f", lambda: f)]]
_l_(357456)

_c_(357458, _n_(357457, "print", lambda: print), "|         NAME           | SCORE |   STATUS   |  DATE STARTED  |    DATE ENDED   |") 
_l_(357459) 

for KI in _n_(357460, "nam", lambda: nam):
  _l_(357475)

  _c_(357473, _n_(357461, "print", lambda: print), "|",_n_(357462, "KI", lambda: KI)[0]," "*22-_c_(357465, _n_(357463, "len", lambda: len), _n_(357464, "KI", lambda: KI)[0]),"|"," ",_n_(357466, "KI", lambda: KI)[1]," ","|",_n_(357467, "KI", lambda: KI)[2]," "*(10-_c_(357470, _n_(357468, "len", lambda: len), _n_(357469, "KI", lambda: KI)[2])),"|",""*2,_n_(357471, "KI", lambda: KI)[3], 
         " "*2,"|"," "*3,_n_(357472, "KI", lambda: KI)[4]," "*2,"|")
  _l_(357474)