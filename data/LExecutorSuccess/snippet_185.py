# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8384737/extract-file-name-from-path-no-matter-what-the-os-path-format
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1547134)

except ImportError:
    pass

my_fullpath = r"D:\MY_FOLDER\TEST\20201108\20201108_073751.DNG"
_l_(1547135)
_c_(1547144, _a_(1547138, _a_(1547137, _n_(1547136, "os", lambda: os), "path"), "basename"), _c_(1547143, _a_(1547140, _n_(1547139, "my_fullpath", lambda: my_fullpath), "replace"), '\\',_a_(1547142, _n_(1547141, "os", lambda: os), "sep")))
_l_(1547145)

my_fullpath = r"/MY_FOLDER/TEST/20201108/20201108_073751.DNG"
_l_(1547146)
_c_(1547155, _a_(1547149, _a_(1547148, _n_(1547147, "os", lambda: os), "path"), "basename"), _c_(1547154, _a_(1547151, _n_(1547150, "my_fullpath", lambda: my_fullpath), "replace"), '\\',_a_(1547153, _n_(1547152, "os", lambda: os), "sep")))
_l_(1547156)

my_fullpath = r"/MY_FOLDER/TEST/20201108/"
_l_(1547157)
_c_(1547166, _a_(1547160, _a_(1547159, _n_(1547158, "os", lambda: os), "path"), "basename"), _c_(1547165, _a_(1547162, _n_(1547161, "my_fullpath", lambda: my_fullpath), "replace"), '\\',_a_(1547164, _n_(1547163, "os", lambda: os), "sep")))
_l_(1547167)

my_fullpath = r"/MY_FOLDER/TEST/20201108"
_l_(1547168)
_c_(1547177, _a_(1547171, _a_(1547170, _n_(1547169, "os", lambda: os), "path"), "basename"), _c_(1547176, _a_(1547173, _n_(1547172, "my_fullpath", lambda: my_fullpath), "replace"), '\\',_a_(1547175, _n_(1547174, "os", lambda: os), "sep")))
_l_(1547178)

