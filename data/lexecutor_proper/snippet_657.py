# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/32370281/how-to-embed-image-or-picture-in-jupyter-notebook-either-from-a-local-machine-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(64083)

except ImportError:
    pass
try:
    from ipywidgets import Image
    _l_(64085)

except ImportError:
    pass

_c_(64091, _n_(64086, "Image", lambda: Image), value=_a_(64090, _c_(64089, _a_(64088, _n_(64087, "requests", lambda: requests), "get"), 'https://octodex.github.com/images/yaktocat.png'), "content"))
_l_(64092)

