# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62996964/attributeerror-on-init-after-overriding-setattr-in-base-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Sub(_n_(551909, "Base", lambda: Base)):
    _l_(551929)

    def __init__(self):
        _l_(551928)

        _c_(551912, _a_(551911, _n_(551910, "super", lambda: super)(), "__init__"))
        _l_(551913)
        row_path = _c_(551915, _n_(551914, "Path", lambda: Path), 'row.json')
        _l_(551916)
        with _c_(551920, _n_(551917, "open", lambda: open), _n_(551918, "template_path", lambda: template_path) / _n_(551919, "row_path", lambda: row_path)) as file:
            _l_(551927)

            _n_(551921, "self", lambda: self).model = _c_(551925, _a_(551923, _n_(551922, "json", lambda: json), "load"), _n_(551924, "file", lambda: file))
            _l_(551926)