# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65586172/sqlalchemy-object-throwing-attribute-error-for-sa-instance-state-in-pytest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Voterlist(_a_(532306, _n_(532305, "db", lambda: db), "Model")):
    _l_(532362)

    id = _c_(532309, _a_(532307, db, "Column"), _a_(532308, db, "Integer"), primary_key=True, default=get_time)
    _l_(532310)
    description = _c_(532314, _a_(532311, db, "Column"), _c_(532313, _a_(532312, db, "String"), 128))
    _l_(532315)
    vendorquery = _c_(532319, _a_(532316, db, "Column"), _c_(532318, _a_(532317, db, "String"), 128))
    _l_(532320)
    campaign = _c_(532324, _a_(532321, db, "Column"), _c_(532323, _a_(532322, db, "String"), 128))
    _l_(532325)
    s3key = _c_(532329, _a_(532326, db, "Column"), _c_(532328, _a_(532327, db, "String"), 128))
    _l_(532330)
    fname = _c_(532334, _a_(532331, db, "Column"), _c_(532333, _a_(532332, db, "String"), 128))
    _l_(532335)
    ftimestamp = _c_(532338, _a_(532336, db, "Column"), _a_(532337, db, "Integer"))
    _l_(532339)
    source = _c_(532343, _a_(532340, db, "Column"), _c_(532342, _a_(532341, db, "String"), 128))
    _l_(532344)
    user = _c_(532348, _a_(532345, db, "Column"), _c_(532347, _a_(532346, db, "String"), 128))
    _l_(532349)
    status = _c_(532352, _a_(532350, db, "Column"), _a_(532351, db, "Integer"), default=0)
    _l_(532353)

    def __repr__(self):
        _l_(532361)

        aux = _c_(532359, _a_(532354, '<List {}: {}>', "format"), _a_(532356, _n_(532355, "self", lambda: self), "id"), _a_(532358, _n_(532357, "self", lambda: self), "campaign"))
        _l_(532360)
        return aux