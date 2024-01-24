# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65226109/pytube-error-attributeerror-nonetype-object-has-no-attribute-download
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pytube import YouTube
    _l_(458490)

except ImportError:
    pass
try:
    import pytube
    _l_(458492)

except ImportError:
    pass
yt_title = _a_(458495, _c_(458494, _n_(458493, "YouTube", lambda: YouTube), 'https://www.youtube.com/watch?v=ZjDZrReZ4EI'), "title")
_l_(458496)
ytd = _c_(458503, _a_(458502, _c_(458501, _a_(458500, _a_(458499, _c_(458498, _n_(458497, "YouTube", lambda: YouTube), 'https://www.youtube.com/watch?v=ZjDZrReZ4EI'), "streams"), "first")), "download"))
_l_(458504)