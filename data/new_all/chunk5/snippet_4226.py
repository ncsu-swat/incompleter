# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61314183/attributeerror-node-object-has-no-attribute-data
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(650290)

    def _init_ (self, left, right, data):
        _l_(650289)

        _n_(650281, "self", lambda: self).left = None
        _l_(650282)
        _n_(650283, "self", lambda: self).right = None
        _l_(650284)
        _n_(650285, "self", lambda: self).data = _c_(650287, _n_(650286, "list", lambda: list)) #Using a list for people with the same first name
        _l_(650288) #Using a list for people with the same first name
def addGuest (root, guest) :
    _l_(650346)

    if _n_(650291, "guest", lambda: guest) < _a_(650293, _n_(650292, "root", lambda: root), "data") [0] :
        _l_(650345)

        if _a_(650295, _n_(650294, "root", lambda: root), "left") == None:
            _l_(650313)

            _n_(650296, "root", lambda: root).left = _c_(650298, _n_(650297, "Node", lambda: Node))
            _l_(650299)
            _c_(650305, _a_(650303, _a_(650302, _a_(650301, _n_(650300, "root", lambda: root), "left"), "data"), "append"), _n_(650304, "guest", lambda: guest))
            _l_(650306)
        else:
            _c_(650311, _n_(650307, "addGuest", lambda: addGuest), _a_(650309, _n_(650308, "root", lambda: root), "left"), _n_(650310, "guest", lambda: guest))
            _l_(650312)
    else: #Defining right requirements
        if _n_(650314, "guest", lambda: guest) > _a_(650316, _n_(650315, "root", lambda: root), "data") [0] :
            _l_(650344)

            if _a_(650318, _n_(650317, "root", lambda: root), "right") == None:
                _l_(650336)

                _n_(650319, "root", lambda: root).right = _c_(650321, _n_(650320, "Nide", lambda: Nide))
                _l_(650322)
                _c_(650328, _a_(650326, _a_(650325, _a_(650324, _n_(650323, "root", lambda: root), "right"), "data"), "append"), _n_(650327, "guest", lambda: guest))
                _l_(650329)
            else:
                _c_(650334, _n_(650330, "addGuest", lambda: addGuest), _a_(650332, _n_(650331, "root", lambda: root), "right"), _n_(650333, "guest", lambda: guest))
                _l_(650335)
        else:
            _c_(650342, _a_(650340, _a_(650339, _a_(650338, _n_(650337, "root", lambda: root), "right"), "data"), "append"), _n_(650341, "guest", lambda: guest))
            _l_(650343)
def printGuest(root) :
    _l_(650365)

    if _n_(650347, "root", lambda: root) == None:
        _l_(650349)

        aux = ""
        _l_(650348)
        return aux
    _c_(650353, _n_(650350, "print", lambda: print), _a_(650352, _n_(650351, "root", lambda: root), "data"))
    _l_(650354)
    _c_(650358, _n_(650355, "printGuest", lambda: printGuest), _a_(650357, _n_(650356, "root", lambda: root), "left")) #printing left and right so both sides of the room are represented.
    _l_(650359) #printing left and right so both sides of the room are represented.
    _c_(650363, _n_(650360, "printGuest", lambda: printGuest), _a_(650362, _n_(650361, "root", lambda: root), "right"))
    _l_(650364)
root = _c_(650367, _n_(650366, "Node", lambda: Node))
_l_(650368)
_c_(650372, _a_(650371, _a_(650370, _n_(650369, "root", lambda: root), "data"), "append"), "M") #M is halfway through the alphabet. Depending on the group, this may need to change
_l_(650373) #M is halfway through the alphabet. Depending on the group, this may need to change
for i in _c_(650375, _n_(650374, "range", lambda: range), 0,8):
    _l_(650382)

    _c_(650380, _n_(650376, "addGuest", lambda: addGuest), _n_(650377, "root", lambda: root), _c_(650379, _n_(650378, "input", lambda: input), "Add Guest"))
    _l_(650381)
_c_(650384, _n_(650383, "print", lambda: print), "Left side:")
_l_(650385)
_c_(650389, _n_(650386, "printGuest", lambda: printGuest), _a_(650388, _n_(650387, "root", lambda: root), "left"))
_l_(650390)
_c_(650392, _n_(650391, "print", lambda: print), "Right Side:")
_l_(650393)
_c_(650397, _n_(650394, "printGuest", lambda: printGuest), _a_(650396, _n_(650395, "root", lambda: root), "right"))
_l_(650398)