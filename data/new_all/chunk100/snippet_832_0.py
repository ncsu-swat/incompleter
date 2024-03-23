# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def personal_details():
    _l_(83037)

    (name, age) = ('Simon', 19)
    _l_(83028)
    _c_(83035, _n_(83029, "print", lambda: print), _c_(83034, _a_(83030, 'Name: {}\nAge: {}\nAddress: {}', "format"), _n_(83031, "name", lambda: name), _n_(83032, "age", lambda: age), _n_(83033, "address", lambda: address)))
    _l_(83036)
_c_(83039, _n_(83038, "personal_details", lambda: personal_details))
_l_(83040)