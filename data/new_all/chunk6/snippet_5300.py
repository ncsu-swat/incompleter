# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72486540/filenotfounderror-the-system-cannot-find-the-file-specified
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(362341)

except ImportError:
    pass
try:
    import ffmpeg
    _l_(362343)

except ImportError:
    pass
try:
    import sys
    _l_(362345)

except ImportError:
    pass
try:
    import os
    _l_(362347)

except ImportError:
    pass

in_filename = "ddd.mp4"
_l_(362348)
out_filename = "THUMBNAIL.jpg"
_l_(362349)


def generate_thumbnail(in_filename, out_filename):
    _l_(362394)

    probe = _c_(362353, _a_(362351, _n_(362350, "ffmpeg", lambda: ffmpeg), "probe"), _n_(362352, "in_filename", lambda: in_filename))
    _l_(362354)
    time = _c_(362357, _n_(362355, "float", lambda: float), _n_(362356, "probe", lambda: probe)["streams"][0]["duration"]) // 2
    _l_(362358)
    width = _n_(362359, "probe", lambda: probe)["streams"][0]["width"]
    _l_(362360)
    try:
        _l_(362393)

        _c_(362375, _a_(362374, _c_(362373, _a_(362372, _c_(362371, _a_(362369, _c_(362368, _a_(362366, _c_(362365, _a_(362362, _n_(362361, "ffmpeg", lambda: ffmpeg), "input"), _n_(362363, "in_filename", lambda: in_filename), ss=_n_(362364, "time", lambda: time)), "filter"), "scale", _n_(362367, "width", lambda: width), -1), "output"), _n_(362370, "out_filename", lambda: out_filename), vframes=1), "overwrite_output")), "run"), capture_stdout=True, capture_stderr=True)
        _l_(362376)
    except _a_(362378, _n_(362377, "ffmpeg", lambda: ffmpeg), "Error") as e:
        _l_(362392)

        _c_(362386, _n_(362379, "print", lambda: print), _c_(362383, _a_(362382, _a_(362381, _n_(362380, "e", lambda: e), "stderr"), "decode")), file=_a_(362385, _n_(362384, "sys", lambda: sys), "stderr"))
        _l_(362387)
        _c_(362390, _a_(362389, _n_(362388, "sys", lambda: sys), "exit"), 1)
        _l_(362391)


_c_(362398, _n_(362395, "generate_thumbnail", lambda: generate_thumbnail), _n_(362396, "in_filename", lambda: in_filename), _n_(362397, "out_filename", lambda: out_filename))
_l_(362399)