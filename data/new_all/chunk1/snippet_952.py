# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69656383/typeerror-cannot-use-a-string-pattern-on-a-bytes-like-object-pyexpect-in-pyth
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
buff = _c_(400220, _n_(400219, "BytesIO", lambda: BytesIO))
_l_(400221)
child = _c_(400230, _a_(400223, _n_(400222, "pexpect", lambda: pexpect), "spawn"), _n_(400224, "path", lambda: path), _n_(400225, "args", lambda: args), logfile=_n_(400226, "buff", lambda: buff), timeout=_a_(400228, _n_(400227, "self", lambda: self), "PASSPHRASE_TIMEOUT"), **_n_(400229, "kwargs", lambda: kwargs))
_l_(400231)
while True:
     _l_(400254)

     idx = _c_(400238, _a_(400233, _n_(400232, "child", lambda: child), "expect"), [_a_(400235, _n_(400234, "self", lambda: self), "PASSPHRASE_RE"),_a_(400237, _n_(400236, "pexpect", lambda: pexpect), "EOF")])
     _l_(400239)
     if _n_(400240, "idx", lambda: idx) == 0:
          _l_(400253)

          _c_(400244, _a_(400242, _n_(400241, "child", lambda: child), "sendline"), _n_(400243, "passphrase", lambda: passphrase))
          _l_(400245)
     elif _n_(400246, "idx", lambda: idx) == 1:
          _l_(400252)

          _c_(400249, _a_(400248, _n_(400247, "child", lambda: child), "wait"))
          _l_(400250)
          break
          _l_(400251)