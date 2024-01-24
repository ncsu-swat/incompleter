# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57756344/attributeerror-modbusioexception-object-has-no-attribute-registers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pymodbus.client.sync import ModbusSerialClient as ModbusClient
    _l_(465542)

except ImportError:
    pass

# mbClient = ModbusClient(method = "rtu", port="COM4", stopbits = 1, bytesize = 8, parity = 'N', baudrate = 9600)
mbClient = _c_(465544, _n_(465543, "ModbusClient", lambda: ModbusClient), method = "rtu", port="COM4")
_l_(465545)
_c_(465548, _a_(465547, _n_(465546, "mbClient", lambda: mbClient), "connect"))
_l_(465549)

totalEnergy = _c_(465552, _a_(465551, _n_(465550, "mbClient", lambda: mbClient), "read_holding_registers"), 0x0000, 2, unit=1)
_l_(465553)
_c_(465557, _n_(465554, "print", lambda: print), _a_(465556, _n_(465555, "totalEnergy", lambda: totalEnergy), "registers"))
_l_(465558)
_c_(465561, _a_(465560, _n_(465559, "mbClient", lambda: mbClient), "close"))
_l_(465562)