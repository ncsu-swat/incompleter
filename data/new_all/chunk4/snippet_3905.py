# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65541371/file-not-found-error-but-showing-contents-of-file-in-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with  _c_(639230, _n_(639229, "open", lambda: open), "songs.txt","r") as filesongs:
            _l_(639237)

            songs=_c_(639235, _a_(639234, _c_(639233, _a_(639232, _n_(639231, "filesongs", lambda: filesongs), "read")), "replace"), '\n', '')
            _l_(639236)

random=_c_(639240, _a_(639239, _n_(639238, "random", lambda: random), "randint"), 0,3)
_l_(639241)
ransong=_c_(639246, _a_(639244, _c_(639243, _n_(639242, "open", lambda: open), "songs.txt","r"), "readline"), 0,_n_(639245, "random", lambda: random))
_l_(639247)