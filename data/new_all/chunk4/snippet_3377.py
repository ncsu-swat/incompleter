# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75181755/function-call-for-pong-game-made-in-python-throwing-attributeerror-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from gamescreen import GameScreen
    _l_(603137)

except ImportError:
    pass
try:
    from player import Player
    _l_(603139)

except ImportError:
    pass
try:
    import time
    _l_(603141)

except ImportError:
    pass
try:
    from ball import Ball
    _l_(603143)

except ImportError:
    pass

screen = _c_(603145, _n_(603144, "GameScreen", lambda: GameScreen))
_l_(603146)
screen = _a_(603148, _n_(603147, "screen", lambda: screen), "screen")
_l_(603149)
player_1 = _c_(603151, _n_(603150, "Player", lambda: Player))
_l_(603152)
player_2 = _c_(603154, _n_(603153, "Player", lambda: Player))
_l_(603155)
_c_(603158, _a_(603157, _n_(603156, "player_1", lambda: player_1), "left"))
_l_(603159)
_c_(603162, _a_(603161, _n_(603160, "player_2", lambda: player_2), "right"))
_l_(603163)
_c_(603166, _a_(603165, _n_(603164, "player_1", lambda: player_1), "show"))
_l_(603167)
_c_(603170, _a_(603169, _n_(603168, "player_2", lambda: player_2), "show"))
_l_(603171)
ball = _c_(603173, _n_(603172, "Ball", lambda: Ball))
_l_(603174)

_c_(603179, _a_(603176, _n_(603175, "screen", lambda: screen), "onkeypress"), fun = _a_(603178, _n_(603177, "player_1", lambda: player_1), "up"), key='w')
_l_(603180)
_c_(603185, _a_(603182, _n_(603181, "screen", lambda: screen), "onkeypress"), fun = _a_(603184, _n_(603183, "player_1", lambda: player_1), "down"), key='s')
_l_(603186)
_c_(603191, _a_(603188, _n_(603187, "screen", lambda: screen), "onkeypress"), fun = _a_(603190, _n_(603189, "player_2", lambda: player_2), "up"), key='Up')
_l_(603192)
_c_(603197, _a_(603194, _n_(603193, "screen", lambda: screen), "onkeypress"), fun = _a_(603196, _n_(603195, "player_2", lambda: player_2), "down"), key='Down')
_l_(603198)

on = True
_l_(603199)
while _n_(603200, "on", lambda: on):
    _l_(603205)

    _c_(603203, _a_(603202, _n_(603201, "ball", lambda: ball), "move"))
    _l_(603204)

_c_(603208, _a_(603207, _n_(603206, "screen", lambda: screen), "exitonclick"))
_l_(603209)