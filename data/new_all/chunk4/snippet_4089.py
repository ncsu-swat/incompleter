# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62942634/attributeerror-nonetype-object-has-no-attribute-ids-in-kivy-when-clock-sche
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(607912)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(607914)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(607916)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(607918)

except ImportError:
    pass
try:
    from kivy.uix.widget import Widget
    _l_(607920)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(607922)

except ImportError:
    pass
try:
    from kivy.uix.image import Image
    _l_(607924)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(607926)

except ImportError:
    pass
try:
    from kivy.clock import Clock
    _l_(607928)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(607930)

except ImportError:
    pass
try:
    from kivy.core.audio import SoundLoader
    _l_(607932)

except ImportError:
    pass
try:
    from kivy.config import Config
    _l_(607934)

except ImportError:
    pass

# You can create your kv code in the Python file

# Create a class for all screens in which you can include
# helpful methods specific to that screen
kv = _c_(607937, _a_(607936, _n_(607935, "Builder", lambda: Builder), "load_file"), "main.kv")
_l_(607938)

class MainWindow(_n_(607939, "Screen", lambda: Screen)):
    _l_(608053)

    cloud_texture = _c_(607941, _n_(607940, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(607942)
    floor_texture = _c_(607944, _n_(607943, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(607945)
    sound = _c_(607947, _n_(607946, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(607948)

    def __init__(self, **kwargs):
        _l_(608009)

        _c_(607952, _a_(607950, _n_(607949, "super", lambda: super)(), "__init__"), **_n_(607951, "kwargs", lambda: kwargs))
        _l_(607953)
        _n_(607954, "self", lambda: self).cloud_texture = _a_(607957, _c_(607956, _n_(607955, "Image", lambda: Image), source = "cloud4.png"), "texture")
        _l_(607958)
        _a_(607960, _n_(607959, "self", lambda: self), "cloud_texture").wrap = 'repeat'
        _l_(607961)
        _a_(607963, _n_(607962, "self", lambda: self), "cloud_texture").uvsize = (_a_(607965, _n_(607964, "Window", lambda: Window), "width")/_a_(607968, _a_(607967, _n_(607966, "self", lambda: self), "cloud_texture"), "width"),-1)
        _l_(607969)
        _n_(607970, "self", lambda: self).floor_texture = _a_(607973, _c_(607972, _n_(607971, "Image", lambda: Image), source = "floor2.jpg"), "texture")
        _l_(607974)
        _a_(607976, _n_(607975, "self", lambda: self), "floor_texture").wrap = 'repeat'
        _l_(607977)
        _a_(607979, _n_(607978, "self", lambda: self), "floor_texture").uvsize = (_a_(607981, _n_(607980, "Window", lambda: Window), "width")/_a_(607984, _a_(607983, _n_(607982, "self", lambda: self), "floor_texture"), "width"),-1)
        _l_(607985)
        _n_(607986, "self", lambda: self).sun_texture = _a_(607989, _c_(607988, _n_(607987, "Image", lambda: Image), source = "sun.png"), "texture")
        _l_(607990)
        _a_(607992, _n_(607991, "self", lambda: self), "sun_texture").uvsize = (_a_(607994, _n_(607993, "Window", lambda: Window), "width")/_a_(607997, _a_(607996, _n_(607995, "self", lambda: self), "sun_texture"), "width"),-1)
        _l_(607998)
        _n_(607999, "self", lambda: self).sound = _c_(608002, _a_(608001, _n_(608000, "SoundLoader", lambda: SoundLoader), "load"), '8bitmenu.wav')
        _l_(608003)
        _c_(608007, _a_(608006, _a_(608005, _n_(608004, "self", lambda: self), "sound"), "play"))
        _l_(608008)

    def scroll_textures(self, time_passed):
        _l_(608052)

        #Update the uvpos
        _a_(608011, _n_(608010, "self", lambda: self), "cloud_texture").uvpos = ((_a_(608014, _a_(608013, _n_(608012, "self", lambda: self), "cloud_texture"), "uvpos")[0] - _n_(608015, "time_passed", lambda: time_passed)/20) % _a_(608017, _n_(608016, "Window", lambda: Window), "width"), _a_(608020, _a_(608019, _n_(608018, "self", lambda: self), "cloud_texture"), "uvpos")[1])
        _l_(608021)
        _a_(608023, _n_(608022, "self", lambda: self), "floor_texture").uvpos = ((_a_(608026, _a_(608025, _n_(608024, "self", lambda: self), "floor_texture"), "uvpos")[0] + _n_(608027, "time_passed", lambda: time_passed)/8) % _a_(608029, _n_(608028, "Window", lambda: Window), "width"), _a_(608032, _a_(608031, _n_(608030, "self", lambda: self), "floor_texture"), "uvpos")[1])
        _l_(608033)
        #Redraw textures
        texture = _c_(608036, _a_(608035, _n_(608034, "self", lambda: self), "property"), 'cloud_texture')
        _l_(608037)
        _c_(608041, _a_(608039, _n_(608038, "texture", lambda: texture), "dispatch"), _n_(608040, "self", lambda: self))
        _l_(608042)

        texture = _c_(608045, _a_(608044, _n_(608043, "self", lambda: self), "property"), 'floor_texture')
        _l_(608046)
        _c_(608050, _a_(608048, _n_(608047, "texture", lambda: texture), "dispatch"), _n_(608049, "self", lambda: self))
        _l_(608051)

class Window1(_n_(608054, "Screen", lambda: Screen)):
    _l_(608056)

    pass
    _l_(608055)

class WindowManager(_n_(608057, "ScreenManager", lambda: ScreenManager)):
    _l_(608059)

    pass
    _l_(608058)


#Config.write()
class MyApp(_n_(608060, "App", lambda: App)):
    _l_(608075)

    def on_start(self):
        _l_(608071)

        _c_(608068, _a_(608062, _n_(608061, "Clock", lambda: Clock), "schedule_interval"), _a_(608067, _a_(608066, _a_(608065, _a_(608064, _n_(608063, "self", lambda: self), "root"), "ids"), "mainwindow"), "scroll_textures"), 1/60.)
        _l_(608069)
        pass
        _l_(608070)
    def build(self):
        _l_(608074)

        aux = _n_(608072, "kv", lambda: kv)
        _l_(608073)
        return aux


_c_(608079, _a_(608078, _c_(608077, _n_(608076, "MyApp", lambda: MyApp)), "run"))
_l_(608080)