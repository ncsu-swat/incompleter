# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55131555/typeerror-not-supported-between-instances-of-member-and-member
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
d = _c_(674649, _n_(674647, "defaultdict", lambda: defaultdict), _n_(674648, "int", lambda: int))
_l_(674650)
@_a_(674652, _n_(674651, "bot", lambda: bot), "event")
async def on_message(message):
    _l_(674663)

    _n_(674653, "d", lambda: d)[_a_(674655, _n_(674654, "message", lambda: message), "author")] += 1
    _l_(674656)
    pass
    _l_(674657)
    await _c_(674661, _a_(674659, _n_(674658, "bot", lambda: bot), "process_commands"), _n_(674660, "message", lambda: message))
    _l_(674662)

@_c_(674666, _a_(674665, _n_(674664, "bot", lambda: bot), "command"))
async def top_messager(ctx):
    _l_(674684)

    sorted_d = _c_(674673, _n_(674667, "sorted", lambda: sorted), ((_n_(674668, "value", lambda: value), _n_(674669, "user", lambda: user)) for user, value in _c_(674672, _a_(674671, _n_(674670, "d", lambda: d), "items"))))
    _l_(674674)
    await _c_(674682, _a_(674676, _n_(674675, "ctx", lambda: ctx), "send"), _c_(674681, _a_(674677, '\n', "join"), (f"{_n_(674678, 'user', lambda: user)}: {_n_(674679, 'value', lambda: value)}" for value, user in _n_(674680, "sorted_d", lambda: sorted_d))))
    _l_(674683)