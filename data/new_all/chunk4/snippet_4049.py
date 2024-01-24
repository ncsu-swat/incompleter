# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63642052/kivy-typeerror-nonetype-object-is-not-callable-for-mainapp-run
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.app import App
    _l_(620164)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(620166)

except ImportError:
    pass

GUI = _c_(620169, _a_(620168, _n_(620167, "Builder", lambda: Builder), "load_file"), 'main.kv')
_l_(620170)


class DigitalLove(_n_(620171, "App", lambda: App)):
    _l_(620179)

    @_n_(620172, "property", lambda: property)
    def build(self):
        _l_(620178)

        aux = _n_(620173, "GUI", lambda: GUI)
        _l_(620174)

        return aux

        monika_art = 'images/monika.png'
        _l_(620175)
        textbox_img = 'images/textbox.png'
        _l_(620176)

        doki_response = 'example text'
        _l_(620177)


if _n_(620180, "__name__", lambda: __name__) == "__main__":
    _l_(620186)

    _c_(620184, _a_(620183, _c_(620182, _n_(620181, "DigitalLove", lambda: DigitalLove)), "run"))
    _l_(620185)