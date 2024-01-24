# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59181118/os-mkdir-returns-error-filenotfounderror-errno-2-no-such-file-or-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ssh_path = f"{_c_(382670, _a_(382669, _n_(382668, 'os', lambda: os), 'getenv'), 'HOME')}/temp/.ssh"
_l_(382671)
_c_(382674, _n_(382672, "print", lambda: print), _n_(382673, "ssh_path", lambda: ssh_path))
_l_(382675)
_c_(382679, _a_(382677, _n_(382676, "os", lambda: os), "mkdir"), _n_(382678, "ssh_path", lambda: ssh_path))
_l_(382680)