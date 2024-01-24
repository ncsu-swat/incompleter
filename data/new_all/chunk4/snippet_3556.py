# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72254923/python-attributeerror-object-has-no-attribute-pointing-to-constructor-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from BaseballPlayer import BaseballPlayer
    _l_(590423)

except ImportError:
    pass
try:
    from CustomExceptions import InvalidPlayerNumException
    _l_(590425)

except ImportError:
    pass
try:
    from CustomExceptions import InvalidBattingException
    _l_(590427)

except ImportError:
    pass

# Try/except block
try:
    _l_(590475)

    name = _c_(590429, _n_(590428, "input", lambda: input), "Enter name: ")
    _l_(590430)
    number = _c_(590434, _n_(590431, "int", lambda: int), _c_(590433, _n_(590432, "input", lambda: input), "Enter number: "))
    _l_(590435)
    position = _c_(590437, _n_(590436, "input", lambda: input), "Enter position: ")
    _l_(590438)
    batting_avg = _c_(590442, _n_(590439, "float", lambda: float), _c_(590441, _n_(590440, "input", lambda: input), "Enter batting average: "))
    _l_(590443)

    # create an instance of a baseball player
    my_player = _c_(590449, _n_(590444, "BaseballPlayer", lambda: BaseballPlayer), _n_(590445, "name", lambda: name), _n_(590446, "number", lambda: number), _n_(590447, "position", lambda: position), _n_(590448, "batting_avg", lambda: batting_avg))
    _l_(590450)

    # invoke the to_string() method and display everything
    _c_(590455, _n_(590451, "print", lambda: print), _c_(590454, _a_(590453, _n_(590452, "my_player", lambda: my_player), "to_string")))
    _l_(590456)

# Exception handling, always go from most specific exception to most generic
except _n_(590457, "InvalidPlayerNumException", lambda: InvalidPlayerNumException) as e:
    _l_(590462)

    _c_(590460, _n_(590458, "print", lambda: print), "Invalid player number: ", _n_(590459, "e", lambda: e))
    _l_(590461)
except _n_(590463, "InvalidBattingException", lambda: InvalidBattingException) as e:
    _l_(590468)

    _c_(590466, _n_(590464, "print", lambda: print), "Invalid batting avg: ", _n_(590465, "e", lambda: e))
    _l_(590467)

# generic exception
except _n_(590469, "Exception", lambda: Exception) as ex:
    _l_(590474)

    _c_(590472, _n_(590470, "print", lambda: print), "Generic exception: ", _n_(590471, "ex", lambda: ex))
    _l_(590473)