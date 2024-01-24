# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58355894/typeerror-init-got-an-unexpected-keyword-argument-choices
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class StudentMarksheetform2(_a_(452970, _n_(452969, "forms", lambda: forms), "Form")):
    _l_(452978)

    subject_code=(
        (1,'CS101'),
        (2,'CS102'),
        (3,'CS103'),
        (4,'CS104'),
        (5,'CS105'),
        (6,'CS106')
    )
    _l_(452971)
    code_title=_c_(452973, _a_(452972, forms, "IntegerField"), choices=subject_code,default='1')
    _l_(452974)

    class Meta():
        _l_(452977)

        model=StudentMarksheetdata2
        _l_(452975)
        fields=['code_title']
        _l_(452976)