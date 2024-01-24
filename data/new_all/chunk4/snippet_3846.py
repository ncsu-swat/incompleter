# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66599498/how-to-fix-pytube-error-attributeerror-nonetype-object-has-no-attribute-do
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pytube import YouTube
    _l_(581267)

except ImportError:
    pass

def dowload_vid(l, d):
    _l_(581308)

    link = _c_(581270, _a_(581269, _n_(581268, "l", lambda: l), "get"))
    _l_(581271)
    dir = _c_(581274, _a_(581273, _n_(581272, "d", lambda: d), "get"))
    _l_(581275)

    try:
        _l_(581284)

        vid = _c_(581278, _n_(581276, "YouTube", lambda: YouTube), _n_(581277, "link", lambda: link))
        _l_(581279)
    except:
        _l_(581283)

        _c_(581281, _n_(581280, "print", lambda: print), "Connection Error or Video doesn't exist")
        _l_(581282)

    vid_res = _c_(581288, _a_(581287, _a_(581286, _n_(581285, "vid", lambda: vid), "streams"), "get_highest_resolution"))
    _l_(581289)

    try:
        _l_(581307)

        _c_(581299, _a_(581297, _c_(581296, _a_(581295, _c_(581294, _a_(581292, _a_(581291, _n_(581290, "vid", lambda: vid), "streams"), "filter"), res=_n_(581293, "vid_res", lambda: vid_res)), "first")), "download"), _n_(581298, "dir", lambda: dir))
        _l_(581300)
    except _n_(581301, "IndexError", lambda: IndexError) as e:
        _l_(581306)

        _c_(581304, _n_(581302, "print", lambda: print), _n_(581303, "e", lambda: e))
        _l_(581305)