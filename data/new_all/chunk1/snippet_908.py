# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44723602/attributeerror-str-object-has-no-attribute-seek-using-textfsm-module-regex
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
          from netmiko import ConnectHandler
          _l_(414723)

except ImportError:
          pass
try:
          from textfsm import *
          _l_(414725)

except ImportError:
          pass

cisco_device = { 'device_type' : 'cisco_ios', 'ip' : 'x.x.x.x', 'username':'****0', 'password':'***9'}
_l_(414726)
net_connect = _c_(414729, _n_(414727, "ConnectHandler", lambda: ConnectHandler), **_n_(414728, "cisco_device", lambda: cisco_device))
_l_(414730)

fo=("test.txt" , 'w')
_l_(414731)

output = _c_(414734, _a_(414733, _n_(414732, "net_connect", lambda: net_connect), "send_command"), "show ip int brief")
_l_(414735)

re_table = _c_(414737, _n_(414736, "TextFSM", lambda: TextFSM), 'xr_show_int_br','r')     
_l_(414738)     

data = _c_(414742, _a_(414740, _n_(414739, "re_table", lambda: re_table), "ParseText"), _n_(414741, "output", lambda: output))
_l_(414743)

_c_(414746, _n_(414744, "print", lambda: print), _n_(414745, "output", lambda: output))
_l_(414747)
_c_(414751, _n_(414748, "print", lambda: print), _a_(414750, _n_(414749, "re_table", lambda: re_table), "header"))
_l_(414752)

for test in _a_(414754, _n_(414753, "re_table", lambda: re_table), "header"):
          _l_(414760)

          _c_(414758, _a_(414756, _n_(414755, "fo", lambda: fo), "write"), _n_(414757, "test", lambda: test))
          _l_(414759)

_c_(414763, _a_(414762, _n_(414761, "fo", lambda: fo), "write"), "\n")
_l_(414764)

for row in _n_(414765, "data", lambda: data):
          _l_(414777)

          for temp_row in _n_(414766, "data", lambda: data):
                    _l_(414772)

                    _c_(414770, _a_(414768, _n_(414767, "fo", lambda: fo), "write"), _n_(414769, "temp_row", lambda: temp_row))
                    _l_(414771)
          _c_(414775, _a_(414774, _n_(414773, "fo", lambda: fo), "write"), "\n")
          _l_(414776)


_a_(414779, _n_(414778, "fo", lambda: fo), "close")
_l_(414780)