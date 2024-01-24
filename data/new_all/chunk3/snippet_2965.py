# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56824119/getting-file-not-found-error-when-trying-to-load-eel-js
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import eel
    _l_(553918)

except ImportError:
    pass

class GUI:
    _l_(553932)

    def __init__(self):
        _l_(553931)

        _c_(553921, _a_(553920, _n_(553919, "eel", lambda: eel), "init"), "web")
        _l_(553922)
        _c_(553925, _a_(553924, _n_(553923, "eel", lambda: eel), "start"), "main.html", block = False)
        _l_(553926)
        _c_(553929, _a_(553928, _n_(553927, "eel", lambda: eel), "sleep"), 5)
        _l_(553930)