# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74534074/typeerror-expected-str-bytes-or-os-pathlike-object-not-function-error-in-my-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Something:
    _l_(605483)

    def load_key(self):
        _l_(605475)

        filename = _a_(605464, _n_(605463, "self", lambda: self), "browse_files")
        _l_(605465)
        with _c_(605468, _n_(605466, "open", lambda: open), _n_(605467, "filename", lambda: filename), "rb") as f:
            _l_(605474)

            _n_(605469, "self", lambda: self).key = _c_(605472, _a_(605471, _n_(605470, "f", lambda: f), "read"))
            _l_(605473)

  
    def browse_files():
        _l_(605482)

        filename = _c_(605478, _a_(605477, _n_(605476, "filedialog", lambda: filedialog), "askopenfilename"), initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
        _l_(605479)
        aux = _n_(605480, "filename", lambda: filename)
        _l_(605481)
        return aux


class App(_a_(605485, _n_(605484, "customtkinter", lambda: customtkinter), "CTk")):
    _l_(605516)

    WIDTH = 780
    _l_(605486)
    HEIGHT = 520
    _l_(605487)

    def __init__(self):
        _l_(605515)

        _c_(605490, _a_(605489, _n_(605488, "super", lambda: super)(), "__init__"))
        _l_(605491)
        
        _c_(605494, _a_(605493, _n_(605492, "customtkinter", lambda: customtkinter), "set_appearance_mode"), "dark")
        _l_(605495)
        _c_(605498, _a_(605497, _n_(605496, "customtkinter", lambda: customtkinter), "set_default_color_theme"), "dark-blue")
        _l_(605499)
   
        _n_(605500, "self", lambda: self).button2 = _c_(605508, _a_(605502, _n_(605501, "customtkinter", lambda: customtkinter), "CTkButton"), master=_n_(605503, "self", lambda: self), text="Load a key",              command=_c_(605507, _a_(605505, _n_(605504, "Something", lambda: Something), "load_key"), _n_(605506, "Something", lambda: Something)), width=450, height=60)
        _l_(605509)
        _c_(605513, _a_(605512, _a_(605511, _n_(605510, "self", lambda: self), "button2"), "pack"), pady=10, padx=50)
        _l_(605514)


if _n_(605517, "__name__", lambda: __name__) == "__main__":
    _l_(605525)

    app = _c_(605519, _n_(605518, "App", lambda: App))
    _l_(605520)
    _c_(605523, _a_(605522, _n_(605521, "app", lambda: app), "mainloop"))
    _l_(605524)