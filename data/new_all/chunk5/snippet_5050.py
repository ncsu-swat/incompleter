# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/20597786/typeerror-unsupported-operand-types-for-type-and-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(668568)

except ImportError:
    pass

class App:
    _l_(668687)

    def __init__(self,master):
        _l_(668656)

        frame = _c_(668571, _n_(668569, "Frame", lambda: Frame), _n_(668570, "master", lambda: master))
        _l_(668572)
        _c_(668575, _a_(668574, _n_(668573, "frame", lambda: frame), "pack"))
        _l_(668576)
        _c_(668581, _a_(668580, _c_(668579, _n_(668577, "Label", lambda: Label), _n_(668578, "frame", lambda: frame), text='Solution in liters:'), "grid"), row=0, column=0)
        _l_(668582)
        _n_(668583, "self", lambda: self).vol = _n_(668584, "DoubleVar", lambda: DoubleVar)
        _l_(668585)
        _c_(668592, _a_(668591, _c_(668590, _n_(668586, "Entry", lambda: Entry), _n_(668587, "frame", lambda: frame), textvariable=_a_(668589, _n_(668588, "self", lambda: self), "vol")), "grid"), row=0, column=1)
        _l_(668593)
        _c_(668598, _a_(668597, _c_(668596, _n_(668594, "Label", lambda: Label), _n_(668595, "frame", lambda: frame), text='Growth Stage (1-5):'), "grid"), row=1, column=0)
        _l_(668599)
        _n_(668600, "self", lambda: self).stage = _n_(668601, "IntVar", lambda: IntVar)
        _l_(668602)
        _c_(668609, _a_(668608, _c_(668607, _n_(668603, "Entry", lambda: Entry), _n_(668604, "frame", lambda: frame), textvariable=_a_(668606, _n_(668605, "self", lambda: self), "stage")), "grid"), row=1, column=1)
        _l_(668610)
        _n_(668611, "self", lambda: self).fgTotal = _n_(668612, "DoubleVar", lambda: DoubleVar)
        _l_(668613)
        _n_(668614, "self", lambda: self).fmTotal = _n_(668615, "DoubleVar", lambda: DoubleVar)
        _l_(668616)
        _n_(668617, "self", lambda: self).fbTotal = _n_(668618, "DoubleVar", lambda: DoubleVar)
        _l_(668619)
        _c_(668626, _a_(668625, _c_(668624, _n_(668620, "Label", lambda: Label), _n_(668621, "frame", lambda: frame), textvariable=_a_(668623, _n_(668622, "self", lambda: self), "fgTotal")), "grid"), row=2, column=0)
        _l_(668627)
        _c_(668634, _a_(668633, _c_(668632, _n_(668628, "Label", lambda: Label), _n_(668629, "frame", lambda: frame), textvariable=_a_(668631, _n_(668630, "self", lambda: self), "fmTotal")), "grid"), row=2, column=2)
        _l_(668635)
        _c_(668642, _a_(668641, _c_(668640, _n_(668636, "Label", lambda: Label), _n_(668637, "frame", lambda: frame), textvariable=_a_(668639, _n_(668638, "self", lambda: self), "fbTotal")), "grid"), row=2, column=3)
        _l_(668643)
        button = _c_(668648, _n_(668644, "Button", lambda: Button), _n_(668645, "frame", lambda: frame), text='Calculate', command=_a_(668647, _n_(668646, "self", lambda: self), "calculate"))
        _l_(668649)
        _c_(668654, _a_(668651, _n_(668650, "button", lambda: button), "grid"), row=3, column=1, sticky=(_n_(668652, "W", lambda: W), _n_(668653, "E", lambda: E)))
        _l_(668655)

    def calculate(self):
        _l_(668686)

        if _a_(668658, _n_(668657, "self", lambda: self), "stage") == 1:
            _l_(668673)

             #Seedlings
            fgML,fmML,fbML = 0.33,0.33,0.33
            _l_(668659)
        elif _a_(668661, _n_(668660, "self", lambda: self), "stage") == 2:
            _l_(668672)

            #Mild Veg
            fgML,fmML,fbML = 1.32,1.32,1.32
            _l_(668662)
        elif _a_(668664, _n_(668663, "self", lambda: self), "stage") == 3:
            _l_(668671)

            #Aggresive Veg
            fgML,fmML,fbML = 3.96,2.64,1.32
            _l_(668665)
        elif _a_(668667, _n_(668666, "self", lambda: self), "stage") == 4:
            _l_(668670)

            #Tranistion to Bloom
            fgML,fmML,fbML = 2.64,2.64,2.64
            _l_(668668)
        else:
            #Blooming and Ripening
            fgML,fmML,fbML = 1.32,2.64,3.96
            _l_(668669)
        fgTotal = _a_(668675, _n_(668674, "self", lambda: self), "vol") * _n_(668676, "fgML", lambda: fgML)
        _l_(668677)
        fmTotal = _a_(668679, _n_(668678, "self", lambda: self), "vol") * _n_(668680, "fmML", lambda: fmML)
        _l_(668681)
        fbTotal = _a_(668683, _n_(668682, "self", lambda: self), "vol") * _n_(668684, "fbML", lambda: fbML)
        _l_(668685)


root = _c_(668689, _n_(668688, "Tk", lambda: Tk))
_l_(668690)
_c_(668693, _a_(668692, _n_(668691, "root", lambda: root), "wm_title"), 'Solution Mixer')
_l_(668694)
app = _c_(668697, _n_(668695, "App", lambda: App), _n_(668696, "root", lambda: root))
_l_(668698)
_c_(668701, _a_(668700, _n_(668699, "root", lambda: root), "mainloop"))
_l_(668702)