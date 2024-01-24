# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66010232/how-to-resolve-typeerror-expected-str-bytes-or-os-pathlike-object-not-io-buf
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
root = _c_(632811, _n_(632810, "Tk", lambda: Tk))
_l_(632812)
def open_f():
    _l_(632821)

    global file
    _l_(632813)
    file = _c_(632815, _n_(632814, "askopenfile", lambda: askopenfile), mode ='rb', filetypes =[('All Files','*.*'),
                  ('pdf files', '*.pdf'),('txt Files','*.txt')])
    _l_(632816)
    _c_(632819, _n_(632817, "print", lambda: print), 'Selected:', _n_(632818, "file", lambda: file))
    _l_(632820)
button1 = _c_(632825, _n_(632822, "Button", lambda: Button), _n_(632823, "root", lambda: root), text ="Select text file",command=_n_(632824, "open_f", lambda: open_f))
_l_(632826)
_c_(632829, _a_(632828, _n_(632827, "button1", lambda: button1), "grid"), row=9,column=1,pady=5)
_l_(632830)
l1=[] 
_l_(632831) 
TextFile = _n_(632832, "file", lambda: file)
_l_(632833)
# open the file for data processing
with _c_(632836, _n_(632834, "open", lambda: open), _n_(632835, "TextFile", lambda: TextFile),encoding="utf8") as IpFile:
    _l_(632848)

    for j in _n_(632837, "IpFile", lambda: IpFile):
        _l_(632847)

        _c_(632845, _a_(632839, _n_(632838, "l1", lambda: l1), "append"), _c_(632844, _a_(632843, _c_(632842, _n_(632840, "str", lambda: str), _n_(632841, "j", lambda: j)), "strip")))   
        _l_(632846)   
_c_(632851, _a_(632850, _n_(632849, "root", lambda: root), "mainloop"))
_l_(632852)