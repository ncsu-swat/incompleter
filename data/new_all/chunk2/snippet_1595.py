# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73149936/pexpect-interact-typeerror-write-argument-must-be-str-not-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
child = _c_(431783, _a_(431782, _n_(431781, "pexpect", lambda: pexpect), "spawn"), 'npm login', timeout=40, encoding='utf-8')
_l_(431784)
_n_(431785, "child", lambda: child).logfile_read = _a_(431787, _n_(431786, "sys", lambda: sys), "stdout")
_l_(431788)
_c_(431791, _a_(431790, _n_(431789, "child", lambda: child), "expect"), 'Username:')
_l_(431792)
_c_(431795, _a_(431794, _n_(431793, "child", lambda: child), "sendline"), 'qiulang2000')
_l_(431796)
_c_(431799, _a_(431798, _n_(431797, "child", lambda: child), "expect"), 'Password:')
_l_(431800)
_c_(431803, _a_(431802, _n_(431801, "child", lambda: child), "sendline"), 'xxxx')
_l_(431804)
...
_l_(431805)
_c_(431808, _a_(431807, _n_(431806, "child", lambda: child), "interact"))
_l_(431809)