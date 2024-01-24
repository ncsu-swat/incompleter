# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71575913/getting-type-error-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def escape_characters(message):
    _l_(371650)

    for escape in _n_(371604, "ESCAPE_TTS_CHARACTERS", lambda: ESCAPE_TTS_CHARACTERS):
        _l_(371611)

        message = _c_(371609, _a_(371606, _n_(371605, "message", lambda: message), "replace"), _n_(371607, "escape", lambda: escape), "\\"+_n_(371608, "escape", lambda: escape))
        _l_(371610)
    for escape in _n_(371612, "ESCAPE_EDI_CHARACTERS", lambda: ESCAPE_EDI_CHARACTERS):
        _l_(371619)

        message = _c_(371617, _a_(371614, _n_(371613, "message", lambda: message), "replace"), _n_(371615, "escape", lambda: escape), "\\"+_n_(371616, "escape", lambda: escape))
        _l_(371618)
    for hexa in _n_(371620, "HEXA_TTS_CHARACTERS", lambda: HEXA_TTS_CHARACTERS):
        _l_(371631)

        message = _c_(371629, _a_(371622, _n_(371621, "message", lambda: message), "replace"), _n_(371623, "hexa", lambda: hexa), "\\x"+ _c_(371628, _n_(371624, "format", lambda: format), _c_(371627, _n_(371625, "ord", lambda: ord), _n_(371626, "hexa", lambda: hexa)), "x"))
        _l_(371630)
    for hexa in _n_(371632, "HEXA_EDI_CHARACTERS", lambda: HEXA_EDI_CHARACTERS):
        _l_(371643)

        message = _c_(371641, _a_(371634, _n_(371633, "message", lambda: message), "replace"), _n_(371635, "hexa", lambda: hexa), "\\x"+ _c_(371640, _n_(371636, "format", lambda: format), _c_(371639, _n_(371637, "ord", lambda: ord), _n_(371638, "hexa", lambda: hexa)), "x"))
        _l_(371642)
    message = _c_(371646, _a_(371645, _n_(371644, "message", lambda: message), "replace"), "\x00", "\\x00")
    _l_(371647)
    aux = _n_(371648, "message", lambda: message)
    _l_(371649)
    return aux
ESCAPE_TTS_CHARACTERS = ["\\", "{", "}"]
_l_(371651)
HEXA_TTS_CHARACTERS = ["$", "%"]
_l_(371652)
ESCAPE_EDI_CHARACTERS = ["'", "*"]
_l_(371653)
HEXA_EDI_CHARACTERS = ["&", "+", "#", "\"", ":"]    
_l_(371654)    

blob=b'\n\x11\n\x06TmgTty\x10\x00\x1a\x05\n\x03SIM\n\x16\n\x05Event\x10\x00\x1a\x0b\n\tDeparture\n\x12\n\x04Unit\x10\x00\x1a\x08\n\x06Minute\n\x11\n\x05Value\x10\x00\x1a\x06\n\x04-976\n\r\n\x07RefCity\x10\x00\x1a\x00\n\n\n\x04Date\x10\x00\x1a\x00\n\n\n\x04Time\x10\x00\x1a\x00\n\x0c\n\x06DftRul\x10\x00\x1a\x00\n\x0e\n\x05TiaId\x10\x00\x1a\x03\n\x011\n\x10\n\x07LastUid\x10\x00\x1a\x03\n\x011\n\x0b\n\x05Cabin\x10\x00\x1a\x00\n\x0e\n\x08BkgClass\x10\x00\x1a\x00\n\x0c\n\x06TgType\x10\x00\x1a\x00\n\r\n\x07TgValue\x10\x00\x1a\x00'
_l_(371655)

_c_(371660, _n_(371656, "print", lambda: print), _c_(371659, _n_(371657, "escape_characters", lambda: escape_characters), _n_(371658, "blob", lambda: blob)))
_l_(371661)