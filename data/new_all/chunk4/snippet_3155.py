# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36967273/python3-attribute-error-type-object-mainwindow-qmainwindow-has-no-attribute
# Imports all the needed modules.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(602841)

except ImportError:
    pass
try:
    from PyQt4 import QtCore, QtGui
    _l_(602843)

except ImportError:
    pass
try:
    from PyQt4.QtCore import *
    _l_(602845)

except ImportError:
    pass
try:
    from PyQt4.QtGui import *
    _l_(602847)

except ImportError:
    pass

# Defines variables needed for the settings dialog.
currentDate = _c_(602851, _a_(602850, _a_(602849, _n_(602848, "QtCore", lambda: QtCore), "QDate"), "currentDate"))
_l_(602852)
maxDate = _c_(602855, _a_(602854, _n_(602853, "QtCore", lambda: QtCore), "QDate"), 2999, 12, 31)
_l_(602856)

class AppSettingsDialog(_a_(602858, _n_(602857, "QtGui", lambda: QtGui), "QDialog")):
    _l_(602978)

    def __init__(self, parent=None):
        _l_(602895)

        # The initializer function for the dialog.
        _c_(602864, _a_(602862, _n_(602859, "super", lambda: super)(_n_(602860, "AppSettingsDialog", lambda: AppSettingsDialog), _n_(602861, "self", lambda: self)), "__init__"), _n_(602863, "parent", lambda: parent))
        _l_(602865)
        _c_(602870, _a_(602867, _n_(602866, "self", lambda: self), "setAttribute"), _a_(602869, _n_(602868, "Qt", lambda: Qt), "WA_DeleteOnClose"))
        _l_(602871)

        _c_(602874, _a_(602873, _n_(602872, "self", lambda: self), "calendarSpecificSettings"))
        _l_(602875)

        mainGridLayout = _c_(602878, _a_(602877, _n_(602876, "QtGui", lambda: QtGui), "QGridLayout"))
        _l_(602879)
        _c_(602884, _a_(602881, _n_(602880, "mainGridLayout", lambda: mainGridLayout), "addWidget"), _a_(602883, _n_(602882, "self", lambda: self), "calendarSpecificSettingsBox"),
                                 0, 0)
        _l_(602885)
        _c_(602889, _a_(602887, _n_(602886, "self", lambda: self), "setLayout"), _n_(602888, "mainGridLayout", lambda: mainGridLayout))
        _l_(602890)

        _c_(602893, _a_(602892, _n_(602891, "self", lambda: self), "exec_"))
        _l_(602894)

    def calendarSpecificSettings(self):
        _l_(602970)

        # Creates a separator to put the widgets in.
        _n_(602896, "self", lambda: self).calendarSpecificSettingsBox = _c_(602899, _a_(602898, _n_(602897, "QtGui", lambda: QtGui), "QGroupBox"), 'Calendar Specific')
        _l_(602900)

        _n_(602901, "self", lambda: self).maxDateLabel = _c_(602904, _a_(602903, _n_(602902, "QtGui", lambda: QtGui), "QLabel"), 'Ma&ximum Date')
        _l_(602905)
        _n_(602906, "self", lambda: self).maxDateEdit = _c_(602909, _a_(602908, _n_(602907, "QtGui", lambda: QtGui), "QDateEdit"))
        _l_(602910)
        _c_(602914, _a_(602913, _a_(602912, _n_(602911, "self", lambda: self), "maxDateEdit"), "setDisplayFormat"), 'dd MMM yyyy')
        _l_(602915)
        _c_(602921, _a_(602918, _a_(602917, _n_(602916, "self", lambda: self), "maxDateEdit"), "setDateRange"), _n_(602919, "currentDate", lambda: currentDate), _n_(602920, "maxDate", lambda: maxDate))
        _l_(602922)
        _c_(602927, _a_(602925, _a_(602924, _n_(602923, "self", lambda: self), "maxDateEdit"), "setDate"), _n_(602926, "maxDate", lambda: maxDate))
        _l_(602928)
        _c_(602934, _a_(602931, _a_(602930, _n_(602929, "self", lambda: self), "maxDateLabel"), "setBuddy"), _a_(602933, _n_(602932, "self", lambda: self), "maxDateEdit"))
        _l_(602935)
        _c_(602942, _a_(602939, _a_(602938, _a_(602937, _n_(602936, "self", lambda: self), "maxDateEdit"), "dateChanged"), "connect"), _a_(602941, _n_(602940, "self", lambda: self), "maximumDateChanged"))
        _l_(602943)
                    # Call to function error here ^

        _n_(602944, "self", lambda: self).calendarSpecificGridLayout = _c_(602947, _a_(602946, _n_(602945, "QtGui", lambda: QtGui), "QGridLayout"))
        _l_(602948)
        _c_(602954, _a_(602951, _a_(602950, _n_(602949, "self", lambda: self), "calendarSpecificGridLayout"), "addWidget"), _a_(602953, _n_(602952, "self", lambda: self), "maxDateLabel"),
                                                  0, 0)
        _l_(602955)
        _c_(602961, _a_(602958, _a_(602957, _n_(602956, "self", lambda: self), "calendarSpecificGridLayout"), "addWidget"), _a_(602960, _n_(602959, "self", lambda: self), "maxDateEdit"),
                                                  0, 1)
        _l_(602962)

        _c_(602968, _a_(602965, _a_(602964, _n_(602963, "self", lambda: self), "calendarSpecificSettingsBox"), "setLayout"), _a_(602967, _n_(602966, "self", lambda: self), "calendarSpecificGridLayout"))
        _l_(602969)

    def maximumDateChanged(self, date):
        _l_(602977)

        _c_(602975, _a_(602973, _a_(602972, _n_(602971, "MainWindow", lambda: MainWindow), "calWidget"), "setMaximumDate"), _n_(602974, "date", lambda: date))
        _l_(602976)

