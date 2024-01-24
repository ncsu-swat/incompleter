# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57757630/typeerror-a-bytes-like-object-is-required-not-str-for-geniatagger
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
tagger = _c_(572168, _n_(572167, "GeniaTagger", lambda: GeniaTagger), './geniatagger/geniatagger')
_l_(572169)
# option1: my_bytes = "This is a pen.".encode()
# option2: my_bytes = b"This is a pen."
# option3: my_bytes = bytes("This is a pen.")
my_bytes = _c_(572171, _a_(572170, "This is a pen.", "encode"), 'utf8')
_l_(572172)
_c_(572177, _n_(572173, "print", lambda: print), _c_(572176, _n_(572174, "type", lambda: type), _n_(572175, "my_bytes", lambda: my_bytes)))
_l_(572178)
x = _c_(572182, _a_(572180, _n_(572179, "tagger", lambda: tagger), "parse"), _n_(572181, "my_bytes", lambda: my_bytes))
_l_(572183)