# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77564932/typeerror-unsupported-format-string-passed-to-list-format-while-trying-to-e
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(367846)

except ImportError:
    pass
try:
    import sys
    _l_(367848)

except ImportError:
    pass
try:
    from PySide6.QtCore import Qt, Slot
    _l_(367850)

except ImportError:
    pass
try:
    from PySide6.QtGui import QAction , QPainter
    _l_(367852)

except ImportError:
    pass
try:
    from PySide6.QtWidgets import (QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit, 
                                   QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, 
                                   QWidget)
    _l_(367854)

except ImportError:
    pass
try:
    from PySide6.QtCharts import QChartView, QPieSeries, QChart
    _l_(367856)

except ImportError:
    pass




class Widget(_n_(367857, "QWidget", lambda: QWidget)):
    _l_(368333)

    def __init__(self):
        _l_(368114)

        _c_(367861, _a_(367859, _n_(367858, "QWidget", lambda: QWidget), "__init__"), _n_(367860, "self", lambda: self))
        _l_(367862)
        _n_(367863, "self", lambda: self).items = 0
        _l_(367864)
        #Dummy Data
        _n_(367865, "self", lambda: self)._data = {"Water": [24], 
                      "Rent": [1000], 
                      "Coffee": [30],
                      "Grocery": [300], 
                      "Phone": [45], 
                      "Internet": [70]}
        _l_(367866)
        with _c_(367868, _n_(367867, "open", lambda: open), "aib_october.csv", 'w', newline='') as file:
            _l_(367886)

            writer = _c_(367874, _a_(367870, _n_(367869, "csv", lambda: csv), "DictWriter"), _n_(367871, "file", lambda: file),fieldnames=_a_(367873, _n_(367872, "self", lambda: self), "_data"))
            _l_(367875)
            _c_(367878, _a_(367877, _n_(367876, "writer", lambda: writer), "writeheader"))
            _l_(367879)
            _c_(367884, _a_(367881, _n_(367880, "writer", lambda: writer), "writerow"), _a_(367883, _n_(367882, "self", lambda: self), "_data"))
            _l_(367885)
        # Left Widget
        _n_(367887, "self", lambda: self).table = _c_(367889, _n_(367888, "QTableWidget", lambda: QTableWidget))
        _l_(367890)
        _c_(367894, _a_(367893, _a_(367892, _n_(367891, "self", lambda: self), "table"), "setColumnCount"), 2)
        _l_(367895)
        _c_(367899, _a_(367898, _a_(367897, _n_(367896, "self", lambda: self), "table"), "setHorizontalHeaderLabels"), ["Description", "Price"])
        _l_(367900)
        _c_(367908, _a_(367905, _c_(367904, _a_(367903, _a_(367902, _n_(367901, "self", lambda: self), "table"), "horizontalHeader")), "setSectionResizeMode"), _a_(367907, _n_(367906, "QHeaderView", lambda: QHeaderView), "Stretch"))
        _l_(367909)

        # Chart
        _n_(367910, "self", lambda: self).chart_view = _c_(367912, _n_(367911, "QChartView", lambda: QChartView))
        _l_(367913)
        _c_(367919, _a_(367916, _a_(367915, _n_(367914, "self", lambda: self), "chart_view"), "setRenderHint"), _a_(367918, _n_(367917, "QPainter", lambda: QPainter), "Antialiasing"))
        _l_(367920)

        # Right Widget
        _n_(367921, "self", lambda: self).description = _c_(367923, _n_(367922, "QLineEdit", lambda: QLineEdit))
        _l_(367924)
        _n_(367925, "self", lambda: self).price = _c_(367927, _n_(367926, "QLineEdit", lambda: QLineEdit))
        _l_(367928)
        _n_(367929, "self", lambda: self).add = _c_(367931, _n_(367930, "QPushButton", lambda: QPushButton), "Add")
        _l_(367932)
        _n_(367933, "self", lambda: self).clear = _c_(367935, _n_(367934, "QPushButton", lambda: QPushButton), "Clear")
        _l_(367936)
        _n_(367937, "self", lambda: self).quit = _c_(367939, _n_(367938, "QPushButton", lambda: QPushButton), "Quit")
        _l_(367940)
        _n_(367941, "self", lambda: self).plot = _c_(367943, _n_(367942, "QPushButton", lambda: QPushButton), "Plot")
        _l_(367944)
        _n_(367945, "self", lambda: self).export = _c_(367947, _n_(367946, "QPushButton", lambda: QPushButton), "export")
        _l_(367948)

        # Disabling 'Add' button
        _c_(367952, _a_(367951, _a_(367950, _n_(367949, "self", lambda: self), "add"), "setEnabled"), False)
        _l_(367953)

        _n_(367954, "self", lambda: self).right = _c_(367956, _n_(367955, "QVBoxLayout", lambda: QVBoxLayout))
        _l_(367957)
        _c_(367963, _a_(367960, _a_(367959, _n_(367958, "self", lambda: self), "right"), "addWidget"), _c_(367962, _n_(367961, "QLabel", lambda: QLabel), "Description"))
        _l_(367964)
        _c_(367970, _a_(367967, _a_(367966, _n_(367965, "self", lambda: self), "right"), "addWidget"), _a_(367969, _n_(367968, "self", lambda: self), "description"))
        _l_(367971)
        _c_(367977, _a_(367974, _a_(367973, _n_(367972, "self", lambda: self), "right"), "addWidget"), _c_(367976, _n_(367975, "QLabel", lambda: QLabel), "Price"))
        _l_(367978)
        _c_(367984, _a_(367981, _a_(367980, _n_(367979, "self", lambda: self), "right"), "addWidget"), _a_(367983, _n_(367982, "self", lambda: self), "price"))
        _l_(367985)
        _c_(367991, _a_(367988, _a_(367987, _n_(367986, "self", lambda: self), "right"), "addWidget"), _a_(367990, _n_(367989, "self", lambda: self), "add"))
        _l_(367992)
        _c_(367998, _a_(367995, _a_(367994, _n_(367993, "self", lambda: self), "right"), "addWidget"), _a_(367997, _n_(367996, "self", lambda: self), "plot"))
        _l_(367999)
        _c_(368005, _a_(368002, _a_(368001, _n_(368000, "self", lambda: self), "right"), "addWidget"), _a_(368004, _n_(368003, "self", lambda: self), "chart_view"))
        _l_(368006)
        _c_(368012, _a_(368009, _a_(368008, _n_(368007, "self", lambda: self), "right"), "addWidget"), _a_(368011, _n_(368010, "self", lambda: self), "export"))
        _l_(368013)
        _c_(368019, _a_(368016, _a_(368015, _n_(368014, "self", lambda: self), "right"), "addWidget"), _a_(368018, _n_(368017, "self", lambda: self), "clear"))
        _l_(368020)
        _c_(368026, _a_(368023, _a_(368022, _n_(368021, "self", lambda: self), "right"), "addWidget"), _a_(368025, _n_(368024, "self", lambda: self), "quit"))
        _l_(368027)

        # QWidget Layout
        _n_(368028, "self", lambda: self).layout = _c_(368030, _n_(368029, "QHBoxLayout", lambda: QHBoxLayout))
        _l_(368031)

        #self.table_view.setSizePolicy(size)
        _c_(368037, _a_(368034, _a_(368033, _n_(368032, "self", lambda: self), "layout"), "addWidget"), _a_(368036, _n_(368035, "self", lambda: self), "table"))
        _l_(368038)
        _c_(368044, _a_(368041, _a_(368040, _n_(368039, "self", lambda: self), "layout"), "addLayout"), _a_(368043, _n_(368042, "self", lambda: self), "right"))
        _l_(368045)

        # Set the layout to the QWidget
        _c_(368050, _a_(368047, _n_(368046, "self", lambda: self), "setLayout"), _a_(368049, _n_(368048, "self", lambda: self), "layout"))
        _l_(368051)

        # Signals and Slots
        _c_(368058, _a_(368055, _a_(368054, _a_(368053, _n_(368052, "self", lambda: self), "add"), "clicked"), "connect"), _a_(368057, _n_(368056, "self", lambda: self), "add_element"))
        _l_(368059)
        _c_(368066, _a_(368063, _a_(368062, _a_(368061, _n_(368060, "self", lambda: self), "quit"), "clicked"), "connect"), _a_(368065, _n_(368064, "self", lambda: self), "quit_application"))
        _l_(368067)
        _c_(368074, _a_(368071, _a_(368070, _a_(368069, _n_(368068, "self", lambda: self), "plot"), "clicked"), "connect"), _a_(368073, _n_(368072, "self", lambda: self), "plot_data"))
        _l_(368075)
        _c_(368082, _a_(368079, _a_(368078, _a_(368077, _n_(368076, "self", lambda: self), "clear"), "clicked"), "connect"), _a_(368081, _n_(368080, "self", lambda: self), "clear_table"))
        _l_(368083)
        _c_(368090, _a_(368087, _a_(368086, _a_(368085, _n_(368084, "self", lambda: self), "export"), "clicked"), "connect"), _a_(368089, _n_(368088, "self", lambda: self), "clear_table"))
        _l_(368091)
        _c_(368099, _a_(368096, _a_(368094, _a_(368093, _n_(368092, "self", lambda: self), "description"), "textChanged")[_n_(368095, "str", lambda: str)], "connect"), _a_(368098, _n_(368097, "self", lambda: self), "check_disable"))
        _l_(368100)
        _c_(368108, _a_(368105, _a_(368103, _a_(368102, _n_(368101, "self", lambda: self), "price"), "textChanged")[_n_(368104, "str", lambda: str)], "connect"), _a_(368107, _n_(368106, "self", lambda: self), "check_disable"))
        _l_(368109)

        # Fill example data
        _c_(368112, _a_(368111, _n_(368110, "self", lambda: self), "fill_table"))
        _l_(368113)

    @_c_(368116, _n_(368115, "Slot", lambda: Slot))
    def add_element(self):
        _l_(368185)

        des = _c_(368120, _a_(368119, _a_(368118, _n_(368117, "self", lambda: self), "description"), "text"))
        _l_(368121)
        price = _c_(368125, _a_(368124, _a_(368123, _n_(368122, "self", lambda: self), "price"), "text"))
        _l_(368126)

        try:
            _l_(368184)

            price_item = _c_(368131, _n_(368127, "QTableWidgetItem", lambda: QTableWidgetItem), f"{_c_(368130, _n_(368128, 'float', lambda: float), _n_(368129, 'price', lambda: price)):.2f}")
            _l_(368132)
            _c_(368137, _a_(368134, _n_(368133, "price_item", lambda: price_item), "setTextAlignment"), _a_(368136, _n_(368135, "Qt", lambda: Qt), "AlignRight"))
            _l_(368138)

            _c_(368144, _a_(368141, _a_(368140, _n_(368139, "self", lambda: self), "table"), "insertRow"), _a_(368143, _n_(368142, "self", lambda: self), "items"))
            _l_(368145)
            description_item = _c_(368148, _n_(368146, "QTableWidgetItem", lambda: QTableWidgetItem), _n_(368147, "des", lambda: des))
            _l_(368149)

            _c_(368156, _a_(368152, _a_(368151, _n_(368150, "self", lambda: self), "table"), "setItem"), _a_(368154, _n_(368153, "self", lambda: self), "items"), 0, _n_(368155, "description_item", lambda: description_item))
            _l_(368157)
            _c_(368164, _a_(368160, _a_(368159, _n_(368158, "self", lambda: self), "table"), "setItem"), _a_(368162, _n_(368161, "self", lambda: self), "items"), 1, _n_(368163, "price_item", lambda: price_item))
            _l_(368165)

            _c_(368169, _a_(368168, _a_(368167, _n_(368166, "self", lambda: self), "description"), "setText"), "")
            _l_(368170)
            _c_(368174, _a_(368173, _a_(368172, _n_(368171, "self", lambda: self), "price"), "setText"), "")
            _l_(368175)

            _n_(368176, "self", lambda: self).items += 1
            _l_(368177)
        except _n_(368178, "ValueError", lambda: ValueError):
            _l_(368183)

            _c_(368181, _n_(368179, "print", lambda: print), "That is not an invalid input:", _n_(368180, "price", lambda: price), "Make sure to enter a price!")
            _l_(368182)


    @_c_(368187, _n_(368186, "Slot", lambda: Slot))
    def check_disable(self, x):
        _l_(368207)

        if not _c_(368191, _a_(368190, _a_(368189, _n_(368188, "self", lambda: self), "description"), "text")) or not _c_(368195, _a_(368194, _a_(368193, _n_(368192, "self", lambda: self), "price"), "text")):
            _l_(368206)

            _c_(368199, _a_(368198, _a_(368197, _n_(368196, "self", lambda: self), "add"), "setEnabled"), False)
            _l_(368200)
        else:
            _c_(368204, _a_(368203, _a_(368202, _n_(368201, "self", lambda: self), "add"), "setEnabled"), True)
            _l_(368205)

    @_c_(368209, _n_(368208, "Slot", lambda: Slot))
    def plot_data(self):
        _l_(368266)

        # Get table information
        series = _c_(368211, _n_(368210, "QPieSeries", lambda: QPieSeries))
        _l_(368212)
        for i in _c_(368218, _n_(368213, "range", lambda: range), _c_(368217, _a_(368216, _a_(368215, _n_(368214, "self", lambda: self), "table"), "rowCount"))):
            _l_(368243)

            text = _c_(368225, _a_(368224, _c_(368223, _a_(368221, _a_(368220, _n_(368219, "self", lambda: self), "table"), "item"), _n_(368222, "i", lambda: i), 0), "text"))
            _l_(368226)
            number = _c_(368235, _n_(368227, "float", lambda: float), _c_(368234, _a_(368233, _c_(368232, _a_(368230, _a_(368229, _n_(368228, "self", lambda: self), "table"), "item"), _n_(368231, "i", lambda: i), 1), "text")))
            _l_(368236)
            _c_(368241, _a_(368238, _n_(368237, "series", lambda: series), "append"), _n_(368239, "text", lambda: text), _n_(368240, "number", lambda: number))
            _l_(368242)

        chart = _c_(368245, _n_(368244, "QChart", lambda: QChart))
        _l_(368246)
        _c_(368250, _a_(368248, _n_(368247, "chart", lambda: chart), "addSeries"), _n_(368249, "series", lambda: series))
        _l_(368251)
        _c_(368258, _a_(368255, _c_(368254, _a_(368253, _n_(368252, "chart", lambda: chart), "legend")), "setAlignment"), _a_(368257, _n_(368256, "Qt", lambda: Qt), "AlignLeft"))
        _l_(368259)
        _c_(368264, _a_(368262, _a_(368261, _n_(368260, "self", lambda: self), "chart_view"), "setChart"), _n_(368263, "chart", lambda: chart))
        _l_(368265)

    @_c_(368268, _n_(368267, "Slot", lambda: Slot))
    def quit_application(self):
        _l_(368273)

        _c_(368271, _a_(368270, _n_(368269, "QApplication", lambda: QApplication), "quit"))
        _l_(368272)

    def fill_table(self, data=None):
        _l_(368322)

        data = _a_(368275, _n_(368274, "self", lambda: self), "_data") if not _n_(368276, "data", lambda: data) else _n_(368277, "data", lambda: data)
        _l_(368278)
        for desc, price in _c_(368281, _a_(368280, _n_(368279, "data", lambda: data), "items")):
            _l_(368321)

            description_item = _c_(368284, _n_(368282, "QTableWidgetItem", lambda: QTableWidgetItem), _n_(368283, "desc", lambda: desc))
            _l_(368285)
            price_item = _c_(368288, _n_(368286, "QTableWidgetItem", lambda: QTableWidgetItem), f"{_n_(368287, 'price', lambda: price):.2f}")
            _l_(368289)
            _c_(368294, _a_(368291, _n_(368290, "price_item", lambda: price_item), "setTextAlignment"), _a_(368293, _n_(368292, "Qt", lambda: Qt), "AlignRight"))
            _l_(368295)
            _c_(368301, _a_(368298, _a_(368297, _n_(368296, "self", lambda: self), "table"), "insertRow"), _a_(368300, _n_(368299, "self", lambda: self), "items"))
            _l_(368302)
            _c_(368309, _a_(368305, _a_(368304, _n_(368303, "self", lambda: self), "table"), "setItem"), _a_(368307, _n_(368306, "self", lambda: self), "items"), 0, _n_(368308, "description_item", lambda: description_item))
            _l_(368310)
            _c_(368317, _a_(368313, _a_(368312, _n_(368311, "self", lambda: self), "table"), "setItem"), _a_(368315, _n_(368314, "self", lambda: self), "items"), 1, _n_(368316, "price_item", lambda: price_item))
            _l_(368318)
            _n_(368319, "self", lambda: self).items += 1
            _l_(368320)

    @_c_(368324, _n_(368323, "Slot", lambda: Slot))
    def clear_table(self):
        _l_(368332)

        _c_(368328, _a_(368327, _a_(368326, _n_(368325, "self", lambda: self), "table"), "setRowCount"), 0)
        _l_(368329)
        _n_(368330, "self", lambda: self).items = 0
        _l_(368331)


