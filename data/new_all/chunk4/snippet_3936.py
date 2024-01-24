# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65160978/getting-nameerror-in-django-views-py-as-nameerror-name-edit-load-table-is
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class facultyload(_a_(585896, _n_(585895, "models", lambda: models), "Model")):
    _l_(585910)

    empId = _c_(585898, _a_(585897, models, "CharField"), max_length=20)
    _l_(585899)
    name = _c_(585901, _a_(585900, models, "CharField"), max_length=50)
    _l_(585902)
    total_load = _c_(585904, _a_(585903, models, "IntegerField"))
    _l_(585905)

    def __str__(self):
        _l_(585909)

        aux = _a_(585907, _n_(585906, "self", lambda: self), "empId")
        _l_(585908)
        return aux

class edit_load_table(_a_(585912, _n_(585911, "models", lambda: models), "Model")):
    _l_(585938)

    empId = _c_(585914, _a_(585913, models, "CharField"), max_length=20) 
    _l_(585915) 
    name = _c_(585917, _a_(585916, models, "CharField"), max_length=50)
    _l_(585918)
    subject_abv = _c_(585920, _a_(585919, models, "CharField"), max_length=10)
    _l_(585921)
    subject_load = _c_(585923, _a_(585922, models, "IntegerField"))
    _l_(585924)
    subject_type = _c_(585926, _a_(585925, models, "CharField"), max_length=10)
    _l_(585927)
    id_key = _c_(585929, _a_(585928, models, "IntegerField"))
    _l_(585930)
    semester = _c_(585932, _a_(585931, models, "CharField"), max_length=20)
    _l_(585933)
    
    def __str__(self):
        _l_(585937)

        aux = _a_(585935, _n_(585934, "self", lambda: self), "empId")
        _l_(585936)
        return aux