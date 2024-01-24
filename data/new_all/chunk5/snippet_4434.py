# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57833141/filenotfounderror-errno-2-no-such-file-or-directory-even-i-have-image-in-th
# Setting up the image pool
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
image_path = "C:\\Users\\New\\Desktop\\images"
_l_(685995)
imgs = _c_(685999, _a_(685997, _n_(685996, "os", lambda: os), "listdir"), _n_(685998, "image_path", lambda: image_path))
_l_(686000)
img_x = img_y = 50 # image size is constant
_l_(686001) # image size is constant
n_samples = _c_(686005, _a_(686003, _n_(686002, "np", lambda: np), "size"), _n_(686004, "imgs", lambda: imgs))
_l_(686006)
_n_(686007, "n_samples", lambda: n_samples) # 20778 originally
_l_(686008) # 20778 originally

# Loading all images...
images = _c_(686027, _a_(686010, _n_(686009, "np", lambda: np), "array"), [_c_(686022, _a_(686021, _c_(686020, _a_(686012, _n_(686011, "np", lambda: np), "array"), _c_(686019, _a_(686018, _c_(686017, _a_(686014, _n_(686013, "Image", lambda: Image), "open"), _n_(686015, "image_path", lambda: image_path) +  
_n_(686016, "imgs", lambda: imgs)), "convert"), "RGB")), "flatten")) for imgs in _c_(686026, _a_(686024, _n_(686023, "os", lambda: os), "listdir"), _n_(686025, "image_path", lambda: image_path))], 
order='F', dtype='uint8')
_l_(686028)
_c_(686032, _a_(686030, _n_(686029, "np", lambda: np), "shape"), _n_(686031, "images", lambda: images))
_l_(686033)