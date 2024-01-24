# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49844007/nameerror-name-temp-output-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def Read_Temp():
        _l_(336025)

        lines = _c_(335992, _n_(335991, "Temp_Raw", lambda: Temp_Raw))
        _l_(335993)
        while _c_(335996, _a_(335995, _n_(335994, "lines", lambda: lines)[0], "strip"))[-3:] != 'YES':
                _l_(336004)

                _c_(335999, _a_(335998, _n_(335997, "time", lambda: time), "sleep"), 0.2)
                _l_(336000)
                lines = _c_(336002, _n_(336001, "Temp_Raw", lambda: Temp_Raw))
                _l_(336003)
        temp_output = _c_(336007, _a_(336006, _n_(336005, "lines", lambda: lines)[1], "find"), 't=')
        _l_(336008)
        if _n_(336009, "temp_output", lambda: temp_output) != -1:
                _l_(336024)

                temp_sting = _c_(336012, _a_(336011, _n_(336010, "lines", lambda: lines)[1], "strip"))[_n_(336013, "temp_output", lambda: temp_output)+2:]
                _l_(336014)
                temp_c = _c_(336017, _n_(336015, "float", lambda: float), _n_(336016, "temp_string", lambda: temp_string)) / 1000.0
                _l_(336018)
                temp_f = _n_(336019, "temp_c", lambda: temp_c) * 9.0 / 5.0 + 32.0
                _l_(336020)
                aux = _n_(336021, "temp_c", lambda: temp_c), _n_(336022, "temp_f", lambda: temp_f)
                _l_(336023)
                return aux
while True:
        _l_(336035)

        _c_(336029, _n_(336026, "print", lambda: print), _c_(336028, _n_(336027, "Read_Temp", lambda: Read_Temp)))
        _l_(336030)
        _c_(336033, _a_(336032, _n_(336031, "time", lambda: time), "sleep"), 1)
        _l_(336034)