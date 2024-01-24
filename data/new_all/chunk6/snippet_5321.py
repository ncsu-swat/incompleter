# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68181312/typeerror-unsupported-operand-types-for-builtin-function-or-method-and
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def solution(s):
    _l_(358791)

 
    word = _c_(358764, _a_(358763, _c_(358762, _n_(358761, "input", lambda: input), "Enter Text:" ), "lower"))
    _l_(358765)
    
    for i in _c_(358770, _n_(358766, "range", lambda: range), 0, _c_(358769, _n_(358767, "len", lambda: len), _n_(358768, "s", lambda: s))):
        _l_(358788)

        if _c_(358774, _a_(358773, _n_(358771, "s", lambda: s)[_n_(358772, "i", lambda: i)], "isupper")):
            _l_(358777)

            word=_n_(358775, "input", lambda: input) + '000001'
            _l_(358776)
        word=_n_(358778, "input", lambda: input)+_n_(358779, "braillecodes", lambda: braillecodes)[_c_(358786, _a_(358781, _n_(358780, "asciicodes", lambda: asciicodes), "index"), _c_(358785, _a_(358784, _n_(358782, "s", lambda: s)[_n_(358783, "i", lambda: i)], "lower")))]
        _l_(358787)
    aux = _n_(358789, "word", lambda: word)
    _l_(358790)
    return aux
#The Alpha Lookup Table
asciicodes = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
_l_(358792)
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
_l_(358793)


#Print 
_c_(358797, _n_(358794, "print", lambda: print), _c_(358796, _n_(358795, "solution", lambda: solution), 's'))
_l_(358798)