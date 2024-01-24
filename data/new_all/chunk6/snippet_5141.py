# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/20023345/another-name-error-for-my-text-adventure-game-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class character(_n_(353102, "object", lambda: object)):
    _l_(353115)

    def __init__(self,name,hp,maxhp):
        _l_(353112)

        _n_(353103, "self", lambda: self).name = _n_(353104, "name", lambda: name)
        _l_(353105)
        _n_(353106, "self", lambda: self).hp = _n_(353107, "hp", lambda: hp)
        _l_(353108)
        _n_(353109, "self", lambda: self).maxhp = _n_(353110, "maxhp", lambda: maxhp)
        _l_(353111)
    def attack(self,other):
        _l_(353114)

        pass
        _l_(353113)



p=_c_(353118, _n_(353116, "player", lambda: player), _n_(353117, "Players_name", lambda: Players_name), 100, 100, 10, 5,)
_l_(353119)
while (_a_(353121, _n_(353120, "p", lambda: p), "hp")>0):
    _l_(353160)

    a=_c_(353123, _n_(353122, "input", lambda: input), "What do you want to do?")
    _l_(353124)
    if _n_(353125, "a", lambda: a)=="Instructions":
        _l_(353159)

        _c_(353127, _n_(353126, "Instructions", lambda: Instructions))
        _l_(353128)
    elif _n_(353129, "a", lambda: a)=="Commands":
        _l_(353158)

        _c_(353131, _n_(353130, "Commands", lambda: Commands))
        _l_(353132)
    elif _n_(353133, "a", lambda: a)=="Fight":
        _l_(353157)

        _c_(353136, _n_(353134, "print", lambda: print), "Level",_n_(353135, "wave", lambda: wave),"Wave Begins")
        _l_(353137)
        if _n_(353138, "wave", lambda: wave) < 6:
            _l_(353156)

            b = _c_(353141, _a_(353140, _n_(353139, "random_enemies", lambda: random_enemies), "weak"))
            _l_(353142)
            _c_(353145, _n_(353143, "print", lambda: print), "A",_n_(353144, "b", lambda: b),"Appeared!")
            _l_(353146)
            _c_(353153, _n_(353147, "print", lambda: print), "Stats of",_n_(353148, "b", lambda: b), ": \n Health=", _a_(353150, _n_(353149, "b", lambda: b), "hp"),"Attack Damage=",_a_(353152, _n_(353151, "b", lambda: b), "attack_damage"))
            _l_(353154)
            continue
            _l_(353155)