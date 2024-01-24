# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67135036/python-json-format-error-typeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
message = _c_(638429, _a_(638428, _n_(638427, "socket", lambda: socket), "recv"))
_l_(638430)
 
_c_(638433, _n_(638431, "print", lambda: print), "DBG#80:orginal message:", _n_(638432, "message", lambda: message))
_l_(638434)
message_string = _c_(638437, _a_(638436, _n_(638435, "message", lambda: message), "decode"), "utf-8")  # VVI important (it removes b" \" etc ")
_l_(638438)  # VVI important (it removes b" \" etc ")
_c_(638441, _n_(638439, "print", lambda: print), "DBG#81:message.decode('utf-8'):", _n_(638440, "message_string", lambda: message_string))
_l_(638442)
  
correlation_id_rcvd = _c_(638446, _a_(638444, _n_(638443, "json", lambda: json), "dumps"), _n_(638445, "message_string", lambda: message_string),separators=(',', ':'))
_l_(638447)
_c_(638450, _n_(638448, "print", lambda: print), "DBG#82:parsed json full=", _n_(638449, "correlation_id_rcvd", lambda: correlation_id_rcvd))
_l_(638451)
_c_(638454, _n_(638452, "print", lambda: print), "DBG#83:message_correlation_id=" ,_n_(638453, "correlation_id_rcvd", lambda: correlation_id_rcvd)["message_correlation_id"])
_l_(638455)