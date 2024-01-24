# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60601415/subprocess-startupinfo-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
filepath = "C:/Users/Linus/Desktop/Test/Audio/"     #Input audio file path
_l_(424902)     #Input audio file path
try:
    from pydub import AudioSegment
    _l_(424904)

except ImportError:
    pass
try:
    import os
    _l_(424906)

except ImportError:
    pass

def mp3_to_wav(audio_file_name):
    _l_(424925)

    if _c_(424909, _a_(424908, _n_(424907, "audio_file_name", lambda: audio_file_name), "split"), '.')[1] == 'mp3':
        _l_(424924)

        sound = _c_(424913, _a_(424911, _n_(424910, "AudioSegment", lambda: AudioSegment), "from_mp3"), _n_(424912, "audio_file_name", lambda: audio_file_name))
        _l_(424914)
        audio_file_name = _c_(424917, _a_(424916, _n_(424915, "audio_file_name", lambda: audio_file_name), "split"), '.')[0] + '.wav'
        _l_(424918)
        _c_(424922, _a_(424920, _n_(424919, "sound", lambda: sound), "export"), _n_(424921, "audio_file_name", lambda: audio_file_name), format="wav")
        _l_(424923)

if _n_(424926, "__name__", lambda: __name__) == "__main__":
    _l_(424945)

    for audio_file_name in _c_(424930, _a_(424928, _n_(424927, "os", lambda: os), "listdir"), _n_(424929, "filepath", lambda: filepath)):
        _l_(424944)

        file_name = _n_(424931, "filepath", lambda: filepath) + _n_(424932, "audio_file_name", lambda: audio_file_name)
        _l_(424933)
        file_name = _c_(424938, _a_(424936, _a_(424935, _n_(424934, "os", lambda: os), "path"), "realpath"), _n_(424937, "file_name", lambda: file_name))
        _l_(424939)
        _c_(424942, _n_(424940, "mp3_to_wav", lambda: mp3_to_wav), _n_(424941, "file_name", lambda: file_name))
        _l_(424943)