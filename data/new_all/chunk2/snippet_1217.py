# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/22518828/type-error-missing-one-positional-argument-self-conways-game-of-life
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(442635)

except ImportError:
    pass
root = _c_(442637, _n_(442636, "Tk", lambda: Tk))
_l_(442638)

class Cell (_n_(442639, "Button", lambda: Button)):
    _l_(442737)

    Dead = 0
    _l_(442640)
    Live = 1
    _l_(442641)

    def __init__ (self,parent):
        _l_(442656)

        _c_(442648, _a_(442643, _n_(442642, "Button", lambda: Button), "__init__"), _n_(442644, "self", lambda: self),_n_(442645, "parent", lambda: parent), relief = "raised" , width = 2 , borderwidth = 1 , command = _a_(442647, _n_(442646, "self", lambda: self), "onpress"))
        _l_(442649)
        _c_(442654, _a_(442651, _n_(442650, "self", lambda: self), "displayState"), _a_(442653, _n_(442652, "Cell", lambda: Cell), "Dead"))
        _l_(442655)

    def onpress (self):
        _l_(442679)

        if _a_(442658, _n_(442657, "self", lambda: self), "state") == _a_(442660, _n_(442659, "Cell", lambda: Cell), "Live"):
            _l_(442678)

            _c_(442665, _a_(442662, _n_(442661, "self", lambda: self), "displayState"), _a_(442664, _n_(442663, "Cell", lambda: Cell), "Dead"))
            _l_(442666)
        elif _a_(442668, _n_(442667, "self", lambda: self), "state") == _a_(442670, _n_(442669, "Cell", lambda: Cell), "Dead"):
            _l_(442677)

            _c_(442675, _a_(442672, _n_(442671, "self", lambda: self), "displayState"), _a_(442674, _n_(442673, "Cell", lambda: Cell), "Live"))
            _l_(442676)

    def setNextState (self , Neighbours):
        _l_(442711)

        if _a_(442681, _n_(442680, "self", lambda: self), "state") == _a_(442683, _n_(442682, "Cell", lambda: Cell), "Live") and (_n_(442684, "Neighbours", lambda: Neighbours) < 2 or _n_(442685, "Neighbours", lambda: Neighbours) > 3):
            _l_(442710)

            _n_(442686, "self", lambda: self).nextState = _a_(442688, _n_(442687, "Cell", lambda: Cell), "Dead")
            _l_(442689)
        elif _a_(442691, _n_(442690, "self", lambda: self), "state") == _a_(442693, _n_(442692, "Cell", lambda: Cell), "Dead") and _n_(442694, "Neighbours", lambda: Neighbours) == 3:
            _l_(442709)

            _n_(442695, "self", lambda: self).nextState = _a_(442697, _n_(442696, "Cell", lambda: Cell), "Live")
            _l_(442698)
        elif _a_(442700, _n_(442699, "self", lambda: self), "state") == _a_(442702, _n_(442701, "Cell", lambda: Cell), "Dead") and _n_(442703, "Neighbours", lambda: Neighbours) != 3:
            _l_(442708)

            _n_(442704, "self", lambda: self).nextState = _a_(442706, _n_(442705, "self", lambda: self), "state")
            _l_(442707)

    def stepToNextState(self):
        _l_(442718)

        _c_(442716, _a_(442713, _n_(442712, "self", lambda: self), "displayState"), _a_(442715, _n_(442714, "self", lambda: self), "nextState"))
        _l_(442717)

    def displayState (self , newstate):
        _l_(442736)

        _n_(442719, "self", lambda: self).state = _n_(442720, "newstate", lambda: newstate)
        _l_(442721)
        if _a_(442723, _n_(442722, "self", lambda: self), "state") == _a_(442725, _n_(442724, "Cell", lambda: Cell), "Live"):
            _l_(442728)

            _n_(442726, "self", lambda: self)["bg"] = "black"
            _l_(442727)
        if _a_(442730, _n_(442729, "self", lambda: self), "state") == _a_(442732, _n_(442731, "Cell", lambda: Cell), "Dead"):
            _l_(442735)

            _n_(442733, "self", lambda: self)["bg"] = "white"
            _l_(442734)

