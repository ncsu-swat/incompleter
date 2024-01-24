# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38555408/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-while
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(686192)

except ImportError:
    pass
try:
    from pytesseract import image_to_string
    _l_(686194)

except ImportError:
    pass
try:
    import os.path
    _l_(686196)

except ImportError:
    pass

if _c_(686199, _a_(686198, _a_(686197, os, "path"), "exists"), 'image.png'):
    _l_(686220)

    filename = 'image.png'
    _l_(686200)
    image = _c_(686204, _a_(686202, _n_(686201, "Image", lambda: Image), "open"), _n_(686203, "filename", lambda: filename))
    _l_(686205)
    _c_(686208, _a_(686207, _n_(686206, "image", lambda: image), "show"))
    _l_(686209)
    s = _c_(686215, _n_(686210, "image_to_string", lambda: image_to_string), _c_(686214, _a_(686212, _n_(686211, "Image", lambda: Image), "open"), _n_(686213, "filename", lambda: filename)))
    _l_(686216)
else:
    _c_(686218, _n_(686217, "print", lambda: print), 'Does not exist')
    _l_(686219)