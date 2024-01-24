# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62406132/django-2-0-13-2-1-upgrade-causes-std-library-function-to-not-find-module-att
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from uwsgi_tasks import set_uwsgi_callbacks, django_setup
    _l_(556867)

except ImportError:
    pass

_c_(556869, _n_(556868, "set_uwsgi_callbacks", lambda: set_uwsgi_callbacks))
_l_(556870)
_c_(556872, _n_(556871, "django_setup", lambda: django_setup))
_l_(556873)