# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63977672/filenotfounderror-errno-2-no-such-file-or-directory-python-writer-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from subprocess import Popen, PIPE
    _l_(591113)

except ImportError:
    pass


p1 = _c_(591116, _n_(591114, "Popen", lambda: Popen), 'python writer.py', stdout=_n_(591115, "PIPE", lambda: PIPE))
_l_(591117)
p2 = _c_(591122, _n_(591118, "Popen", lambda: Popen), 'python reader.py', stdin=_a_(591120, _n_(591119, "p1", lambda: p1), "stdout"), stdout=_n_(591121, "PIPE", lambda: PIPE))
_l_(591123)
output = _c_(591126, _a_(591125, _n_(591124, "p2", lambda: p2), "communicate"))[0]
_l_(591127)
_c_(591130, _n_(591128, "print", lambda: print), _n_(591129, "output", lambda: output))
_l_(591131)