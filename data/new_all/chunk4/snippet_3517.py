# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73074930/nameerror-name-aiter-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
async def numbers(num):
    _l_(591513)

    for i in _c_(591505, _n_(591503, "range", lambda: range), _n_(591504, "num", lambda: num)):
        _l_(591512)

        yield _n_(591506, "i", lambda: i)
        _l_(591507)
        await _c_(591510, _a_(591509, _n_(591508, "asyncio", lambda: asyncio), "sleep"), 0.5)
        _l_(591511)

async def check_odd(num):
    _l_(591534)

    it = _c_(591518, _n_(591514, "aiter", lambda: aiter), _c_(591517, _n_(591515, "numbers", lambda: numbers), _n_(591516, "num", lambda: num)))
    _l_(591519)
    while True:
        _l_(591533)

        x = await _c_(591522, _n_(591520, "anext", lambda: anext), _n_(591521, "it", lambda: it), 'end')
        _l_(591523)
        if _n_(591524, "x", lambda: x) == 'end':
            _l_(591532)

            break
            _l_(591525)
        elif _n_(591526, "x", lambda: x) % 2 != 0:
            _l_(591531)

            _c_(591529, _n_(591527, "print", lambda: print), f"{_n_(591528, 'x', lambda: x)} is Odd!!")
            _l_(591530)

if _n_(591535, "__name__", lambda: __name__) == " __main__":
    _l_(591552)

    event_loop = _c_(591538, _a_(591537, _n_(591536, "asyncio", lambda: asyncio), "get_event_loop"))
    _l_(591539)
    try:
        _l_(591551)

        _c_(591544, _a_(591541, _n_(591540, "event_loop", lambda: event_loop), "run_until_complete"), _c_(591543, _n_(591542, "check_odd", lambda: check_odd), 10))
        _l_(591545)
    finally:
        _l_(591550)

        _c_(591548, _a_(591547, _n_(591546, "event_loop", lambda: event_loop), "close"))
        _l_(591549)

_c_(591555, _a_(591554, _n_(591553, "nest_asyncio", lambda: nest_asyncio), "apply"))
_l_(591556)
_c_(591561, _a_(591558, _n_(591557, "asyncio", lambda: asyncio), "run"), _c_(591560, _n_(591559, "check_odd", lambda: check_odd), 10))
_l_(591562)