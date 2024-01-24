# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74642934/how-to-resolve-attribute-error-array-array-object-has-no-attribute-read-in-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(543862)

except ImportError:
    pass
try:
    from functools import reduce
    _l_(543864)

except ImportError:
    pass
try:
    import numpy
    _l_(543866)

except ImportError:
    pass
try:
    import array
    _l_(543868)

except ImportError:
    pass
try:
    from utils import *
    _l_(543870)

except ImportError:
    pass

def load_raw_data_with_mhd(filename):
    _l_(543957)

    meta_dict = _c_(543873, _n_(543871, "read_meta_header", lambda: read_meta_header), _n_(543872, "filename", lambda: filename))
    _l_(543874)
    dim = _c_(543877, _n_(543875, "int", lambda: int), _n_(543876, "meta_dict", lambda: meta_dict)['NDims'])
    _l_(543878)
    assert(_n_(543879, "meta_dict", lambda: meta_dict)['ElementType']=='MET_FLOAT')
    _l_(543880)
    arr = [_c_(543883, _n_(543881, "int", lambda: int), _n_(543882, "i", lambda: i)) for i in _c_(543886, _a_(543885, _n_(543884, "meta_dict", lambda: meta_dict)['DimSize'], "split"))]
    _l_(543887)
    volume = _c_(543893, _n_(543888, "reduce", lambda: reduce), lambda x,y: _n_(543889, "x", lambda: x)*_n_(543890, "y", lambda: y), _n_(543891, "arr", lambda: arr)[0:_n_(543892, "dim", lambda: dim)-1], 1)
    _l_(543894)
    pwd = _c_(543899, _a_(543897, _a_(543896, _n_(543895, "os", lambda: os), "path"), "split"), _n_(543898, "filename", lambda: filename))[0]
    _l_(543900)
    if _n_(543901, "pwd", lambda: pwd):
        _l_(543907)

        data_file = _n_(543902, "pwd", lambda: pwd) +'/' + _n_(543903, "meta_dict", lambda: meta_dict)['ElementDataFile']
        _l_(543904)
    else:
        data_file = _n_(543905, "meta_dict", lambda: meta_dict)['ElementDataFile']
        _l_(543906)
    _c_(543910, _n_(543908, "print", lambda: print), _n_(543909, "data_file", lambda: data_file))
    _l_(543911)
    fid = _c_(543914, _n_(543912, "open", lambda: open), _n_(543913, "data_file", lambda: data_file),'rb')
    _l_(543915)
    binvalues = _c_(543918, _a_(543917, _n_(543916, "array", lambda: array), "array"), 'f')
    _l_(543919)
    _c_(543926, _a_(543921, _n_(543920, "binvalues", lambda: binvalues), "read"), _n_(543922, "fid", lambda: fid), _n_(543923, "volume", lambda: volume)*_n_(543924, "arr", lambda: arr)[_n_(543925, "dim", lambda: dim)-1])
    _l_(543927)
    if _c_(543929, _n_(543928, "is_little_endian", lambda: is_little_endian)):
        _l_(543934)

        _c_(543932, _a_(543931, _n_(543930, "binvalues", lambda: binvalues), "byteswap"))
        _l_(543933)
    _c_(543937, _a_(543936, _n_(543935, "fid", lambda: fid), "close"))
    _l_(543938)
    data = _c_(543944, _a_(543940, _n_(543939, "numpy", lambda: numpy), "array"), _n_(543941, "binvalues", lambda: binvalues), _a_(543943, _n_(543942, "numpy", lambda: numpy), "float"))
    _l_(543945)
    data = _c_(543952, _a_(543947, _n_(543946, "numpy", lambda: numpy), "reshape"), _n_(543948, "data", lambda: data), (_n_(543949, "arr", lambda: arr)[_n_(543950, "dim", lambda: dim)-1], _n_(543951, "volume", lambda: volume)))
    _l_(543953)
    aux = (_n_(543954, "data", lambda: data), _n_(543955, "meta_dict", lambda: meta_dict))
    _l_(543956)
    return aux