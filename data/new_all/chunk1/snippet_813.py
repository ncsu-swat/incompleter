# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33473140/attributeerror-module-object-has-no-attribute-ensure-future
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import asyncio
   _l_(403380)

except ImportError:
   pass
try:
   import aiohttp
   _l_(403382)

except ImportError:
   pass
try:
   import json
   _l_(403384)

except ImportError:
   pass
try:
   import logging
   _l_(403386)

except ImportError:
   pass

# async def fetch_content(url, symbols):
# yield from  aiohttp.post(url, symbols=symbols)

@_a_(403388, _n_(403387, "asyncio", lambda: asyncio), "coroutine")
def fetch_page(writer, url, data):
   _l_(403409)

   response = yield from _c_(403393, _a_(403390, _n_(403389, "aiohttp", lambda: aiohttp), "post"), _n_(403391, "url", lambda: url), data=_n_(403392, "data", lambda: data))
   _l_(403394)
   resp = yield from _c_(403397, _a_(403396, _n_(403395, "response", lambda: response), "read_and_close"))
   _l_(403398)
   _c_(403401, _n_(403399, "print", lambda: print), _n_(403400, "resp", lambda: resp))
   _l_(403402)
   _c_(403406, _a_(403404, _n_(403403, "writer", lambda: writer), "write"), _n_(403405, "resp", lambda: resp)) 
   _l_(403407) 
   aux = ""           
   _l_(403408)           
   return aux           


@_a_(403411, _n_(403410, "asyncio", lambda: asyncio), "coroutine")
def process_payload(writer, data, scale):
   _l_(403501)

   tasks = []
   _l_(403412)
   data = _c_(403415, _a_(403414, _n_(403413, "data", lambda: data), "split"), '\r\n\r\n')[1]
   _l_(403416)
   data = _c_(403419, _a_(403418, _n_(403417, "data", lambda: data), "split"), '\n')
   _l_(403420)
   data = [_c_(403423, _a_(403422, _n_(403421, "x", lambda: x), "split"), ':') for x in _n_(403424, "data", lambda: data)]
   _l_(403425)
   _c_(403428, _n_(403426, "print", lambda: print), _n_(403427, "data", lambda: data))
   _l_(403429)
   data = {_n_(403430, "x", lambda: x)[0]: _n_(403431, "x", lambda: x)[1] for x in _n_(403432, "data", lambda: data)}
   _l_(403433)
   _c_(403436, _n_(403434, "print", lambda: print), _n_(403435, "data", lambda: data))                 
   _l_(403437)                 
   # data = data[0].split(':')[1]
   data = _n_(403438, "data", lambda: data)['symbols']
   _l_(403439)
   _c_(403442, _n_(403440, "print", lambda: print), _n_(403441, "data", lambda: data))
   _l_(403443)
   data = _c_(403446, _a_(403445, _n_(403444, "data", lambda: data), "split"), ',')
   _l_(403447)
   data_len = _c_(403450, _n_(403448, "len", lambda: len), _n_(403449, "data", lambda: data))
   _l_(403451)
   data_first = 0
   _l_(403452)
   data_last = _n_(403453, "scale", lambda: scale)
   _l_(403454)
   url = 'http://xxxxxx.xxxxxx.xxx/xxxx/xxxx'
   _l_(403455)
   while _n_(403456, "data_last", lambda: data_last) < _n_(403457, "data_len", lambda: data_len):
      _l_(403478)

      _c_(403472, _a_(403459, _n_(403458, "tasks", lambda: tasks), "append"), _c_(403471, _a_(403461, _n_(403460, "asyncio", lambda: asyncio), "ensure_future"), _c_(403470, _n_(403462, "fetch_page", lambda: fetch_page), _n_(403463, "writer", lambda: writer), _n_(403464, "url", lambda: url),{'symbols': _c_(403469, _a_(403465, ",", "join"), _n_(403466, "data", lambda: data)[_n_(403467, "data_first", lambda: data_first):_n_(403468, "data_last", lambda: data_last)])})))
      _l_(403473)
      data_first += _n_(403474, "scale", lambda: scale)
      _l_(403475)
      data_last += _n_(403476, "scale", lambda: scale) 
      _l_(403477) 

   _c_(403493, _a_(403480, _n_(403479, "tasks", lambda: tasks), "append"), _c_(403492, _a_(403482, _n_(403481, "asyncio", lambda: asyncio), "ensure_future"), _c_(403491, _n_(403483, "fetch_page", lambda: fetch_page), _n_(403484, "writer", lambda: writer), _n_(403485, "url", lambda: url),{'symbols': _c_(403490, _a_(403486, ",", "join"), _n_(403487, "data", lambda: data)[_n_(403488, "data_first", lambda: data_first):_n_(403489, "data_last", lambda: data_last)])})))
   _l_(403494)
   _c_(403498, _a_(403496, _n_(403495, "loop", lambda: loop), "run_until_complete"), _n_(403497, "tasks", lambda: tasks))    
   _l_(403499)    
   aux = "" 
   _l_(403500) 
   return aux 

@_a_(403503, _n_(403502, "asyncio", lambda: asyncio), "coroutine")
def process_url(url):
   _l_(403505)

   pass
   _l_(403504)

@_a_(403507, _n_(403506, "asyncio", lambda: asyncio), "coroutine")
def echo_server():
   _l_(403513)

   yield from _c_(403511, _a_(403509, _n_(403508, "asyncio", lambda: asyncio), "start_server"), _n_(403510, "handle_connection", lambda: handle_connection), 'xxxxxx.xxxx.xxx', 3000)
   _l_(403512)

@_a_(403515, _n_(403514, "asyncio", lambda: asyncio), "coroutine")
def handle_connection(reader, writer):
   _l_(403543)

   data = yield from _c_(403518, _a_(403517, _n_(403516, "reader", lambda: reader), "read"), 8192)
   _l_(403519)

   if _n_(403520, "data", lambda: data):
      _l_(403534)

      message =  _c_(403523, _a_(403522, _n_(403521, "data", lambda: data), "decode"), 'utf-8')
      _l_(403524)
      _c_(403527, _n_(403525, "print", lambda: print), _n_(403526, "message", lambda: message))
      _l_(403528)
      yield from _c_(403532, _n_(403529, "process_payload", lambda: process_payload), _n_(403530, "writer", lambda: writer), _n_(403531, "message", lambda: message), 400)
      _l_(403533)

   _c_(403537, _a_(403536, _n_(403535, "writer", lambda: writer), "write_eof"))   
   _l_(403538)   
   _c_(403541, _a_(403540, _n_(403539, "writer", lambda: writer), "close"))
   _l_(403542)


#url = 'http://XXXXXXX.xxxxx.xxx/xxxx/xxxxxx/xxx'
data = {'symbols': 'GD-US,14174T10,04523Y10,88739910,03209R10,46071F10,77543110,92847N10'}
_l_(403544)

loop = _c_(403547, _a_(403546, _n_(403545, "asyncio", lambda: asyncio), "get_event_loop"))
_l_(403548)
_c_(403553, _a_(403550, _n_(403549, "loop", lambda: loop), "run_until_complete"), _c_(403552, _n_(403551, "echo_server", lambda: echo_server)))
_l_(403554)
try:
   _l_(403564)

   _c_(403557, _a_(403556, _n_(403555, "loop", lambda: loop), "run_forever"))
   _l_(403558)
finally:
   _l_(403563)

   _c_(403561, _a_(403560, _n_(403559, "loop", lambda: loop), "close"))
   _l_(403562)