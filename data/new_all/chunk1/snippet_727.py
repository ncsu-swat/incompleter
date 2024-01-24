# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36021430/getting-a-typeerror-for-unknown-reason
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(384602)

except ImportError:
    pass
try:
    import operator
    _l_(384604)

except ImportError:
    pass
_c_(384607, _a_(384606, _n_(384605, "pygame", lambda: pygame), "init"))
_l_(384608)
screen = _c_(384612, _a_(384611, _a_(384610, _n_(384609, "pygame", lambda: pygame), "display"), "set_mode"), (400, 711))
_l_(384613)
_c_(384617, _a_(384616, _a_(384615, _n_(384614, "pygame", lambda: pygame), "display"), "set_caption"), "INIX")
_l_(384618)
Calculator_Screen = _c_(384622, _a_(384621, _a_(384620, _n_(384619, "pygame", lambda: pygame), "image"), "load"), "Calculator.Screen.png")
_l_(384623)
op = {
    "+": _a_(384625, _n_(384624, "operator", lambda: operator), "add"),
    "-": _a_(384627, _n_(384626, "operator", lambda: operator), "sub"),
    "*": _a_(384629, _n_(384628, "operator", lambda: operator), "mul"),
    "/": _a_(384631, _n_(384630, "operator", lambda: operator), "truediv"),
}
_l_(384632)
def calculator_module():
    _l_(384750)


    events = _c_(384638, _n_(384633, "list", lambda: list), _c_(384637, _a_(384636, _a_(384635, _n_(384634, "pygame", lambda: pygame), "event"), "get")))
    _l_(384639)
    for event in _n_(384640, "events", lambda: events):
        _l_(384749)

        if _a_(384642, _n_(384641, "event", lambda: event), "type") == _a_(384644, _n_(384643, "pygame", lambda: pygame), "QUIT"):
            _l_(384648)

            Calculator = False
            _l_(384645)
            aux = _n_(384646, "Calculator", lambda: Calculator)
            _l_(384647)
            return aux
        if _a_(384650, _n_(384649, "event", lambda: event), "type") == _a_(384652, _n_(384651, "pygame", lambda: pygame), "MOUSEBUTTONUP"):
            _l_(384748)

            x, y = _c_(384656, _a_(384655, _a_(384654, _n_(384653, "pygame", lambda: pygame), "mouse"), "get_pos"))
            _l_(384657)
            if _n_(384658, "x", lambda: x) > 17 and _n_(384659, "x", lambda: x) < 107 and _n_(384660, "y", lambda: y) > 445 and _n_(384661, "y", lambda: y) < 530:
                _l_(384747)

                aux = "1"
                _l_(384662)
                return aux
            elif _n_(384663, "x", lambda: x) > 108 and _n_(384664, "x", lambda: x) < 198 and _n_(384665, "y", lambda: y) > 445 and _n_(384666, "y", lambda: y) < 530:
                _l_(384746)

                aux = "2"
                _l_(384667)
                return aux
            elif _n_(384668, "x", lambda: x) > 199 and _n_(384669, "x", lambda: x) < 290 and _n_(384670, "y", lambda: y) > 445 and _n_(384671, "y", lambda: y) < 530:
                _l_(384745)

                aux = "3"
                _l_(384672)
                return aux
            elif _n_(384673, "x", lambda: x) > 17 and _n_(384674, "x", lambda: x) < 107 and _n_(384675, "y", lambda: y) > 336 and _n_(384676, "y", lambda: y) < 443:
                _l_(384744)

                aux = "4"
                _l_(384677)
                return aux
            elif _n_(384678, "x", lambda: x) > 108 and _n_(384679, "x", lambda: x) < 198 and _n_(384680, "y", lambda: y) > 336 and _n_(384681, "y", lambda: y) < 443:
                _l_(384743)

                aux = "5"
                _l_(384682)
                return aux
            elif _n_(384683, "x", lambda: x) > 199 and _n_(384684, "x", lambda: x) < 290 and _n_(384685, "y", lambda: y) > 336 and _n_(384686, "y", lambda: y) < 443:
                _l_(384742)

                aux = "6"
                _l_(384687)
                return aux
            elif _n_(384688, "x", lambda: x) > 17 and _n_(384689, "x", lambda: x) < 107 and _n_(384690, "y", lambda: y) > 268 and _n_(384691, "y", lambda: y) < 334:
                _l_(384741)

                aux = "7"
                _l_(384692)
                return aux
            elif _n_(384693, "x", lambda: x) > 108 and _n_(384694, "x", lambda: x) < 198 and _n_(384695, "y", lambda: y) > 268 and _n_(384696, "y", lambda: y) < 334:
                _l_(384740)

                aux = "8"
                _l_(384697)
                return aux
            elif _n_(384698, "x", lambda: x) > 199 and _n_(384699, "x", lambda: x) < 290 and _n_(384700, "y", lambda: y) > 268 and _n_(384701, "y", lambda: y) < 334:
                _l_(384739)

                aux = "9"
                _l_(384702)
                return aux
            elif _n_(384703, "x", lambda: x) > 17 and _n_(384704, "x", lambda: x) < 107 and _n_(384705, "y", lambda: y) > 532 and _n_(384706, "y", lambda: y) < 620:
                _l_(384738)

                aux = "0"
                _l_(384707)
                return aux
            elif _n_(384708, "x", lambda: x) > 199 and _n_(384709, "x", lambda: x) < 290 and _n_(384710, "y", lambda: y) > 532 and _n_(384711, "y", lambda: y) < 620:
                _l_(384737)

                aux = "="
                _l_(384712)
                return aux
            elif _n_(384713, "x", lambda: x) > 292 and _n_(384714, "x", lambda: x) < 380 and _n_(384715, "y", lambda: y) > 532 and _n_(384716, "y", lambda: y) < 620:
                _l_(384736)

                aux = "+"
                _l_(384717)
                return aux
            elif _n_(384718, "x", lambda: x) > 292 and _n_(384719, "x", lambda: x) < 380 and _n_(384720, "y", lambda: y) > 445 and _n_(384721, "y", lambda: y) < 530:
                _l_(384735)

                aux = "-"
                _l_(384722)
                return aux
            elif _n_(384723, "x", lambda: x) > 292 and _n_(384724, "x", lambda: x) < 380 and _n_(384725, "y", lambda: y) > 268 and _n_(384726, "y", lambda: y) < 334:
                _l_(384734)

                aux = "/"
                _l_(384727)
                return aux
            elif _n_(384728, "x", lambda: x) > 292 and _n_(384729, "x", lambda: x) < 380 and _n_(384730, "y", lambda: y) > 336 and _n_(384731, "y", lambda: y) < 443:
                _l_(384733)

                aux = "*"
                _l_(384732)
                return aux

