# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64922421/attributeerror-tuple-object-has-no-attribute-get-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _c_(692691, _n_(692687, "range", lambda: range), _c_(692690, _n_(692688, "len", lambda: len), _n_(692689, "uniquecandidate", lambda: uniquecandidate))):
    _l_(692697)

    result = _c_(692695, _n_(692692, "zip", lambda: zip), _n_(692693, "uniquecandidate", lambda: uniquecandidate), _n_(692694, "votes", lambda: votes)) # zips two lists together  
    _l_(692696) # zips two lists together  

result_list = _c_(692700, _n_(692698, "list", lambda: list), _n_(692699, "result", lambda: result))
_l_(692701)
_c_(692706, _n_(692702, "print", lambda: print), _c_(692705, _n_(692703, "type", lambda: type), _n_(692704, "result_list", lambda: result_list)))   # returns <class 'list'>
_l_(692707)   # returns <class 'list'>

_c_(692713, _a_(692709, _n_(692708, "result_list", lambda: result_list), "sort"), key=lambda x: _c_(692712, _a_(692711, _n_(692710, "x", lambda: x), "get"), 'votes'), reverse=True) #sort by vote number
_l_(692714) #sort by vote number

_c_(692717, _n_(692715, "print", lambda: print), _n_(692716, "result_list", lambda: result_list), end='\n\n')
_l_(692718)