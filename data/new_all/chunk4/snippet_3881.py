# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66010232/how-to-resolve-typeerror-expected-str-bytes-or-os-pathlike-object-not-io-buf
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
root = _c_(580179, _n_(580178, "Tk", lambda: Tk))
_l_(580180)
def open_f():
    _l_(580189)

    global file
    _l_(580181)
    file = _c_(580183, _n_(580182, "askopenfile", lambda: askopenfile), mode ='rb', filetypes =[('All Files','*.*'),
                  ('pdf files', '*.pdf'),('txt Files','*.txt')])
    _l_(580184)
    _c_(580187, _n_(580185, "print", lambda: print), 'Selected:', _n_(580186, "file", lambda: file))
    _l_(580188)
button1 = _c_(580193, _n_(580190, "Button", lambda: Button), _n_(580191, "root", lambda: root), text ="Select text file",command=_n_(580192, "open_f", lambda: open_f))
_l_(580194)
_c_(580197, _a_(580196, _n_(580195, "button1", lambda: button1), "grid"), row=9,column=1,pady=5)
_l_(580198)
l1=[] 
_l_(580199) 
TextFile = _n_(580200, "file", lambda: file)
_l_(580201)
# open the file for data processing
with _c_(580204, _n_(580202, "open", lambda: open), _n_(580203, "TextFile", lambda: TextFile),encoding="utf8") as IpFile:
    _l_(580216)

    for j in _n_(580205, "IpFile", lambda: IpFile):
        _l_(580215)

        _c_(580213, _a_(580207, _n_(580206, "l1", lambda: l1), "append"), _c_(580212, _a_(580211, _c_(580210, _n_(580208, "str", lambda: str), _n_(580209, "j", lambda: j)), "strip")))   
        _l_(580214)   
_c_(580219, _a_(580218, _n_(580217, "root", lambda: root), "mainloop"))
_l_(580220)