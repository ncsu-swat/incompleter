# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43670450/attributeerror-when-creating-zipfile
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlretrieve
    _l_(446780)

except ImportError:
    pass
try:
    from os import path
    _l_(446782)

except ImportError:
    pass
try:
    from zipfile import ZipFile
    _l_(446784)

except ImportError:
    pass

download_url = "https://www.dropbox.com/s/obiqvrt4m53pmoz/tesseract-4.0.0-alpha.zip?dl=1"
_l_(446785)


def setup_program():
    _l_(446805)

    zip_name = _c_(446788, _n_(446786, "urlretrieve", lambda: urlretrieve), _n_(446787, "download_url", lambda: download_url))
    _l_(446789)

    zip_file = _c_(446792, _n_(446790, "ZipFile", lambda: ZipFile), _n_(446791, "zip_name", lambda: zip_name), "r")
    _l_(446793)
    _c_(446799, _a_(446795, _n_(446794, "zip_file", lambda: zip_file), "extractall"), _c_(446798, _a_(446797, _n_(446796, "path", lambda: path), "abspath"), "__tesseract/"))
    _l_(446800)
    _c_(446803, _a_(446802, _n_(446801, "zip_file", lambda: zip_file), "close"))
    _l_(446804)

_c_(446807, _n_(446806, "setup_program", lambda: setup_program))  # REMOVE after test
_l_(446808)  # REMOVE after test