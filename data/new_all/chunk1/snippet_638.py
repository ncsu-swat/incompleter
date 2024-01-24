# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28116807/python3-pyqt5-nonetype-error-when-setting-value-in-radiobutton-connect
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(378683, _a_(378682, _n_(378681, "QtCore", lambda: QtCore), "pyqtSlot"))
def setInterval(self,i):
    _l_(378718)


    if _n_(378684, "i", lambda: i) == 1:
        _l_(378717)

        n = 1/_c_(378688, _a_(378687, _a_(378686, _n_(378685, "self", lambda: self), "doubleSpinBox_TimeIndexStep"), "value")) #TODO: use math.floor/ceiling to geht integers
        _l_(378689) #TODO: use math.floor/ceiling to geht integers
        _a_(378692, _a_(378691, _n_(378690, "self", lambda: self), "spinBox_CopyInterval"), "setEnabled")
        _l_(378693)
        _c_(378698, _a_(378696, _a_(378695, _n_(378694, "self", lambda: self), "spinBox_CopyInterval"), "setValue"), _n_(378697, "n", lambda: n))
        _l_(378699)
    elif _n_(378700, "i", lambda: i) == 10:
        _l_(378716)

        n = 10/_c_(378704, _a_(378703, _a_(378702, _n_(378701, "self", lambda: self), "doubleSpinBox_TimeIndexStep"), "value"))
        _l_(378705)
        _a_(378708, _a_(378707, _n_(378706, "self", lambda: self), "spinBox_CopyInterval"), "setEnabled")
        _l_(378709)
        _c_(378714, _a_(378712, _a_(378711, _n_(378710, "self", lambda: self), "spinBox_CopyInterval"), "setValue"), _n_(378713, "n", lambda: n))
        _l_(378715)