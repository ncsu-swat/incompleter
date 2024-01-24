# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59117289/python-error-code-attributeerror-tuple-object-has-no-attribute-save
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(698168)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(698170)

except ImportError:
    pass
try:
    import numpy as np
    _l_(698172)

except ImportError:
    pass

def int_to_bin(rgb):
    _l_(698185)

    r, g, b = _n_(698173, "rgb", lambda: rgb)
    _l_(698174)
    aux = (_c_(698177, _a_(698175, '{0:08b}', "format"), _n_(698176, "r", lambda: r)), _c_(698180, _a_(698178, '{0:08b}', "format"), _n_(698179, "g", lambda: g)), _c_(698183, _a_(698181, '{0:08b}', "format"), _n_(698182, "b", lambda: b))) 
    _l_(698184) 
    return aux 

def merge_rgb(rgb1, rgb2):
    _l_(698199)

    r1, b1, g1 = _n_(698186, "rgb1", lambda: rgb1)
    _l_(698187)
    r2, b2, g2 = _n_(698188, "rgb2", lambda: rgb2)
    _l_(698189)

    rgb = (_n_(698190, "r1", lambda: r1)[:4] + _n_(698191, "r2", lambda: r2)[:4], _n_(698192, "g1", lambda: g1)[:4] + _n_(698193, "g2", lambda: g2)[:4], _n_(698194, "b1", lambda: b1)[:4] + _n_(698195, "b2", lambda: b2)[:4])
    _l_(698196)
    aux = _n_(698197, "rgb", lambda: rgb)
    _l_(698198)

    return aux

im = "bunga.jpg"
_l_(698200)
img1 =  _c_(698204, _a_(698202, _n_(698201, "Image", lambda: Image), "open"), _n_(698203, "im", lambda: im),'r')
_l_(698205)

im2 = "index.jpg"
_l_(698206)
img2 = _c_(698210, _a_(698208, _n_(698207, "Image", lambda: Image), "open"), _n_(698209, "im2", lambda: im2),'r')
_l_(698211)

pixel_map1 = _c_(698214, _a_(698213, _n_(698212, "img1", lambda: img1), "load"))
_l_(698215)
pixel_map2 = _c_(698218, _a_(698217, _n_(698216, "img2", lambda: img2), "load"))
_l_(698219)

for i in _c_(698223, _n_(698220, "range", lambda: range), _a_(698222, _n_(698221, "img1", lambda: img1), "size")[0]):
    _l_(698253)

    for j in _c_(698227, _n_(698224, "range", lambda: range), _a_(698226, _n_(698225, "img1", lambda: img1), "size")[1]):
        _l_(698252)

        rgb1 = _c_(698232, _n_(698228, "int_to_bin", lambda: int_to_bin), _n_(698229, "pixel_map1", lambda: pixel_map1)[_n_(698230, "i", lambda: i), _n_(698231, "j", lambda: j)])
        _l_(698233)

        if _n_(698234, "i", lambda: i) < _a_(698236, _n_(698235, "img2", lambda: img2), "size")[0] and _n_(698237, "j", lambda: j) < _a_(698239, _n_(698238, "img2", lambda: img2), "size")[1]:
            _l_(698251)

            rgb2 = _c_(698244, _n_(698240, "int_to_bin", lambda: int_to_bin), _n_(698241, "pixel_map2", lambda: pixel_map2)[_n_(698242, "i", lambda: i), _n_(698243, "j", lambda: j)])
            _l_(698245)
            rgb = _c_(698249, _n_(698246, "merge_rgb", lambda: merge_rgb), _n_(698247, "rgb1", lambda: rgb1), _n_(698248, "rgb2", lambda: rgb2))
            _l_(698250)

merged_image = _n_(698254, "rgb", lambda: rgb)
_l_(698255)
img = _c_(698258, _a_(698257, _n_(698256, "merged_image", lambda: merged_image), "save"), "decode_konversiGreykeBiner.jpg")
_l_(698259)