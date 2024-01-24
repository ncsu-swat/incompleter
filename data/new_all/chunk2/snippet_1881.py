# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44007989/attributeerror-generator-object-has-no-attribute-connect-pydle-asyncio
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_a_(427344, _n_(427343, "asyncio", lambda: asyncio), "coroutine")
class MyOwnBot(_a_(427346, _n_(427345, "pydle", lambda: pydle), "Client")):
     _l_(427352)

     async def on_connect(self):
          _l_(427351)

          await _c_(427349, _a_(427348, _n_(427347, "self", lambda: self), "join"), '#new')
          _l_(427350)

iclient = _c_(427354, _n_(427353, "MyOwnBot", lambda: MyOwnBot), 'testeee', realname='tester')
_l_(427355)
loop = _c_(427358, _a_(427357, _n_(427356, "asyncio", lambda: asyncio), "get_event_loop"))
_l_(427359)
_c_(427366, _a_(427361, _n_(427360, "asyncio", lambda: asyncio), "ensure_future"), _c_(427364, _a_(427363, _n_(427362, "iclient", lambda: iclient), "connect"), 'irc.test.net', 6697, tls=True,tls_verify=False), loop=_n_(427365, "loop", lambda: loop))
_l_(427367)