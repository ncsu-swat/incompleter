# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52969193/netmiko-attributeerror-nonetype-object-has-no-attribute-recv-ready
    #!/home/ipautowppprod/.pyenv/shims/python

# cisco_auto_back_up_v4

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from netmiko import ConnectHandler, redispatch
    _l_(467927)

except ImportError:
    pass
try:
    from netmiko import NetMikoAuthenticationException, NetMikoTimeoutException
    _l_(467929)

except ImportError:
    pass
try:
    import datetime
    _l_(467931)

except ImportError:
    pass
try:
    import sys
    _l_(467933)

except ImportError:
    pass
try:
    import time
    _l_(467935)

except ImportError:
    pass

now = _c_(467939, _a_(467938, _a_(467937, _n_(467936, "datetime", lambda: datetime), "datetime"), "now"))
_l_(467940)
time_now = _c_(467943, _a_(467942, _n_(467941, "now", lambda: now), "strftime"), "%Y-%m-%d_%H:%M:%S")
_l_(467944)

target_info = _c_(467948, _a_(467947, _a_(467946, _n_(467945, "sys", lambda: sys), "argv")[1], "split"), ',')
_l_(467949)
ipmon_info = _c_(467953, _a_(467952, _a_(467951, _n_(467950, "sys", lambda: sys), "argv")[2], "split"), ',')
_l_(467954)

target_info = [_c_(467957, _a_(467956, _n_(467955, "x", lambda: x), "strip")) for x in _n_(467958, "target_info", lambda: target_info)]
_l_(467959)
ipmon_info = [_c_(467962, _a_(467961, _n_(467960, "x", lambda: x), "strip")) for x in _n_(467963, "ipmon_info", lambda: ipmon_info)]
_l_(467964)

target_device = {
    'device_type': 'cisco_ios',
    'ip': _n_(467965, "target_info", lambda: target_info)[0],
    "host": _n_(467966, "target_info", lambda: target_info)[1],
    'username': _n_(467967, "target_info", lambda: target_info)[2],
    'password': _n_(467968, "target_info", lambda: target_info)[3],
    'secret': _n_(467969, "target_info", lambda: target_info)[4]
}
_l_(467970)

ipmon = {
    'device_type': 'linux',
    'ip': _n_(467971, "ipmon_info", lambda: ipmon_info)[0],
    'username': _n_(467972, "ipmon_info", lambda: ipmon_info)[1],
    'password': _n_(467973, "ipmon_info", lambda: ipmon_info)[2]
}
_l_(467974)

