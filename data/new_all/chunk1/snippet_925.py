# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34562737/attributeerror-using-pyqt4
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(386907)

except ImportError:
    pass
try:
    from PyQt4 import QtGui,QtCore
    _l_(386909)

except ImportError:
    pass
class Line(_a_(386911, _n_(386910, "QtGui", lambda: QtGui), "QWidget")):
    _l_(387202)

    def __init__(self):
        _l_(386930)

        _c_(386916, _a_(386915, _n_(386912, "super", lambda: super)(_n_(386913, "Line", lambda: Line),_n_(386914, "self", lambda: self)), "__init__"))
        _l_(386917)
        _n_(386918, "self", lambda: self).x1=-1
        _l_(386919)
        _n_(386920, "self", lambda: self).x2=-1
        _l_(386921)
        _n_(386922, "self", lambda: self).y1=-1
        _l_(386923)
        _n_(386924, "self", lambda: self).y2=-1
        _l_(386925)
        _c_(386928, _a_(386927, _n_(386926, "self", lambda: self), "initUI"))
        _l_(386929)

    def initUI(self):
        _l_(387081)


        b1=_c_(386934, _a_(386932, _n_(386931, "QtGui", lambda: QtGui), "QPushButton"), "Draw Line",_n_(386933, "self", lambda: self))
        _l_(386935)
        _c_(386938, _a_(386937, _n_(386936, "b1", lambda: b1), "setGeometry"), 250,25,100,30)
        _l_(386939)
        _c_(386945, _a_(386942, _a_(386941, _n_(386940, "b1", lambda: b1), "clicked"), "connect"), _a_(386944, _n_(386943, "self", lambda: self), "repaint"))
        _l_(386946)
        l1=_c_(386950, _a_(386948, _n_(386947, "QtGui", lambda: QtGui), "QLabel"), "x1 :",_n_(386949, "self", lambda: self))
        _l_(386951)
        l2=_c_(386955, _a_(386953, _n_(386952, "QtGui", lambda: QtGui), "QLabel"), "x2 :",_n_(386954, "self", lambda: self))
        _l_(386956)
        l3=_c_(386960, _a_(386958, _n_(386957, "QtGui", lambda: QtGui), "QLabel"), "y1 :",_n_(386959, "self", lambda: self))
        _l_(386961)
        l4=_c_(386965, _a_(386963, _n_(386962, "QtGui", lambda: QtGui), "QLabel"), "y2 :",_n_(386964, "self", lambda: self))
        _l_(386966)
        l5=_c_(386970, _a_(386968, _n_(386967, "QtGui", lambda: QtGui), "QLabel"), _n_(386969, "self", lambda: self))
        _l_(386971)
        _c_(386974, _a_(386973, _n_(386972, "l1", lambda: l1), "setGeometry"), 100,250,100,100)
        _l_(386975)
        _c_(386978, _a_(386977, _n_(386976, "l2", lambda: l2), "setGeometry"), 250,250,100,100)
        _l_(386979)
        _c_(386982, _a_(386981, _n_(386980, "l3", lambda: l3), "setGeometry"), 100,350,100,100)
        _l_(386983)
        _c_(386986, _a_(386985, _n_(386984, "l4", lambda: l4), "setGeometry"), 250,350,100,100)
        _l_(386987)
        _c_(386990, _a_(386989, _n_(386988, "l5", lambda: l5), "setGeometry"), 1000,1000,1000,1000)
        _l_(386991)
        _n_(386992, "self", lambda: self).x_1=_c_(386996, _a_(386994, _n_(386993, "QtGui", lambda: QtGui), "QLineEdit"), _n_(386995, "self", lambda: self))
        _l_(386997)
        _n_(386998, "self", lambda: self).x_2=_c_(387002, _a_(387000, _n_(386999, "QtGui", lambda: QtGui), "QLineEdit"), _n_(387001, "self", lambda: self))
        _l_(387003)
        _n_(387004, "self", lambda: self).y_1=_c_(387008, _a_(387006, _n_(387005, "QtGui", lambda: QtGui), "QLineEdit"), _n_(387007, "self", lambda: self))
        _l_(387009)
        _n_(387010, "self", lambda: self).y_2=_c_(387014, _a_(387012, _n_(387011, "QtGui", lambda: QtGui), "QLineEdit"), _n_(387013, "self", lambda: self))
        _l_(387015)
        _c_(387019, _a_(387018, _a_(387017, _n_(387016, "self", lambda: self), "x_1"), "setGeometry"), 130,275,100,50)
        _l_(387020)
        _c_(387024, _a_(387023, _a_(387022, _n_(387021, "self", lambda: self), "x_2"), "setGeometry"), 280,272,100,50)
        _l_(387025)
        _c_(387029, _a_(387028, _a_(387027, _n_(387026, "self", lambda: self), "y_1"), "setGeometry"), 130,375,100,50)
        _l_(387030)
        _c_(387034, _a_(387033, _a_(387032, _n_(387031, "self", lambda: self), "y_2"), "setGeometry"), 280,375,100,50)
        _l_(387035)
        _n_(387036, "self", lambda: self).r1=_c_(387040, _a_(387038, _n_(387037, "QtGui", lambda: QtGui), "QRadioButton"), "Thin Line",_n_(387039, "self", lambda: self))
        _l_(387041)
        _c_(387045, _a_(387044, _a_(387043, _n_(387042, "self", lambda: self), "r1"), "move"), 100,25)
        _l_(387046)
        _n_(387047, "self", lambda: self).r2=_c_(387051, _a_(387049, _n_(387048, "QtGui", lambda: QtGui), "QRadioButton"), "Thick Line",_n_(387050, "self", lambda: self))
        _l_(387052)
        _c_(387056, _a_(387055, _a_(387054, _n_(387053, "self", lambda: self), "r2"), "move"), 100,55)
        _l_(387057)
        _n_(387058, "self", lambda: self).r3=_c_(387062, _a_(387060, _n_(387059, "QtGui", lambda: QtGui), "QRadioButton"), "Dotted Line",_n_(387061, "self", lambda: self))
        _l_(387063)
        _c_(387067, _a_(387066, _a_(387065, _n_(387064, "self", lambda: self), "r3"), "move"), 100,85)
        _l_(387068)
        _c_(387071, _a_(387070, _n_(387069, "self", lambda: self), "setGeometry"), 150,150,500,500)
        _l_(387072)
        _c_(387075, _a_(387074, _n_(387073, "self", lambda: self), "setWindowTitle"), "Line")
        _l_(387076)
        _c_(387079, _a_(387078, _n_(387077, "self", lambda: self), "show"))
        _l_(387080)

    def paintEvent(self,e):
        _l_(387104)

        _n_(387082, "self", lambda: self).qp=_c_(387085, _a_(387084, _n_(387083, "QtGui", lambda: QtGui), "QPainter"))
        _l_(387086)
        _c_(387091, _a_(387089, _a_(387088, _n_(387087, "self", lambda: self), "qp"), "begin"), _n_(387090, "self", lambda: self))
        _l_(387092)
        _c_(387097, _a_(387094, _n_(387093, "self", lambda: self), "draw"), _a_(387096, _n_(387095, "self", lambda: self), "qp"))
        _l_(387098)
        _c_(387102, _a_(387101, _a_(387100, _n_(387099, "self", lambda: self), "qp"), "end"))
        _l_(387103)

    def draw(self,qp):
        _l_(387201)

        _n_(387105, "self", lambda: self).x1=_c_(387111, _a_(387110, _c_(387109, _a_(387108, _a_(387107, _n_(387106, "self", lambda: self), "x_1"), "text")), "toInt"))[0]
        _l_(387112)
        _n_(387113, "self", lambda: self).x2=_c_(387119, _a_(387118, _c_(387117, _a_(387116, _a_(387115, _n_(387114, "self", lambda: self), "x_2"), "text")), "toInt"))[0]
        _l_(387120)
        _n_(387121, "self", lambda: self).y1=_c_(387127, _a_(387126, _c_(387125, _a_(387124, _a_(387123, _n_(387122, "self", lambda: self), "y_1"), "text")), "toInt"))[0]
        _l_(387128)
        _n_(387129, "self", lambda: self).y2=_c_(387135, _a_(387134, _c_(387133, _a_(387132, _a_(387131, _n_(387130, "self", lambda: self), "y_2"), "text")), "toInt"))[0]
        _l_(387136)

        pen=_c_(387142, _a_(387138, _n_(387137, "QtGui", lambda: QtGui), "QPen"), _a_(387141, _a_(387140, _n_(387139, "QtCore", lambda: QtCore), "Qt"), "black"),1)
        _l_(387143)
        _c_(387149, _a_(387145, _n_(387144, "pen", lambda: pen), "setStyle"), _a_(387148, _a_(387147, _n_(387146, "QtCore", lambda: QtCore), "Qt"), "SolidLine"))
        _l_(387150)

        if _c_(387154, _a_(387153, _a_(387152, _n_(387151, "self", lambda: self), "r1"), "isChecked")):
            _l_(387162)

            _c_(387160, _a_(387156, _n_(387155, "pen", lambda: pen), "setStyle"), _a_(387159, _a_(387158, _n_(387157, "QtCore", lambda: QtCore), "Qt"), "SolidLine"))
            _l_(387161)
        if _c_(387166, _a_(387165, _a_(387164, _n_(387163, "self", lambda: self), "r2"), "isChecked")):
            _l_(387171)

            _c_(387169, _a_(387168, _n_(387167, "pen", lambda: pen), "setWidth"), 2)
            _l_(387170)
        if _c_(387175, _a_(387174, _a_(387173, _n_(387172, "self", lambda: self), "r3"), "isChecked")):
            _l_(387183)

            _c_(387181, _a_(387177, _n_(387176, "pen", lambda: pen), "setStyle"), _a_(387180, _a_(387179, _n_(387178, "QtCore", lambda: QtCore), "Qt"), "DashLine"))
            _l_(387182)
        _c_(387187, _a_(387185, _n_(387184, "qp", lambda: qp), "setPen"), _n_(387186, "pen", lambda: pen))
        _l_(387188)

        _c_(387199, _a_(387190, _n_(387189, "qp", lambda: qp), "drawLine"), _a_(387192, _n_(387191, "self", lambda: self), "x1"),_a_(387194, _n_(387193, "self", lambda: self), "y1"),_a_(387196, _n_(387195, "self", lambda: self), "x2"),_a_(387198, _n_(387197, "self", lambda: self), "y2"))
        _l_(387200)

def main():
    _l_(387219)

    app=_c_(387207, _a_(387204, _n_(387203, "QtGui", lambda: QtGui), "QApplication"), _a_(387206, _n_(387205, "sys", lambda: sys), "argv"))
    _l_(387208)
    l1=_c_(387210, _n_(387209, "Line", lambda: Line))
    _l_(387211)
    _c_(387217, _a_(387213, _n_(387212, "sys", lambda: sys), "exit"), _c_(387216, _a_(387215, _n_(387214, "app", lambda: app), "exec_")))
    _l_(387218)

if _n_(387220, "__name__", lambda: __name__)=='__main__':
    _l_(387224)

    _c_(387222, _n_(387221, "main", lambda: main))
    _l_(387223)