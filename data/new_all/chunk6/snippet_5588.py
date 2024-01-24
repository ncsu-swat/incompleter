# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71575913/getting-type-error-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def escape_characters(message):
    _l_(363232)

    for escape in _n_(363186, "ESCAPE_TTS_CHARACTERS", lambda: ESCAPE_TTS_CHARACTERS):
        _l_(363193)

        message = _c_(363191, _a_(363188, _n_(363187, "message", lambda: message), "replace"), _n_(363189, "escape", lambda: escape), "\\"+_n_(363190, "escape", lambda: escape))
        _l_(363192)
    for escape in _n_(363194, "ESCAPE_EDI_CHARACTERS", lambda: ESCAPE_EDI_CHARACTERS):
        _l_(363201)

        message = _c_(363199, _a_(363196, _n_(363195, "message", lambda: message), "replace"), _n_(363197, "escape", lambda: escape), "\\"+_n_(363198, "escape", lambda: escape))
        _l_(363200)
    for hexa in _n_(363202, "HEXA_TTS_CHARACTERS", lambda: HEXA_TTS_CHARACTERS):
        _l_(363213)

        message = _c_(363211, _a_(363204, _n_(363203, "message", lambda: message), "replace"), _n_(363205, "hexa", lambda: hexa), "\\x"+ _c_(363210, _n_(363206, "format", lambda: format), _c_(363209, _n_(363207, "ord", lambda: ord), _n_(363208, "hexa", lambda: hexa)), "x"))
        _l_(363212)
    for hexa in _n_(363214, "HEXA_EDI_CHARACTERS", lambda: HEXA_EDI_CHARACTERS):
        _l_(363225)

        message = _c_(363223, _a_(363216, _n_(363215, "message", lambda: message), "replace"), _n_(363217, "hexa", lambda: hexa), "\\x"+ _c_(363222, _n_(363218, "format", lambda: format), _c_(363221, _n_(363219, "ord", lambda: ord), _n_(363220, "hexa", lambda: hexa)), "x"))
        _l_(363224)
    message = _c_(363228, _a_(363227, _n_(363226, "message", lambda: message), "replace"), "\x00", "\\x00")
    _l_(363229)
    aux = _n_(363230, "message", lambda: message)
    _l_(363231)
    return aux
ESCAPE_TTS_CHARACTERS = ["\\", "{", "}"]
_l_(363233)
HEXA_TTS_CHARACTERS = ["$", "%"]
_l_(363234)
ESCAPE_EDI_CHARACTERS = ["'", "*"]
_l_(363235)
HEXA_EDI_CHARACTERS = ["&", "+", "#", "\"", ":"]    
_l_(363236)    

blob=b'\n\x11\n\x06TmgTty\x10\x00\x1a\x05\n\x03SIM\n\x16\n\x05Event\x10\x00\x1a\x0b\n\tDeparture\n\x12\n\x04Unit\x10\x00\x1a\x08\n\x06Minute\n\x11\n\x05Value\x10\x00\x1a\x06\n\x04-976\n\r\n\x07RefCity\x10\x00\x1a\x00\n\n\n\x04Date\x10\x00\x1a\x00\n\n\n\x04Time\x10\x00\x1a\x00\n\x0c\n\x06DftRul\x10\x00\x1a\x00\n\x0e\n\x05TiaId\x10\x00\x1a\x03\n\x011\n\x10\n\x07LastUid\x10\x00\x1a\x03\n\x011\n\x0b\n\x05Cabin\x10\x00\x1a\x00\n\x0e\n\x08BkgClass\x10\x00\x1a\x00\n\x0c\n\x06TgType\x10\x00\x1a\x00\n\r\n\x07TgValue\x10\x00\x1a\x00'
_l_(363237)

_c_(363242, _n_(363238, "print", lambda: print), _c_(363241, _n_(363239, "escape_characters", lambda: escape_characters), _n_(363240, "blob", lambda: blob)))
_l_(363243)