# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69774299/typeerror-float-argument-must-be-a-string-or-a-number-not-datetime-timedelt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(449423)

except ImportError:
    pass
try:
    import numpy as np
    _l_(449425)

except ImportError:
    pass
try:
    import serial as ser
    _l_(449427)

except ImportError:
    pass
try:
    import time
    _l_(449429)

except ImportError:
    pass
try:
    import datetime
    _l_(449431)

except ImportError:
    pass
try:
    import mysql.connector
    _l_(449433)

except ImportError:
    pass


my_connect = _c_(449436, _a_(449435, _a_(449434, mysql, "connector"), "connect"), host="localhost", user="Kennedy", passwd="Kennerdol05071994", database="ecg_db", auth_plugin="mysql_native_password")
_l_(449437)
mycursor = _c_(449440, _a_(449439, _n_(449438, "my_connect", lambda: my_connect), "cursor"))
_l_(449441)

voltage_container = []
_l_(449442)
time_container = []
_l_(449443)


def fetch_voltage():
    _l_(449491)

    pat_id = 1
    _l_(449444)
    query = "SELECT voltage, time FROM ecg_data_tbl where patient_id = 1 "
    _l_(449445)
    _c_(449449, _a_(449447, _n_(449446, "mycursor", lambda: mycursor), "execute"), _n_(449448, "query", lambda: query))
    _l_(449450)
    result = _c_(449453, _a_(449452, _n_(449451, "mycursor", lambda: mycursor), "fetchall"))
    _l_(449454)
    voltage, time = _c_(449459, _n_(449455, "list", lambda: list), _c_(449458, _n_(449456, "zip", lambda: zip), *_n_(449457, "result", lambda: result)))
    _l_(449460)
    for volts in _n_(449461, "voltage", lambda: voltage):
        _l_(449472)

        _c_(449465, _a_(449463, _n_(449462, "voltage_container", lambda: voltage_container), "append"), _n_(449464, "volts", lambda: volts))
        _l_(449466)
        voltage_data = _c_(449470, _a_(449468, _n_(449467, "np", lambda: np), "array"), _n_(449469, "voltage_container", lambda: voltage_container))
        _l_(449471)
    for tim in _n_(449473, "time", lambda: time):
        _l_(449484)

        _c_(449477, _a_(449475, _n_(449474, "time_container", lambda: time_container), "append"), _n_(449476, "tim", lambda: tim))
        _l_(449478)
        time_data = _c_(449482, _a_(449480, _n_(449479, "np", lambda: np), "array"), _n_(449481, "time_container", lambda: time_container))
        _l_(449483)
    _c_(449489, _a_(449486, _n_(449485, "plt", lambda: plt), "plot"), _n_(449487, "time_data", lambda: time_data), _n_(449488, "voltage_data", lambda: voltage_data))
    _l_(449490)

_c_(449493, _n_(449492, "fetch_voltage", lambda: fetch_voltage))
_l_(449494)