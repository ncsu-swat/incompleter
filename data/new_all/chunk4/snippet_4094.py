# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62981032/python-filenotfounderror-errno-2-no-such-file-or-directory-how-to-add-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image, ImageFilter
    _l_(634284)

except ImportError:
    pass
try:
    import os
    _l_(634286)

except ImportError:
    pass

root_dir= _c_(634294, _a_(634289, _a_(634288, _n_(634287, "os", lambda: os), "path"), "dirname"), _c_(634293, _a_(634292, _a_(634291, _n_(634290, "os", lambda: os), "path"), "abspath"), r'C:\Users\User\eclipse-workspace\Practice Python CS50 2019\images\Mario.png'))
_l_(634295)
before = _c_(634298, _a_(634297, _n_(634296, "Image", lambda: Image), "open"), 'Mario.png')
_l_(634299)
after=_c_(634304, _a_(634301, _n_(634300, "before", lambda: before), "filter"), _a_(634303, _n_(634302, "ImageFilter", lambda: ImageFilter), "BLUR"))
_l_(634305)
_c_(634308, _a_(634307, _n_(634306, "after", lambda: after), "save"), "MarioBLUR.png")
_l_(634309)