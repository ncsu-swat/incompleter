# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58469331/kivy-attributeerror-with-property-defined-in-kv-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(458408)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(458410)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(458412)

except ImportError:
    pass
try:
    from kivy.uix.anchorlayout import AnchorLayout
    _l_(458414)

except ImportError:
    pass

_c_(458417, _a_(458416, _n_(458415, "kivy", lambda: kivy), "require"), '1.9.0')
_l_(458418)

_c_(458421, _a_(458420, _n_(458419, "Builder", lambda: Builder), "load_file"), 'toolbox.kv')
_l_(458422)
_c_(458425, _a_(458424, _n_(458423, "Builder", lambda: Builder), "load_file"), 'drawingspace.kv')
_l_(458426)
_c_(458429, _a_(458428, _n_(458427, "Builder", lambda: Builder), "load_file"), 'comicwidgets.kv')
_l_(458430)
_c_(458433, _a_(458432, _n_(458431, "Builder", lambda: Builder), "load_file"), 'generaloptions.kv')
_l_(458434)
_c_(458437, _a_(458436, _n_(458435, "Builder", lambda: Builder), "load_file"), 'statusbar.kv')
_l_(458438)


class ComicCreator(_n_(458439, "AnchorLayout", lambda: AnchorLayout)):
    _l_(458441)

    pass
    _l_(458440)


class ComicCreatorApp(_n_(458442, "App", lambda: App)):
    _l_(458447)

    def build(self):
        _l_(458446)

        aux = _c_(458444, _n_(458443, "ComicCreator", lambda: ComicCreator))
        _l_(458445)
        return aux


if _n_(458448, "__name__", lambda: __name__) == '__main__':
    _l_(458454)

    _c_(458452, _a_(458451, _c_(458450, _n_(458449, "ComicCreatorApp", lambda: ComicCreatorApp)), "run"))
    _l_(458453)