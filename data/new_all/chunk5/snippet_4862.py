# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44871876/scope-error-nameerror-name-date-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(676565)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(676567)

except ImportError:
    pass

class Application(_a_(676569, _n_(676568, "tk", lambda: tk), "Frame")):
    _l_(676717)


    def __init__(self, master):
        _l_(676679)

        _c_(676575, _a_(676572, _a_(676571, _n_(676570, "tk", lambda: tk), "Frame"), "__init__"), _n_(676573, "self", lambda: self), _n_(676574, "master", lambda: master))
        _l_(676576)
        _n_(676577, "self", lambda: self).master = _n_(676578, "master", lambda: master)
        _l_(676579)
        _c_(676582, _a_(676581, _n_(676580, "master", lambda: master), "title"), "Trade Finance")
        _l_(676583)
        _c_(676586, _a_(676585, _n_(676584, "master", lambda: master), "minsize"), width=250, height=200)
        _l_(676587)
        _c_(676590, _a_(676589, _n_(676588, "master", lambda: master), "maxsize"), width=250, height=200)
        _l_(676591)
        _n_(676592, "self", lambda: self).date = None
        _l_(676593)


        #Input of expiry date
        label = _c_(676597, _a_(676595, _n_(676594, "tk", lambda: tk), "LabelFrame"), _n_(676596, "master", lambda: master), text = "Input", bd = 2, font='none 8 italic')
        _l_(676598)
        _c_(676601, _a_(676600, _n_(676599, "label", lambda: label), "pack"))
        _l_(676602)
        _c_(676608, _a_(676607, _c_(676606, _a_(676604, _n_(676603, "tk", lambda: tk), "Label"), _n_(676605, "label", lambda: label), text="Expiry Date (YYYY-MM-DD)",font = 'none 10'), "pack"))
        _l_(676609)

        _n_(676610, "self", lambda: self).userinput1 = _c_(676613, _a_(676612, _n_(676611, "tk", lambda: tk), "StringVar"))
        _l_(676614)
        _c_(676622, _a_(676621, _c_(676620, _a_(676616, _n_(676615, "tk", lambda: tk), "Entry"), _n_(676617, "label", lambda: label),textvariable = _a_(676619, _n_(676618, "self", lambda: self), "userinput1")), "pack"))
        _l_(676623)

        #Input of non-renewal days
        _c_(676629, _a_(676628, _c_(676627, _a_(676625, _n_(676624, "tk", lambda: tk), "Label"), _n_(676626, "label", lambda: label), text="Non-Renewal Days",font = 'none 10'), "pack"))
        _l_(676630)

        _n_(676631, "self", lambda: self).userinput2 = _c_(676634, _a_(676633, _n_(676632, "tk", lambda: tk), "StringVar"))
        _l_(676635)
        _c_(676643, _a_(676642, _c_(676641, _a_(676637, _n_(676636, "tk", lambda: tk), "Entry"), _n_(676638, "label", lambda: label), textvariable = _a_(676640, _n_(676639, "self", lambda: self), "userinput2")), "pack"))
        _l_(676644)

        #output results
        label_1 = _c_(676648, _a_(676646, _n_(676645, "tk", lambda: tk), "LabelFrame"), _n_(676647, "master", lambda: master), text = "Output", bd = 2, font='none 8 italic')
        _l_(676649)
        _c_(676652, _a_(676651, _n_(676650, "label_1", lambda: label_1), "pack"))
        _l_(676653)
        _c_(676659, _a_(676658, _c_(676657, _a_(676655, _n_(676654, "tk", lambda: tk), "Label"), _n_(676656, "label_1", lambda: label_1),text= 'Review Date',font= 'none 10'), "pack"))
        _l_(676660)
        button = _c_(676668, _a_(676667, _c_(676666, _a_(676662, _n_(676661, "tk", lambda: tk), "Button"), _n_(676663, "label_1", lambda: label_1), text="Calculate", fg ='white', bg = 'black',font= 'none 10 bold',command=_a_(676665, _n_(676664, "self", lambda: self), "result")), "pack"))
        _l_(676669)
        _c_(676677, _a_(676676, _c_(676675, _a_(676671, _n_(676670, "tk", lambda: tk), "Entry"), _n_(676672, "label_1", lambda: label_1), textvariable = _a_(676674, _n_(676673, "self", lambda: self), "result")), "pack"))
        _l_(676678)


    def expiry(self):
        _l_(676697)

        while True:
            _l_(676696)

            date = _c_(676683, _a_(676682, _a_(676681, _n_(676680, "self", lambda: self), "userinput1"), "get"))
            _l_(676684)
            try:
                _l_(676695)

                aux = _c_(676688, _a_(676686, _n_(676685, "datetime", lambda: datetime), "strptime"), _n_(676687, "date", lambda: date), '%Y-%m-%d')
                _l_(676689)
                return aux
            except _n_(676690, "ValueError", lambda: ValueError):
                _l_(676694)

                _c_(676692, _n_(676691, "print", lambda: print), 'Please follow the date format')
                _l_(676693)


    def notice_days(self):
        _l_(676707)

        ndays = _c_(676701, _a_(676700, _a_(676699, _n_(676698, "self", lambda: self), "userinput2"), "get"))
        _l_(676702)
        aux = _c_(676705, _n_(676703, "timedelta", lambda: timedelta), days=_n_(676704, "ndays", lambda: ndays))
        _l_(676706)
        return aux

    def result(self):
        _l_(676716)

        result = _c_(676712, _a_(676709, _n_(676708, "datetime", lambda: datetime), "date"), _n_(676710, "date", lambda: date) - _n_(676711, "days", lambda: days))
        _l_(676713)
        aux = _n_(676714, "result", lambda: result)
        _l_(676715)
        return aux

if _n_(676718, "__name__", lambda: __name__)=='__main__':
    _l_(676731)

    root = _c_(676721, _a_(676720, _n_(676719, "tk", lambda: tk), "Tk"))
    _l_(676722)
    app = _c_(676725, _n_(676723, "Application", lambda: Application), _n_(676724, "root", lambda: root))
    _l_(676726)
    _c_(676729, _a_(676728, _n_(676727, "app", lambda: app), "mainloop"))
    _l_(676730)