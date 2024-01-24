# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49454529/django-forms-typeerror-init-got-an-unexpected-keyword-argument-instance
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ImpcalendarForm(_a_(425466, _n_(425465, "forms", lambda: forms), "Form")):
    _l_(425488)

    establishment = _c_(425471, _a_(425467, forms, "ModelChoiceField"), queryset = _c_(425470, _a_(425469, _a_(425468, Establishments, "objects"), "all")))
    _l_(425472)
    page = _c_(425475, _a_(425473, forms, "CharField"), widget=_a_(425474, forms, "Textarea"))
    _l_(425476)
    pageold = _c_(425479, _a_(425477, forms, "CharField"), widget=_a_(425478, forms, "Textarea"))
    _l_(425480)
    change = _c_(425483, _a_(425481, forms, "CharField"), widget=_a_(425482, forms, "Textarea"))
    _l_(425484)
    class Meta:
        _l_(425487)

        model = Impcalendar
        _l_(425485)
        fields = '__all__'
        _l_(425486)