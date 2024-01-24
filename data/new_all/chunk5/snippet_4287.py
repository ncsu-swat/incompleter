# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58819446/attribute-error-join-object-has-no-attribute-implicit-returning
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Example(_n_(705770, "Base", lambda: Base)):
    _l_(705779)

    __tablename__ = 'example'
    _l_(705771)

    id = _c_(705773, Column, _c_(705772, ForeignKey, u'visit.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True, unique=True)
    _l_(705774)
    startdate = _c_(705775, Column, Date, nullable=False)
    _l_(705776)
    enddate = _c_(705777, Column, Date)
    _l_(705778)