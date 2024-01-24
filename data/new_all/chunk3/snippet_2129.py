# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62406132/django-2-0-13-2-1-upgrade-causes-std-library-function-to-not-find-module-att
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(561778)

except ImportError:
    pass
try:
    import sys
    _l_(561780)

except ImportError:
    pass

if _n_(561781, "__name__", lambda: __name__) == "__main__":
    _l_(561824)

    package_dir = _c_(561790, _a_(561784, _a_(561783, _n_(561782, "os", lambda: os), "path"), "dirname"), _c_(561789, _a_(561787, _a_(561786, _n_(561785, "os", lambda: os), "path"), "abspath"), _n_(561788, "__file__", lambda: __file__)))
    _l_(561791)
    _c_(561796, _a_(561794, _a_(561793, _n_(561792, "sys", lambda: sys), "path"), "remove"), _n_(561795, "package_dir", lambda: package_dir))
    _l_(561797)
    _c_(561810, _a_(561800, _a_(561799, _n_(561798, "sys", lambda: sys), "path"), "insert"), 0, _c_(561809, _a_(561803, _a_(561802, _n_(561801, "os", lambda: os), "path"), "normpath"), _c_(561808, _a_(561806, _a_(561805, _n_(561804, "os", lambda: os), "path"), "join"), _n_(561807, "package_dir", lambda: package_dir), '..')))
    _l_(561811)
    _c_(561815, _a_(561814, _a_(561813, _n_(561812, "os", lambda: os), "environ"), "setdefault"), "DJANGO_SETTINGS_MODULE", "mysite.settings")
    _l_(561816)
    try:
        from django.core.management import execute_from_command_line
        _l_(561818)

    except ImportError:
        pass

    _c_(561822, _n_(561819, "execute_from_command_line", lambda: execute_from_command_line), _a_(561821, _n_(561820, "sys", lambda: sys), "argv"))
    _l_(561823)