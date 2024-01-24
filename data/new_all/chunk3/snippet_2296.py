# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53139681/typeerror-kivy-weakproxy-weakproxy-object-is-not-callable-kivi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(576297)

except ImportError:
    pass
try:
    import glob
    _l_(576299)

except ImportError:
    pass
try:
    from os import path
    _l_(576301)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(576303)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(576305)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(576307)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(576309)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(576311)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(576313)

except ImportError:
    pass
try:
    from kivy.uix.gridlayout import GridLayout
    _l_(576315)

except ImportError:
    pass

_c_(576318, _a_(576317, _n_(576316, "kivy", lambda: kivy), "require"), '1.9.0')
_l_(576319)

class FilesPanel(_n_(576320, "GridLayout", lambda: GridLayout)):
    _l_(576365)

    frames_list = _c_(576322, _n_(576321, "ObjectProperty", lambda: ObjectProperty))
    _l_(576323)

    def open_files(self):
        _l_(576340)

        root = _c_(576326, _a_(576325, _n_(576324, "tk", lambda: tk), "Tk"))
        _l_(576327)
        _c_(576330, _a_(576329, _n_(576328, "root", lambda: root), "withdraw"))
        _l_(576331)

        _c_(576338, _a_(576333, _n_(576332, "self", lambda: self), "load_files"), _c_(576337, _a_(576335, _n_(576334, "filedialog", lambda: filedialog), "askdirectory"), parent=_n_(576336, "root", lambda: root),initialdir="/", title='Please select a directory'))
        _l_(576339)

    def load_files(self, selected_folder):
        _l_(576364)

        all_bin_files = _c_(576347, _a_(576342, _n_(576341, "glob", lambda: glob), "glob"), _c_(576346, _a_(576344, _n_(576343, "path", lambda: path), "join"), _n_(576345, "selected_folder", lambda: selected_folder), '*.bin'))
        _l_(576348)

        for bin_file in _n_(576349, "all_bin_files", lambda: all_bin_files):
            _l_(576363)

            _c_(576356, _a_(576354, _a_(576353, _a_(576352, _a_(576351, _n_(576350, "self", lambda: self), "frames_list"), "adapter"), "data"), "extend"), [_n_(576355, "bin_file", lambda: bin_file)])
            _l_(576357)
            _c_(576361, _a_(576360, _a_(576359, _n_(576358, "self", lambda: self), "frames_list"), "_trigger_reset_populate"))
            _l_(576362)


class BinsPlayerMain(_n_(576366, "GridLayout", lambda: GridLayout)):
    _l_(576368)

    pass
    _l_(576367)


class Bins_PlayerApp(_n_(576369, "App", lambda: App)):
    _l_(576380)

    def build(self):
        _l_(576379)

        _n_(576370, "Window", lambda: Window).clearcolor = (1, 1, 1, 1)
        _l_(576371)
        _n_(576372, "self", lambda: self).title = 'Bins Player'
        _l_(576373)
        _n_(576374, "self", lambda: self).icon = 'BinsPlayer.ico'
        _l_(576375)
        aux = _c_(576377, _n_(576376, "BinsPlayerMain", lambda: BinsPlayerMain))
        _l_(576378)
        return aux


if _n_(576381, "__name__", lambda: __name__) == "__main__":
    _l_(576387)

    _c_(576385, _a_(576384, _c_(576383, _n_(576382, "Bins_PlayerApp", lambda: Bins_PlayerApp)), "run"))
    _l_(576386)