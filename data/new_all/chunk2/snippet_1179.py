# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57621345/python-typeerror-shows-up-during-ci-cd-process
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pkg_resources
    _l_(467509)

except ImportError:
    pass

DATA_PATH = 'package.name.data'
_l_(467510)
MY_DATA_PATH = _c_(467514, _a_(467512, _n_(467511, "pkg_resources", lambda: pkg_resources), "resource_filename"), _n_(467513, "DATA_PATH", lambda: DATA_PATH), 'MY_DATA.txt')
_l_(467515)


def do_some_stuff_with_data(data_path=_n_(467516, "MY_DATA_PATH", lambda: MY_DATA_PATH)):
    _l_(467518)

    ...
    _l_(467517)