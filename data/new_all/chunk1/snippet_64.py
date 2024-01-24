# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53247533/attributeerror-module-asyncio-has-no-attribute-create-task
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
async def main():
    _l_(383901)

    task1 = _c_(383877, _a_(383874, _n_(383873, "asyncio", lambda: asyncio), "ensure_future"), _c_(383876, _n_(383875, "async_say", lambda: async_say), 4, 'hello'))
    _l_(383878)
    task2 = _c_(383883, _a_(383880, _n_(383879, "asyncio", lambda: asyncio), "ensure_future"), _c_(383882, _n_(383881, "async_say", lambda: async_say), 6, 'world'))
    _l_(383884)

    _c_(383889, _n_(383885, "print", lambda: print), f"started at {_c_(383888, _a_(383887, _n_(383886, 'time', lambda: time), 'strftime'), '%X')}")
    _l_(383890)
    await _n_(383891, "task1", lambda: task1)
    _l_(383892)
    await _n_(383893, "task2", lambda: task2)
    _l_(383894)
    _c_(383899, _n_(383895, "print", lambda: print), f"finished at {_c_(383898, _a_(383897, _n_(383896, 'time', lambda: time), 'strftime'), '%X')}")
    _l_(383900)

loop = _c_(383904, _a_(383903, _n_(383902, "asyncio", lambda: asyncio), "get_event_loop"))
_l_(383905)
_c_(383910, _a_(383907, _n_(383906, "loop", lambda: loop), "run_until_complete"), _c_(383909, _n_(383908, "main", lambda: main)))
_l_(383911)