class Grid:
    _l_(442873)

    def __init__(self,parent,sizex,sizey):
        _l_(442778)

        _n_(442738, "self", lambda: self).sizex = _n_(442739, "sizex", lambda: sizex)
        _l_(442740)
        _n_(442741, "self", lambda: self).sizey = _n_(442742, "sizey", lambda: sizey)
        _l_(442743)
        _n_(442744, "self", lambda: self).cells = []
        _l_(442745)
        for a in _c_(442749, _n_(442746, "range", lambda: range), 0,_a_(442748, _n_(442747, "self", lambda: self), "sizex")):
            _l_(442777)

            rowcells = []
            _l_(442750)
            for b in _c_(442754, _n_(442751, "range", lambda: range), 0, _a_(442753, _n_(442752, "self", lambda: self), "sizey")):
                _l_(442770)

                c = _c_(442757, _n_(442755, "Cell", lambda: Cell), _n_(442756, "parent", lambda: parent))
                _l_(442758)
                _c_(442763, _a_(442760, _n_(442759, "c", lambda: c), "grid"), row=_n_(442761, "b", lambda: b) , column=_n_(442762, "a", lambda: a))
                _l_(442764)
                _c_(442768, _a_(442766, _n_(442765, "rowcells", lambda: rowcells), "append"), _n_(442767, "c", lambda: c))
                _l_(442769)
            _c_(442775, _a_(442773, _a_(442772, _n_(442771, "self", lambda: self), "cells"), "append"), _n_(442774, "rowcells", lambda: rowcells))
            _l_(442776)

    def step (self):
        _l_(442860)

        cells = _a_(442780, _n_(442779, "self", lambda: self), "cells")
        _l_(442781)
        for x in _c_(442785, _n_(442782, "range", lambda: range), 0,_a_(442784, _n_(442783, "self", lambda: self), "sizex")):
            _l_(442859)

            if _n_(442786, "x", lambda: x)==0:
                _l_(442790)

x_down = _a_(442788, _n_(442787, "self", lambda: self), "sizex")-1            else: x_down = _n_(442789, "x", lambda: x)-1
            if _n_(442791, "x", lambda: x)==_a_(442793, _n_(442792, "self", lambda: self), "sizex")-1:
                _l_(442795)

x_up = 0            else: x_up = _n_(442794, "x", lambda: x)+1
            for y in _c_(442799, _n_(442796, "range", lambda: range), 0,_a_(442798, _n_(442797, "self", lambda: self), "sizey")):
                _l_(442843)

                if _n_(442800, "y", lambda: y)==0:
                    _l_(442804)

y_down = _a_(442802, _n_(442801, "self", lambda: self), "sizey")-1                else: Y_down = _n_(442803, "y", lambda: y)-1
                if _n_(442805, "y", lambda: y)==_a_(442807, _n_(442806, "self", lambda: self), "sizey")-1:
                    _l_(442809)

