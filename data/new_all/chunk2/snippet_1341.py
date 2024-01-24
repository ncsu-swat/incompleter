# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34029387/text-adventure-game-receives-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import gamedata
    _l_(452334)

except ImportError:
    pass


if _n_(452335, "__name__", lambda: __name__) == "__main__":
    _l_(452385)

    WORLD = _c_(452337, _n_(452336, "World", lambda: World), "map.txt", "locations.txt", "items.txt")
    _l_(452338)
    PLAYER = _c_(452340, _n_(452339, "Player", lambda: Player), 0,0) # set starting location of player; you may change the x, y coordinates here as appropriate
    _l_(452341) # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit", "back"]
    _l_(452342)

    while not _a_(452344, _n_(452343, "PLAYER", lambda: PLAYER), "victory"):
        _l_(452384)

        location = _c_(452351, _a_(452346, _n_(452345, "WORLD", lambda: WORLD), "get_location"), _a_(452348, _n_(452347, "PLAYER", lambda: PLAYER), "x"), _a_(452350, _n_(452349, "PLAYER", lambda: PLAYER), "y"))
        _l_(452352)

    # ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
    # depending on whether or not it's been visited before,
    #   print either full description (first time visit) or brief description (every subsequent visit)

        _c_(452354, _n_(452353, "print", lambda: print), "What to do? \n")
        _l_(452355)
        _c_(452357, _n_(452356, "print", lambda: print), "[menu]")
        _l_(452358)
        for action in _c_(452361, _a_(452360, _n_(452359, "location", lambda: location), "available_actions")):
            _l_(452366)

            _c_(452364, _n_(452362, "print", lambda: print), _n_(452363, "action", lambda: action))
            _l_(452365)
        choice = _c_(452368, _n_(452367, "input", lambda: input), "\nEnter action: ")
        _l_(452369)

        if (_n_(452370, "choice", lambda: choice) == "[menu]"):
            _l_(452383)

            _c_(452372, _n_(452371, "print", lambda: print), "Menu Options: \n")
            _l_(452373)
            for option in _n_(452374, "menu", lambda: menu):
                _l_(452379)

                _c_(452377, _n_(452375, "print", lambda: print), _n_(452376, "option", lambda: option))
                _l_(452378)
            choice = _c_(452381, _n_(452380, "input", lambda: input), "\nChoose action: ")
            _l_(452382)