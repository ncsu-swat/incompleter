# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66552353/pillow-attributeerror-photoimage-object-has-no-attribute-photoimage-photo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
path = _c_(600820, _n_(600812, "str", lambda: str), _c_(600819, _a_(600818, _a_(600817, _c_(600816, _a_(600814, _n_(600813, "pathlib", lambda: pathlib), "Path"), _n_(600815, "__file__", lambda: __file__)), "parent"), "absolute"))) + '/Chess/Sprites/W_K.png'
_l_(600821)
norm_img = _c_(600825, _a_(600823, _n_(600822, "Image", lambda: Image), "open"), _n_(600824, "path", lambda: path))
_l_(600826)
img = _c_(600829, _a_(600828, _n_(600827, "norm_img", lambda: norm_img), "resize"), (50,50))
_l_(600830)
photo = _c_(600834, _a_(600832, _n_(600831, "ImageTk", lambda: ImageTk), "PhotoImage"), image=_n_(600833, "img", lambda: img))
_l_(600835)
king = _c_(600840, _a_(600838, _a_(600837, _n_(600836, "self", lambda: self), "base"), "create_image"), (100,100),image=_n_(600839, "photo", lambda: photo))
_l_(600841)