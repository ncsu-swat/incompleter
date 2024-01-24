# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62453020/attributeerror-nonetype-object-has-no-attribute-media-player-new
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import vlc
    _l_(387530)

except ImportError:
    pass

media = _c_(387533, _a_(387532, _n_(387531, "vlc", lambda: vlc), "MediaPlayer"), 'annonce.mp4')
_l_(387534)
_c_(387537, _a_(387536, _n_(387535, "media", lambda: media), "play"))
_l_(387538)