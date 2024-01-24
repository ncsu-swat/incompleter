# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55807656/rows-cols-frame-shape-attributeerror-nonetype-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while True:
    _l_(671184)

    _, frame = _c_(671169, _a_(671168, _n_(671167, "cap", lambda: cap), "read"))
    _l_(671170)
    # frame = cv2.resize(frame, None, fx=0.8, fy=0.8)
    rows, cols, _ = _a_(671172, _n_(671171, "frame", lambda: frame), "shape")
    _l_(671173)
    _n_(671174, "keyboard", lambda: keyboard)[:] = (26, 26, 26)
    _l_(671175)
    frames += 1
    _l_(671176)
    gray = _c_(671182, _a_(671178, _n_(671177, "cv2", lambda: cv2), "cvtColor"), _n_(671179, "frame", lambda: frame), _a_(671181, _n_(671180, "cv2", lambda: cv2), "COLOR_BGR2GRAY"))
    _l_(671183)