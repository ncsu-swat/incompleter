# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50538447/attributeerror-module-zbar-has-no-attribute-imagescanner
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyqrcode
    _l_(534519)

except ImportError:
    pass
try:
    from qrtools import qrtools
    _l_(534521)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(534523)

except ImportError:
    pass
try:
    import zbar
    _l_(534525)

except ImportError:
    pass
qr = _c_(534528, _a_(534527, _n_(534526, "pyqrcode", lambda: pyqrcode), "create"), "She got two litle horns and they get me a litle bit")
_l_(534529)
_c_(534532, _a_(534531, _n_(534530, "qr", lambda: qr), "png"), "horn.png", scale=6)
_l_(534533)
qr = _c_(534536, _a_(534535, _n_(534534, "qrtools", lambda: qrtools), "QR"))
_l_(534537)
scanner = _c_(534540, _a_(534539, _n_(534538, "zbar", lambda: zbar), "Scanner"))
_l_(534541)
_c_(534544, _a_(534543, _n_(534542, "qr", lambda: qr), "decode"), "horn.png")
_l_(534545)
_c_(534549, _n_(534546, "print", lambda: print), _a_(534548, _n_(534547, "qr", lambda: qr), "data"))
_l_(534550)