class MainWindow(_n_(368334, "QMainWindow", lambda: QMainWindow)):
    _l_(368389)

    def __init__(self, widget):
        _l_(368381)

        _c_(368338, _a_(368336, _n_(368335, "QMainWindow", lambda: QMainWindow), "__init__"), _n_(368337, "self", lambda: self))
        _l_(368339)
        _c_(368342, _a_(368341, _n_(368340, "self", lambda: self), "setWindowTitle"), "The pynancial advisor")
        _l_(368343)

        # Menu
        _n_(368344, "self", lambda: self).menu = _c_(368347, _a_(368346, _n_(368345, "self", lambda: self), "menuBar"))
        _l_(368348)
        _n_(368349, "self", lambda: self).file_menu = _c_(368353, _a_(368352, _a_(368351, _n_(368350, "self", lambda: self), "menu"), "addMenu"), "File")
        _l_(368354)

        # Exit QAction
        exit_action = _c_(368357, _n_(368355, "QAction", lambda: QAction), "Exit", _n_(368356, "self", lambda: self))
        _l_(368358)
        _c_(368361, _a_(368360, _n_(368359, "exit_action", lambda: exit_action), "setShortcut"), "Ctrl+Q")
        _l_(368362)
        _c_(368368, _a_(368365, _a_(368364, _n_(368363, "exit_action", lambda: exit_action), "triggered"), "connect"), _a_(368367, _n_(368366, "self", lambda: self), "exit_app"))
        _l_(368369)

        _c_(368374, _a_(368372, _a_(368371, _n_(368370, "self", lambda: self), "file_menu"), "addAction"), _n_(368373, "exit_action", lambda: exit_action))
        _l_(368375)
        _c_(368379, _a_(368377, _n_(368376, "self", lambda: self), "setCentralWidget"), _n_(368378, "widget", lambda: widget))
        _l_(368380)

    @_c_(368383, _n_(368382, "Slot", lambda: Slot))
    def exit_app(self, checked):
        _l_(368388)

        _c_(368386, _a_(368385, _n_(368384, "QApplication", lambda: QApplication), "quit"))
        _l_(368387)


if _n_(368390, "__name__", lambda: __name__) == "__main__":
    _l_(368418)

    # Qt Application
    app = _c_(368394, _n_(368391, "QApplication", lambda: QApplication), _a_(368393, _n_(368392, "sys", lambda: sys), "argv"))
    _l_(368395)
    # QWidget
    widget = _c_(368397, _n_(368396, "Widget", lambda: Widget))
    _l_(368398)
    # QMainWindow using QWidget as central widget
    window = _c_(368401, _n_(368399, "MainWindow", lambda: MainWindow), _n_(368400, "widget", lambda: widget))
    _l_(368402)
    _c_(368405, _a_(368404, _n_(368403, "window", lambda: window), "resize"), 800, 600)
    _l_(368406)
    _c_(368409, _a_(368408, _n_(368407, "window", lambda: window), "show"))
    _l_(368410)

    # Execute application
    _c_(368416, _a_(368412, _n_(368411, "sys", lambda: sys), "exit"), _c_(368415, _a_(368414, _n_(368413, "app", lambda: app), "exec")))
    _l_(368417)