Calculator = True
_l_(384751)
while _n_(384752, "Calculator", lambda: Calculator):
    _l_(384844)

    _c_(384756, _a_(384754, _n_(384753, "screen", lambda: screen), "blit"), _n_(384755, "Calculator_Screen", lambda: Calculator_Screen), (0, 0))
    _l_(384757)
    _c_(384761, _a_(384760, _a_(384759, _n_(384758, "pygame", lambda: pygame), "display"), "update"))
    _l_(384762)
    events = _c_(384768, _n_(384763, "list", lambda: list), _c_(384767, _a_(384766, _a_(384765, _n_(384764, "pygame", lambda: pygame), "event"), "get")))
    _l_(384769)
    for event in _n_(384770, "events", lambda: events):
        _l_(384843)

        if _a_(384772, _n_(384771, "event", lambda: event), "type") == _a_(384774, _n_(384773, "pygame", lambda: pygame), "QUIT"):
            _l_(384776)

            Calculator = False
            _l_(384775)
        if _a_(384778, _n_(384777, "event", lambda: event), "type") == _a_(384780, _n_(384779, "pygame", lambda: pygame), "MOUSEBUTTONUP"):
            _l_(384842)

            x, y = _c_(384784, _a_(384783, _a_(384782, _n_(384781, "pygame", lambda: pygame), "mouse"), "get_pos"))
            _l_(384785)
            if _n_(384786, "x", lambda: x) > 180 and _n_(384787, "x", lambda: x) < 218 and _n_(384788, "y", lambda: y) > 670 and _n_(384789, "y", lambda: y) < 708:
                _l_(384791)

                Calculator = False
                _l_(384790)

            while True:
                _l_(384841)

                current = 0
                _l_(384792)
                num1 = 0
                _l_(384793)
                num2 = 0
                _l_(384794)

                while _n_(384795, "current", lambda: current) not in _n_(384796, "op", lambda: op):
                    _l_(384805)

                    num1 = _n_(384797, "num1", lambda: num1)*10 + _c_(384800, _n_(384798, "int", lambda: int), _n_(384799, "current", lambda: current))
                    _l_(384801)
                    current = _c_(384803, _n_(384802, "calculator_module", lambda: calculator_module))
                    _l_(384804)
                last_op = _n_(384806, "current", lambda: current)
                _l_(384807)
                current = 0
                _l_(384808)
                while _n_(384809, "current", lambda: current) != "=":
                    _l_(384830)

                    if _n_(384810, "current", lambda: current) in _n_(384811, "op", lambda: op):
                        _l_(384826)

                        num1 = _c_(384816, _n_(384812, "op", lambda: op)[_n_(384813, "last_op", lambda: last_op)], _n_(384814, "num1", lambda: num1), _n_(384815, "num2", lambda: num2))
                        _l_(384817)
                        last_op = _n_(384818, "current", lambda: current)
                        _l_(384819)
                        num2 = 0
                        _l_(384820)
                    else:
                        num2 = _n_(384821, "num2", lambda: num2)*10 + _c_(384824, _n_(384822, "int", lambda: int), _n_(384823, "current", lambda: current))
                        _l_(384825)
                    current = _c_(384828, _n_(384827, "calculator_module", lambda: calculator_module))
                    _l_(384829)
                res = _c_(384835, _n_(384831, "op", lambda: op)[_n_(384832, "last_op", lambda: last_op)], _n_(384833, "num1", lambda: num1), _n_(384834, "num2", lambda: num2))
                _l_(384836)
                _c_(384839, _n_(384837, "print", lambda: print), _n_(384838, "res", lambda: res))
                _l_(384840)