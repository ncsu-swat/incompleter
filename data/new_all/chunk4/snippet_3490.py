# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73542588/typeerror-argument-1-has-unexpected-type-qpushbutton
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(592110)

except ImportError:
    pass
try:
    import os
    _l_(592112)

except ImportError:
    pass
try:
    from cameraID import CameraID
    _l_(592114)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import QFileDialog, QDialog
    _l_(592116)

except ImportError:
    pass
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    _l_(592118)

except ImportError:
    pass


class Ui_Test(_n_(592119, "QDialog", lambda: QDialog)):
    _l_(592418)


    def browse_file_src(self):
        _l_(592134)

        _c_(592121, _n_(592120, "print", lambda: print), 'in the function')
        _l_(592122)
        file_name = _c_(592126, _a_(592124, _n_(592123, "QFileDialog", lambda: QFileDialog), "getOpenFileName"), _n_(592125, "self", lambda: self), 'Open file', '/home/qauser/')
        _l_(592127)
        _c_(592132, _a_(592130, _a_(592129, _n_(592128, "self", lambda: self), "lineEdit"), "setText"), _n_(592131, "file_name", lambda: file_name)[0])
        _l_(592133)

    def get_all_serials(self):
        _l_(592166)

        _n_(592135, "self", lambda: self).serial = _c_(592137, _n_(592136, "CameraID", lambda: CameraID))
        _l_(592138)
        _c_(592142, _a_(592141, _a_(592140, _n_(592139, "self", lambda: self), "serial"), "getAllSerial"))
        _l_(592143)
        return_list = _c_(592147, _a_(592146, _a_(592145, _n_(592144, "self", lambda: self), "serial"), "getAllSerial"))
        _l_(592148)
        if _c_(592151, _n_(592149, "len", lambda: len), _n_(592150, "return_list", lambda: return_list)) > 0:
            _l_(592165)

            for i in _n_(592152, "return_list", lambda: return_list):
                _l_(592159)

                _c_(592157, _a_(592155, _a_(592154, _n_(592153, "self", lambda: self), "comboBox"), "addItem"), _n_(592156, "i", lambda: i))
                _l_(592158)
        else:
            _c_(592163, _a_(592162, _a_(592161, _n_(592160, "self", lambda: self), "comboBox"), "addItem"), "None")
            _l_(592164)

    def setupUi(self, Test):
        _l_(592378)

        _c_(592169, _a_(592168, _n_(592167, "Test", lambda: Test), "setObjectName"), "Test")
        _l_(592170)
        _c_(592173, _a_(592172, _n_(592171, "Test", lambda: Test), "resize"), 397, 108)
        _l_(592174)
        _n_(592175, "self", lambda: self).centralwidget = _c_(592179, _a_(592177, _n_(592176, "QtWidgets", lambda: QtWidgets), "QWidget"), _n_(592178, "Test", lambda: Test))
        _l_(592180)
        _c_(592184, _a_(592183, _a_(592182, _n_(592181, "self", lambda: self), "centralwidget"), "setObjectName"), "centralwidget")
        _l_(592185)

        _n_(592186, "self", lambda: self).lineEdit = _c_(592191, _a_(592188, _n_(592187, "QtWidgets", lambda: QtWidgets), "QLineEdit"), _a_(592190, _n_(592189, "self", lambda: self), "centralwidget"))
        _l_(592192)
        _c_(592199, _a_(592195, _a_(592194, _n_(592193, "self", lambda: self), "lineEdit"), "setGeometry"), _c_(592198, _a_(592197, _n_(592196, "QtCore", lambda: QtCore), "QRect"), 10, 10, 291, 21))
        _l_(592200)
        _c_(592204, _a_(592203, _a_(592202, _n_(592201, "self", lambda: self), "lineEdit"), "setObjectName"), "lineEdit")
        _l_(592205)
        _c_(592209, _a_(592208, _a_(592207, _n_(592206, "self", lambda: self), "lineEdit"), "setPlaceholderText"), "Chose file")
        _l_(592210)

        _n_(592211, "self", lambda: self).browseBtn = _c_(592216, _a_(592213, _n_(592212, "QtWidgets", lambda: QtWidgets), "QPushButton"), _a_(592215, _n_(592214, "self", lambda: self), "centralwidget"))#, clicked=lambda: self.browseBtn)
        _l_(592217)#, clicked=lambda: self.browseBtn)
        _c_(592224, _a_(592220, _a_(592219, _n_(592218, "self", lambda: self), "browseBtn"), "setGeometry"), _c_(592223, _a_(592222, _n_(592221, "QtCore", lambda: QtCore), "QRect"), 310, 10, 80, 23))
        _l_(592225)
        _c_(592229, _a_(592228, _a_(592227, _n_(592226, "self", lambda: self), "browseBtn"), "setObjectName"), "browseBtn")
        _l_(592230)
        _c_(592237, _a_(592234, _a_(592233, _a_(592232, _n_(592231, "self", lambda: self), "browseBtn"), "clicked"), "connect"), _a_(592236, _n_(592235, "self", lambda: self), "browseBtn"))
        _l_(592238)

        _n_(592239, "self", lambda: self).radioButton = _c_(592244, _a_(592241, _n_(592240, "QtWidgets", lambda: QtWidgets), "QRadioButton"), _a_(592243, _n_(592242, "self", lambda: self), "centralwidget"))
        _l_(592245)
        _c_(592252, _a_(592248, _a_(592247, _n_(592246, "self", lambda: self), "radioButton"), "setGeometry"), _c_(592251, _a_(592250, _n_(592249, "QtCore", lambda: QtCore), "QRect"), 10, 40, 51, 21))
        _l_(592253)
        _c_(592257, _a_(592256, _a_(592255, _n_(592254, "self", lambda: self), "radioButton"), "setObjectName"), "radioButton")
        _l_(592258)

        _n_(592259, "self", lambda: self).radioButton_2 = _c_(592264, _a_(592261, _n_(592260, "QtWidgets", lambda: QtWidgets), "QRadioButton"), _a_(592263, _n_(592262, "self", lambda: self), "centralwidget"))
        _l_(592265)
        _c_(592272, _a_(592268, _a_(592267, _n_(592266, "self", lambda: self), "radioButton_2"), "setGeometry"), _c_(592271, _a_(592270, _n_(592269, "QtCore", lambda: QtCore), "QRect"), 60, 40, 71, 21))
        _l_(592273)
        _c_(592277, _a_(592276, _a_(592275, _n_(592274, "self", lambda: self), "radioButton_2"), "setObjectName"), "radioButton_2")
        _l_(592278)

        _n_(592279, "self", lambda: self).pushButton = _c_(592284, _a_(592281, _n_(592280, "QtWidgets", lambda: QtWidgets), "QPushButton"), _a_(592283, _n_(592282, "self", lambda: self), "centralwidget"))
        _l_(592285)
        _c_(592292, _a_(592288, _a_(592287, _n_(592286, "self", lambda: self), "pushButton"), "setGeometry"), _c_(592291, _a_(592290, _n_(592289, "QtCore", lambda: QtCore), "QRect"), 310, 40, 80, 23))
        _l_(592293)
        _c_(592297, _a_(592296, _a_(592295, _n_(592294, "self", lambda: self), "pushButton"), "setObjectName"), "pushButton")
        _l_(592298)

        _n_(592299, "self", lambda: self).comboBox = _c_(592304, _a_(592301, _n_(592300, "QtWidgets", lambda: QtWidgets), "QComboBox"), _a_(592303, _n_(592302, "self", lambda: self), "centralwidget"))
        _l_(592305)
        _c_(592312, _a_(592308, _a_(592307, _n_(592306, "self", lambda: self), "comboBox"), "setGeometry"), _c_(592311, _a_(592310, _n_(592309, "QtCore", lambda: QtCore), "QRect"), 120, 40, 181, 23))
        _l_(592313)
        _c_(592317, _a_(592316, _a_(592315, _n_(592314, "self", lambda: self), "comboBox"), "setObjectName"), "comboBox")
        _l_(592318)

        _c_(592323, _a_(592320, _n_(592319, "Test", lambda: Test), "setCentralWidget"), _a_(592322, _n_(592321, "self", lambda: self), "centralwidget"))
        _l_(592324)
        _n_(592325, "self", lambda: self).menubar = _c_(592329, _a_(592327, _n_(592326, "QtWidgets", lambda: QtWidgets), "QMenuBar"), _n_(592328, "Test", lambda: Test))
        _l_(592330)
        _c_(592337, _a_(592333, _a_(592332, _n_(592331, "self", lambda: self), "menubar"), "setGeometry"), _c_(592336, _a_(592335, _n_(592334, "QtCore", lambda: QtCore), "QRect"), 0, 0, 397, 20))
        _l_(592338)
        _c_(592342, _a_(592341, _a_(592340, _n_(592339, "self", lambda: self), "menubar"), "setObjectName"), "menubar")
        _l_(592343)
        _c_(592348, _a_(592345, _n_(592344, "Test", lambda: Test), "setMenuBar"), _a_(592347, _n_(592346, "self", lambda: self), "menubar"))
        _l_(592349)
        _n_(592350, "self", lambda: self).statusbar = _c_(592354, _a_(592352, _n_(592351, "QtWidgets", lambda: QtWidgets), "QStatusBar"), _n_(592353, "Test", lambda: Test))
        _l_(592355)
        _c_(592359, _a_(592358, _a_(592357, _n_(592356, "self", lambda: self), "statusbar"), "setObjectName"), "statusbar")
        _l_(592360)
        _c_(592365, _a_(592362, _n_(592361, "Test", lambda: Test), "setStatusBar"), _a_(592364, _n_(592363, "self", lambda: self), "statusbar"))
        _l_(592366)

        _c_(592370, _a_(592368, _n_(592367, "self", lambda: self), "retranslateUi"), _n_(592369, "Test", lambda: Test))
        _l_(592371)
        _c_(592376, _a_(592374, _a_(592373, _n_(592372, "QtCore", lambda: QtCore), "QMetaObject"), "connectSlotsByName"), _n_(592375, "Test", lambda: Test))
        _l_(592377)

    def retranslateUi(self, Test):
        _l_(592417)

        _translate = _a_(592381, _a_(592380, _n_(592379, "QtCore", lambda: QtCore), "QCoreApplication"), "translate")
        _l_(592382)
        _c_(592387, _a_(592384, _n_(592383, "Test", lambda: Test), "setWindowTitle"), _c_(592386, _n_(592385, "_translate", lambda: _translate), "Test", "MainWindow"))
        _l_(592388)
        _c_(592394, _a_(592391, _a_(592390, _n_(592389, "self", lambda: self), "browseBtn"), "setText"), _c_(592393, _n_(592392, "_translate", lambda: _translate), "Test", "Browse"))
        _l_(592395)
        _c_(592401, _a_(592398, _a_(592397, _n_(592396, "self", lambda: self), "radioButton"), "setText"), _c_(592400, _n_(592399, "_translate", lambda: _translate), "Test", "Ok"))
        _l_(592402)
        _c_(592408, _a_(592405, _a_(592404, _n_(592403, "self", lambda: self), "radioButton_2"), "setText"), _c_(592407, _n_(592406, "_translate", lambda: _translate), "Test", "Failed"))
        _l_(592409)
        _c_(592415, _a_(592412, _a_(592411, _n_(592410, "self", lambda: self), "pushButton"), "setText"), _c_(592414, _n_(592413, "_translate", lambda: _translate), "Test", "Start"))
        _l_(592416)



if _n_(592419, "__name__", lambda: __name__) == "__main__":
    _l_(592451)

    try:
        import sys
        _l_(592421)

    except ImportError:
        pass
    app = _c_(592426, _a_(592423, _n_(592422, "QtWidgets", lambda: QtWidgets), "QApplication"), _a_(592425, _n_(592424, "sys", lambda: sys), "argv"))
    _l_(592427)
    Test = _c_(592430, _a_(592429, _n_(592428, "QtWidgets", lambda: QtWidgets), "QMainWindow"))
    _l_(592431)
    ui = _c_(592433, _n_(592432, "Ui_Test", lambda: Ui_Test))
    _l_(592434)
    _c_(592438, _a_(592436, _n_(592435, "ui", lambda: ui), "setupUi"), _n_(592437, "Test", lambda: Test))
    _l_(592439)
    _c_(592442, _a_(592441, _n_(592440, "Test", lambda: Test), "show"))
    _l_(592443)
    _c_(592449, _a_(592445, _n_(592444, "sys", lambda: sys), "exit"), _c_(592448, _a_(592447, _n_(592446, "app", lambda: app), "exec_")))
    _l_(592450)