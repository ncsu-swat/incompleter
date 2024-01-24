# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46284357/python-subclass-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class socialNetwork:
    _l_(589191)

    class node:
        _l_(589190)

        def __init__(self, name, friendList):
            _l_(589173)

            _n_(589167, "self", lambda: self).name=_n_(589168, "name", lambda: name)
            _l_(589169)
            _n_(589170, "self", lambda: self).friendList=_n_(589171, "friendList", lambda: friendList)
            _l_(589172)

        def __init__(self):
            _l_(589176)

            _n_(589174, "self", lambda: self).nodeList=[]
            _l_(589175)

        def addPerson(self, name, friendList):
            _l_(589189)

            person=_c_(589181, _a_(589178, _n_(589177, "self", lambda: self), "node"), _n_(589179, "name", lambda: name),_n_(589180, "friendList", lambda: friendList))
            _l_(589182)
            _c_(589187, _a_(589185, _a_(589184, _n_(589183, "self", lambda: self), "nodeList"), "append"), _n_(589186, "person", lambda: person))
            _l_(589188)

s = _c_(589193, _n_(589192, "socialNetwork", lambda: socialNetwork))
_l_(589194)
_c_(589197, _a_(589196, _n_(589195, "s", lambda: s), "addPerson"), "John",["Alice","Bob"])
_l_(589198)
_c_(589201, _a_(589200, _n_(589199, "s", lambda: s), "addPerson"), "Alice",["John","Bob","Jeff"])
_l_(589202)
_c_(589205, _a_(589204, _n_(589203, "s", lambda: s), "addPerson"), "Bob",["John","Alice","Jeff","Ken"])
_l_(589206)
_c_(589209, _a_(589208, _n_(589207, "s", lambda: s), "addPerson"), "Jeff",["Alice","Bob","Barbra"])
_l_(589210)
_c_(589213, _a_(589212, _n_(589211, "s", lambda: s), "addPerson"), "Ken",["Bob","Barbra"])
_l_(589214)
_c_(589217, _a_(589216, _n_(589215, "s", lambda: s), "addPerson"), "Barbra",["Jeff","Ken"])
_l_(589218)
for person in _a_(589220, _n_(589219, "s", lambda: s), "nodeList"):
    _l_(589228)

    _c_(589226, _n_(589221, "print", lambda: print), "name: ",_a_(589223, _n_(589222, "person", lambda: person), "name"), "\n\t friends: ",_a_(589225, _n_(589224, "person", lambda: person), "friendList"))
    _l_(589227)