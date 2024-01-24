# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53247533/attributeerror-module-asyncio-has-no-attribute-create-task
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import asyncio
    _l_(411147)

except ImportError:
    pass
try:
    import time
    _l_(411149)

except ImportError:
    pass

async def async_say(delay, msg):
    _l_(411159)

    await _c_(411153, _a_(411151, _n_(411150, "asyncio", lambda: asyncio), "sleep"), _n_(411152, "delay", lambda: delay))
    _l_(411154)
    _c_(411157, _n_(411155, "print", lambda: print), _n_(411156, "msg", lambda: msg))
    _l_(411158)

async def main():
    _l_(411188)

    task1 = _c_(411164, _a_(411161, _n_(411160, "asyncio", lambda: asyncio), "create_task"), _c_(411163, _n_(411162, "async_say", lambda: async_say), 4, 'hello'))
    _l_(411165)
    task2 = _c_(411170, _a_(411167, _n_(411166, "asyncio", lambda: asyncio), "create_task"), _c_(411169, _n_(411168, "async_say", lambda: async_say), 6, 'world'))
    _l_(411171)

    _c_(411176, _n_(411172, "print", lambda: print), f"started at {_c_(411175, _a_(411174, _n_(411173, 'time', lambda: time), 'strftime'), '%X')}")
    _l_(411177)
    await _n_(411178, "task1", lambda: task1)
    _l_(411179)
    await _n_(411180, "task2", lambda: task2)
    _l_(411181)
    _c_(411186, _n_(411182, "print", lambda: print), f"finished at {_c_(411185, _a_(411184, _n_(411183, 'time', lambda: time), 'strftime'), '%X')}")
    _l_(411187)

loop = _c_(411191, _a_(411190, _n_(411189, "asyncio", lambda: asyncio), "get_event_loop"))
_l_(411192)
_c_(411197, _a_(411194, _n_(411193, "loop", lambda: loop), "run_until_complete"), _c_(411196, _n_(411195, "main", lambda: main)))
_l_(411198)