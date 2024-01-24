# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47784216/django-rest-framework-attributeerror-function-object-has-no-attribute-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(415048)

except ImportError:
    pass


class Education(_a_(415050, _n_(415049, "models", lambda: models), "Model")):
    _l_(415059)

    university =  _c_(415053, _a_(415052, _n_(415051, "models", lambda: models), "CharField"), max_length=50)
    _l_(415054)
    year_of_graduation = _c_(415057, _a_(415056, _n_(415055, "models", lambda: models), "DateField"))
    _l_(415058)


class Empl_history(_a_(415061, _n_(415060, "models", lambda: models), "Model")):
    _l_(415078)

    company = _c_(415064, _a_(415063, _n_(415062, "models", lambda: models), "CharField"), max_length=50)
    _l_(415065)
    role = _c_(415068, _a_(415067, _n_(415066, "models", lambda: models), "CharField"), max_length=30)
    _l_(415069)
    fr = _c_(415072, _a_(415071, _n_(415070, "models", lambda: models), "DateField"), verbose_name='from')
    _l_(415073)
    to = _c_(415076, _a_(415075, _n_(415074, "models", lambda: models), "DateField"))
    _l_(415077)


class Developers(_a_(415080, _n_(415079, "models", lambda: models), "Model")):
    _l_(415105)

    name = _c_(415083, _a_(415082, _n_(415081, "models", lambda: models), "CharField"), max_length=50)
    _l_(415084)
    surname = _c_(415087, _a_(415086, _n_(415085, "models", lambda: models), "CharField"), max_length=30)
    _l_(415088)
    skills = _c_(415093, _a_(415090, _n_(415089, "models", lambda: models), "ForeignKey"), 'Skills', on_delete=_a_(415092, _n_(415091, "models", lambda: models), "CASCADE"))
    _l_(415094)
    education = _c_(415098, _a_(415096, _n_(415095, "models", lambda: models), "ManyToManyField"), _n_(415097, "Education", lambda: Education))
    _l_(415099)
    employment_history = _c_(415103, _a_(415101, _n_(415100, "models", lambda: models), "ManyToManyField"), _n_(415102, "Empl_history", lambda: Empl_history))
    _l_(415104)


class Skills(_a_(415107, _n_(415106, "models", lambda: models), "Model")):
    _l_(415113)

    SKILLS_CHOICES = (
    ('p', 'Python'),
    ('d',  'Django'),
    ('drf', 'Django Rest Framework'),
    )
    _l_(415108)
    skills_choices = _c_(415111, _a_(415110, _n_(415109, "models", lambda: models), "CharField"), max_length=2, choices=SKILLS_CHOICES,)
    _l_(415112)