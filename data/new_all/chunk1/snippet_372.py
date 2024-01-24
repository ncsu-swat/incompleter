# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49240581/sqalchemy-postgres-attributeerror-cant-set-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class User(_a_(411247, _n_(411246, "db", lambda: db), "Model"), _n_(411248, "UserMixin", lambda: UserMixin)):
    _l_(411279)

    """
    A user who has an account on the website.
    """

    __tablename__ = 'user'
    _l_(411249)

    id = _c_(411252, _a_(411250, db, "Column"), _a_(411251, db, "Integer"),
                   primary_key=True,
                   nullable=False,
                   unique=True,
                   autoincrement=True)
    _l_(411253)
    first_name = _c_(411256, _a_(411254, db, "Column"), _a_(411255, db, "String"))
    _l_(411257)
    last_name = _c_(411260, _a_(411258, db, "Column"), _a_(411259, db, "String"))
    _l_(411261)
    phone = _c_(411264, _a_(411262, db, "Column"), _a_(411263, db, "String"))
    _l_(411265)
    email = _c_(411268, _a_(411266, db, "Column"), _a_(411267, db, "String"), unique=True)
    _l_(411269)
    photo = _c_(411272, _a_(411270, db, "Column"), _a_(411271, db, "String"), default="No Picture")
    _l_(411273)
    _password = _c_(411277, _a_(411274, db, "Column"), _c_(411276, _a_(411275, db, "Binary"), 60))
    _l_(411278)