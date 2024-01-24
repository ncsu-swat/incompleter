# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38931066/typeerror-string-indices-must-be-integer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(703241, _a_(703238, _n_(703237, "api", lambda: api), "authenticate"), _n_(703239, "LOGIN", lambda: LOGIN), _n_(703240, "CONN", lambda: CONN))
_l_(703242)
profil = _c_(703245, _a_(703244, _n_(703243, "api", lambda: api), "get_profile"), "abc")
_l_(703246)
data = _c_(703250, _a_(703248, _n_(703247, "json", lambda: json), "dumps"), _n_(703249, "profil", lambda: profil), indent=4)
_l_(703251)
_c_(703254, _n_(703252, "print", lambda: print), _n_(703253, "data", lambda: data)["login"])
_l_(703255)