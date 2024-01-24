# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65839209/typeerror-can-only-concatenate-list-not-str-to-list-create-a-script-that-co
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(640891)

except ImportError:
    pass
inputList = []
_l_(640892)
for file in ['text1.txt','text2.txt']:
    _l_(640930)

    with _c_(640895, _n_(640893, "open", lambda: open), _n_(640894, "file", lambda: file),'r') as infile:
        _l_(640929)

        k = 0
        _l_(640896)
        for line in _n_(640897, "infile", lambda: infile):
            _l_(640927)

            i = 0
            _l_(640898)
            if _n_(640899, "i", lambda: i) < _c_(640902, _n_(640900, "len", lambda: len), _n_(640901, "inputList", lambda: inputList)) and _n_(640903, "k", lambda: k):
                _l_(640925)

                _c_(640913, _a_(640906, _n_(640904, "inputList", lambda: inputList)[_n_(640905, "i", lambda: i)], "extend"), _c_(640912, _a_(640911, _c_(640910, _a_(640908, _n_(640907, "re", lambda: re), "sub"), '[^A-Za-z0-9,]+', '', _n_(640909, "line", lambda: line)), "split"), ","))
                _l_(640914)
            else :
                _c_(640923, _a_(640916, _n_(640915, "inputList", lambda: inputList), "append"), _c_(640922, _a_(640921, _c_(640920, _a_(640918, _n_(640917, "re", lambda: re), "sub"), '[^A-Za-z0-9,]+', '', _n_(640919, "line", lambda: line)), "split"), ","))
                _l_(640924)
            i += 1
            _l_(640926)
        k = 1
        _l_(640928)
_c_(640933, _n_(640931, "print", lambda: print), _n_(640932, "inputList", lambda: inputList))
_l_(640934)
with _c_(640936, _n_(640935, "open", lambda: open), 'text3','w') as outfile:
    _l_(640944)

    for line in _n_(640937, "inputList", lambda: inputList):
        _l_(640943)

        _c_(640941, _a_(640939, _n_(640938, "outfile", lambda: outfile), "write"), _n_(640940, "line", lambda: line) + '\n')
        _l_(640942)