# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58591221/kivy-attribute-error-object-has-no-attribute-trying-to-connect-widgets-in-kv
# keysigchooser.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.app import App
    _l_(379999)

except ImportError:
    pass
try:
    from kivy.properties import NumericProperty, ObjectProperty
    _l_(380001)

except ImportError:
    pass
try:
    from kivy.uix.floatlayout import FloatLayout
    _l_(380003)

except ImportError:
    pass
try:
    from kivy.uix.relativelayout import RelativeLayout
    _l_(380005)

except ImportError:
    pass

chrom_scale = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
_l_(380006)
chrom_scale2 = ['C', 'C/D', 'D', 'D/E', 'E', 'F', 'F/G', 'G', 'G/A', 'A', 'A/B', 'B']
_l_(380007)


class ModeChooser(_n_(380008, "FloatLayout", lambda: FloatLayout)):
    _l_(380010)

    pass
    _l_(380009)


class RootNoteChooser(_n_(380011, "FloatLayout", lambda: FloatLayout)):
    _l_(380032)

    note_idx = _c_(380013, _n_(380012, "NumericProperty", lambda: NumericProperty), 0)
    _l_(380014)

    def increment_note_idx(self):
        _l_(380019)

        _n_(380015, "self", lambda: self).note_idx = (_a_(380017, _n_(380016, "self", lambda: self), "note_idx") + 1) % 12
        _l_(380018)

    def decrement_note_idx(self):
        _l_(380024)

        _n_(380020, "self", lambda: self).note_idx = (_a_(380022, _n_(380021, "self", lambda: self), "note_idx") - 1) % 12
        _l_(380023)

    def on_note_idx(self, instance, value):
        _l_(380031)

        _a_(380026, _n_(380025, "self", lambda: self), "note_text").text = _n_(380027, "chrom_scale", lambda: chrom_scale)[_a_(380029, _n_(380028, "self", lambda: self), "note_idx")]
        _l_(380030)


class KeySigChooserContainer(_n_(380033, "FloatLayout", lambda: FloatLayout)):
    _l_(380065)

    def on_size(self, instance, value):
        _l_(380064)

        target_ratio = 60/20
        _l_(380034)
        width, height = _a_(380036, _n_(380035, "self", lambda: self), "size")
        _l_(380037)
        # check which size is the limiting factor
        if _n_(380038, "width", lambda: width) / _n_(380039, "height", lambda: height) > _n_(380040, "target_ratio", lambda: target_ratio):
            _l_(380063)

            # window is "wider" than targeted, so the limitation is the height.
            _a_(380043, _a_(380042, _n_(380041, "self", lambda: self), "ids"), "box").height = _n_(380044, "height", lambda: height)
            _l_(380045)
            _a_(380048, _a_(380047, _n_(380046, "self", lambda: self), "ids"), "box").width = _n_(380049, "height", lambda: height) * _n_(380050, "target_ratio", lambda: target_ratio)
            _l_(380051)
        else:
            _a_(380054, _a_(380053, _n_(380052, "self", lambda: self), "ids"), "box").width = _n_(380055, "width", lambda: width)
            _l_(380056)
            _a_(380059, _a_(380058, _n_(380057, "self", lambda: self), "ids"), "box").height = _n_(380060, "width", lambda: width) / _n_(380061, "target_ratio", lambda: target_ratio)
            _l_(380062)


class KeySigChooserApp(_n_(380066, "App", lambda: App)):
    _l_(380071)

    def build(self):
        _l_(380070)

        aux = _c_(380068, _n_(380067, "KeySigChooserContainer", lambda: KeySigChooserContainer))
        _l_(380069)
        return aux


if _n_(380072, "__name__", lambda: __name__) == "__main__":
    _l_(380078)

    _c_(380076, _a_(380075, _c_(380074, _n_(380073, "KeySigChooserApp", lambda: KeySigChooserApp)), "run"))
    _l_(380077)