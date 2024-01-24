# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64110840/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
seqnum = None
_l_(474893)
lstFile = _c_(474896, _n_(474894, "open", lambda: open), _n_(474895, "inListFileName", lambda: inListFileName))
_l_(474897)

for lstLn in _c_(474900, _a_(474899, _n_(474898, "lstFile", lambda: lstFile), "readlines")):
    _l_(474968)

    lstVals = _c_(474905, _a_(474904, _c_(474903, _a_(474902, _n_(474901, "lstLn", lambda: lstLn), "strip")), "split"))
    _l_(474906)

    basePath=_c_(474909, _a_(474908, _n_(474907, "os", lambda: os), "getcwd"))
    _l_(474910)
    file=_c_(474916, _a_(474913, _a_(474912, _n_(474911, "os", lambda: os), "path"), "join"), _n_(474914, "basePath", lambda: basePath), 'OUT_ST',_n_(474915, "lstVals", lambda: lstVals)[1])
    _l_(474917)

    if _c_(474920, _n_(474918, "len", lambda: len), _n_(474919, "lstVals", lambda: lstVals)) > 1:
        _l_(474967)

        loadArray = _c_(474926, _a_(474925, _c_(474924, _a_(474922, _n_(474921, "np", lambda: np), "loadtxt"), _n_(474923, "file", lambda: file)), "flatten"))
        _l_(474927)

        if _n_(474928, "seqnum", lambda: seqnum) is None:
            _l_(474936)

            seqnum = _c_(474934, _a_(474930, _n_(474929, "np", lambda: np), "arange"), 1, _c_(474933, _n_(474931, "len", lambda: len), _n_(474932, "loadArray", lambda: loadArray)) + 1)
            _l_(474935)
    
        arrayTuple = _c_(474944, _n_(474937, "map", lambda: map), _n_(474938, "tuple", lambda: tuple), _c_(474943, _a_(474940, _n_(474939, "np", lambda: np), "column_stack"), (_n_(474941, "seqnum", lambda: seqnum), _n_(474942, "loadArray", lambda: loadArray))))
        _l_(474945)
        
        strucArray = _c_(474957, _a_(474947, _n_(474946, "np", lambda: np), "array"), _n_(474948, "arrayTuple", lambda: arrayTuple), _c_(474956, _a_(474950, _n_(474949, "np", lambda: np), "dtype"), [('inSeqNum', _a_(474952, _n_(474951, "np", lambda: np), "int")), (_n_(474953, "lstVals", lambda: lstVals)[0], _a_(474955, _n_(474954, "np", lambda: np), "float"))]))
        _l_(474958)
    
        _c_(474965, _a_(474961, _a_(474960, _n_(474959, "arcpy", lambda: arcpy), "da"), "ExtendTable"), _n_(474962, "target", lambda: target), _n_(474963, "seqFieldName", lambda: seqFieldName), _n_(474964, "strucArray", lambda: strucArray), 'inSeqNum', False)
        _l_(474966)

_c_(474971, _a_(474970, _n_(474969, "lstFile", lambda: lstFile), "close"))
_l_(474972)