# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59036061/how-to-fix-typeerror-while-plotting-using-pyqtgraph
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyqtgraph as pg
    _l_(704014)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import QMainWindow
    _l_(704016)

except ImportError:
    pass
try:
    from PyQt5.QtCore import pyqtSlot, pyqtSignal
    _l_(704018)

except ImportError:
    pass
try:
    from Ui_GraphicsLayout import Ui_GraphicsLayout
    _l_(704020)

except ImportError:
    pass

class Polar(_n_(704021, "QMainWindow", lambda: QMainWindow)):
    _l_(704085)


    def __init__(self, title = "Time Domain Plot", name = "Channel"):
        _l_(704076)

        _c_(704024, _a_(704023, _n_(704022, "super", lambda: super)(), "__init__"))
        _l_(704025)

        _c_(704028, _a_(704027, _n_(704026, "pg", lambda: pg), "setConfigOption"), 'background', 'w')
        _l_(704029)

        _n_(704030, "self", lambda: self).__ui = _c_(704032, _n_(704031, "Ui_GraphicsLayout", lambda: Ui_GraphicsLayout))
        _l_(704033)
        _c_(704038, _a_(704036, _a_(704035, _n_(704034, "self", lambda: self), "__ui"), "setupUi"), _n_(704037, "self", lambda: self))
        _l_(704039)

        _c_(704045, _a_(704041, _n_(704040, "self", lambda: self), "setWindowTitle"), _c_(704044, _a_(704042, "Measurement System - {:s}", "format"), _n_(704043, "title", lambda: title)))
        _l_(704046)

        _n_(704047, "self", lambda: self).__plot = _c_(704053, _a_(704051, _a_(704050, _a_(704049, _n_(704048, "self", lambda: self), "__ui"), "widget"), "addPlot"), title = _n_(704052, "name", lambda: name), row = 0, col = 0);
        _l_(704054)
        _n_(704055, "self", lambda: self).__pditem = _c_(704059, _a_(704058, _a_(704057, _n_(704056, "self", lambda: self), "__plot"), "plot"), pen=None, symbol = 'o', symbolSize=5)
        _l_(704060)

        _c_(704064, _a_(704063, _a_(704062, _n_(704061, "self", lambda: self), "__plot"), "setAspectLocked"))
        _l_(704065)
        _c_(704069, _a_(704068, _a_(704067, _n_(704066, "self", lambda: self), "__plot"), "addLine"), x=0, pen=0.2)
        _l_(704070)
        _c_(704074, _a_(704073, _a_(704072, _n_(704071, "self", lambda: self), "__plot"), "addLine"), y=0, pen=0.2)
        _l_(704075)

    def plot(self, data1, data2):
        _l_(704084)

        _c_(704082, _a_(704079, _a_(704078, _n_(704077, "self", lambda: self), "__pditem"), "setData"), _n_(704080, "data1", lambda: data1),_n_(704081, "data2", lambda: data2))
        _l_(704083)