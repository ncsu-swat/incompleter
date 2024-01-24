# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73590895/attributeerror-wsgirequest-object-has-no-attribute-get-i-got-this-error-ear
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.forms import ModelForm
    _l_(581498)

except ImportError:
    pass
try:
    from .models import Project
    _l_(581500)

except ImportError:
    pass


class ProjectForm(_n_(581501, "ModelForm", lambda: ModelForm)):
    _l_(581506)

    class Meta:
        _l_(581505)

        model = _n_(581502, "Project", lambda: Project)
        _l_(581503)
        fields = '__all__'
        _l_(581504)