# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74713051/attributeerror-modbusioexception-object-has-no-attribute-bits
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pymodbus.client import ModbusTcpClient
    _l_(638893)

except ImportError:
    pass

PLC_IP = '192.168.0.200'
_l_(638894)
PLC_PORT = 502
_l_(638895)
client = _c_(638899, _n_(638896, "ModbusTcpClient", lambda: ModbusTcpClient), _n_(638897, "PLC_IP", lambda: PLC_IP), _n_(638898, "PLC_PORT", lambda: PLC_PORT))
_l_(638900)
status = _c_(638903, _a_(638902, _n_(638901, "client", lambda: client), "connect"))
_l_(638904)
_c_(638907, _n_(638905, "print", lambda: print), _n_(638906, "status", lambda: status))
_l_(638908)
result = _c_(638911, _a_(638910, _n_(638909, "client", lambda: client), "read_coils"), 1,5)
_l_(638912)
if _a_(638914, _n_(638913, "result", lambda: result), "bits")[0] == True:
    _l_(638918)

    _c_(638916, _n_(638915, "print", lambda: print), "Hello world")
    _l_(638917)
_c_(638921, _a_(638920, _n_(638919, "client", lambda: client), "close"))
_l_(638922)