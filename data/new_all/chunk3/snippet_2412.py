# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44726772/attributeerror-tuple-object-has-no-attribute-write-error-while-writing-into
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
          from netmiko import ConnectHandler
          _l_(543742)

except ImportError:
          pass
try:
          from textfsm import *
          _l_(543744)

except ImportError:
          pass

cisco_device = { 'device_type' : 'cisco_ios', 'ip' : 'x.x.x.x', 'username':'gtomy200', 'password':'xxxxx'}
_l_(543745)
net_connect = _c_(543748, _n_(543746, "ConnectHandler", lambda: ConnectHandler), **_n_(543747, "cisco_device", lambda: cisco_device))
_l_(543749)

fo=("testme.txt" , 'w')
_l_(543750)

output = _c_(543753, _a_(543752, _n_(543751, "net_connect", lambda: net_connect), "send_command"), "show int brief")
_l_(543754)

re_table = _c_(543758, _n_(543755, "TextFSM", lambda: TextFSM), _c_(543757, _n_(543756, "open", lambda: open), 'xr_show_int_br','r'))    
_l_(543759)    

data = _c_(543763, _a_(543761, _n_(543760, "re_table", lambda: re_table), "ParseText"), _n_(543762, "output", lambda: output))
_l_(543764)

_c_(543767, _n_(543765, "print", lambda: print), _n_(543766, "output", lambda: output))
_l_(543768)

for s in _a_(543770, _n_(543769, "re_table", lambda: re_table), "header"):
          _l_(543776)


          _c_(543774, _a_(543772, _n_(543771, "fo", lambda: fo), "write"), "%s;" %_n_(543773, "s", lambda: s))
          _l_(543775)

_c_(543779, _a_(543778, _n_(543777, "fo", lambda: fo), "write"), "\n")
_l_(543780)

for row in _n_(543781, "data", lambda: data):
          _l_(543797)

          _c_(543784, _n_(543782, "print", lambda: print), _n_(543783, "row", lambda: row))
          _l_(543785)
          for s in _n_(543786, "row", lambda: row):
                    _l_(543796)


                    _c_(543790, _a_(543788, _n_(543787, "fo", lambda: fo), "write"), "%s" %_n_(543789, "s", lambda: s))
                    _l_(543791)
                    _c_(543794, _a_(543793, _n_(543792, "fo", lambda: fo), "write"), "\n")
                    _l_(543795)

_c_(543800, _a_(543799, _n_(543798, "fo", lambda: fo), "close"))
_l_(543801)