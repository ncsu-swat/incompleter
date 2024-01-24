# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68793171/python-typeerror-asyncio-future-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import asyncio
    _l_(397888)

except ImportError:
    pass
try:
    import requests
    _l_(397890)

except ImportError:
    pass

jsonHashes = {}
_l_(397891)
responses = []
_l_(397892)

def pinToIPFS(number):
    _l_(397923)

    url = 'https://api.pinata.cloud/pinning/pinFileToIPFS'
    _l_(397893)
    par = {
        'pinata_api_key': 'blabla',
        'pinata_secret_api_key': 'blabla'
    }
    _l_(397894)
    file = {'file': _c_(397899, _n_(397895, "open", lambda: open), _c_(397898, _n_(397896, "str", lambda: str), _n_(397897, "number", lambda: number)) + '.jpg', 'rb')}
    _l_(397900)

    res = _c_(397906, _a_(397902, _n_(397901, "requests", lambda: requests), "post"), _n_(397903, "url", lambda: url), headers = _n_(397904, "par", lambda: par), files = _n_(397905, "file", lambda: file))
    _l_(397907)
    _n_(397908, "jsonHashes", lambda: jsonHashes)[_c_(397911, _a_(397910, _n_(397909, "res", lambda: res), "json"))['IpfsHash']] = _n_(397912, "number", lambda: number)
    _l_(397913)
    _c_(397921, _n_(397914, "print", lambda: print), _c_(397917, _a_(397916, _n_(397915, "res", lambda: res), "json"))['IpfsHash'] + ' = ' + _c_(397920, _n_(397918, "str", lambda: str), _n_(397919, "number", lambda: number)))
    _l_(397922)


async def main():
    _l_(397948)

    loop = _c_(397926, _a_(397925, _n_(397924, "asyncio", lambda: asyncio), "get_event_loop"))
    _l_(397927)
    futures = []
    _l_(397928)
    for i in _c_(397930, _n_(397929, "range", lambda: range), 2):
        _l_(397937)

        futures = _c_(397935, _a_(397932, _n_(397931, "loop", lambda: loop), "run_in_executor"), None, _n_(397933, "pinToIPFS", lambda: pinToIPFS), _n_(397934, "i", lambda: i))
        _l_(397936)
    for i in _c_(397939, _n_(397938, "range", lambda: range), 2):
        _l_(397947)

        _n_(397940, "jsonHashes", lambda: jsonHashes)[await _c_(397944, _a_(397943, _n_(397941, "futures", lambda: futures)[_n_(397942, "i", lambda: i)], "json"))['IpfsHash']] = _n_(397945, "i", lambda: i)
        _l_(397946)

loop = _c_(397951, _a_(397950, _n_(397949, "asyncio", lambda: asyncio), "get_event_loop"))
_l_(397952)
_c_(397957, _a_(397954, _n_(397953, "loop", lambda: loop), "run_until_complete"), _c_(397956, _n_(397955, "main", lambda: main)))
_l_(397958)


_c_(397961, _n_(397959, "print", lambda: print), _n_(397960, "jsonHashes", lambda: jsonHashes))
_l_(397962)