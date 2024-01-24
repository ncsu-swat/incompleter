# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64922421/attributeerror-tuple-object-has-no-attribute-get-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _c_(703265, _n_(703261, "range", lambda: range), _c_(703264, _n_(703262, "len", lambda: len), _n_(703263, "uniquecandidate", lambda: uniquecandidate))):
    _l_(703271)

    result = _c_(703269, _n_(703266, "zip", lambda: zip), _n_(703267, "uniquecandidate", lambda: uniquecandidate), _n_(703268, "votes", lambda: votes)) # zips two lists together  
    _l_(703270) # zips two lists together  

result_list = _c_(703274, _n_(703272, "list", lambda: list), _n_(703273, "result", lambda: result))
_l_(703275)
_c_(703280, _n_(703276, "print", lambda: print), _c_(703279, _n_(703277, "type", lambda: type), _n_(703278, "result_list", lambda: result_list)))   # returns <class 'list'>
_l_(703281)   # returns <class 'list'>

_c_(703287, _a_(703283, _n_(703282, "result_list", lambda: result_list), "sort"), key=lambda x: _c_(703286, _a_(703285, _n_(703284, "x", lambda: x), "get"), 'votes'), reverse=True) #sort by vote number
_l_(703288) #sort by vote number

_c_(703291, _n_(703289, "print", lambda: print), _n_(703290, "result_list", lambda: result_list), end='\n\n')
_l_(703292)