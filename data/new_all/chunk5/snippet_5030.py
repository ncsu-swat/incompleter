# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52245947/typeerror-list-iterator-object-is-not-async-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests as req
    _l_(658525)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup as bs
    _l_(658527)

except ImportError:
    pass
try:
    import os
    _l_(658529)

except ImportError:
    pass
try:
    import asyncio
    _l_(658531)

except ImportError:
    pass
try:
    from aiostream import stream, pipe
    _l_(658533)

except ImportError:
    pass

myList = []
_l_(658534)

def get_myList():
    _l_(658535)

    """
    Append values to myList in the format [(,), (,), (,), ...]
    """

async def download(link, title):
    _l_(658545)


    # Download a page
    try:
        _l_(658544)

        page = await _c_(658539, _a_(658537, _n_(658536, "req", lambda: req), "get"), _n_(658538, "link", lambda: link))
        _l_(658540)
        # Process with BeautifulSoup
        pass
        _l_(658541)
    except:
        _l_(658543)

        pass
        _l_(658542)

async def main():
    _l_(658559)

    _c_(658547, _n_(658546, "get_myList", lambda: get_myList))
    _l_(658548)

    min_iterList = _c_(658551, _n_(658549, "iter", lambda: iter), _n_(658550, "myList", lambda: myList)[:])
    _l_(658552)

    _c_(658557, _a_(658554, _n_(658553, "stream", lambda: stream), "starmap"), _n_(658555, "min_iterList", lambda: min_iterList), _n_(658556, "download", lambda: download), ordered=True, task_limit=10)
    _l_(658558)

if _n_(658560, "__name__", lambda: __name__)=="__main__":
    _l_(658578)

    _c_(658562, _n_(658561, "freeze_support", lambda: freeze_support))
    _l_(658563)
    loop = _c_(658566, _a_(658565, _n_(658564, "asyncio", lambda: asyncio), "get_event_loop"))
    _l_(658567)
    _c_(658572, _a_(658569, _n_(658568, "loop", lambda: loop), "run_until_complete"), _c_(658571, _n_(658570, "main", lambda: main)))
    _l_(658573)
    _c_(658576, _a_(658575, _n_(658574, "loop", lambda: loop), "close"))
    _l_(658577)