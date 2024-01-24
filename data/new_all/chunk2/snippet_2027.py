# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68431205/typeerror-asyncio-runners-run-argument-after-must-be-an-iterable-not-corou
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
f = _c_(464169, _n_(464168, "open", lambda: open), "tokens.txt", "r")
_l_(464170)
lines = _c_(464173, _a_(464172, _n_(464171, "f", lambda: f), "readlines"))
_l_(464174)
for line in _n_(464175, "lines", lambda: lines):
    _l_(464183)

    _c_(464181, _n_(464176, "print", lambda: print), _c_(464179, _n_(464177, "type", lambda: type), _n_(464178, "line", lambda: line)), _n_(464180, "line", lambda: line))
    _l_(464182)


async def hosting(token):
    _l_(464197)


    bot = _c_(464186, _a_(464185, _n_(464184, "discord", lambda: discord), "Client"))
    _l_(464187)
    await _c_(464191, _a_(464189, _n_(464188, "bot", lambda: bot), "login"), _n_(464190, "token", lambda: token))
    _l_(464192)
    _c_(464195, _n_(464193, "print", lambda: print), f"Connected as: {_n_(464194, 'token', lambda: token)}")
    _l_(464196)

async def do_something_important():
    _l_(464201)

    await _c_(464199, _n_(464198, "print", lambda: print), 10)
    _l_(464200)


if _n_(464202, "__name__", lambda: __name__) == "__main__":
    _l_(464218)


    for token in _n_(464203, "lines", lambda: lines):
        _l_(464217)

        _thread = _c_(464211, _a_(464205, _n_(464204, "threading", lambda: threading), "Thread"), target=_a_(464207, _n_(464206, "asyncio", lambda: asyncio), "run"), args=_c_(464210, _n_(464208, "hosting", lambda: hosting), _n_(464209, "token", lambda: token)))
        _l_(464212)
        _c_(464215, _a_(464214, _n_(464213, "_thread", lambda: _thread), "start"))
        _l_(464216)