class MainWindow(_a_(602980, _n_(602979, "QtGui", lambda: QtGui), "QMainWindow")):
    _l_(603051)

    def __init__(self):
        _l_(603046)

        # The initializer function for the window.
        _c_(602985, _a_(602984, _n_(602981, "super", lambda: super)(_n_(602982, "MainWindow", lambda: MainWindow), _n_(602983, "self", lambda: self)), "__init__"))
        _l_(602986)
        mainMenu = _c_(602989, _a_(602988, _n_(602987, "self", lambda: self), "menuBar"))
        _l_(602990)

        menuOptions = _c_(602993, _a_(602992, _n_(602991, "mainMenu", lambda: mainMenu), "addMenu"), 'Options')
        _l_(602994)
        actionSettings = _c_(602998, _a_(602996, _n_(602995, "QtGui", lambda: QtGui), "QAction"), 'Settings...', _n_(602997, "self", lambda: self))
        _l_(602999)
        _c_(603005, _a_(603002, _a_(603001, _n_(603000, "actionSettings", lambda: actionSettings), "triggered"), "connect"), _a_(603004, _n_(603003, "self", lambda: self), "appSettings"))
        _l_(603006)
        _c_(603010, _a_(603008, _n_(603007, "menuOptions", lambda: menuOptions), "addAction"), _n_(603009, "actionSettings", lambda: actionSettings))
        _l_(603011)

        calWidget = _c_(603015, _a_(603013, _n_(603012, "QtGui", lambda: QtGui), "QCalendarWidget"), _n_(603014, "self", lambda: self))
        _l_(603016)
        _c_(603019, _a_(603018, _n_(603017, "calWidget", lambda: calWidget), "resize"), 300, 300)
        _l_(603020)
        _c_(603023, _a_(603022, _n_(603021, "calWidget", lambda: calWidget), "setGridVisible"), True)
        _l_(603024)
        _c_(603027, _a_(603026, _n_(603025, "calWidget", lambda: calWidget), "setNavigationBarVisible"), True)
        _l_(603028)
        _c_(603032, _a_(603030, _n_(603029, "self", lambda: self), "setCentralWidget"), _n_(603031, "calWidget", lambda: calWidget))
        _l_(603033)

        _c_(603038, _a_(603037, _c_(603036, _a_(603035, _n_(603034, "self", lambda: self), "statusBar")), "setSizeGripEnabled"), True)
        _l_(603039)
        _c_(603044, _a_(603043, _c_(603042, _a_(603041, _n_(603040, "self", lambda: self), "statusBar")), "showMessage"), 'Ready', 5000)
        _l_(603045)

    def appSettings(self):
        _l_(603050)

        # The function that invokes the dialog.
        _c_(603048, _n_(603047, "AppSettingsDialog", lambda: AppSettingsDialog))
        _l_(603049)

# One way to initialize the application.
if _n_(603052, "__name__", lambda: __name__) == '__main__':
    _l_(603073)

    app = _c_(603057, _a_(603054, _n_(603053, "QtGui", lambda: QtGui), "QApplication"), _a_(603056, _n_(603055, "sys", lambda: sys), "argv"))
    _l_(603058)
    GUI = _c_(603060, _n_(603059, "MainWindow", lambda: MainWindow))
    _l_(603061)
    _c_(603064, _a_(603063, _n_(603062, "GUI", lambda: GUI), "show"))
    _l_(603065)
    _c_(603071, _a_(603067, _n_(603066, "sys", lambda: sys), "exit"), _c_(603070, _a_(603069, _n_(603068, "app", lambda: app), "exec_")))
    _l_(603072)