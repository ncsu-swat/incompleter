# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69183938/python3-apache-mod-wsgi-filenotfounderror-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask
    _l_(586088)

except ImportError:
    pass


def create_app():
    _l_(586108)

    app = _c_(586091, _n_(586089, "Flask", lambda: Flask), _n_(586090, "__name__", lambda: __name__), instance_relative_config=False)
    _l_(586092)

    @_c_(586095, _a_(586094, _n_(586093, "app", lambda: app), "route"), "/")
    def home():
        _l_(586105)

        try:
            import sys
            _l_(586097)

        except ImportError:
            pass
        string = f"Python version {_a_(586099, _n_(586098, 'sys', lambda: sys), 'version')} Version info {_a_(586101, _n_(586100, 'sys', lambda: sys), 'version_info')}"
        _l_(586102)
        aux = _n_(586103, "string", lambda: string)
        _l_(586104)
        return aux
    aux = _n_(586106, "app", lambda: app)
    _l_(586107)

    return aux