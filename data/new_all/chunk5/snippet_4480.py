# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56867560/nameerror-name-paramiko-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import paramiko
    _l_(664276)

except ImportError:
    pass

ssh = _c_(664279, _a_(664278, _n_(664277, "paramiko", lambda: paramiko), "SSHClient"))
_l_(664280)
_c_(664286, _a_(664282, _n_(664281, "ssh", lambda: ssh), "set_missing_host_key_policy"), _c_(664285, _a_(664284, _n_(664283, "paramiko", lambda: paramiko), "AutoAddPolicy")))
_l_(664287)
_c_(664290, _n_(664288, "print", lambda: print), _n_(664289, "ssh", lambda: ssh))
_l_(664291)