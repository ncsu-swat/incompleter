# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/20023345/another-name-error-for-my-text-adventure-game-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class character(_n_(370116, "object", lambda: object)):
    _l_(370129)

    def __init__(self,name,hp,maxhp):
        _l_(370126)

        _n_(370117, "self", lambda: self).name = _n_(370118, "name", lambda: name)
        _l_(370119)
        _n_(370120, "self", lambda: self).hp = _n_(370121, "hp", lambda: hp)
        _l_(370122)
        _n_(370123, "self", lambda: self).maxhp = _n_(370124, "maxhp", lambda: maxhp)
        _l_(370125)
    def attack(self,other):
        _l_(370128)

        pass
        _l_(370127)



p=_c_(370132, _n_(370130, "player", lambda: player), _n_(370131, "Players_name", lambda: Players_name), 100, 100, 10, 5,)
_l_(370133)
while (_a_(370135, _n_(370134, "p", lambda: p), "hp")>0):
    _l_(370174)

    a=_c_(370137, _n_(370136, "input", lambda: input), "What do you want to do?")
    _l_(370138)
    if _n_(370139, "a", lambda: a)=="Instructions":
        _l_(370173)

        _c_(370141, _n_(370140, "Instructions", lambda: Instructions))
        _l_(370142)
    elif _n_(370143, "a", lambda: a)=="Commands":
        _l_(370172)

        _c_(370145, _n_(370144, "Commands", lambda: Commands))
        _l_(370146)
    elif _n_(370147, "a", lambda: a)=="Fight":
        _l_(370171)

        _c_(370150, _n_(370148, "print", lambda: print), "Level",_n_(370149, "wave", lambda: wave),"Wave Begins")
        _l_(370151)
        if _n_(370152, "wave", lambda: wave) < 6:
            _l_(370170)

            b = _c_(370155, _a_(370154, _n_(370153, "random_enemies", lambda: random_enemies), "weak"))
            _l_(370156)
            _c_(370159, _n_(370157, "print", lambda: print), "A",_n_(370158, "b", lambda: b),"Appeared!")
            _l_(370160)
            _c_(370167, _n_(370161, "print", lambda: print), "Stats of",_n_(370162, "b", lambda: b), ": \n Health=", _a_(370164, _n_(370163, "b", lambda: b), "hp"),"Attack Damage=",_a_(370166, _n_(370165, "b", lambda: b), "attack_damage"))
            _l_(370168)
            continue
            _l_(370169)