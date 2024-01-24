# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71310475/typeerror-async-generator-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import asyncio
    _l_(471124)

except ImportError:
    pass

async def gen_random_numbers():
    _l_(471136)

    for i in _c_(471126, _n_(471125, "range", lambda: range), 1, 3):
        _l_(471135)

        await _c_(471129, _a_(471128, _n_(471127, "asyncio", lambda: asyncio), "sleep"), 2)
        _l_(471130)
        yield [_n_(471131, "i", lambda: i) for i in _c_(471133, _n_(471132, "range", lambda: range), 1, 11)]
        _l_(471134)


async def random_processor():
    _l_(471147)

    async for i, numbers in _c_(471140, _n_(471137, "enumerate", lambda: enumerate), _c_(471139, _n_(471138, "gen_random_numbers", lambda: gen_random_numbers))):
        _l_(471146)

        _c_(471144, _n_(471141, "print", lambda: print), f"working with the batch {_n_(471142, 'i', lambda: i)}  and processing {_n_(471143, 'numbers', lambda: numbers)}")
        _l_(471145)


_c_(471152, _a_(471149, _n_(471148, "asyncio", lambda: asyncio), "run"), _c_(471151, _n_(471150, "random_processor", lambda: random_processor)))
_l_(471153)