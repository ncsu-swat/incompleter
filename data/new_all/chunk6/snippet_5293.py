# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72486540/filenotfounderror-the-system-cannot-find-the-file-specified
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(365922)

except ImportError:
    pass
try:
    import ffmpeg
    _l_(365924)

except ImportError:
    pass
try:
    import sys
    _l_(365926)

except ImportError:
    pass
try:
    import os
    _l_(365928)

except ImportError:
    pass

in_filename = "ddd.mp4"
_l_(365929)
out_filename = "THUMBNAIL.jpg"
_l_(365930)


def generate_thumbnail(in_filename, out_filename):
    _l_(365975)

    probe = _c_(365934, _a_(365932, _n_(365931, "ffmpeg", lambda: ffmpeg), "probe"), _n_(365933, "in_filename", lambda: in_filename))
    _l_(365935)
    time = _c_(365938, _n_(365936, "float", lambda: float), _n_(365937, "probe", lambda: probe)["streams"][0]["duration"]) // 2
    _l_(365939)
    width = _n_(365940, "probe", lambda: probe)["streams"][0]["width"]
    _l_(365941)
    try:
        _l_(365974)

        _c_(365956, _a_(365955, _c_(365954, _a_(365953, _c_(365952, _a_(365950, _c_(365949, _a_(365947, _c_(365946, _a_(365943, _n_(365942, "ffmpeg", lambda: ffmpeg), "input"), _n_(365944, "in_filename", lambda: in_filename), ss=_n_(365945, "time", lambda: time)), "filter"), "scale", _n_(365948, "width", lambda: width), -1), "output"), _n_(365951, "out_filename", lambda: out_filename), vframes=1), "overwrite_output")), "run"), capture_stdout=True, capture_stderr=True)
        _l_(365957)
    except _a_(365959, _n_(365958, "ffmpeg", lambda: ffmpeg), "Error") as e:
        _l_(365973)

        _c_(365967, _n_(365960, "print", lambda: print), _c_(365964, _a_(365963, _a_(365962, _n_(365961, "e", lambda: e), "stderr"), "decode")), file=_a_(365966, _n_(365965, "sys", lambda: sys), "stderr"))
        _l_(365968)
        _c_(365971, _a_(365970, _n_(365969, "sys", lambda: sys), "exit"), 1)
        _l_(365972)


_c_(365979, _n_(365976, "generate_thumbnail", lambda: generate_thumbnail), _n_(365977, "in_filename", lambda: in_filename), _n_(365978, "out_filename", lambda: out_filename))
_l_(365980)