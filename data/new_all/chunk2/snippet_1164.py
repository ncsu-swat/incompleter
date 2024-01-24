# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/21964297/typeerror-unorderable-types-function-int
#While loop function for user input
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def numInput():
    _l_(444455)

    numbers = []
    _l_(444438)

    while True:
        _l_(444452)

        num = _c_(444442, _n_(444439, "int", lambda: int), _c_(444441, _n_(444440, "input", lambda: input), 'Enter a number (-9999 to end):'))
        _l_(444443)
        if _n_(444444, "num", lambda: num) == -9999:
            _l_(444446)

            break
            _l_(444445)
        _c_(444450, _a_(444448, _n_(444447, "numbers", lambda: numbers), "append"), _n_(444449, "num", lambda: num))
        _l_(444451)
    aux = _n_(444453, "numbers", lambda: numbers)
    _l_(444454)
    return aux

#Average of all numbers function
def allNumAvg(numList):
    _l_(444463)

    aux = _c_(444458, _n_(444456, "sum", lambda: sum), _n_(444457, "numList", lambda: numList)) / _c_(444461, _n_(444459, "len", lambda: len), _n_(444460, "numList", lambda: numList))
    _l_(444462)
    return aux


#Average of all positive numbers function
def posNumAvg(numList):
    _l_(444479)

    for num in [_n_(444464, "numList", lambda: numList)]:
        _l_(444475)

        if _n_(444465, "num", lambda: num) > 0:
            _l_(444474)

            posNum = _c_(444468, _n_(444466, "sum", lambda: sum), _n_(444467, "num", lambda: num))
            _l_(444469)
            posLen = _c_(444472, _n_(444470, "len", lambda: len), _n_(444471, "num", lambda: num))
            _l_(444473)
    aux = _n_(444476, "posNum", lambda: posNum) / _n_(444477, "posLen", lambda: posLen)
    _l_(444478)
    return aux

#Avg of all negative numbers function
def nonPosAvg(numList):
    _l_(444495)

    for num in [_n_(444480, "numList", lambda: numList)]:
        _l_(444491)

        if _n_(444481, "num", lambda: num) < 0:
            _l_(444490)

            negNum = _c_(444484, _n_(444482, "sum", lambda: sum), _n_(444483, "num", lambda: num))
            _l_(444485)
            negLen = _c_(444488, _n_(444486, "len", lambda: len), _n_(444487, "num", lambda: num))
            _l_(444489)
    aux = _n_(444492, "negNum", lambda: negNum) / _n_(444493, "negLen", lambda: negLen)
    _l_(444494)
    return aux

#Creates Dictionary
myDict = {'AvgPositive':_c_(444498, _n_(444496, "posNumAvg", lambda: posNumAvg), _n_(444497, "numInput", lambda: numInput)), 'AvgNonPos':_c_(444501, _n_(444499, "nonPosAvg", lambda: nonPosAvg), _n_(444500, "numInput", lambda: numInput)), 'AvgAllNum':_c_(444504, _n_(444502, "allNumAvg", lambda: allNumAvg), _n_(444503, "numInput", lambda: numInput))}   
_l_(444505)   

#Prints List
_c_(444509, _n_(444506, "print", lambda: print), 'The list of of all numbers entered is\n', _c_(444508, _n_(444507, "numInput", lambda: numInput)),'\n')
_l_(444510)

#Prints Dictionary
_c_(444513, _n_(444511, "print", lambda: print), 'The dictionary with averages is\n', _n_(444512, "myDict", lambda: myDict))
_l_(444514)