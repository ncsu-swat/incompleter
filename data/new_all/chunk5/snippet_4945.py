# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38555408/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-while
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(690719)

except ImportError:
    pass
try:
    from pytesseract import image_to_string
    _l_(690721)

except ImportError:
    pass
try:
    import os.path
    _l_(690723)

except ImportError:
    pass

if _c_(690726, _a_(690725, _a_(690724, os, "path"), "exists"), 'image.png'):
    _l_(690747)

    filename = 'image.png'
    _l_(690727)
    image = _c_(690731, _a_(690729, _n_(690728, "Image", lambda: Image), "open"), _n_(690730, "filename", lambda: filename))
    _l_(690732)
    _c_(690735, _a_(690734, _n_(690733, "image", lambda: image), "show"))
    _l_(690736)
    s = _c_(690742, _n_(690737, "image_to_string", lambda: image_to_string), _c_(690741, _a_(690739, _n_(690738, "Image", lambda: Image), "open"), _n_(690740, "filename", lambda: filename)))
    _l_(690743)
else:
    _c_(690745, _n_(690744, "print", lambda: print), 'Does not exist')
    _l_(690746)