try:
    _l_(468112)

    _c_(467976, _n_(467975, "print", lambda: print), "Attempting to Connect...")
    _l_(467977)
    # Connect to ipmon
    net_connect = _c_(467980, _n_(467978, "ConnectHandler", lambda: ConnectHandler), **_n_(467979, "ipmon", lambda: ipmon))
    _l_(467981)
    _c_(467986, _n_(467982, "print", lambda: print), _c_(467985, _a_(467984, _n_(467983, "net_connect", lambda: net_connect), "find_prompt")))
    _l_(467987)

    _c_(467994, _a_(467989, _n_(467988, "net_connect", lambda: net_connect), "write_channel"), _c_(467993, _a_(467990, "ssh {}@{}\n", "format"), _n_(467991, "target_device", lambda: target_device)["username"],
                                                   _n_(467992, "target_device", lambda: target_device)["ip"]))
    _l_(467995)
    _c_(467998, _a_(467997, _n_(467996, "time", lambda: time), "sleep"), 1)
    _l_(467999)
    output = _c_(468002, _a_(468001, _n_(468000, "net_connect", lambda: net_connect), "read_channel"))
    _l_(468003)

    _c_(468006, _n_(468004, "print", lambda: print), _n_(468005, "output", lambda: output))
    _l_(468007)

    if "RSA" in _n_(468008, "output", lambda: output):
        _l_(468025)

        _c_(468011, _a_(468010, _n_(468009, "net_connect", lambda: net_connect), "write_channel"), "yes\n")
        _l_(468012)
        _c_(468015, _a_(468014, _n_(468013, "time", lambda: time), "sleep"), 1)
        _l_(468016)
        output = _c_(468019, _a_(468018, _n_(468017, "net_connect", lambda: net_connect), "read_channel"))
        _l_(468020)
        _c_(468023, _n_(468021, "print", lambda: print), _n_(468022, "output", lambda: output))
        _l_(468024)
    if "user" in _n_(468026, "output", lambda: output):
        _l_(468040)

        _c_(468030, _a_(468028, _n_(468027, "net_connect", lambda: net_connect), "write_channel"), _n_(468029, "target_device", lambda: target_device)["username"] + "\n")
        _l_(468031)
        _c_(468034, _a_(468033, _n_(468032, "time", lambda: time), "sleep"), 1)
        _l_(468035)
        output = _c_(468038, _a_(468037, _n_(468036, "net_connect", lambda: net_connect), "read_channel"))
        _l_(468039)
    if "password" in _n_(468041, "output", lambda: output):
        _l_(468055)

        _c_(468045, _a_(468043, _n_(468042, "net_connect", lambda: net_connect), "write_channel"), _n_(468044, "target_device", lambda: target_device)["password"] + "\n")
        _l_(468046)
        _c_(468049, _a_(468048, _n_(468047, "time", lambda: time), "sleep"), 5)
        _l_(468050)
        output = _c_(468053, _a_(468052, _n_(468051, "net_connect", lambda: net_connect), "read_channel"))
        _l_(468054)
    if "password" in _n_(468056, "output", lambda: output):
        _l_(468077)

        _c_(468058, _n_(468057, "print", lambda: print), "Wrong credentials.")
        _l_(468059)
        _c_(468062, _a_(468061, _n_(468060, "sys", lambda: sys), "exit"), 1)
        _l_(468063)
    elif "refused" in _n_(468064, "output", lambda: output):
        _l_(468076)

        _c_(468067, _a_(468066, _n_(468065, "net_connect", lambda: net_connect), "disconnect"))
        _l_(468068)
        _c_(468070, _n_(468069, "print", lambda: print), "Connection Refused")
        _l_(468071)
    else:
        _c_(468074, _a_(468073, _n_(468072, "net_connect", lambda: net_connect), "disconnect"))
        _l_(468075)

    # Connect to device
    _c_(468081, _n_(468078, "redispatch", lambda: redispatch), _n_(468079, "net_connect", lambda: net_connect), device_type=_n_(468080, "target_device", lambda: target_device)['device_type'])
    _l_(468082)
    CMD = _c_(468085, _a_(468084, _n_(468083, "net_connect", lambda: net_connect), "send_command_timing"), 'show running-config')
    _l_(468086)

    # Converts CMD output to a string
    cmd_output = _c_(468090, _n_(468087, "str", lambda: str), _a_(468089, _n_(468088, "CMD", lambda: CMD), "stdout"))
    _l_(468091)

except _n_(468092, "NetMikoAuthenticationException", lambda: NetMikoAuthenticationException) as autom_err:
    _l_(468101)

    _c_(468095, _n_(468093, "print", lambda: print), _n_(468094, "autom_err", lambda: autom_err))
    _l_(468096)
    _c_(468099, _a_(468098, _n_(468097, "sys", lambda: sys), "exit"), 1)
    _l_(468100)

except _n_(468102, "NetMikoTimeoutException", lambda: NetMikoTimeoutException) as timeout_err:
    _l_(468111)

    _c_(468105, _n_(468103, "print", lambda: print), _n_(468104, "timeout_err", lambda: timeout_err))
    _l_(468106)
    _c_(468109, _a_(468108, _n_(468107, "sys", lambda: sys), "exit"), 1)
    _l_(468110)