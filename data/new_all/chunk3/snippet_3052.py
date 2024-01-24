# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51384612/python-typeerror-object-takes-no-parameters-while-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tank import Tank
    _l_(556618)

except ImportError:
    pass

tanks = {"a":_c_(556620, _n_(556619, "Tank", lambda: Tank), "Alice"), "b":_c_(556622, _n_(556621, "Tank", lambda: Tank), "Bob"), "c":_c_(556624, _n_(556623, "Tank", lambda: Tank), "Crane") }
_l_(556625)
alive_tanks = _c_(556628, _n_(556626, "len", lambda: len), _n_(556627, "tanks", lambda: tanks))
_l_(556629)

while _n_(556630, "alive_tanks", lambda: alive_tanks) > 1:
    _l_(556707)

    _c_(556632, _n_(556631, "print", lambda: print))
    _l_(556633)
    for tank_name in _c_(556636, _n_(556634, "sorted", lambda: sorted), _n_(556635, "tanks", lambda: tanks)):
        _l_(556643)

        _c_(556641, _n_(556637, "print", lambda: print), _n_(556638, "tank_name", lambda: tank_name),_n_(556639, "tanks", lambda: tanks)[_n_(556640, "tank_name", lambda: tank_name)])
        _l_(556642)

    first = _c_(556647, _a_(556646, _c_(556645, _n_(556644, "raw_input", lambda: raw_input), "Who fires ?"), "lower"))
    _l_(556648)
    second = _c_(556652, _a_(556651, _c_(556650, _n_(556649, "raw_input", lambda: raw_input), "Who at ?"), "lower"))
    _l_(556653)

    try:
        _l_(556666)

        first_tank = _n_(556654, "tanks", lambda: tanks)[_n_(556655, "first", lambda: first)]
        _l_(556656)
        second_tank = _n_(556657, "tanks", lambda: tanks)[_n_(556658, "second", lambda: second)]
        _l_(556659)
    except _n_(556660, "KeyError", lambda: KeyError):
        _l_(556665)

        _c_(556662, _n_(556661, "print", lambda: print), "No such Tank ")
        _l_(556663)
        continue
        _l_(556664)

    if not _a_(556668, _n_(556667, "first_tank", lambda: first_tank), "alive") or not _a_(556670, _n_(556669, "second_tank", lambda: second_tank), "alive"):
        _l_(556675)

        _c_(556672, _n_(556671, "print", lambda: print), "One of those is dead!")
        _l_(556673)
        continue
        _l_(556674)

    _c_(556677, _n_(556676, "print", lambda: print))
    _l_(556678)
    _c_(556680, _n_(556679, "print", lambda: print), "*"*30)
    _l_(556681)

    _c_(556685, _a_(556683, _n_(556682, "first_tank", lambda: first_tank), "fire_at"), _n_(556684, "second_tank", lambda: second_tank))
    _l_(556686)
    if not _a_(556688, _n_(556687, "second_tank", lambda: second_tank), "alive"):
        _l_(556690)

        alive_tanks -= 1
        _l_(556689)

    _c_(556692, _n_(556691, "print", lambda: print), "*"*30)
    _l_(556693)

    for tank in _c_(556696, _a_(556695, _n_(556694, "tanks", lambda: tanks), "value")):
        _l_(556706)

        if _a_(556698, _n_(556697, "tank", lambda: tank), "alive"):
            _l_(556705)

            _c_(556702, _n_(556699, "print", lambda: print), _a_(556701, _n_(556700, "tank", lambda: tank), "name")," is the winner !")
            _l_(556703)
            break
            _l_(556704)