# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64357846/nameerror-name-win-is-not-defined-with-tkinter-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(350040)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(350042)

except ImportError:
    pass
def zui(kaj,saj):
    _l_(350058)

    zun=_n_(350043, "kaj", lambda: kaj)
    _l_(350044)
    kaj=_n_(350045, "kaj", lambda: kaj)+"=tk.Tk()"
    _l_(350046)
    _c_(350049, _n_(350047, "exec", lambda: exec), _n_(350048, "kaj", lambda: kaj))
    _l_(350050)
    saj=_n_(350051, "zun", lambda: zun)+".title('"+_n_(350052, "saj", lambda: saj)+"')"
    _l_(350053)
    _c_(350056, _n_(350054, "exec", lambda: exec), _n_(350055, "saj", lambda: saj))
    _l_(350057)
def zabel(self,naj,iaj,oaj,baj,gaj,taj):
    _l_(350075)

    spsp=_n_(350059, "self", lambda: self)+"="+"Label("+_n_(350060, "naj", lambda: naj)+", text='"+_n_(350061, "iaj", lambda: iaj)+"', bg='"+_n_(350062, "oaj", lambda: oaj)+"', height="+_n_(350063, "gaj", lambda: gaj)+", width="+_n_(350064, "taj", lambda: taj)+",fg='"+_n_(350065, "baj", lambda: baj)+"')"
    _l_(350066)
    spsp=_c_(350069, _n_(350067, "str", lambda: str), _n_(350068, "spsp", lambda: spsp))
    _l_(350070)
    _c_(350073, _n_(350071, "exec", lambda: exec), _n_(350072, "spsp", lambda: spsp))
    _l_(350074)
def zosition(qak,iak,nak):
    _l_(350084)

    sspp=_n_(350076, "qak", lambda: qak)+".grid(row="+_n_(350077, "iak", lambda: iak)+", column="+_n_(350078, "nak", lambda: nak)+")"
    _l_(350079)
    _c_(350082, _n_(350080, "exec", lambda: exec), _n_(350081, "sspp", lambda: sspp))
    _l_(350083)
def zainzoop(tak):
    _l_(350091)

    sft=_n_(350085, "tak", lambda: tak)+".mainloop()"
    _l_(350086)
    _c_(350089, _n_(350087, "exec", lambda: exec), _n_(350088, "sft", lambda: sft))
    _l_(350090)
_c_(350093, _n_(350092, "zui", lambda: zui), "win","zahid app")
_l_(350094)
_c_(350096, _n_(350095, "zabel", lambda: zabel), "label","win","hello world","white","black","4","10")
_l_(350097)
_c_(350099, _n_(350098, "zosition", lambda: zosition), "win","1","1")
_l_(350100)
_c_(350102, _n_(350101, "zainzoop", lambda: zainzoop), "win")
_l_(350103)