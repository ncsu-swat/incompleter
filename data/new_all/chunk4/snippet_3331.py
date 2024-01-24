# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75594525/pytest-monkeypatching-dataclass-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from dataclasses import dataclass
    _l_(620785)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(620787)

except ImportError:
    pass

@_n_(620788, "dataclass", lambda: dataclass)
class PathConfiguration:
    _l_(620793)

    home: _n_(620789, "Path", lambda: Path)
    _l_(620790)
    other: _n_(620791, "Path", lambda: Path)
    _l_(620792)

@_n_(620794, "dataclass", lambda: dataclass)
class Configuration:
    _l_(620797)

    path: _n_(620795, "PathConfiguration", lambda: PathConfiguration)
    _l_(620796)