# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56938663/trouble-changing-text-of-kivy-textinput-widget-using-id-raises-error-attribut
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.app import App
    _l_(673974)

except ImportError:
    pass
try:
    from kivy.uix.tabbedpanel import TabbedPanel
    _l_(673976)

except ImportError:
    pass
try:
    import nibabel as nib
    _l_(673978)

except ImportError:
    pass
try:
    from kivy.garden.filebrowser import FileBrowser
    _l_(673980)

except ImportError:
    pass
try:
    from kivy.utils import platform
    _l_(673982)

except ImportError:
    pass
try:
    from kivy.uix.popup import Popup
    _l_(673984)

except ImportError:
    pass
try:
    from kivy.uix.textinput import TextInput
    _l_(673986)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(673988)

except ImportError:
    pass

_c_(673991, _a_(673990, _n_(673989, "Builder", lambda: Builder), "load_file"), "stack-test2.kv")
_l_(673992)

class Tabs(_n_(673993, "TabbedPanel", lambda: TabbedPanel)):
    _l_(674002)


    def nOpen(self):
        _l_(674001)

        npop = _c_(673995, _n_(673994, "niiPop", lambda: niiPop))
        _l_(673996)
        _c_(673999, _a_(673998, _n_(673997, "npop", lambda: npop), "open"))
        _l_(674000)

class niiPop(_n_(674003, "Popup", lambda: Popup)):
    _l_(674062)


    pathVariable = ' '
    _l_(674004)
    file = ' '
    _l_(674005)

    def nProcessor(self):
        _l_(674061)

        if _c_(674011, _n_(674006, "len", lambda: len), _a_(674010, _a_(674009, _a_(674008, _n_(674007, "self", lambda: self), "ids"), "nFile"), "selection")) == 1:
            _l_(674060)

            _n_(674012, "niiPop", lambda: niiPop).pathVariable = _c_(674018, _n_(674013, "str", lambda: str), _a_(674017, _a_(674016, _a_(674015, _n_(674014, "self", lambda: self), "ids"), "nFile"), "selection")[0])
            _l_(674019)
            _n_(674020, "niiPop", lambda: niiPop).file = _c_(674025, _a_(674022, _n_(674021, "nib", lambda: nib), "load"), _a_(674024, _n_(674023, "niiPop", lambda: niiPop), "pathVariable"))
            _l_(674026)
            displayHeader = _c_(674033, _n_(674027, "TextInput", lambda: TextInput), text = _c_(674032, _n_(674028, "str", lambda: str), _a_(674031, _a_(674030, _n_(674029, "niiPop", lambda: niiPop), "file"), "header")), readonly = True)
            _l_(674034)
            _c_(674039, _a_(674038, _a_(674037, _a_(674036, _n_(674035, "self", lambda: self), "ids"), "nFile"), "clear_widgets"))
            _l_(674040)
            _c_(674046, _a_(674044, _a_(674043, _a_(674042, _n_(674041, "self", lambda: self), "ids"), "nFile"), "add_widget"), _n_(674045, "displayHeader", lambda: displayHeader))
            _l_(674047)
            _n_(674048, "niiPop", lambda: niiPop).auto_dismiss = True
            _l_(674049)
            _a_(674052, _a_(674051, _n_(674050, "self", lambda: self), "ids"), "fld1").text = _a_(674054, _n_(674053, "niiPop", lambda: niiPop), "pathVariable")
            _l_(674055)
        else:
            _a_(674058, _a_(674057, _n_(674056, "self", lambda: self), "ids"), "nFile").filename = ''
            _l_(674059)

class stackTest1(_n_(674063, "App", lambda: App)):
    _l_(674070)

    def build(self):
        _l_(674069)

        _n_(674064, "self", lambda: self).title = 'Test app'
        _l_(674065)
        aux = _c_(674067, _n_(674066, "Tabs", lambda: Tabs))
        _l_(674068)
        return aux

if _n_(674071, "__name__", lambda: __name__) == "__main__":
    _l_(674079)

    app = _c_(674073, _n_(674072, "stackTest1", lambda: stackTest1))
    _l_(674074)
    _c_(674077, _a_(674076, _n_(674075, "app", lambda: app), "run"))
    _l_(674078)