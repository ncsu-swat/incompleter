# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51717417/nameerror-name-move-is-note-defined-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(669063)

except ImportError:
    pass
try:
    from classes.carte import Carte
    _l_(669065)

except ImportError:
    pass
try:
    from fonctions.receiveRobotMoves import *
    _l_(669067)

except ImportError:
    pass
try:
    from fonctions.move import *
    _l_(669069)

except ImportError:
    pass
...
_l_(669070)
isOnExit = False
_l_(669071)
while _n_(669072, "isOnExit", lambda: isOnExit) == False:
    _l_(669084)

    #On demande au joueur la direction qu'il veut prendre
    _c_(669074, _n_(669073, "receiveRobotMoves", lambda: receiveRobotMoves))
    _l_(669075)

    #On fait avancer le robot
    conteneur = _c_(669080, _n_(669076, "move", lambda: move), _n_(669077, "Labyrinthe", lambda: Labyrinthe), _n_(669078, "movesInformation", lambda: movesInformation)['direction'], 
_n_(669079, "movesInformation", lambda: movesInformation)['steps'])
    _l_(669081)
    #On met à jour le labyrinthe
    Labyrinthe = _n_(669082, "conteneur", lambda: conteneur)
    _l_(669083)