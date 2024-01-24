# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56321383/typeerror-int-object-is-not-callable-1
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Line:
    _l_(541788)

    def __init__(self,coor1,coor2):
        _l_(541762)

        _n_(541756, "self", lambda: self).coor1= _n_(541757, "coor1", lambda: coor1)
        _l_(541758)
        _n_(541759, "self", lambda: self).coor2= _n_(541760, "coor2", lambda: coor2)
        _l_(541761)
    def distance(self):
        _l_(541775)

        _c_(541773, _n_(541763, "print", lambda: print), ((_a_(541765, _n_(541764, "self", lambda: self), "coor1")[0]-_a_(541767, _n_(541766, "self", lambda: self), "coor2")[0])**_c_(541772, 2, _a_(541769, _n_(541768, "self", lambda: self), "coor1")[1]-_a_(541771, _n_(541770, "self", lambda: self), "coor2")[1])**2)**0.5)
        _l_(541774)
    def slope (self):
        _l_(541787)

        _c_(541785, _n_(541776, "print", lambda: print), (_a_(541778, _n_(541777, "self", lambda: self), "coor2")[1]-_a_(541780, _n_(541779, "self", lambda: self), "coor1")[1])/(_a_(541782, _n_(541781, "self", lambda: self), "coor2")[0]-_a_(541784, _n_(541783, "self", lambda: self), "coor1")[0]))
        _l_(541786)
coordinate1 = (3,2)
_l_(541789)
coordinate2 = (8,10)
_l_(541790)

li = _c_(541794, _n_(541791, "Line", lambda: Line), _n_(541792, "coordinate1", lambda: coordinate1),_n_(541793, "coordinate2", lambda: coordinate2))
_l_(541795)
_c_(541798, _a_(541797, _n_(541796, "li", lambda: li), "distance"))
_l_(541799)