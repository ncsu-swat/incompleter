# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51088691/typeerror-in-bar-plot-of-matplotlib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def RGB_hist(image):
    _l_(468958)

    colours = ('r','g','b')
    _l_(468915)
    for i, c in _c_(468918, _n_(468916, "enumerate", lambda: enumerate), _n_(468917, "colours", lambda: colours)):
        _l_(468957)

        _c_(468921, _a_(468920, _n_(468919, "plt", lambda: plt), "figure"), figsize=(20, 4))
        _l_(468922)
        histr = _c_(468927, _a_(468924, _n_(468923, "cv2", lambda: cv2), "calcHist"), [_n_(468925, "image", lambda: image)], [_n_(468926, "i", lambda: i)], None, [256], [0, 256])
        _l_(468928)

        if _n_(468929, "c", lambda: c) == 'r':
            _l_(468933)

colours = [((_n_(468930, "i", lambda: i)/256, 0, 0)) for i in _c_(468932, _n_(468931, "range", lambda: range), 0, 256)]        if _n_(468934, "c", lambda: c) == 'g':
            _l_(468938)

colours = [((0, _n_(468935, "i", lambda: i)/256, 0)) for i in _c_(468937, _n_(468936, "range", lambda: range), 0, 256)]        if _n_(468939, "c", lambda: c) == 'b':
            _l_(468943)

colours = [((0, 0, _n_(468940, "i", lambda: i)/256)) for i in _c_(468942, _n_(468941, "range", lambda: range), 0, 256)]

        _c_(468951, _a_(468945, _n_(468944, "plt", lambda: plt), "bar"), _c_(468947, _n_(468946, "range", lambda: range), 0, 256), _n_(468948, "histr", lambda: histr), color=_n_(468949, "colours", lambda: colours), edgecolor=_n_(468950, "colours", lambda: colours), width=1)
        _l_(468952)

        _c_(468955, _a_(468954, _n_(468953, "plt", lambda: plt), "show"))
        _l_(468956)

_c_(468961, _n_(468959, "RGB_hist", lambda: RGB_hist), _n_(468960, "image", lambda: image))
_l_(468962)