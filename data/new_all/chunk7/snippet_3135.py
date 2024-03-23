# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41939088/typeerror-when-using-moviepy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from moviepy.editor import *
    _l_(609599)

except ImportError:
    pass

x = _c_(609603, _n_(609600, "int", lambda: int), _c_(609602, _n_(609601, "input", lambda: input), "When do you want the cut to start? "))
_l_(609604)
y = _c_(609608, _n_(609605, "int", lambda: int), _c_(609607, _n_(609606, "input", lambda: input), "When do you want the cut to end? "))
_l_(609609)


video = _c_(609615, _a_(609612, _c_(609611, _n_(609610, "VideoFileClip", lambda: VideoFileClip), "D:\Videos\Gatlinburgh Drone River 2.MOV"), "subclip"), _n_(609613, "x", lambda: x),_n_(609614, "y", lambda: y))
_l_(609616)

##video = VideoFileClip("D:\SF_ep\T_R_D.mov").subclip(x,y)  #Path is correct


txt_clip = _c_(609622, _a_(609621, _c_(609620, _a_(609619, _c_(609618, _n_(609617, "TextClip", lambda: TextClip), "The Red Dot episode",fontsize=70,color='white'), "set_position"), 'center'), "set_duration"), 10)
_l_(609623)

result = _c_(609627, _n_(609624, "CompositeVideoClip", lambda: CompositeVideoClip), [_n_(609625, "video", lambda: video), _n_(609626, "txt_clip", lambda: txt_clip)])
_l_(609628)

_c_(609631, _a_(609630, _n_(609629, "result", lambda: result), "write_videofile"), "Text on Screen.webm",fps=25)
_l_(609632)