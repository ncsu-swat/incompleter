# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57361606/getting-type-error-expected-string-or-bytes-like-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(391648)

except ImportError:
    pass
def clean_str(string):
    _l_(391680)

    """
    Tokenization/string cleaning for dataset
    Every dataset is lower cased except
    """
    string = _c_(391652, _a_(391650, _n_(391649, "re", lambda: re), "sub"), r"\n", "", _n_(391651, "string", lambda: string))    
    _l_(391653)    
    string = _c_(391657, _a_(391655, _n_(391654, "re", lambda: re), "sub"), r"\r", "", _n_(391656, "string", lambda: string)) 
    _l_(391658) 
    string = _c_(391662, _a_(391660, _n_(391659, "re", lambda: re), "sub"), r"[0-9]", "digit", _n_(391661, "string", lambda: string))
    _l_(391663)
    string = _c_(391667, _a_(391665, _n_(391664, "re", lambda: re), "sub"), r"\'", "", _n_(391666, "string", lambda: string))   
    _l_(391668)   
    string = _c_(391672, _a_(391670, _n_(391669, "re", lambda: re), "sub"), r"\"", "", _n_(391671, "string", lambda: string))    
    _l_(391673)    
    aux = _c_(391678, _a_(391677, _c_(391676, _a_(391675, _n_(391674, "string", lambda: string), "strip")), "lower"))
    _l_(391679)
    return aux
X = []
_l_(391681)
for i in _c_(391685, _n_(391682, "range", lambda: range), _a_(391684, _n_(391683, "df", lambda: df), "shape")[0]):
    _l_(391695)

    _c_(391693, _a_(391687, _n_(391686, "X", lambda: X), "append"), _c_(391692, _n_(391688, "clean_str", lambda: clean_str), _a_(391690, _n_(391689, "df", lambda: df), "iloc")[_n_(391691, "i", lambda: i)][1])) #0,1,2,3
    _l_(391694) #0,1,2,3
y = _c_(391699, _a_(391697, _n_(391696, "np", lambda: np), "array"), _n_(391698, "df", lambda: df)["Standardpositionsname"])
_l_(391700)