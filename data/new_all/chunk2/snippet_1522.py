# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45897466/typeerror-pygame-surface-object-is-not-callable-pygame-module
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def town ():
    _l_(421977)

    global outTown
    _l_(421893)
    while not _n_(421894, "outTown", lambda: outTown):
        _l_(421976)

        for event in _c_(421898, _a_(421897, _a_(421896, _n_(421895, "pygame", lambda: pygame), "event"), "get")):
            _l_(421934)

            if _a_(421900, _n_(421899, "event", lambda: event), "type") == _a_(421902, _n_(421901, "pygame", lambda: pygame), "MOUSEBUTTONDOWN"):
                _l_(421921)

                _c_(421905, _n_(421903, "print", lambda: print), _n_(421904, "event", lambda: event))
                _l_(421906)
                mx, my = _c_(421910, _a_(421909, _a_(421908, _n_(421907, "pygame", lambda: pygame), "mouse"), "get_pos"))
                _l_(421911)
                mx = _n_(421912, "mx", lambda: mx) + _n_(421913, "my", lambda: my)
                _l_(421914)
                if 375 <= _n_(421915, "mx", lambda: mx) <= 448:
                    _l_(421920)

                    outTown = True
                    _l_(421916)
                    _c_(421918, _n_(421917, "print", lambda: print), "OK!")
                    _l_(421919)
            if _a_(421923, _n_(421922, "event", lambda: event), "type") == _a_(421925, _n_(421924, "pygame", lambda: pygame), "QUIT"):
                _l_(421933)

                _c_(421928, _a_(421927, _n_(421926, "pygame", lambda: pygame), "quit"))
                _l_(421929)
                _c_(421931, _n_(421930, "quit", lambda: quit))
                _l_(421932)

        houseSpr1 = _c_(421938, _a_(421937, _a_(421936, _n_(421935, "pygame", lambda: pygame), "image"), "load"), 'houseD.png') # default house img
        _l_(421939) # default house img
        _c_(421941, _n_(421940, "houseSpr1", lambda: houseSpr1), 0,250)
        _l_(421942)
        _c_(421946, _a_(421944, _n_(421943, "gameDisplay", lambda: gameDisplay), "fill"), _n_(421945, "green", lambda: green)) # background
        _l_(421947) # background
        _c_(421953, _a_(421950, _a_(421949, _n_(421948, "pygame", lambda: pygame), "draw"), "rect"), _n_(421951, "gameDisplay", lambda: gameDisplay),_n_(421952, "grey", lambda: grey),(0,400,1280,50)) # main path
        _l_(421954) # main path
        _c_(421960, _a_(421957, _a_(421956, _n_(421955, "pygame", lambda: pygame), "draw"), "rect"), _n_(421958, "gameDisplay", lambda: gameDisplay),_n_(421959, "grey", lambda: grey),(200,125,50,280)) # branch path
        _l_(421961) # branch path
        _c_(421965, _n_(421962, "player", lambda: player), _n_(421963, "x", lambda: x),_n_(421964, "y", lambda: y))
        _l_(421966)
        _c_(421970, _a_(421969, _a_(421968, _n_(421967, "pygame", lambda: pygame), "display"), "update"))
        _l_(421971)
        _c_(421974, _a_(421973, _n_(421972, "clock", lambda: clock), "tick"), 60)
        _l_(421975)

def houseSpr1(a,b):
    _l_(421983)

    _c_(421981, _a_(421979, _n_(421978, "gameDisplay", lambda: gameDisplay), "blit"), _n_(421980, "houseSpr1", lambda: houseSpr1), (0,250))
    _l_(421982)

def house1():
    _l_(421992)

    global outHouse
    _l_(421984)
    while not _n_(421985, "outHouse", lambda: outHouse):
        _l_(421991)

        _c_(421989, _a_(421987, _n_(421986, "gameDisplay", lambda: gameDisplay), "fill"), _n_(421988, "black", lambda: black))
        _l_(421990)
_c_(421994, _n_(421993, "town", lambda: town))
_l_(421995)
_c_(421997, _n_(421996, "houseSpr1", lambda: houseSpr1))
_l_(421998)
_c_(422000, _n_(421999, "gameIntro", lambda: gameIntro))
_l_(422001)
_c_(422003, _n_(422002, "house1", lambda: house1))
_l_(422004)
_c_(422007, _a_(422006, _n_(422005, "pygame", lambda: pygame), "quit"))
_l_(422008)
_c_(422010, _n_(422009, "quit", lambda: quit))
_l_(422011)