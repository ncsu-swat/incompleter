# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68181312/typeerror-unsupported-operand-types-for-builtin-function-or-method-and
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def solution(s):
    _l_(354157)

 
    word = _c_(354130, _a_(354129, _c_(354128, _n_(354127, "input", lambda: input), "Enter Text:" ), "lower"))
    _l_(354131)
    
    for i in _c_(354136, _n_(354132, "range", lambda: range), 0, _c_(354135, _n_(354133, "len", lambda: len), _n_(354134, "s", lambda: s))):
        _l_(354154)

        if _c_(354140, _a_(354139, _n_(354137, "s", lambda: s)[_n_(354138, "i", lambda: i)], "isupper")):
            _l_(354143)

            word=_n_(354141, "input", lambda: input) + '000001'
            _l_(354142)
        word=_n_(354144, "input", lambda: input)+_n_(354145, "braillecodes", lambda: braillecodes)[_c_(354152, _a_(354147, _n_(354146, "asciicodes", lambda: asciicodes), "index"), _c_(354151, _a_(354150, _n_(354148, "s", lambda: s)[_n_(354149, "i", lambda: i)], "lower")))]
        _l_(354153)
    aux = _n_(354155, "word", lambda: word)
    _l_(354156)
    return aux
#The Alpha Lookup Table
asciicodes = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
_l_(354158)
braillecodes = [
'000000',
'100000',
'110000',
'100100',
'100110',
'100010',
'110100',
'110110',
'110010',
'010100',
'010110',
'101000',
'111000',
'101100',
'101110',
'101010',
'111100',
'111110',
'111010',
'011100',
'011110',
'101001',
'111001',
'010111',
'101101',
'101111',
'101011']
_l_(354159)


#Print 
_c_(354163, _n_(354160, "print", lambda: print), _c_(354162, _n_(354161, "solution", lambda: solution), 's'))
_l_(354164)