# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56453398/attributeerror-stringvar-object-has-no-attribute-tk
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(532091)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(532093)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(532095)

except ImportError:
    pass

class loginUser:
    _l_(532229)

    def __init__(self, window, master=None):
        _l_(532160)

        _n_(532096, "self", lambda: self).wind = _n_(532097, "window", lambda: window)
        _l_(532098)
        _c_(532102, _a_(532101, _a_(532100, _n_(532099, "self", lambda: self), "wind"), "title"), "System F2T")
        _l_(532103)

        #Definicoes de fonte p/ o layout de login
        _n_(532104, "self", lambda: self).fonteTitulo = ("Arial","10","bold")
        _l_(532105)
        _n_(532106, "self", lambda: self).fontePadrao = ("Arial", "10")
        _l_(532107)

        _n_(532108, "self", lambda: self).var = _c_(532111, _a_(532110, _n_(532109, "tk", lambda: tk), "StringVar"))
        _l_(532112)
        _n_(532113, "self", lambda: self).var2 = _c_(532116, _a_(532115, _n_(532114, "tk", lambda: tk), "StringVar"))
        _l_(532117)

        _n_(532118, "self", lambda: self).userLabel = _c_(532124, _a_(532123, _c_(532122, _n_(532119, "Label", lambda: Label), text="Digite seu usuário:", font=_a_(532121, _n_(532120, "self", lambda: self), "fontePadrao"),bg="#000",fg="#FFF"), "place"), x=27,y=60)
        _l_(532125)
        _n_(532126, "self", lambda: self).user = _c_(532132, _n_(532127, "Entry", lambda: Entry), textvariable=_a_(532129, _n_(532128, "self", lambda: self), "var"), font=_a_(532131, _n_(532130, "self", lambda: self), "fontePadrao"),bg="#FFF",fg="#000")
        _l_(532133)
        _c_(532137, _a_(532136, _a_(532135, _n_(532134, "self", lambda: self), "user"), "place"), x=140,y=60,width=110)
        _l_(532138)

        _n_(532139, "self", lambda: self).senhaLabel = _c_(532145, _a_(532144, _c_(532143, _n_(532140, "Label", lambda: Label), text="Digite sua senha:", font=_a_(532142, _n_(532141, "self", lambda: self), "fontePadrao"),bg="#000",fg="#FFF"), "place"), x=29,y=90)
        _l_(532146)
        _n_(532147, "self", lambda: self).senha = _c_(532153, _n_(532148, "Entry", lambda: Entry), _a_(532150, _n_(532149, "self", lambda: self), "var2"), font=_a_(532152, _n_(532151, "self", lambda: self), "fontePadrao"),show="*",bg="#FFF",fg="#000")
        _l_(532154)
        _c_(532158, _a_(532157, _a_(532156, _n_(532155, "self", lambda: self), "senha"), "place"), x=140,y=90,width=110)
        _l_(532159)

    def limiteUsuario(self,*args):
        _l_(532200)

        u = _c_(532164, _a_(532163, _a_(532162, _n_(532161, "self", lambda: self), "var"), "get"))
        _l_(532165)
        if _c_(532168, _n_(532166, "len", lambda: len), _n_(532167, "u", lambda: u)) == 1 and not 65<=_c_(532171, _n_(532169, "ord", lambda: ord), _n_(532170, "u", lambda: u))<=68:
            _l_(532199)

            _c_(532175, _a_(532174, _a_(532173, _n_(532172, "self", lambda: self), "var"), "set"), "")
            _l_(532176)
        elif _c_(532179, _n_(532177, "len", lambda: len), _n_(532178, "u", lambda: u)) > 1:
            _l_(532198)

            if not 65<=_c_(532182, _n_(532180, "ord", lambda: ord), _n_(532181, "u", lambda: u)[-1])<=68:
                _l_(532197)

                _c_(532187, _a_(532185, _a_(532184, _n_(532183, "self", lambda: self), "var"), "set"), _n_(532186, "u", lambda: u)[:-1])
                _l_(532188)
            else: # aproveitar apenas os primeiros 5 chars
                _c_(532195, _a_(532191, _a_(532190, _n_(532189, "self", lambda: self), "var"), "set"), _n_(532192, "u", lambda: u)[:_a_(532194, _n_(532193, "self", lambda: self), "max_user")])
                _l_(532196)

    def limiteSenha(self,*args):
        _l_(532228)

        s = _c_(532204, _a_(532203, _a_(532202, _n_(532201, "self", lambda: self), "var2"), "get"))
        _l_(532205)
        if _c_(532208, _n_(532206, "len", lambda: len), _n_(532207, "s", lambda: s)) > 4:
            _l_(532227)

            if not _c_(532211, _a_(532210, _n_(532209, "s", lambda: s)[-1], "isdigit")):
                _l_(532226)

                _c_(532216, _a_(532214, _a_(532213, _n_(532212, "self", lambda: self), "var2"), "set"), _n_(532215, "s", lambda: s)[:-1])
                _l_(532217)
            else: # aproveitar apenas os primeiros 5 chars
                _c_(532224, _a_(532220, _a_(532219, _n_(532218, "self", lambda: self), "var2"), "set"), _n_(532221, "s", lambda: s)[:_a_(532223, _n_(532222, "self", lambda: self), "max_senha")])
                _l_(532225)

if _n_(532230, "__name__", lambda: __name__) == "__main__":
    _l_(532248)

    root = _c_(532232, _n_(532231, "Tk", lambda: Tk))
    _l_(532233)
    _n_(532234, "root", lambda: root)['bg'] = "#000"
    _l_(532235)
    _c_(532238, _n_(532236, "loginUser", lambda: loginUser), _n_(532237, "root", lambda: root))
    _l_(532239)
    #Tamanho da janela
    _c_(532242, _a_(532241, _n_(532240, "root", lambda: root), "geometry"), "330x200")
    _l_(532243)
    _c_(532246, _a_(532245, _n_(532244, "root", lambda: root), "mainloop"))
    _l_(532247)