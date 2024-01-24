# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46482252/attributeerror-resume-object-has-no-attribute-prefetch-related
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Resume(_a_(453619, _n_(453618, "models", lambda: models), "Model")):
    _l_(453627)

    applicant = _c_(453622, _a_(453620, models, "OneToOneField"), User, on_delete=_a_(453621, models, "CASCADE"))
    _l_(453623)
    name = _c_(453625, _a_(453624, models, "CharField"), max_length=100, blank=False, null=False, help_text="Full Name")
    _l_(453626)

class Education(_a_(453629, _n_(453628, "models", lambda: models), "Model")):
    _l_(453637)

    resume = _c_(453632, _a_(453630, models, "ForeignKey"), _n_(453631, "Resume", lambda: Resume), related_name='educations')
    _l_(453633)
    name = _c_(453635, _a_(453634, models, "CharField"), max_length=100, blank=False, null=False, help_text="Name of an institution")
    _l_(453636)