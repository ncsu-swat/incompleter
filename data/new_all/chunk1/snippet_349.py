# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38918748/why-does-mocking-open-and-returning-a-filenotfounderror-raise-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(405537)

except ImportError:
    pass
try:
    import so_config
    _l_(405539)

except ImportError:
    pass


def load_savelocation():
    _l_(405571)

    path = _c_(405547, _a_(405542, _a_(405541, _n_(405540, "os", lambda: os), "path"), "join"), _a_(405544, _n_(405543, "so_config", lambda: so_config), "ROOT"), _a_(405546, _n_(405545, "so_config", lambda: so_config), "SAVELOCATION_FN"))
    _l_(405548)
    savelocation_path = _c_(405553, _a_(405551, _a_(405550, _n_(405549, "os", lambda: os), "path"), "normpath"), _n_(405552, "path", lambda: path))
    _l_(405554)
    try:
        _l_(405570)

        with _c_(405557, _n_(405555, "open", lambda: open), _n_(405556, "savelocation_path", lambda: savelocation_path)) as f:
            _l_(405563)

            _n_(405558, "so_config", lambda: so_config).SAVELOCATION_PATH = _c_(405561, _a_(405560, _n_(405559, "f", lambda: f), "readline"))
            _l_(405562)
    except _n_(405564, "FileNotFoundError", lambda: FileNotFoundError):
        _l_(405569)

        _n_(405565, "so_config", lambda: so_config).SAVELOCATION_PATH = _a_(405567, _n_(405566, "so_config", lambda: so_config), "ROOT")
        _l_(405568)