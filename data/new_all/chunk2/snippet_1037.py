# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51232871/typeerror-a-bytes-like-object-is-required-not-str-espeakng
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
esng = _c_(450282, _n_(450281, "ESpeakNG", lambda: ESpeakNG), voice='english-us')
_l_(450283)
_n_(450284, "esng", lambda: esng).pitch = 32
_l_(450285)
_n_(450286, "esng", lambda: esng).speed = 150
_l_(450287)
_c_(450290, _a_(450289, _n_(450288, "esng", lambda: esng), "say"), 'Hello World!', sync=True)
_l_(450291)