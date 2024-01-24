# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64404150/python3-replace-yielding-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
s = _c_(403284, _a_(403283, _n_(403282, "paramiko", lambda: paramiko), "SSHClient"))
_l_(403285)
_c_(403288, _a_(403287, _n_(403286, "s", lambda: s), "load_system_host_keys"))
_l_(403289)
_c_(403295, _a_(403291, _n_(403290, "s", lambda: s), "set_missing_host_key_policy"), _c_(403294, _a_(403293, _n_(403292, "paramiko", lambda: paramiko), "AutoAddPolicy")))
_l_(403296)
_c_(403303, _a_(403298, _n_(403297, "s", lambda: s), "connect"), _n_(403299, "hostname", lambda: hostname), _n_(403300, "port", lambda: port), _n_(403301, "username", lambda: username), _n_(403302, "password", lambda: password))
_l_(403304)
command = 'xe vm-list'
_l_(403305)
(stdin, stdout, stderr) = _c_(403309, _a_(403307, _n_(403306, "s", lambda: s), "exec_command"), _n_(403308, "command", lambda: command))
_l_(403310)

output = _c_(403313, _a_(403312, _n_(403311, "stdout", lambda: stdout), "read"))
_l_(403314)
x = _c_(403319, _a_(403318, _c_(403317, _a_(403316, _n_(403315, "output", lambda: output), "replace"), "\n", ","), "strip"))
_l_(403320)
_c_(403323, _n_(403321, "print", lambda: print), _n_(403322, "x", lambda: x))
_l_(403324)
_c_(403327, _a_(403326, _n_(403325, "s", lambda: s), "close"))
_l_(403328)