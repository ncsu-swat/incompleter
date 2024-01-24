# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72463918/attributeerror-module-nats-has-no-attribute-connect
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import asyncio
    _l_(432377)

except ImportError:
    pass
try:
    import nats
    _l_(432379)

except ImportError:
    pass

async def main():
    _l_(432404)

    # Connect to NATS!
    nc = await _c_(432382, _a_(432381, _n_(432380, "nats", lambda: nats), "connect"), servers=["nats://216.48.189.5:4222"])
    _l_(432383)

    # Receive messages on 'foo'
    sub = await _c_(432386, _a_(432385, _n_(432384, "nc", lambda: nc), "subscribe"), "foo")
    _l_(432387)

    # Publish a message to 'foo'
    await _c_(432390, _a_(432389, _n_(432388, "nc", lambda: nc), "publish"), "foo", b'Hello from Python!')
    _l_(432391)

    # Process a message
    msg = await _c_(432394, _a_(432393, _n_(432392, "sub", lambda: sub), "next_msg"))
    _l_(432395)
    _c_(432398, _n_(432396, "print", lambda: print), "Received:", _n_(432397, "msg", lambda: msg))
    _l_(432399)

    # Close NATS connection
    await _c_(432402, _a_(432401, _n_(432400, "nc", lambda: nc), "close"))
    _l_(432403)

if _n_(432405, "__name__", lambda: __name__) == '__main__':
    _l_(432412)

    _c_(432410, _a_(432407, _n_(432406, "asyncio", lambda: asyncio), "run"), _c_(432409, _n_(432408, "main", lambda: main)))
    _l_(432411)