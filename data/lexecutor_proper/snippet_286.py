# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-writing-to-a-file-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for line in _n_(62202, "lines", lambda: lines):
    _l_(62214)

    _c_(62207, _n_(62203, "print", lambda: print), _c_(62206, _n_(62204, "type", lambda: type), _n_(62205, "line", lambda: line)))# <class 'bytes'>
    _l_(62208)# <class 'bytes'>
    if 'substring' in _n_(62209, "line", lambda: line):
        _l_(62213)

        _c_(62211, _n_(62210, "print", lambda: print), 'success')
        _l_(62212)

for line in _n_(62215, "lines", lambda: lines):
    _l_(62231)

    line = _c_(62218, _a_(62217, _n_(62216, "line", lambda: line), "decode"))
    _l_(62219)
    _c_(62224, _n_(62220, "print", lambda: print), _c_(62223, _n_(62221, "type", lambda: type), _n_(62222, "line", lambda: line)))# <class 'str'>
    _l_(62225)# <class 'str'>
    if 'substring' in _n_(62226, "line", lambda: line):
        _l_(62230)

        _c_(62228, _n_(62227, "print", lambda: print), 'success')
        _l_(62229)

