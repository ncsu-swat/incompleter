# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63756195/super-init-kwargs-typeerror-init-got-an-unexpected-keyword-argum
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django import forms
    _l_(469240)

except ImportError:
    pass
try:
    from .models import Student
    _l_(469242)

except ImportError:
    pass


class StudentRegistraion(_a_(469244, _n_(469243, "forms", lambda: forms), "ModelForm")):
    _l_(469262)

    class Meta:
        _l_(469261)

        model = _n_(469245, "Student", lambda: Student)
        _l_(469246)
        fields = ['name', 'roll_num', 'email', 'password']
        _l_(469247)
        widgets = {
            'name': _c_(469250, _a_(469249, _n_(469248, "forms", lambda: forms), "CharField"), attrs={'class': 'form-control'}),
            'roll_num': _c_(469253, _a_(469252, _n_(469251, "forms", lambda: forms), "IntegerField"), attrs={'class': 'form-control'}),
            'email': _c_(469256, _a_(469255, _n_(469254, "forms", lambda: forms), "EmailInput"), attrs={'class': 'form-control'}),
            'password': _c_(469259, _a_(469258, _n_(469257, "forms", lambda: forms), "PasswordInput"), attrs={'class': 'form-control'}),

        }
        _l_(469260)