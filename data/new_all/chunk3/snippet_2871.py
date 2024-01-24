# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60381766/how-do-i-create-a-field-in-my-serializer-to-avoid-a-typeerror-cannot-unpack-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Coop(_a_(565829, _n_(565828, "models", lambda: models), "Model")):
    _l_(565850)

    name = _c_(565831, _a_(565830, models, "CharField"), max_length=250, null=False)
    _l_(565832)
    type = _c_(565834, _a_(565833, models, "ForeignKey"), CoopType, on_delete=None)
    _l_(565835)
    address = _c_(565837, AddressField, on_delete=_a_(565836, models, "CASCADE"))
    _l_(565838)
    enabled = _c_(565840, _a_(565839, models, "BooleanField"), default=True, null=False)
    _l_(565841)
    phone = _c_(565842, PhoneNumberField, null=True)
    _l_(565843)
    email = _c_(565845, _a_(565844, models, "EmailField"), null=True)
    _l_(565846)
    web_site = _c_(565848, _a_(565847, models, "TextField"))
    _l_(565849)