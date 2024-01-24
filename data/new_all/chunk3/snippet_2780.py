# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63306805/kivy-android-attributeerror-nonetype-object-has-no-attribute-play
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(550836)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(550838)

except ImportError:
    pass
try:
    from kivy.uix.button import Label
    _l_(550840)

except ImportError:
    pass
try:
    from kivy.core.audio import SoundLoader
    _l_(550842)

except ImportError:
    pass

class HelloApp(_n_(550843, "App", lambda: App)):
    _l_(550858)

    def build(self):
        _l_(550857)

        _n_(550844, "self", lambda: self).sound = _c_(550847, _a_(550846, _n_(550845, "SoundLoader", lambda: SoundLoader), "load"), 'back.mp3') # open the background music
        _l_(550848) # open the background music
        _c_(550852, _a_(550851, _a_(550850, _n_(550849, "self", lambda: self), "sound"), "play")) # play the sound
        _l_(550853) # play the sound
        aux = _c_(550855, _n_(550854, "Label", lambda: Label), text='>>>>>')
        _l_(550856)
        return aux
if _n_(550859, "__name__", lambda: __name__)=="__main__":
    _l_(550865)

    _c_(550863, _a_(550862, _c_(550861, _n_(550860, "HelloApp", lambda: HelloApp)), "run"))
    _l_(550864)