# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68237545/python-json-object-typeerror
#!/usr/bin/python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import platform
    _l_(546967)

except ImportError:
    pass
try:
    import subprocess
    _l_(546969)

except ImportError:
    pass
try:
    import json
    _l_(546971)

except ImportError:
    pass
try:
    import time
    _l_(546973)

except ImportError:
    pass

router = "192.168.178.1"
_l_(546974)
web_ip_address = "1.1.1.1"
_l_(546975)

def ping(web_ip_address):
    _l_(546990)

    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    # Option for the number of packets as a function of
    param = '-n' if _c_(546980, _a_(546979, _c_(546978, _a_(546977, _n_(546976, "platform", lambda: platform), "system")), "lower"))=='windows' else '-c'
    _l_(546981)

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', _n_(546982, "param", lambda: param), '1', '-q', _n_(546983, "web_ip_address", lambda: web_ip_address)]
    _l_(546984)
    aux = _c_(546988, _a_(546986, _n_(546985, "subprocess", lambda: subprocess), "call"), _n_(546987, "command", lambda: command)) == 0
    _l_(546989)

    return aux

response = _c_(546993, _n_(546991, "ping", lambda: ping), _n_(546992, "web_ip_address", lambda: web_ip_address))
_l_(546994)
localresponse = _c_(546997, _n_(546995, "ping", lambda: ping), _n_(546996, "router", lambda: router))
_l_(546998)

data = {
    "router_online": _n_(546999, "localresponse", lambda: localresponse),
    "ip_address": _n_(547000, "web_ip_address", lambda: web_ip_address),
    "timestamp": _c_(547003, _a_(547002, _n_(547001, "time", lambda: time), "ctime"))
}
_l_(547004)

if _n_(547005, "response", lambda: response) == True:
    _l_(547028)

    _c_(547008, _n_(547006, "print", lambda: print), _n_(547007, "web_ip_address", lambda: (web_ip_address)), 'is reachable!')
    _l_(547009)
else:
  _c_(547012, _n_(547010, "print", lambda: print), _n_(547011, "web_ip_address", lambda: (web_ip_address)), 'is unreachable!') #writes the data only if the internet connection is down
  _l_(547013) #writes the data only if the internet connection is down
  obj = _c_(547017, _a_(547015, _n_(547014, "json", lambda: json), "loads"), _n_(547016, "data", lambda: data))
  _l_(547018)

  with _c_(547020, _n_(547019, "open", lambda: open), 'Downtime_Data.json', 'a') as json_file:
      _l_(547027)

      _c_(547025, _a_(547022, _n_(547021, "json", lambda: json), "dump"), _n_(547023, "obj", lambda: obj), _n_(547024, "json_file", lambda: json_file), indent = 2 , sort_keys = True,)
      _l_(547026)