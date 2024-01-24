# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59518408/mutagen-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
audio = _c_(650400, _n_(650399, "FLAC", lambda: FLAC), "music.flac")
_l_(650401)
_n_(650402, "audio", lambda: audio)['artist'] = _a_(650405, _a_(650404, _n_(650403, "sarki", lambda: sarki), "artist"), "name")
_l_(650406)
_n_(650407, "audio", lambda: audio)['title'] = _a_(650409, _n_(650408, "sarki", lambda: sarki), "name")
_l_(650410)
pic = _c_(650412, _n_(650411, "Picture", lambda: Picture))
_l_(650413)
_n_(650414, "pic", lambda: pic).type = _a_(650417, _a_(650416, _n_(650415, "id3", lambda: id3), "PictureType"), "COVER_FRONT")
_l_(650418)
_n_(650419, "pic", lambda: pic).width = 640
_l_(650420)
_n_(650421, "pic", lambda: pic).height = 640
_l_(650422)
_n_(650423, "pic", lambda: pic).mime = 'image/jpeg'
_l_(650424)
_n_(650425, "pic", lambda: pic).data = "music.jpg"
_l_(650426)

_c_(650430, _a_(650428, _n_(650427, "audio", lambda: audio), "add_picture"), _n_(650429, "pic", lambda: pic))
_l_(650431)
_c_(650434, _a_(650433, _n_(650432, "audio", lambda: audio), "save"))
_l_(650435)