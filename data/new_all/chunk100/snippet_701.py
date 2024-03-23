# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5055042/whats-the-best-practice-using-a-settings-file-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import yaml
    _l_(61634)

except ImportError:
    pass
config = _c_(61639, _a_(61636, _n_(61635, "yaml", lambda: yaml), "safe_load"), _c_(61638, _n_(61637, "open", lambda: open), "path/to/config.yml"))
_l_(61640)

