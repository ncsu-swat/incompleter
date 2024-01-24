# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42227047/error-importing-videofileclip-from-moviepy-attributeerror-permissionerror-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from moviepy.editor import VideoFileClip
    _l_(460840)

except ImportError:
    pass
try:
    from moviepy.video.io.VideoFileClip import VideoFileClip
    _l_(460842)

except ImportError:
    pass