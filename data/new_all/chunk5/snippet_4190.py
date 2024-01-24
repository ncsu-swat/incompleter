# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61899384/how-to-handle-python-subprocess-filenotfounderror-winerror-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import ffmpeg_streaming
    _l_(706808)

except ImportError:
    pass
try:
    from ffmpeg_streaming import Formats, Bitrate, Representation, Size
    _l_(706810)

except ImportError:
    pass
try:
    import subprocess
    _l_(706812)

except ImportError:
    pass
try:
    import sys
    _l_(706814)

except ImportError:
    pass

def monitor(ffmpeg, duration, time_):
    _l_(706833)

    per = _c_(706818, _n_(706815, "round", lambda: round), _n_(706816, "time_", lambda: time_) / _n_(706817, "duration", lambda: duration) * 100)
    _l_(706819)
    _c_(706826, _a_(706822, _a_(706821, _n_(706820, "sys", lambda: sys), "stdout"), "write"), "\rTranscoding...(%s%%) [%s%s]" % (_n_(706823, "per", lambda: per), '#' * _n_(706824, "per", lambda: per), '-' * (100 - _n_(706825, "per", lambda: per))))
    _l_(706827)
    _c_(706831, _a_(706830, _a_(706829, _n_(706828, "sys", lambda: sys), "stdout"), "flush"))
    _l_(706832)

video = _c_(706836, _a_(706835, _n_(706834, "ffmpeg_streaming", lambda: ffmpeg_streaming), "input"), 'http://freja.hiof.no:1935/rtplive/_definst_/hessdalen03.stream/playlist.m3u8')
_l_(706837)

_360p = _c_(706843, _n_(706838, "Representation", lambda: Representation), _c_(706840, _n_(706839, "Size", lambda: Size), 640, 360), _c_(706842, _n_(706841, "Bitrate", lambda: Bitrate), 276 * 1024, 128 * 1024))
_l_(706844)
_480p = _c_(706850, _n_(706845, "Representation", lambda: Representation), _c_(706847, _n_(706846, "Size", lambda: Size), 854, 480), _c_(706849, _n_(706848, "Bitrate", lambda: Bitrate), 750 * 1024, 192 * 1024))
_l_(706851)
_720p = _c_(706857, _n_(706852, "Representation", lambda: Representation), _c_(706854, _n_(706853, "Size", lambda: Size), 1280, 720), _c_(706856, _n_(706855, "Bitrate", lambda: Bitrate), 2048 * 1024, 320 * 1024))
_l_(706858)

hls_stream = _c_(706864, _a_(706860, _n_(706859, "video", lambda: video), "hls"), _c_(706863, _a_(706862, _n_(706861, "Formats", lambda: Formats), "h264")), hls_list_size = 1, hls_time = 60)
_l_(706865)
_c_(706869, _a_(706867, _n_(706866, "hls_stream", lambda: hls_stream), "representations"), _n_(706868, "_480p", lambda: _480p))
_l_(706870)
_c_(706873, _a_(706872, _n_(706871, "hls_stream", lambda: hls_stream), "output"), 'C:/Users/Documents/mashpy/VideoAnalytics_Mediaserver/ffmpeg_exec_test/video_fragments/hl_test.m3u8')
_l_(706874)