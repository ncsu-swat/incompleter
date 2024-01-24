# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57426599/mpld3-error-attributeerror-list-object-has-no-attribute-canvas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(548192, _a_(548191, _n_(548190, "plt", lambda: plt), "subplots"), 1, 1, figsize=(8, 2))
_l_(548193)
ecg = _n_(548194, "X", lambda: X)
_l_(548195)
fig=_c_(548198, _a_(548197, _n_(548196, "plt", lambda: plt), "figure"))
_l_(548199)
alt = _c_(548205, _a_(548201, _n_(548200, "np", lambda: np), "arange"), _c_(548204, _n_(548202, "len", lambda: len), _n_(548203, "ecg", lambda: ecg)))/125
_l_(548206)
fig= _c_(548211, _a_(548208, _n_(548207, "plt", lambda: plt), "plot"), _n_(548209, "alt", lambda: alt),_n_(548210, "ecg", lambda: ecg))
_l_(548212)
_c_(548216, _a_(548214, _n_(548213, "mpld3", lambda: mpld3), "save_html"), _n_(548215, "fig", lambda: fig),"test.html")
_l_(548217)
_c_(548221, _a_(548219, _n_(548218, "mpld3", lambda: mpld3), "fig_to_html"), _n_(548220, "fig", lambda: fig),template_type="simple")
_l_(548222)
_c_(548225, _a_(548224, _n_(548223, "mpld3", lambda: mpld3), "disable_notebook"))
_l_(548226)
_c_(548229, _a_(548228, _n_(548227, "mpld3", lambda: mpld3), "show"))
_l_(548230)