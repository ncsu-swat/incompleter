# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59932201/filenotfounderror-errno-2-no-such-file-or-directory-c-users-dell-coil-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
original_dataset_dir=r"C:\Users\DELL\coil-20-unproc"
_l_(460544)
# Copy object1 images to train_obj1_dir
fnames = [_c_(460547, _a_(460545, 'obj1_{}.png', "format"), _n_(460546, "i", lambda: i)) for i in _c_(460549, _n_(460548, "range", lambda: range), 0,72)]
_l_(460550)
for fname in _n_(460551, "fnames", lambda: fnames):
    _l_(460572)

    src = _c_(460557, _a_(460554, _a_(460553, _n_(460552, "os", lambda: os), "path"), "join"), _n_(460555, "original_dataset_dir", lambda: original_dataset_dir), _n_(460556, "fname", lambda: fname))
    _l_(460558)
    dst = _c_(460564, _a_(460561, _a_(460560, _n_(460559, "os", lambda: os), "path"), "join"), _n_(460562, "train_obj1_dir", lambda: train_obj1_dir), _n_(460563, "fname", lambda: fname))
    _l_(460565)
    _c_(460570, _a_(460567, _n_(460566, "shutil", lambda: shutil), "copyfile"), _n_(460568, "src", lambda: src), _n_(460569, "dst", lambda: dst))
    _l_(460571)