# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38441889/get-nameerror-name-ip-is-not-defined-error-message
#!/usr/bin/python

#for python 3 , must install scapy for python3 first by type command "pip3 install scapy-python3"
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scapy.all
    _l_(448049)

except ImportError:
    pass

frame = _c_(448052, _a_(448051, _a_(448050, scapy, "all"), "Ether"), dst="15:16:89:fa:dd:09") / _c_(448054, _n_(448053, "IP", lambda: IP), dst="9.16.5.4") / _c_(448056, _n_(448055, "TCP", lambda: TCP)) / "This is my payload"
_l_(448057)