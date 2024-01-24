# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57208264/nameerror-name-ptime-is-not-defined-using-tkinter-scale-scroller
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def set_Tk_var():
    _l_(667351)

    global Ptime
    _l_(667341)
    Ptime = _c_(667344, _a_(667343, _n_(667342, "tk", lambda: tk), "DoubleVar"))
    _l_(667345)
    global Pspeed
    _l_(667346)
    Pspeed = _c_(667349, _a_(667348, _n_(667347, "tk", lambda: tk), "StringVar"))
    _l_(667350)

text = "play: timecode: 00:00:0" + _c_(667354, _n_(667352, "str", lambda: str), _n_(667353, "Ptime", lambda: Ptime)) + ";00 \\nc"
_l_(667355)
def IRplay():
    _l_(667375)

    _c_(667357, _n_(667356, "print", lambda: print), 'testguiPAGE_support.IRplay')
    _l_(667358)
    _c_(667361, _a_(667360, _n_(667359, "session", lambda: session), "write"), b"stop\n")
    _l_(667362)
    _c_(667368, _a_(667364, _n_(667363, "session", lambda: session), "write"), _c_(667367, _a_(667366, _n_(667365, "text", lambda: text), "encode")) )
    _l_(667369)
    _c_(667373, _a_(667372, _a_(667371, _n_(667370, "sys", lambda: sys), "stdout"), "flush"))
    _l_(667374)