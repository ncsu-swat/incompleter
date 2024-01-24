# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56920338/some-time-program-works-fine-and-some-times-shows-height-width-layers-img-sh
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
img_array = []
_l_(358138)
for filename in _c_(358141, _a_(358140, _n_(358139, "glob", lambda: glob), "glob"), '/home/adnan/Downloads/*.png'):
    _l_(358162)

    img = _c_(358145, _a_(358143, _n_(358142, "cv2", lambda: cv2), "imread"), _n_(358144, "filename", lambda: filename))
    _l_(358146)
    _c_(358149, _n_(358147, "print", lambda: print), _n_(358148, "img", lambda: img))
    _l_(358150)
    height, width, layers = _a_(358152, _n_(358151, "img", lambda: img), "shape")
    _l_(358153)
    size = (_n_(358154, "width", lambda: width),_n_(358155, "height", lambda: height))
    _l_(358156)
    _c_(358160, _a_(358158, _n_(358157, "img_array", lambda: img_array), "append"), _n_(358159, "img", lambda: img))
    _l_(358161)


out = _c_(358169, _a_(358164, _n_(358163, "cv2", lambda: cv2), "VideoWriter"), 'project.mp4',_c_(358167, _a_(358166, _n_(358165, "cv2", lambda: cv2), "VideoWriter_fourcc"), *'DIVX'), 5, _n_(358168, "size", lambda: size))
_l_(358170)

for i in _c_(358175, _n_(358171, "range", lambda: range), _c_(358174, _n_(358172, "len", lambda: len), _n_(358173, "img_array", lambda: img_array))):
    _l_(358182)

    _c_(358180, _a_(358177, _n_(358176, "out", lambda: out), "write"), _n_(358178, "img_array", lambda: img_array)[_n_(358179, "i", lambda: i)])
    _l_(358181)
_c_(358185, _a_(358184, _n_(358183, "out", lambda: out), "release"))
_l_(358186)