# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58819446/attribute-error-join-object-has-no-attribute-implicit-returning
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Example(_n_(657319, "Base", lambda: Base)):
    _l_(657328)

    __tablename__ = 'example'
    _l_(657320)

    id = _c_(657322, Column, _c_(657321, ForeignKey, u'visit.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True, unique=True)
    _l_(657323)
    startdate = _c_(657324, Column, Date, nullable=False)
    _l_(657325)
    enddate = _c_(657326, Column, Date)
    _l_(657327)