y_up = 0                else: y_up = _n_(442808, "y", lambda: y)+1
                sum = _a_(442813, _n_(442810, "cells", lambda: cells)[_n_(442811, "x_down", lambda: x_down)][_n_(442812, "y", lambda: y)], "state") + _a_(442817, _n_(442814, "cells", lambda: cells)[_n_(442815, "x_up", lambda: x_up)][_n_(442816, "y", lambda: y)], "state") + _a_(442821, _n_(442818, "cells", lambda: cells)[_n_(442819, "x", lambda: x)][_n_(442820, "y_down", lambda: y_down)], "state") + _a_(442825, _n_(442822, "cells", lambda: cells)[_n_(442823, "x", lambda: x)][_n_(442824, "y_up", lambda: y_up)], "state") + _a_(442829, _n_(442826, "cells", lambda: cells)[_n_(442827, "x_down", lambda: x_down)][_n_(442828, "y_down", lambda: y_down)], "state") +_a_(442833, _n_(442830, "cells", lambda: cells)[_n_(442831, "x_up", lambda: x_up)][_n_(442832, "y_up", lambda: y_up)], "state") + _a_(442837, _n_(442834, "cells", lambda: cells)[_n_(442835, "x_down", lambda: x_down)][_n_(442836, "y_up", lambda: y_up)], "state") + _a_(442841, _n_(442838, "cells", lambda: cells)[_n_(442839, "x_up", lambda: x_up)][_n_(442840, "y_down", lambda: y_down)], "state")
                _l_(442842)
            _c_(442849, _a_(442847, _n_(442844, "cells", lambda: cells)[_n_(442845, "x", lambda: x)][_n_(442846, "y", lambda: y)], "setNextState"), _n_(442848, "sum", lambda: sum))
            _l_(442850)
            for row in _n_(442851, "cells", lambda: cells):
                _l_(442858)

                for cell in _n_(442852, "row", lambda: row):
                    _l_(442857)

                    _c_(442855, _a_(442854, _n_(442853, "cell", lambda: cell), "stepToNextState"))
                    _l_(442856)

    def clear(self):
        _l_(442872)

        for row in _a_(442862, _n_(442861, "self", lambda: self), "cells"):
            _l_(442871)

            for cell in _n_(442863, "row", lambda: row):
                _l_(442870)

                _c_(442868, _a_(442865, _n_(442864, "cell", lambda: cell), "displayState"), _a_(442867, _n_(442866, "Cell", lambda: Cell), "Dead"))
                _l_(442869)

def GridStep():
    _l_(442878)

    _c_(442876, _a_(442875, _n_(442874, "Grid", lambda: Grid), "step"))
    _l_(442877)

def GridClear():
    _l_(442883)

    _c_(442881, _a_(442880, _n_(442879, "Grid", lambda: Grid), "step"))
    _l_(442882)

if _n_(442884, "__name__", lambda: __name__) == "__main__":
    _l_(442931)

    frame = _c_(442887, _n_(442885, "Frame", lambda: Frame), _n_(442886, "root", lambda: root))
    _l_(442888)
    _c_(442891, _a_(442890, _n_(442889, "frame", lambda: frame), "pack"))
    _l_(442892)
    grid = _c_(442895, _n_(442893, "Grid", lambda: Grid), _n_(442894, "frame", lambda: frame),25,25)
    _l_(442896)
    bottomFrame = _c_(442899, _n_(442897, "Frame", lambda: Frame), _n_(442898, "root", lambda: root))
    _l_(442900)
    _c_(442904, _a_(442902, _n_(442901, "bottomFrame", lambda: bottomFrame), "pack"), side = _n_(442903, "BOTTOM", lambda: BOTTOM))
    _l_(442905)
    buttonStep = _c_(442909, _n_(442906, "Button", lambda: Button), _n_(442907, "bottomFrame", lambda: bottomFrame) , text="Step" , command=_n_(442908, "GridStep", lambda: GridStep))
    _l_(442910)
    _c_(442914, _a_(442912, _n_(442911, "buttonStep", lambda: buttonStep), "pack"), side = _n_(442913, "LEFT", lambda: LEFT))
    _l_(442915)
    buttonClear = _c_(442919, _n_(442916, "Button", lambda: Button), _n_(442917, "bottomFrame", lambda: bottomFrame), text = "Clear", command=_n_(442918, "GridClear", lambda: GridClear))
    _l_(442920)
    _c_(442925, _a_(442922, _n_(442921, "buttonClear", lambda: buttonClear), "pack"), side=_n_(442923, "LEFT", lambda: LEFT) , after=_n_(442924, "buttonStep", lambda: buttonStep))
    _l_(442926)
    _c_(442929, _a_(442928, _n_(442927, "root", lambda: root), "mainloop"))
    _l_(442930)