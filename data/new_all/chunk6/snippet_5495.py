# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63198481/os-rename-does-not-succeed-in-renaming-in-subdirectories-throws-filenotfounderr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cwd = _c_(343687, _a_(343686, _n_(343685, "os", lambda: os), "getcwd"))
_l_(343688)
fileListOld = _c_(343693, _a_(343690, _n_(343689, "glob", lambda: glob), "glob"), f"{_n_(343691, 'cwd', lambda: cwd)}/**/{_n_(343692, 'old_name', lambda: old_name)}", recursive=True)
_l_(343694)