# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55003113/attributeerror-nonetype-object-has-no-attribute-magnitude
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Force:
    _l_(660261)

    def __init__(self,magnitude,angle):
        _l_(660229)

        _n_(660223, "self", lambda: self).magnitude = _n_(660224, "magnitude", lambda: magnitude)
        _l_(660225)
        _n_(660226, "self", lambda: self).angle = _n_(660227, "angle", lambda: angle)
        _l_(660228)

    def get_horizontal(self):
        _l_(660239)

        aux = _a_(660231, _n_(660230, "self", lambda: self), "magnitude") * _c_(660237, _n_(660232, "cos", lambda: cos), _c_(660236, _n_(660233, "radians", lambda: radians), _a_(660235, _n_(660234, "self", lambda: self), "angle")))
        _l_(660238)
        return aux

    def get_vertical(self):
        _l_(660249)

        aux = _a_(660241, _n_(660240, "self", lambda: self), "magnitude") * _c_(660247, _n_(660242, "sin", lambda: sin), _c_(660246, _n_(660243, "radians", lambda: radians), _a_(660245, _n_(660244, "self", lambda: self), "angle")))
        _l_(660248)
        return aux

    def get_angle(self,use_degrees = True):
        _l_(660260)

        if _n_(660250, "use_degrees", lambda: use_degrees):
            _l_(660259)

            aux = _a_(660252, _n_(660251, "self", lambda: self), "angle")
            _l_(660253)
            return aux
        else:
            aux = _c_(660257, _n_(660254, "radians", lambda: radians), _a_(660256, _n_(660255, "self", lambda: self), "angle"))
            _l_(660258)
            return aux

def find_net_force(forces):
    _l_(660292)

    tot_hor = 0
    _l_(660262)
    tot_ver = 0
    _l_(660263)
    for i in _n_(660264, "forces", lambda: forces):
        _l_(660273)

        tot_hor += _c_(660267, _a_(660266, _n_(660265, "i", lambda: i), "get_horizontal"))
        _l_(660268)
        tot_ver += _c_(660271, _a_(660270, _n_(660269, "i", lambda: i), "get_vertical"))
        _l_(660272)

    magnitude = (_n_(660274, "tot_hor", lambda: tot_hor) ** 2 + _n_(660275, "tot_ver", lambda: tot_ver) ** 2) ** 0.5
    _l_(660276)
    magnitude = _c_(660279, _n_(660277, "round", lambda: round), _n_(660278, "magnitude", lambda: magnitude),1)
    _l_(660280)
    angle = _c_(660286, _n_(660281, "degrees", lambda: degrees), _c_(660285, _n_(660282, "atan2", lambda: atan2), _n_(660283, "tot_ver", lambda: (tot_ver)),_n_(660284, "tot_hor", lambda: (tot_hor))))
    _l_(660287)
    angle = _c_(660290, _n_(660288, "round", lambda: round), _n_(660289, "angle", lambda: angle),1)
    _l_(660291)

force_1 = _c_(660294, _n_(660293, "Force", lambda: Force), 50, 90)
_l_(660295)
force_2 = _c_(660297, _n_(660296, "Force", lambda: Force), 75, -90)
_l_(660298)
force_3 = _c_(660300, _n_(660299, "Force", lambda: Force), 100, 0)
_l_(660301)
forces = [_n_(660302, "force_1", lambda: force_1), _n_(660303, "force_2", lambda: force_2), _n_(660304, "force_3", lambda: force_3)]
_l_(660305)
net_force = _c_(660308, _n_(660306, "find_net_force", lambda: find_net_force), _n_(660307, "forces", lambda: forces))
_l_(660309)
_c_(660313, _n_(660310, "print", lambda: print), _a_(660312, _n_(660311, "net_force", lambda: net_force), "magnitude"))
_l_(660314)
_c_(660319, _n_(660315, "print", lambda: print), _c_(660318, _a_(660317, _n_(660316, "nIt_force", lambda: nIt_force), "get_angle")))
_l_(660320)