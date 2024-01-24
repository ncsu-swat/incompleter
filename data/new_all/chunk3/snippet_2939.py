# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57548878/getting-a-typeerror-unhashable-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
user = _c_(530694, _a_(530693, _c_(530692, _n_(530691, "input", lambda: input), 'Name any1 who is near to you '), "split"), ',')
_l_(530695)
friends_open = _c_(530697, _n_(530696, "open", lambda: open), 'friends.txt', 'r')
_l_(530698)
friends_read = _c_(530701, _a_(530700, _n_(530699, "friends_open", lambda: friends_open), "readlines"))
_l_(530702)
_c_(530705, _a_(530704, _n_(530703, "friends_open", lambda: friends_open), "close"))
_l_(530706)

near_by  = []
_l_(530707)
_c_(530711, _a_(530709, _n_(530708, "near_by", lambda: near_by), "append"), _n_(530710, "user", lambda: user))
_l_(530712)

setting_near = _c_(530715, _n_(530713, "set", lambda: set), _n_(530714, "near_by", lambda: near_by))
_l_(530716)
setting_friends = _c_(530719, _n_(530717, "set", lambda: set), _n_(530718, "friends_read", lambda: friends_read))
_l_(530720)

intersect = _c_(530724, _a_(530722, _n_(530721, "setting_near", lambda: setting_near), "intersection"), _n_(530723, "setting_friends", lambda: setting_friends))
_l_(530725)

for n in _n_(530726, "intersect", lambda: intersect):
    _l_(530731)

    _c_(530729, _n_(530727, "print", lambda: print), f'your {_n_(530728, "intersect", lambda: intersect)} friend is here!! meet him ')
    _l_(530730)