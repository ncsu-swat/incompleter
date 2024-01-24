# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68231990/filenotfounderror-errno-2-no-such-file-or-directory-interview-part2-mp3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from os import path
    _l_(628787)

except ImportError:
    pass
try:
    from pydub import AudioSegment
    _l_(628789)

except ImportError:
    pass

#files
src = 'Interview-part2.mp3'
_l_(628790)
dst = 'Interview-part2.wav'
_l_(628791)
    
#Convert mp3 to wav
sound = _c_(628795, _a_(628793, _n_(628792, "AudioSegment", lambda: AudioSegment), "from_mp3"), _n_(628794, "src", lambda: src))
_l_(628796)