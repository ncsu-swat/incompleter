# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69183938/python3-apache-mod-wsgi-filenotfounderror-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask
    _l_(632550)

except ImportError:
    pass


def create_app():
    _l_(632570)

    app = _c_(632553, _n_(632551, "Flask", lambda: Flask), _n_(632552, "__name__", lambda: __name__), instance_relative_config=False)
    _l_(632554)

    @_c_(632557, _a_(632556, _n_(632555, "app", lambda: app), "route"), "/")
    def home():
        _l_(632567)

        try:
            import sys
            _l_(632559)

        except ImportError:
            pass
        string = f"Python version {_a_(632561, _n_(632560, 'sys', lambda: sys), 'version')} Version info {_a_(632563, _n_(632562, 'sys', lambda: sys), 'version_info')}"
        _l_(632564)
        aux = _n_(632565, "string", lambda: string)
        _l_(632566)
        return aux
    aux = _n_(632568, "app", lambda: app)
    _l_(632569)

    return aux