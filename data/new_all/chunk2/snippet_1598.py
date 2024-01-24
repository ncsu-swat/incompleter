# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72952618/error-message-through-data-readout-of-an-opc-ua-node-attributeerror-str-obj
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(453286, _a_(453285, _n_(453284, "client", lambda: client), "connect"))
_l_(453287)

forceAS = _c_(453290, _a_(453289, _n_(453288, "client", lambda: client), "get_node"), "ns=3;g=V:0.3.0.0.1")
_l_(453291)
meaForceAS = _c_(453294, _a_(453293, _n_(453292, "forceAS", lambda: forceAS), "get_data_value")) # here I get the error
_l_(453295) # here I get the error