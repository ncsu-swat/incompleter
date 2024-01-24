# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27092337/why-am-i-getting-a-typeerror-unsupported-operand-types-for-nonetype-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def testDenary(testValue):
    _l_(412528)

    if _n_(412513, "testValue", lambda: testValue) < _c_(412515, _n_(412514, "int", lambda: int), 0):
        _l_(412527)

        _c_(412517, _n_(412516, "print", lambda: print), "Error: Negative value input. Please try again!")
        _l_(412518)
        aux = False
        _l_(412519)
        return aux
    elif _n_(412520, "testValue", lambda: testValue) > 255:
        _l_(412526)

        _c_(412522, _n_(412521, "print", lambda: print), "Error: Input value too high. Please try again!")
        _l_(412523)
        aux = False
        _l_(412524)
        return aux
    else:
        aux = True
        _l_(412525)
        return aux

def getDenary():
    _l_(412543)

    denIn = _c_(412532, _n_(412529, "int", lambda: int), _c_(412531, _n_(412530, "input", lambda: input), "Please enter a number between 0 and 255: "))
    _l_(412533)
    if _c_(412536, _n_(412534, "testDenary", lambda: testDenary), _n_(412535, "denIn", lambda: denIn)):
        _l_(412542)

        aux = _n_(412537, "denIn", lambda: denIn)
        _l_(412538)
        return aux
    else:
        _c_(412540, _n_(412539, "getDenary", lambda: getDenary))
        _l_(412541)

def convertToBinary(denaryIn):
    _l_(412577)

    x = 0
    _l_(412544)
    result = []
    _l_(412545)
    for number in _c_(412547, _n_(412546, "range", lambda: range), 8):
        _l_(412563)

        bit = _n_(412548, "denaryIn", lambda: denaryIn) % 2
        _l_(412549)
        _c_(412553, _a_(412551, _n_(412550, "result", lambda: result), "append"), _n_(412552, "bit", lambda: bit))
        _l_(412554)
        denaryIn = _n_(412555, "denaryIn", lambda: denaryIn) // 2
        _l_(412556)
        _c_(412561, _n_(412557, "print", lambda: print), _c_(412560, _n_(412558, "type", lambda: type), _n_(412559, "denaryIn", lambda: denaryIn)))
        _l_(412562)
    _c_(412566, _a_(412565, _n_(412564, "result", lambda: result), "reverse"))
    _l_(412567)
    str1 = _c_(412573, _a_(412568, "", "join"), (_c_(412571, _n_(412569, "str", lambda: str), _n_(412570, "x", lambda: x))for x in _n_(412572, "result", lambda: result)))
    _l_(412574)
    aux = _n_(412575, "str1", lambda: str1)
    _l_(412576)
    return aux

def main():
    _l_(412592)

    denary = _c_(412579, _n_(412578, "getDenary", lambda: getDenary))
    _l_(412580)
    answer = _c_(412583, _n_(412581, "convertToBinary", lambda: convertToBinary), _n_(412582, "denary", lambda: denary))
    _l_(412584)
    _c_(412587, _n_(412585, "print", lambda: print), "Binary version = " + _n_(412586, "answer", lambda: answer))
    _l_(412588)
    _c_(412590, _n_(412589, "main", lambda: main))
    _l_(412591)

_c_(412594, _n_(412593, "main", lambda: main))
_l_(412595)