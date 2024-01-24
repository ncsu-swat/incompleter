# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58025208/attributeerror-float-object-has-no-attribute-append
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
y = 1/2
_l_(353395)
b = 1/4
_l_(353396)


t = []
_l_(353397)
p = [0,25,43.3013,50,43.3013,25,0,0,0,0,0]
_l_(353398)

u = []
_l_(353399)
v = []
_l_(353400)
p = []
_l_(353401)
a = []
_l_(353402)

x = 0.0
_l_(353403)
for i in _c_(353405, _n_(353404, "range", lambda: range), 11):
    _l_(353415)

    a = 0.0 + _n_(353406, "x", lambda: x)
    _l_(353407)
    _c_(353411, _a_(353409, _n_(353408, "t", lambda: t), "append"), _n_(353410, "a", lambda: a))
    _l_(353412)
    x = _n_(353413, "x", lambda: x) + 0.1
    _l_(353414)

m = 0.45594
_l_(353416)
k = 18
_l_(353417)
c = 0.2865
_l_(353418)

_c_(353421, _a_(353420, _n_(353419, "u", lambda: u), "append"), 0)
_l_(353422)
_c_(353425, _a_(353424, _n_(353423, "v", lambda: v), "append"), 0)
_l_(353426)
_c_(353429, _a_(353428, _n_(353427, "p", lambda: p), "append"), 0)
_l_(353430)

_c_(353439, _a_(353432, _n_(353431, "a", lambda: a), "append"), (_n_(353433, "p", lambda: p)[0]-_n_(353434, "c", lambda: c)*_n_(353435, "v", lambda: v)[0]-_n_(353436, "k", lambda: k)*_n_(353437, "u", lambda: u)[0])/_n_(353438, "m", lambda: m))
_l_(353440)
dt = 0.1
_l_(353441)

_c_(353452, _a_(353443, _n_(353442, "a", lambda: a), "append"), _n_(353444, "m", lambda: m)/(_n_(353445, "b", lambda: b)*_n_(353446, "dt", lambda: dt)*_n_(353447, "dt", lambda: dt))+_n_(353448, "y", lambda: y)*_n_(353449, "c", lambda: c)/(_n_(353450, "b", lambda: b)*_n_(353451, "dt", lambda: dt)))
_l_(353453)
_c_(353462, _a_(353455, _n_(353454, "a", lambda: a), "append"), _n_(353456, "m", lambda: m)/(_n_(353457, "b", lambda: b)*_n_(353458, "dt", lambda: dt))+(_n_(353459, "y", lambda: y)/_n_(353460, "b", lambda: b)-1)*_n_(353461, "c", lambda: c))
_l_(353463)
_c_(353472, _a_(353465, _n_(353464, "a", lambda: a), "append"), ((1/(2*_n_(353466, "b", lambda: b)))-1)*_n_(353467, "m", lambda: m) + _n_(353468, "dt", lambda: dt)*((_n_(353469, "y", lambda: y)/(2*_n_(353470, "b", lambda: b)))-1)*_n_(353471, "c", lambda: c))
_l_(353473)
kn = _n_(353474, "k", lambda: k) + _n_(353475, "a", lambda: a)[1]
_l_(353476)