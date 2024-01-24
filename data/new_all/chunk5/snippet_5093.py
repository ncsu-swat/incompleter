# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72013969/nameerror-name-mark-safe-is-not-defined-django
# "admin.py"

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib.admin.widgets import AdminFileWidget
    _l_(672678)

except ImportError:
    pass

class CustomAdminFileWidget(_n_(672679, "AdminFileWidget", lambda: AdminFileWidget)):
    _l_(672712)

    def render(self, name, value, attrs=None, renderer=None):
        _l_(672711)

        result = []
        _l_(672680)
        if _c_(672683, _n_(672681, "hasattr", lambda: hasattr), _n_(672682, "value", lambda: value), "url"):
            _l_(672693)

            _c_(672691, _a_(672685, _n_(672684, "result", lambda: result), "append"), f'''<a href="{_a_(672687, _n_(672686, "value", lambda: value), "url")}" target="_blank">
                      <img 
                        src="{_a_(672689, _n_(672688, "value", lambda: value), "url")}" alt="{_n_(672690, "value", lambda: value)}" 
                        width="100" height="100"
                        style="object-fit: cover;"
                      />
                    </a>'''
            )
            _l_(672692)
        _c_(672703, _a_(672695, _n_(672694, "result", lambda: result), "append"), _c_(672702, _a_(672697, _n_(672696, "super", lambda: super)(), "render"), _n_(672698, "name", lambda: name), _n_(672699, "value", lambda: value), _n_(672700, "attrs", lambda: attrs), _n_(672701, "renderer", lambda: renderer)))
        _l_(672704)
        aux = _c_(672709, _n_(672705, "mark_safe", lambda: mark_safe), _c_(672708, _a_(672706, "", "join"), _n_(672707, "result", lambda: result)))
        _l_(672710)
        return aux