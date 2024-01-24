# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59437405/why-when-i-run-my-script-the-downloaded-image-files-have-zero-bytes-and-i-recei
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
imageFile = _c_(656946, _n_(656936, "open", lambda: open), _c_(656945, _a_(656939, _a_(656938, _n_(656937, "os", lambda: os), "path"), "join"), 'redditpics', _c_(656944, _a_(656942, _a_(656941, _n_(656940, "os", lambda: os), "path"), "basename"), _n_(656943, "url", lambda: url))), 'wb')
_l_(656947)
for chunk in _c_(656950, _a_(656949, _n_(656948, "url", lambda: url), "iter_content"), 100000):
    _l_(656960)

    _c_(656953, _n_(656951, "print", lambda: print), "saving " + _n_(656952, "imageFile", lambda: imageFile))
    _l_(656954)

    _c_(656958, _a_(656956, _n_(656955, "imageFile", lambda: imageFile), "write"), _n_(656957, "chunk", lambda: chunk))
    _l_(656959)
_c_(656963, _a_(656962, _n_(656961, "imageFile", lambda: imageFile), "close"))
_l_(656964)
_c_(656966, _n_(656965, "print", lambda: print), 'Done.')
_l_(656967)