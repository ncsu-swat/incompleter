# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51717417/nameerror-name-move-is-note-defined-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(673862)

except ImportError:
    pass
try:
    from classes.carte import Carte
    _l_(673864)

except ImportError:
    pass
try:
    from fonctions.receiveRobotMoves import *
    _l_(673866)

except ImportError:
    pass
try:
    from fonctions.move import *
    _l_(673868)

except ImportError:
    pass
...
_l_(673869)
isOnExit = False
_l_(673870)
while _n_(673871, "isOnExit", lambda: isOnExit) == False:
    _l_(673883)

    #On demande au joueur la direction qu'il veut prendre
    _c_(673873, _n_(673872, "receiveRobotMoves", lambda: receiveRobotMoves))
    _l_(673874)

    #On fait avancer le robot
    conteneur = _c_(673879, _n_(673875, "move", lambda: move), _n_(673876, "Labyrinthe", lambda: Labyrinthe), _n_(673877, "movesInformation", lambda: movesInformation)['direction'], 
_n_(673878, "movesInformation", lambda: movesInformation)['steps'])
    _l_(673880)
    #On met à jour le labyrinthe
    Labyrinthe = _n_(673881, "conteneur", lambda: conteneur)
    _l_(673882)