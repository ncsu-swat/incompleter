# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75594525/pytest-monkeypatching-dataclass-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pytest
    _l_(597954)

except ImportError:
    pass
try:
    from my_module.settings import PathConfiguration, Configuration
    _l_(597956)

except ImportError:
    pass

@_a_(597958, _n_(597957, "pytest", lambda: pytest), "fixture")
def configuration(monkeypatch, tmp_path):
    _l_(597966)

    _c_(597964, _a_(597960, _n_(597959, "monkeypatch", lambda: monkeypatch), "setattr"), _a_(597962, _n_(597961, "Configuration", lambda: Configuration), "path"), 'home', _n_(597963, "tmp_path", lambda: tmp_path))
    _l_(597965)