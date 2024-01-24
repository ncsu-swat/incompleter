# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53247533/attributeerror-module-asyncio-has-no-attribute-create-task
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
async def main():
    _l_(378001)

    loop = _c_(377971, _a_(377970, _n_(377969, "asyncio", lambda: asyncio), "get_event_loop"))
    _l_(377972)
    task1 = _c_(377977, _a_(377974, _n_(377973, "loop", lambda: loop), "create_task"), _c_(377976, _n_(377975, "async_say", lambda: async_say), 4, 'hello'))
    _l_(377978)
    task2 = _c_(377983, _a_(377980, _n_(377979, "loop", lambda: loop), "create_task"), _c_(377982, _n_(377981, "async_say", lambda: async_say), 6, 'world'))
    _l_(377984)

    _c_(377989, _n_(377985, "print", lambda: print), f"started at {_c_(377988, _a_(377987, _n_(377986, 'time', lambda: time), 'strftime'), '%X')}")
    _l_(377990)
    await _n_(377991, "task1", lambda: task1)
    _l_(377992)
    await _n_(377993, "task2", lambda: task2)
    _l_(377994)
    _c_(377999, _n_(377995, "print", lambda: print), f"finished at {_c_(377998, _a_(377997, _n_(377996, 'time', lambda: time), 'strftime'), '%X')}")
    _l_(378000)

loop = _c_(378004, _a_(378003, _n_(378002, "asyncio", lambda: asyncio), "get_event_loop"))
_l_(378005)
_c_(378010, _a_(378007, _n_(378006, "loop", lambda: loop), "run_until_complete"), _c_(378009, _n_(378008, "main", lambda: main)))
_l_(378011)