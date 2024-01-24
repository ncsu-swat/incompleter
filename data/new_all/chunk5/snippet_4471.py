# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57064929/typeerror-ord-expected-a-character-but-string-of-length-5-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(679094)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(679096)

except ImportError:
    pass

class loginUser:
    _l_(679278)

    def __init__(self, window, master=None):
        _l_(679177)

        _n_(679097, "self", lambda: self).wind = _n_(679098, "window", lambda: window)
        _l_(679099)
        _c_(679103, _a_(679102, _a_(679101, _n_(679100, "self", lambda: self), "wind"), "title"), "System F2T")
        _l_(679104)

        #Definicoes de fonte p/ o layout de login
        _n_(679105, "self", lambda: self).fonteTitulo = ("Arial","10","bold")
        _l_(679106)
        _n_(679107, "self", lambda: self).fontePadrao = ("Arial", "10")
        _l_(679108)

        _n_(679109, "self", lambda: self).var = _c_(679111, _n_(679110, "StringVar", lambda: StringVar)) #create the var first before you assign them
        _l_(679112) #create the var first before you assign them
        _n_(679113, "self", lambda: self).var2 = _c_(679115, _n_(679114, "StringVar", lambda: StringVar))
        _l_(679116)

        #Labels e campos de texto do sistema de login
        _n_(679117, "self", lambda: self).userLabel = _c_(679123, _a_(679122, _c_(679121, _n_(679118, "Label", lambda: Label), text="Digite seu usuário:", font=_a_(679120, _n_(679119, "self", lambda: self), "fontePadrao"),bg="#000",fg="#FFF"), "place"), x=27,y=60)
        _l_(679124)
        _n_(679125, "self", lambda: self).user = _c_(679131, _n_(679126, "Entry", lambda: Entry), textvariable=_a_(679128, _n_(679127, "self", lambda: self), "var"), font=_a_(679130, _n_(679129, "self", lambda: self), "fontePadrao"),bg="#FFF",fg="#000")
        _l_(679132)
        _c_(679136, _a_(679135, _a_(679134, _n_(679133, "self", lambda: self), "user"), "place"), x=140,y=60,width=110)
        _l_(679137)

        _n_(679138, "self", lambda: self).senhaLabel = _c_(679144, _a_(679143, _c_(679142, _n_(679139, "Label", lambda: Label), text="Digite sua senha:", font=_a_(679141, _n_(679140, "self", lambda: self), "fontePadrao"),bg="#000",fg="#FFF"), "place"), x=29,y=90)
        _l_(679145)
        _n_(679146, "self", lambda: self).senha = _c_(679152, _n_(679147, "Entry", lambda: Entry), textvariable=_a_(679149, _n_(679148, "self", lambda: self), "var2"), font=_a_(679151, _n_(679150, "self", lambda: self), "fontePadrao"),bg="#FFF",fg="#000")
        _l_(679153)
        _c_(679157, _a_(679156, _a_(679155, _n_(679154, "self", lambda: self), "senha"), "place"), x=140,y=90,width=110)
        _l_(679158)

        _n_(679159, "self", lambda: self).max_user = 1
        _l_(679160)
        _c_(679166, _a_(679163, _a_(679162, _n_(679161, "self", lambda: self), "var"), "trace"), "w", _a_(679165, _n_(679164, "self", lambda: self), "limiteUsuario"))
        _l_(679167)
        _n_(679168, "self", lambda: self).max_senha = 4
        _l_(679169)
        _c_(679175, _a_(679172, _a_(679171, _n_(679170, "self", lambda: self), "var2"), "trace"), "w", _a_(679174, _n_(679173, "self", lambda: self), "limiteSenha"))
        _l_(679176)

    def limiteUsuario(self,*args):
        _l_(679220)

        u = _c_(679181, _a_(679180, _a_(679179, _n_(679178, "self", lambda: self), "var"), "get"))
        _l_(679182)
        if _c_(679185, _n_(679183, "len", lambda: len), _n_(679184, "u", lambda: u)) == 1 and not 65<=_c_(679188, _n_(679186, "ord", lambda: ord), _n_(679187, "u", lambda: u))<=68 and not 48<=_c_(679191, _n_(679189, "ord", lambda: ord), _n_(679190, "u", lambda: u))<=57:
            _l_(679219)

            _c_(679195, _a_(679194, _a_(679193, _n_(679192, "self", lambda: self), "var"), "set"), "")
            _l_(679196)
        elif _c_(679199, _n_(679197, "len", lambda: len), _n_(679198, "u", lambda: u)) > 1:
            _l_(679218)

            if not 65<=_c_(679202, _n_(679200, "ord", lambda: ord), _n_(679201, "u", lambda: u)[-1])<=68:
                _l_(679217)

                _c_(679207, _a_(679205, _a_(679204, _n_(679203, "self", lambda: self), "var"), "set"), _n_(679206, "u", lambda: u)[:-1])
                _l_(679208)
            else: # aproveitar apenas os primeiros 5 chars
                _c_(679215, _a_(679211, _a_(679210, _n_(679209, "self", lambda: self), "var"), "set"), _n_(679212, "u", lambda: u)[:_a_(679214, _n_(679213, "self", lambda: self), "max_user")])
                _l_(679216)

    def limiteSenha(self,*args):
        _l_(679277)

        text = _c_(679224, _a_(679223, _a_(679222, _n_(679221, "self", lambda: self), "var2"), "get"))
        _l_(679225)
        text = _c_(679230, _a_(679226, '', "join"), (_n_(679227, "char", lambda: char) for char in _n_(679228, "text", lambda: text) if _n_(679229, "char", lambda: char) in 'ABCD'))
        _l_(679231)
        if _c_(679234, _n_(679232, "len", lambda: len), _n_(679233, "text", lambda: text)) == 4 and not 65<=_c_(679237, _n_(679235, "ord", lambda: ord), _n_(679236, "text", lambda: text))<=68 and not 48<=_c_(679240, _n_(679238, "ord", lambda: ord), _n_(679239, "text", lambda: text))<=57:
            _l_(679268)

            _c_(679244, _a_(679243, _a_(679242, _n_(679241, "self", lambda: self), "var2"), "set"), "")
            _l_(679245)
        elif _c_(679248, _n_(679246, "len", lambda: len), _n_(679247, "text", lambda: text)) > 4:
            _l_(679267)

            if not 65<=_c_(679251, _n_(679249, "ord", lambda: ord), _n_(679250, "text", lambda: text)[-1])<=68:
                _l_(679266)

                _c_(679256, _a_(679254, _a_(679253, _n_(679252, "self", lambda: self), "var2"), "set"), _n_(679255, "text", lambda: text)[:-1])
                _l_(679257)
            else: # aproveitar apenas os primeiros 5 chars
                _c_(679264, _a_(679260, _a_(679259, _n_(679258, "self", lambda: self), "var2"), "set"), _n_(679261, "text", lambda: text)[:_a_(679263, _n_(679262, "self", lambda: self), "max_senha")])
                _l_(679265)
        _c_(679275, _n_(679269, "print", lambda: print), _c_(679274, _a_(679272, _a_(679271, _n_(679270, "self", lambda: self), "var2"), "set"), _n_(679273, "text", lambda: text)))
        _l_(679276)

if _n_(679279, "__name__", lambda: __name__) == "__main__":
    _l_(679297)

    root = _c_(679281, _n_(679280, "Tk", lambda: Tk))
    _l_(679282)
    _n_(679283, "root", lambda: root)['bg'] = "#000"
    _l_(679284)
    _c_(679287, _n_(679285, "loginUser", lambda: loginUser), _n_(679286, "root", lambda: root))
    _l_(679288)
    #Tamanho da janela
    _c_(679291, _a_(679290, _n_(679289, "root", lambda: root), "geometry"), "330x200")
    _l_(679292)
    _c_(679295, _a_(679294, _n_(679293, "root", lambda: root), "mainloop"))
    _l_(679296)