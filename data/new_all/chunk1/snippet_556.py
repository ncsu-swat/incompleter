# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30953615/typeerror-object-is-not-json-serializable-in-django-1-8-python-3-4
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class GreenBased(_a_(399384, _n_(399383, "models", lambda: models), "Model")):
    _l_(399394)

    NumOfStudents = _c_(399386, _a_(399385, models, "CharField"), max_length=300,blank=True)
    _l_(399387)
    Green = _c_(399389, _a_(399388, models, "CharField"), max_length=300,blank=True)
    _l_(399390)
    class Meta:
        _l_(399393)

        managed = False
        _l_(399391)
        db_table = "GreenStats"
        _l_(399392)

class YelloBased(_a_(399396, _n_(399395, "models", lambda: models), "Model")):
    _l_(399406)

    NumOfStudents = _c_(399398, _a_(399397, models, "CharField"), max_length=300,blank=True)
    _l_(399399)
    Yellow = _c_(399401, _a_(399400, models, "CharField"), max_length=300,blank=True)
    _l_(399402)
    class Meta:
        _l_(399405)

        managed = False
        _l_(399403)
        db_table = "YellowStats"
        _l_(399404)