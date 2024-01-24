# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77687579/attributeerror-module-django-conf-global-settings-has-no-attribute-root-urlc
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main():
    _l_(553161)

    """Run administrative tasks."""
    _c_(553146, _a_(553145, _a_(553144, _n_(553143, "os", lambda: os), "environ"), "setdefault"), 'DJANGO_SETTINGS_MODULE', 'mojspecjalista.settings')
    _l_(553147)
    try:
        _l_(553155)

        from django.core.management import execute_from_command_line
        _l_(553148)
    except _n_(553149, "ImportError", lambda: ImportError) as exc:
        _l_(553154)

        raise _c_(553151, _n_(553150, "ImportError", lambda: ImportError), "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from _n_(553152, "exc", lambda: exc)
        _l_(553153)
    _c_(553159, _n_(553156, "execute_from_command_line", lambda: execute_from_command_line), _a_(553158, _n_(553157, "sys", lambda: sys), "argv"))
    _l_(553160)


if _n_(553162, "__name__", lambda: __name__) == '__main__':
    _l_(553166)

    _c_(553164, _n_(553163, "main", lambda: main))
    _l_(553165)