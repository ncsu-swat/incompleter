# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66194956/typeerror-contact-got-an-unexpected-keyword-argument-name-while-using-flask
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class contact(_a_(526335, _n_(526334, "db", lambda: db), "Model")):
    _l_(526364)

    name = _c_(526339, _a_(526336, db, "Column"), _c_(526338, _a_(526337, db, "String"), 120), nullable=False) 
    _l_(526340) 
    email = _c_(526344, _a_(526341, db, "Column"), _c_(526343, _a_(526342, db, "String"), 120), nullable=False)
    _l_(526345)
    phone_no = _c_(526348, _a_(526346, db, "Column"), _a_(526347, db, "String"), nullable=False)
    _l_(526349)
    msg = _c_(526353, _a_(526350, db, "Column"), _c_(526352, _a_(526351, db, "String"), 120), nullable=False)
    _l_(526354)
    date = _c_(526358, _a_(526355, db, "Column"), _c_(526357, _a_(526356, db, "String"), 120), nullable=True)
    _l_(526359)
    id = _c_(526362, _a_(526360, db, "Column"), _a_(526361, db, "Integer"), primary_key=True)
    _l_(526363)