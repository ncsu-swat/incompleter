# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61565222/generating-video-using-moviepy-using-image-and-text-but-getting-error-like-size
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import glob
    _l_(549195)

except ImportError:
    pass
try:
    import os
    _l_(549197)

except ImportError:
    pass
try:
    from natsort import natsorted
    _l_(549199)

except ImportError:
    pass
try:
    from moviepy.editor import *
    _l_(549201)

except ImportError:
    pass

base_dir = _c_(549205, _a_(549204, _a_(549203, _n_(549202, "os", lambda: os), "path"), "realpath"), "./images/")
_l_(549206)
_c_(549209, _n_(549207, "print", lambda: print), _n_(549208, "base_dir", lambda: base_dir))
_l_(549210)

gif_name = 'pic'
_l_(549211)
fps = 24
_l_(549212)

file_list = _c_(549215, _a_(549214, _n_(549213, "glob", lambda: glob), "glob"), './images/*.jpg')  # Get all the pngs in the current directory
_l_(549216)  # Get all the pngs in the current directory
file_list_sorted = _c_(549219, _n_(549217, "natsorted", lambda: natsorted), _n_(549218, "file_list", lambda: file_list),reverse=False)  # Sort the images
_l_(549220)  # Sort the images

clips = [_c_(549225, _a_(549224, _c_(549223, _n_(549221, "ImageClip", lambda: ImageClip), _n_(549222, "m", lambda: m)), "set_duration"), 5)
         for m in _n_(549226, "file_list_sorted", lambda: file_list_sorted)]
_l_(549227)
_c_(549230, _n_(549228, "print", lambda: print), _n_(549229, "clips", lambda: clips))
_l_(549231)



text_list = ["Piggy", "Kermit", "Gonzo", "Fozzie"]
_l_(549232)
clip_list = []
_l_(549233)

for text in _n_(549234, "text_list", lambda: text_list):
    _l_(549259)

    try:
        _l_(549258)

        txt_clip = _c_(549239, _a_(549238, _c_(549237, _n_(549235, "TextClip", lambda: TextClip), _n_(549236, "text", lambda: text), fontsize = 70, color = 'white'), "set_duration"), 2)
        _l_(549240)
        _c_(549244, _a_(549242, _n_(549241, "clip_list", lambda: clip_list), "append"), _n_(549243, "txt_clip", lambda: txt_clip))
        _l_(549245)
    except _n_(549246, "UnicodeEncodeError", lambda: UnicodeEncodeError):
        _l_(549257)

        txt_clip = _c_(549250, _a_(549249, _c_(549248, _n_(549247, "TextClip", lambda: TextClip), "Issue with text", fontsize = 70, color = 'white'), "set_duration"), 2)
        _l_(549251)
        _c_(549255, _a_(549253, _n_(549252, "clip_list", lambda: clip_list), "append"), _n_(549254, "txt_clip", lambda: txt_clip))
        _l_(549256)
_c_(549262, _n_(549260, "print", lambda: print), _n_(549261, "clip_list", lambda: clip_list))
_l_(549263)


final_clip = _c_(549267, _n_(549264, "CompositeVideoClip", lambda: CompositeVideoClip), [_n_(549265, "clips", lambda: clips), _n_(549266, "clip_list", lambda: clip_list)])
_l_(549268)
_c_(549271, _a_(549270, _n_(549269, "final_clip", lambda: final_clip), "write_videofile"), "./video/export.mp4", fps = 24, codec = 'mpeg4')
_l_(549272)