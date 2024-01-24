# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67339079/attributeerror-function-object-has-no-attribute-insert-while-writting-tkint
#So after clicking for ex. button with "5" fucnction has to write 5 on calc

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(584087)

except ImportError:
    pass

symbols=["7", "8", "9", "/", "\u21BA","4", "5", "6", "*", "C", "1", "2", "3", "-", "x^2", "0", "+", "\u221A"]
_l_(584088)

def window():
    _l_(584107)

    root=_c_(584091, _a_(584090, _n_(584089, "tk", lambda: tk), "Tk"))
    _l_(584092)

    _c_(584095, _a_(584094, _n_(584093, "root", lambda: root), "configure"), bg="light gray")
    _l_(584096)

    _c_(584099, _a_(584098, _n_(584097, "root", lambda: root), "geometry"), '460x430')
    _l_(584100)

    _c_(584103, _a_(584102, _n_(584101, "root", lambda: root), "title"), "Kalkurator ONP")
    _l_(584104)
    aux = _n_(584105, "root", lambda: root)
    _l_(584106)

    return aux

def screen(root):
    _l_(584129)


    screen=[_c_(584111, _a_(584109, _n_(584108, "tk", lambda: tk), "Label"), _n_(584110, "root", lambda: root), width=65, anchor="w", borderwidth=2, bg='#C0CBCB') for i in _c_(584113, _n_(584112, "range", lambda: range), 3)]
    _l_(584114)

    for i in _c_(584119, _n_(584115, "range", lambda: range), _c_(584118, _n_(584116, "len", lambda: len), _n_(584117, "screen", lambda: screen))):
        _l_(584126)


        #ipadx and ipady are margins
        _c_(584124, _a_(584122, _n_(584120, "screen", lambda: screen)[_n_(584121, "i", lambda: i)], "grid"), row=_n_(584123, "i", lambda: i), columnspan=5, ipady=15, ipadx=1)
        _l_(584125)
    aux = _n_(584127, "screen", lambda: screen)
    _l_(584128)

    return aux

def dataLabel(root, screen):
    _l_(584157)

    label_for_data=_c_(584133, _a_(584131, _n_(584130, "tk", lambda: tk), "Entry"), _n_(584132, "root", lambda: root), borderwidth=0, highlightcolor="white", highlightbackground="white")
    _l_(584134)
    _c_(584140, _a_(584136, _n_(584135, "label_for_data", lambda: label_for_data), "grid"), row=_c_(584139, _n_(584137, "len", lambda: len), _n_(584138, "screen", lambda: screen)), columnspan=5, ipadx=160, ipady=10)
    _l_(584141)

    info=_c_(584145, _a_(584143, _n_(584142, "tk", lambda: tk), "Label"), _n_(584144, "root", lambda: root), width=65, anchor="w", borderwidth=2, bg='white')
    _l_(584146)
    _c_(584152, _a_(584148, _n_(584147, "info", lambda: info), "grid"), row=_c_(584151, _n_(584149, "len", lambda: len), _n_(584150, "screen", lambda: screen))+1, columnspan=5, ipady=15, ipadx=1)
    _l_(584153)
    aux = _n_(584154, "label_for_data", lambda: label_for_data), _n_(584155, "info", lambda: info)
    _l_(584156)

    return aux

def afterClickingBtn(lfd, symbol):
    _l_(584168)

    def f():
        _l_(584165)

        _c_(584163, _a_(584159, _n_(584158, "lfd", lambda: lfd), "insert"), _a_(584161, _n_(584160, "tk", lambda: tk), "END"), _n_(584162, "symbol", lambda: symbol))#Here is the problem
        _l_(584164)#Here is the problem
    aux = _n_(584166, "f", lambda: f)
    _l_(584167)
    return aux

def buttons(root, screen):
    _l_(584221)


    j=_c_(584171, _n_(584169, "len", lambda: len), _n_(584170, "screen", lambda: screen))+2
    _l_(584172)

    button=[_c_(584177, _a_(584174, _n_(584173, "tk", lambda: tk), "Button"), _n_(584175, "root", lambda: root), text=_n_(584176, "symbol", lambda: symbol), bg="light gray", borderwidth=0) for symbol in _n_(584178, "symbols", lambda: symbols)]
    _l_(584179)
    for i in _c_(584184, _n_(584180, "range", lambda: range), _c_(584183, _n_(584181, "len", lambda: len), _n_(584182, "symbols", lambda: symbols))):
        _l_(584205)

        if _n_(584185, "i", lambda: i)%5==0:
            _l_(584187)

            j+=1
            _l_(584186)
        _c_(584193, _a_(584190, _n_(584188, "button", lambda: button)[_n_(584189, "i", lambda: i)], "grid"), row=_n_(584191, "j", lambda: j), column=_n_(584192, "i", lambda: i)%5, ipadx=15, ipady=10)
        _l_(584194)
        _c_(584203, _a_(584197, _n_(584195, "button", lambda: button)[_n_(584196, "i", lambda: i)], "configure"), command=_c_(584202, _n_(584198, "afterClickingBtn", lambda: afterClickingBtn), _n_(584199, "dataLabel", lambda: dataLabel), _n_(584200, "button", lambda: button)[_n_(584201, "i", lambda: i)]["text"]))
        _l_(584204)

    equal_button=_c_(584209, _a_(584207, _n_(584206, "tk", lambda: tk), "Button"), _n_(584208, "root", lambda: root), text="=", bg="green", borderwidth=0)
    _l_(584210)
    _c_(584216, _a_(584212, _n_(584211, "equal_button", lambda: equal_button), "grid"), row=_c_(584215, _n_(584213, "len", lambda: len), _n_(584214, "screen", lambda: screen))+6, column=3, columnspan=2, ipadx=60, ipady=10)
    _l_(584217)
    aux = _n_(584218, "button", lambda: button), _n_(584219, "equal_button", lambda: equal_button)
    _l_(584220)

    return aux

def main():
    _l_(584243)

    root=_c_(584223, _n_(584222, "window", lambda: window))
    _l_(584224)

    sc=_c_(584227, _n_(584225, "screen", lambda: screen), _n_(584226, "root", lambda: root))
    _l_(584228)

    lfd=_c_(584232, _n_(584229, "dataLabel", lambda: dataLabel), _n_(584230, "root", lambda: root), _n_(584231, "sc", lambda: sc))
    _l_(584233)
    
    btn=_c_(584237, _n_(584234, "buttons", lambda: buttons), _n_(584235, "root", lambda: root), _n_(584236, "sc", lambda: sc))
    _l_(584238)

    #End of loop
    _c_(584241, _a_(584240, _n_(584239, "root", lambda: root), "mainloop"))
    _l_(584242)

if _n_(584244, "__name__", lambda: __name__)=="__main__":
    _l_(584248)

    _c_(584246, _n_(584245, "main", lambda: main))
    _l_(584247)