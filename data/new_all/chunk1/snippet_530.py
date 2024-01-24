# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51110863/mutagen-python-filenotfounderror-handling
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from mutagen.easyid3 import EasyID3
    _l_(395166)

except ImportError:
    pass

def getGenre(filename):
    _l_(395183)

    try:
        _l_(395182)

        audiofile = _c_(395169, _n_(395167, "EasyID3", lambda: EasyID3), _n_(395168, "filename", lambda: filename))
        _l_(395170)
        #No genre
        if not _n_(395171, "audiofile", lambda: audiofile)['genre']:
            _l_(395175)

            aux = None
            _l_(395172)
            return aux
        else:
            aux = _n_(395173, "audiofile", lambda: audiofile)['genre']
            _l_(395174)
            return aux

    except (_n_(395176, "FileNotFoundError", lambda: FileNotFoundError),_n_(395177, "IOError", lambda: IOError)):
        _l_(395181)

        _c_(395179, _n_(395178, "print", lambda: print), "Wrong file or file path")
        _l_(395180)


_c_(395185, _n_(395184, "getGenre", lambda: getGenre), "xyz.mp3")
_l_(395186)