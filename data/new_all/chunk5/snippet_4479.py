# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56938663/trouble-changing-text-of-kivy-textinput-widget-using-id-raises-error-attribut
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.app import App
    _l_(649708)

except ImportError:
    pass
try:
    from kivy.uix.tabbedpanel import TabbedPanel
    _l_(649710)

except ImportError:
    pass
try:
    import nibabel as nib
    _l_(649712)

except ImportError:
    pass
try:
    from kivy.garden.filebrowser import FileBrowser
    _l_(649714)

except ImportError:
    pass
try:
    from kivy.utils import platform
    _l_(649716)

except ImportError:
    pass
try:
    from kivy.uix.popup import Popup
    _l_(649718)

except ImportError:
    pass
try:
    from kivy.uix.textinput import TextInput
    _l_(649720)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(649722)

except ImportError:
    pass

_c_(649725, _a_(649724, _n_(649723, "Builder", lambda: Builder), "load_file"), "stack-test2.kv")
_l_(649726)

class Tabs(_n_(649727, "TabbedPanel", lambda: TabbedPanel)):
    _l_(649736)


    def nOpen(self):
        _l_(649735)

        npop = _c_(649729, _n_(649728, "niiPop", lambda: niiPop))
        _l_(649730)
        _c_(649733, _a_(649732, _n_(649731, "npop", lambda: npop), "open"))
        _l_(649734)

class niiPop(_n_(649737, "Popup", lambda: Popup)):
    _l_(649796)


    pathVariable = ' '
    _l_(649738)
    file = ' '
    _l_(649739)

    def nProcessor(self):
        _l_(649795)

        if _c_(649745, _n_(649740, "len", lambda: len), _a_(649744, _a_(649743, _a_(649742, _n_(649741, "self", lambda: self), "ids"), "nFile"), "selection")) == 1:
            _l_(649794)

            _n_(649746, "niiPop", lambda: niiPop).pathVariable = _c_(649752, _n_(649747, "str", lambda: str), _a_(649751, _a_(649750, _a_(649749, _n_(649748, "self", lambda: self), "ids"), "nFile"), "selection")[0])
            _l_(649753)
            _n_(649754, "niiPop", lambda: niiPop).file = _c_(649759, _a_(649756, _n_(649755, "nib", lambda: nib), "load"), _a_(649758, _n_(649757, "niiPop", lambda: niiPop), "pathVariable"))
            _l_(649760)
            displayHeader = _c_(649767, _n_(649761, "TextInput", lambda: TextInput), text = _c_(649766, _n_(649762, "str", lambda: str), _a_(649765, _a_(649764, _n_(649763, "niiPop", lambda: niiPop), "file"), "header")), readonly = True)
            _l_(649768)
            _c_(649773, _a_(649772, _a_(649771, _a_(649770, _n_(649769, "self", lambda: self), "ids"), "nFile"), "clear_widgets"))
            _l_(649774)
            _c_(649780, _a_(649778, _a_(649777, _a_(649776, _n_(649775, "self", lambda: self), "ids"), "nFile"), "add_widget"), _n_(649779, "displayHeader", lambda: displayHeader))
            _l_(649781)
            _n_(649782, "niiPop", lambda: niiPop).auto_dismiss = True
            _l_(649783)
            _a_(649786, _a_(649785, _n_(649784, "self", lambda: self), "ids"), "fld1").text = _a_(649788, _n_(649787, "niiPop", lambda: niiPop), "pathVariable")
            _l_(649789)
        else:
            _a_(649792, _a_(649791, _n_(649790, "self", lambda: self), "ids"), "nFile").filename = ''
            _l_(649793)

class stackTest1(_n_(649797, "App", lambda: App)):
    _l_(649804)

    def build(self):
        _l_(649803)

        _n_(649798, "self", lambda: self).title = 'Test app'
        _l_(649799)
        aux = _c_(649801, _n_(649800, "Tabs", lambda: Tabs))
        _l_(649802)
        return aux

if _n_(649805, "__name__", lambda: __name__) == "__main__":
    _l_(649813)

    app = _c_(649807, _n_(649806, "stackTest1", lambda: stackTest1))
    _l_(649808)
    _c_(649811, _a_(649810, _n_(649809, "app", lambda: app), "run"))
    _l_(649812)