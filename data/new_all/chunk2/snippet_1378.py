# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68000190/why-i-get-attributeerror-class-class-name-has-no-attribute-attribute-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Parser:
    _l_(428164)

    def __init__(self, inst, type):
        _l_(428145)

        _n_(428134, "self", lambda: self).inst = _c_(428137, _a_(428136, _n_(428135, "inst", lambda: inst), "strip"))
        _l_(428138)
        _n_(428139, "self", lambda: self).type = None
        _l_(428140)
        _c_(428143, _a_(428142, _n_(428141, "self", lambda: self), "checkType"))
        _l_(428144)

    def checkType(self):
        _l_(428163)

        if _c_(428149, _a_(428148, _a_(428147, _n_(428146, "self", lambda: self), "inst"), "startswith"), '//') or _a_(428151, _n_(428150, "self", lambda: self), "inst") in ['\n', '\r\n']:
            _l_(428162)

            aux = ""
            _l_(428152)
            return aux

        elif _c_(428156, _a_(428155, _a_(428154, _n_(428153, "self", lambda: self), "inst"), "startswith"), '@'):
            _l_(428161)

            _n_(428157, "self", lambda: self).type = 'A'
            _l_(428158)

        else:
            _n_(428159, "self", lambda: self).type = 'C'
            _l_(428160)

def main():
    _l_(428180)

    with _c_(428168, _n_(428165, "open", lambda: open), _a_(428167, _n_(428166, "sys", lambda: sys), "argv")[1], 'r') as asm:
        _l_(428179)

        for inst in _n_(428169, "asm", lambda: asm):
            _l_(428178)

            P = _a_(428171, _n_(428170, "Parser", lambda: Parser), "inst")
            _l_(428172)
            _c_(428176, _n_(428173, "print", lambda: print), _a_(428175, _n_(428174, "p", lambda: p), "type"))
            _l_(428177)


if _n_(428181, "__name__", lambda: __name__) == "__main__":
    _l_(428185)

    _c_(428183, _n_(428182, "main", lambda: main))
    _l_(428184)