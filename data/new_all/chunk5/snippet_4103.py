# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62942634/attributeerror-nonetype-object-has-no-attribute-ids-in-kivy-when-clock-sche
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(701721)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(701723)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(701725)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(701727)

except ImportError:
    pass
try:
    from kivy.uix.widget import Widget
    _l_(701729)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(701731)

except ImportError:
    pass
try:
    from kivy.uix.image import Image
    _l_(701733)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(701735)

except ImportError:
    pass
try:
    from kivy.clock import Clock
    _l_(701737)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(701739)

except ImportError:
    pass
try:
    from kivy.core.audio import SoundLoader
    _l_(701741)

except ImportError:
    pass
try:
    from kivy.config import Config
    _l_(701743)

except ImportError:
    pass

# You can create your kv code in the Python file

# Create a class for all screens in which you can include
# helpful methods specific to that screen
kv = _c_(701746, _a_(701745, _n_(701744, "Builder", lambda: Builder), "load_file"), "main.kv")
_l_(701747)

class MainWindow(_n_(701748, "Screen", lambda: Screen)):
    _l_(701862)

    cloud_texture = _c_(701750, _n_(701749, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(701751)
    floor_texture = _c_(701753, _n_(701752, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(701754)
    sound = _c_(701756, _n_(701755, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(701757)

    def __init__(self, **kwargs):
        _l_(701818)

        _c_(701761, _a_(701759, _n_(701758, "super", lambda: super)(), "__init__"), **_n_(701760, "kwargs", lambda: kwargs))
        _l_(701762)
        _n_(701763, "self", lambda: self).cloud_texture = _a_(701766, _c_(701765, _n_(701764, "Image", lambda: Image), source = "cloud4.png"), "texture")
        _l_(701767)
        _a_(701769, _n_(701768, "self", lambda: self), "cloud_texture").wrap = 'repeat'
        _l_(701770)
        _a_(701772, _n_(701771, "self", lambda: self), "cloud_texture").uvsize = (_a_(701774, _n_(701773, "Window", lambda: Window), "width")/_a_(701777, _a_(701776, _n_(701775, "self", lambda: self), "cloud_texture"), "width"),-1)
        _l_(701778)
        _n_(701779, "self", lambda: self).floor_texture = _a_(701782, _c_(701781, _n_(701780, "Image", lambda: Image), source = "floor2.jpg"), "texture")
        _l_(701783)
        _a_(701785, _n_(701784, "self", lambda: self), "floor_texture").wrap = 'repeat'
        _l_(701786)
        _a_(701788, _n_(701787, "self", lambda: self), "floor_texture").uvsize = (_a_(701790, _n_(701789, "Window", lambda: Window), "width")/_a_(701793, _a_(701792, _n_(701791, "self", lambda: self), "floor_texture"), "width"),-1)
        _l_(701794)
        _n_(701795, "self", lambda: self).sun_texture = _a_(701798, _c_(701797, _n_(701796, "Image", lambda: Image), source = "sun.png"), "texture")
        _l_(701799)
        _a_(701801, _n_(701800, "self", lambda: self), "sun_texture").uvsize = (_a_(701803, _n_(701802, "Window", lambda: Window), "width")/_a_(701806, _a_(701805, _n_(701804, "self", lambda: self), "sun_texture"), "width"),-1)
        _l_(701807)
        _n_(701808, "self", lambda: self).sound = _c_(701811, _a_(701810, _n_(701809, "SoundLoader", lambda: SoundLoader), "load"), '8bitmenu.wav')
        _l_(701812)
        _c_(701816, _a_(701815, _a_(701814, _n_(701813, "self", lambda: self), "sound"), "play"))
        _l_(701817)

    def scroll_textures(self, time_passed):
        _l_(701861)

        #Update the uvpos
        _a_(701820, _n_(701819, "self", lambda: self), "cloud_texture").uvpos = ((_a_(701823, _a_(701822, _n_(701821, "self", lambda: self), "cloud_texture"), "uvpos")[0] - _n_(701824, "time_passed", lambda: time_passed)/20) % _a_(701826, _n_(701825, "Window", lambda: Window), "width"), _a_(701829, _a_(701828, _n_(701827, "self", lambda: self), "cloud_texture"), "uvpos")[1])
        _l_(701830)
        _a_(701832, _n_(701831, "self", lambda: self), "floor_texture").uvpos = ((_a_(701835, _a_(701834, _n_(701833, "self", lambda: self), "floor_texture"), "uvpos")[0] + _n_(701836, "time_passed", lambda: time_passed)/8) % _a_(701838, _n_(701837, "Window", lambda: Window), "width"), _a_(701841, _a_(701840, _n_(701839, "self", lambda: self), "floor_texture"), "uvpos")[1])
        _l_(701842)
        #Redraw textures
        texture = _c_(701845, _a_(701844, _n_(701843, "self", lambda: self), "property"), 'cloud_texture')
        _l_(701846)
        _c_(701850, _a_(701848, _n_(701847, "texture", lambda: texture), "dispatch"), _n_(701849, "self", lambda: self))
        _l_(701851)

        texture = _c_(701854, _a_(701853, _n_(701852, "self", lambda: self), "property"), 'floor_texture')
        _l_(701855)
        _c_(701859, _a_(701857, _n_(701856, "texture", lambda: texture), "dispatch"), _n_(701858, "self", lambda: self))
        _l_(701860)

class Window1(_n_(701863, "Screen", lambda: Screen)):
    _l_(701865)

    pass
    _l_(701864)

class WindowManager(_n_(701866, "ScreenManager", lambda: ScreenManager)):
    _l_(701868)

    pass
    _l_(701867)


#Config.write()
class MyApp(_n_(701869, "App", lambda: App)):
    _l_(701884)

    def on_start(self):
        _l_(701880)

        _c_(701877, _a_(701871, _n_(701870, "Clock", lambda: Clock), "schedule_interval"), _a_(701876, _a_(701875, _a_(701874, _a_(701873, _n_(701872, "self", lambda: self), "root"), "ids"), "mainwindow"), "scroll_textures"), 1/60.)
        _l_(701878)
        pass
        _l_(701879)
    def build(self):
        _l_(701883)

        aux = _n_(701881, "kv", lambda: kv)
        _l_(701882)
        return aux


_c_(701888, _a_(701887, _c_(701886, _n_(701885, "MyApp", lambda: MyApp)), "run"))
_l_(701889)