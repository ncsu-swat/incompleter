# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72486540/filenotfounderror-the-system-cannot-find-the-file-specified
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(357477)

except ImportError:
    pass
try:
    import ffmpeg
    _l_(357479)

except ImportError:
    pass
try:
    import sys
    _l_(357481)

except ImportError:
    pass
try:
    import os
    _l_(357483)

except ImportError:
    pass

in_filename = "ddd.mp4"
_l_(357484)
out_filename = "THUMBNAIL.jpg"
_l_(357485)


def generate_thumbnail(in_filename, out_filename):
    _l_(357530)

    probe = _c_(357489, _a_(357487, _n_(357486, "ffmpeg", lambda: ffmpeg), "probe"), _n_(357488, "in_filename", lambda: in_filename))
    _l_(357490)
    time = _c_(357493, _n_(357491, "float", lambda: float), _n_(357492, "probe", lambda: probe)["streams"][0]["duration"]) // 2
    _l_(357494)
    width = _n_(357495, "probe", lambda: probe)["streams"][0]["width"]
    _l_(357496)
    try:
        _l_(357529)

        _c_(357511, _a_(357510, _c_(357509, _a_(357508, _c_(357507, _a_(357505, _c_(357504, _a_(357502, _c_(357501, _a_(357498, _n_(357497, "ffmpeg", lambda: ffmpeg), "input"), _n_(357499, "in_filename", lambda: in_filename), ss=_n_(357500, "time", lambda: time)), "filter"), "scale", _n_(357503, "width", lambda: width), -1), "output"), _n_(357506, "out_filename", lambda: out_filename), vframes=1), "overwrite_output")), "run"), capture_stdout=True, capture_stderr=True)
        _l_(357512)
    except _a_(357514, _n_(357513, "ffmpeg", lambda: ffmpeg), "Error") as e:
        _l_(357528)

        _c_(357522, _n_(357515, "print", lambda: print), _c_(357519, _a_(357518, _a_(357517, _n_(357516, "e", lambda: e), "stderr"), "decode")), file=_a_(357521, _n_(357520, "sys", lambda: sys), "stderr"))
        _l_(357523)
        _c_(357526, _a_(357525, _n_(357524, "sys", lambda: sys), "exit"), 1)
        _l_(357527)


_c_(357534, _n_(357531, "generate_thumbnail", lambda: generate_thumbnail), _n_(357532, "in_filename", lambda: in_filename), _n_(357533, "out_filename", lambda: out_filename))
_l_(357535)