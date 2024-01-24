# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40072913/attributeerror-in-a-pygame-sprite-sprite-subclass
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Entity(_a_(538229, _a_(538228, _n_(538227, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(538289)

    entitiesTop = _c_(538232, _a_(538231, _a_(538230, pygame, "sprite"), "Group"))
    _l_(538233)
    entitiesMid = _c_(538236, _a_(538235, _a_(538234, pygame, "sprite"), "Group"))
    _l_(538237)
    entitiesBot = _c_(538240, _a_(538239, _a_(538238, pygame, "sprite"), "Group"))
    _l_(538241)
    entities = [entitiesBot, entitiesMid, entitiesTop]
    _l_(538242)

    def __init__(self, force = None):
        _l_(538288)

        _c_(538248, _a_(538246, _a_(538245, _a_(538244, _n_(538243, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(538247, "self", lambda: self))
        _l_(538249)
        if _n_(538250, "force", lambda: force) is None:
            _l_(538287)

            if _c_(538254, _n_(538251, "isinstance", lambda: isinstance), _n_(538252, "self", lambda: self), _n_(538253, "Platform", lambda: Platform)):
                _l_(538279)

                _c_(538259, _a_(538257, _a_(538256, _n_(538255, "Entity", lambda: Entity), "entitiesTop"), "add"), _n_(538258, "self", lambda: self))
                _l_(538260)
            elif _c_(538265, _n_(538261, "isinstance", lambda: isinstance), _n_(538262, "self", lambda: self), (_n_(538263, "Bullet", lambda: Bullet), _n_(538264, "Gun", lambda: Gun))):
                _l_(538278)

                _c_(538270, _a_(538268, _a_(538267, _n_(538266, "Entity", lambda: Entity), "entitiesMid"), "add"), _n_(538269, "self", lambda: self))
                _l_(538271)
            else:
                _c_(538276, _a_(538274, _a_(538273, _n_(538272, "Entity", lambda: Entity), "entitiesBot"), "add"), _n_(538275, "self", lambda: self))
                _l_(538277)
        else:
            _c_(538285, _a_(538283, _a_(538281, _n_(538280, "Entity", lambda: Entity), "entities")[_n_(538282, "force", lambda: force)], "add"), _n_(538284, "self", lambda: self))
            _l_(538286)