# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71988882/attribute-error-property-object-has-no-attribute-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pytube import YouTube
    _l_(582143)

except ImportError:
    pass
try:
    import pytube
    _l_(582145)

except ImportError:
    pass

SAVE_PATH = "c:users\pavit\Desktop" #to_do
_l_(582146) #to_do


link=_c_(582148, _n_(582147, "input", lambda: input), "enter the link")
_l_(582149)

try:
    _l_(582158)

    # object creation using YouTube
    # which was imported in the beginning
    yt = _c_(582152, _n_(582150, "YouTube", lambda: YouTube), _n_(582151, "link", lambda: link))
    _l_(582153)
except:
    _l_(582157)

    _c_(582155, _n_(582154, "print", lambda: print), "Connection Error") #to handle exception
    _l_(582156) #to handle exception

mp4files = _c_(582162, _a_(582161, _a_(582160, _n_(582159, "YouTube", lambda: YouTube), "streams"), "filter"))
_l_(582163)
_c_(582171, _a_(582170, _c_(582169, _a_(582168, _c_(582167, _a_(582166, _a_(582165, _n_(582164, "yt", lambda: yt), "streams"), "filter"), progressive=True, file_extension='mp4'), "order_by"), 'resolution')[-1], "download"))
_l_(582172)

d_video = _c_(582179, _a_(582174, _n_(582173, "yt", lambda: yt), "get"), _a_(582176, _n_(582175, "mp4files", lambda: mp4files)[-1], "extension"),_a_(582178, _n_(582177, "mp4files", lambda: mp4files)[-1], "resolution"))
_l_(582180)
try:
    _l_(582190)


    _c_(582184, _a_(582182, _n_(582181, "d_video", lambda: d_video), "download"), _n_(582183, "SAVE_PATH", lambda: SAVE_PATH))
    _l_(582185)
except:
    _l_(582189)

    _c_(582187, _n_(582186, "print", lambda: print), "Some Error!")
    _l_(582188)
_c_(582192, _n_(582191, "print", lambda: print), 'Task Completed!')
_l_(582193)