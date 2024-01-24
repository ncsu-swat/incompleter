# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61365330/celery-running-signature-from-database-attributeerror-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(522553, "object_1", lambda: object_1) # Signature
_l_(522554) # Signature
_n_(522555, "object_2", lambda: object_2) # Signature
_l_(522556) # Signature
_n_(522557, "object_3", lambda: object_3) # _chain
_l_(522558) # _chain

ch = _n_(522559, "object_1", lambda: object_1) | _n_(522560, "object_2", lambda: object_2) | _n_(522561, "object_3", lambda: object_3)
_l_(522562)
_c_(522565, _a_(522564, _n_(522563, "ch", lambda: ch), "apply_async"))
_l_(522566)