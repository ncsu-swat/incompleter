# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74975991/shutil-copyfile-permissionerror-or-filenotfounderror-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
DATA_DIR = _c_(548844, _a_(548843, _n_(548842, "Path", lambda: Path), "cwd")) / 'sourceFolder'
_l_(548845)
files = _c_(548849, _a_(548847, _n_(548846, "os", lambda: os), "listdir"), _n_(548848, "DATA_DIR", lambda: DATA_DIR))
_l_(548850)
des = _c_(548855, _a_(548853, _a_(548852, _n_(548851, "os", lambda: os), "path"), "join"), '/destFolder', _n_(548854, "files", lambda: files)[0])
_l_(548856)
_c_(548865, _a_(548858, _n_(548857, "shutil", lambda: shutil), "copyfile"), _c_(548863, _a_(548861, _a_(548860, _n_(548859, "os", lambda: os), "path"), "join"), 'sourceFolder', _n_(548862, "files", lambda: files)[0]), _n_(548864, "des", lambda: des))
_l_(548866)