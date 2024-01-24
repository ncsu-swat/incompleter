# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61871631/typeerror-list-indices-must-be-integers-or-slices-not-re-pattern
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(545502)

except ImportError:
    pass

regexcode0 = _c_(545505, _a_(545504, _n_(545503, "re", lambda: re), "compile"), r'Test 0')
_l_(545506)
regexcode1 = _c_(545509, _a_(545508, _n_(545507, "re", lambda: re), "compile"), r'Test 1')
_l_(545510)
regexcode2 = _c_(545513, _a_(545512, _n_(545511, "re", lambda: re), "compile"), r'Test 2')
_l_(545514)

results_Test0 = []
_l_(545515)
results_Test1 = []
_l_(545516)
results_Test2 = []
_l_(545517)

allResults = [_n_(545518, "results_Test0", lambda: results_Test0), _n_(545519, "results_Test1", lambda: results_Test1), _n_(545520, "results_Test2", lambda: results_Test2)]
_l_(545521)
regexlist = [_n_(545522, "regexcode0", lambda: regexcode0), _n_(545523, "regexcode1", lambda: regexcode1), _n_(545524, "regexcode2", lambda: regexcode2)]
_l_(545525)

textBody = 'Hi there, Test 2 was a failure'
_l_(545526)

def text_extract(text):
    _l_(545556)

    for i in _n_(545527, "regexlist", lambda: regexlist):
        _l_(545553)

        match = _c_(545532, _a_(545529, _n_(545528, "re", lambda: re), "search"), _n_(545530, "i", lambda: i), _n_(545531, "text", lambda: text))
        _l_(545533)
        if _n_(545534, "match", lambda: match):
            _l_(545545)

            matchObj = _c_(545537, _a_(545536, _n_(545535, "match", lambda: match), "group"))
            _l_(545538)
            _c_(545543, _a_(545541, _n_(545539, "allResults", lambda: allResults)[_n_(545540, "i", lambda: i)], "append"), _n_(545542, "matchObj", lambda: matchObj))
            _l_(545544)

        if not _n_(545546, "match", lambda: match):
            _l_(545552)

            _c_(545550, _a_(545549, _n_(545547, "allResults", lambda: allResults)[_n_(545548, "i", lambda: i)], "append"), 'No Solution')
            _l_(545551)
    aux = _n_(545554, "allResults", lambda: allResults)
    _l_(545555)

    return aux

_c_(545561, _n_(545557, "print", lambda: print), _c_(545560, _n_(545558, "text_extract", lambda: text_extract), _n_(545559, "textBody", lambda: textBody)))
_l_(545562)