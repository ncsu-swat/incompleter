# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50557518/getting-nameerror-name-room-path-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def room():
    _l_(536893)

    room_path=["1","2"]
    _l_(536891)
    user_choice = ""
    _l_(536892)

_c_(536895, _n_(536894, "print", lambda: print), "If you decide to ditch Todd and go to the campfire alone, enter 1")
_l_(536896)
_c_(536898, _n_(536897, "print", lambda: print), "If you decide to drag Todd with you to the campfire, enter 2")
_l_(536899)
user_choice = _c_(536901, _n_(536900, "input", lambda: input), "your option number")
_l_(536902)

if _n_(536903, "user_choice", lambda: user_choice) == _n_(536904, "room_path", lambda: room_path) [1]:
    _l_(536914)

    _c_(536906, _n_(536905, "print", lambda: print), "yes")
    _l_(536907)
elif _n_(536908, "user_choice", lambda: user_choice) == _n_(536909, "room_path", lambda: room_path) [2]:
    _l_(536913)

    _c_(536911, _n_(536910, "print", lambda: print), "no")
    _l_(536912)