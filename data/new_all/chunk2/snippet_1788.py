# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55875134/wtf-forms-populate-object-attributeerror-heatingcircuit-object-has-no-attribu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Heatingcircuit(_a_(443243, _n_(443242, "db", lambda: db), "Model")):
    _l_(443298)

    id = _c_(443246, _a_(443244, db, "Column"), _a_(443245, db, "Integer"), primary_key=True)
    _l_(443247)
    name = _c_(443251, _a_(443248, db, "Column"), _c_(443250, _a_(443249, db, "String"), 64))
    _l_(443252)
    sensor_ID1 = _c_(443256, _a_(443253, db, "Column"), _c_(443255, _a_(443254, db, "String"), 30))
    _l_(443257)
    sensor_ID2 = _c_(443261, _a_(443258, db, "Column"), _c_(443260, _a_(443259, db, "String"), 30))
    _l_(443262)
    sensor_ID3 = _c_(443266, _a_(443263, db, "Column"), _c_(443265, _a_(443264, db, "String"), 30))
    _l_(443267)
    pin_ID1 = _c_(443270, _a_(443268, db, "Column"), _a_(443269, db, "Integer"))
    _l_(443271)
    pin_ID2 = _c_(443274, _a_(443272, db, "Column"), _a_(443273, db, "Integer"))
    _l_(443275)
    pin_ID3 = _c_(443278, _a_(443276, db, "Column"), _a_(443277, db, "Integer"))
    _l_(443279)
    temp = _c_(443282, _a_(443280, db, "Column"), _a_(443281, db, "Float"))
    _l_(443283)
    state = _c_(443287, _a_(443284, db, "Column"), _c_(443286, _a_(443285, db, "String"), 9))
    _l_(443288)
    timer = _c_(443290, _a_(443289, db, "relationship"), 'Timers', backref='time')
    _l_(443291)

    def __repr__(self):
        _l_(443297)

        aux = _c_(443295, _a_(443292, '{}', "format"), _a_(443294, _n_(443293, "self", lambda: self), "id"))
        _l_(443296)
        return aux