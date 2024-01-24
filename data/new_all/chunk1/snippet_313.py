# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54262306/ffmpeg-python-wrapper-ffmpeg-run-getting-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import ffmpeg
    _l_(414068)

except ImportError:
    pass

videoInput = _c_(414071, _a_(414070, _n_(414069, "ffmpeg", lambda: ffmpeg), "input"), 'vid.mp4')
_l_(414072)

videoOutput = _c_(414075, _a_(414074, _n_(414073, "videoInput", lambda: videoInput), "output"), 'test.avi')
_l_(414076)

_c_(414079, _a_(414078, _n_(414077, "videoOutput", lambda: videoOutput), "run"))
_l_(414080)