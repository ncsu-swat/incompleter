# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77564932/typeerror-unsupported-format-string-passed-to-list-format-while-trying-to-e
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(422931)

except ImportError:
    pass
try:
    import sys
    _l_(422933)

except ImportError:
    pass
try:
    from PySide6.QtCore import Qt, Slot
    _l_(422935)

except ImportError:
    pass
try:
    from PySide6.QtGui import QAction , QPainter
    _l_(422937)

except ImportError:
    pass
try:
    from PySide6.QtWidgets import (QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit, 
                                   QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, 
                                   QWidget)
    _l_(422939)

except ImportError:
    pass
try:
    from PySide6.QtCharts import QChartView, QPieSeries, QChart
    _l_(422941)

except ImportError:
    pass




class Widget(_n_(422942, "QWidget", lambda: QWidget)):
    _l_(423418)

    def __init__(self):
        _l_(423199)

        _c_(422946, _a_(422944, _n_(422943, "QWidget", lambda: QWidget), "__init__"), _n_(422945, "self", lambda: self))
        _l_(422947)
        _n_(422948, "self", lambda: self).items = 0
        _l_(422949)
        #Dummy Data
        _n_(422950, "self", lambda: self)._data = {"Water": [24], 
                      "Rent": [1000], 
                      "Coffee": [30],
                      "Grocery": [300], 
                      "Phone": [45], 
                      "Internet": [70]}
        _l_(422951)
        with _c_(422953, _n_(422952, "open", lambda: open), "aib_october.csv", 'w', newline='') as file:
            _l_(422971)

            writer = _c_(422959, _a_(422955, _n_(422954, "csv", lambda: csv), "DictWriter"), _n_(422956, "file", lambda: file),fieldnames=_a_(422958, _n_(422957, "self", lambda: self), "_data"))
            _l_(422960)
            _c_(422963, _a_(422962, _n_(422961, "writer", lambda: writer), "writeheader"))
            _l_(422964)
            _c_(422969, _a_(422966, _n_(422965, "writer", lambda: writer), "writerow"), _a_(422968, _n_(422967, "self", lambda: self), "_data"))
            _l_(422970)
        # Left Widget
        _n_(422972, "self", lambda: self).table = _c_(422974, _n_(422973, "QTableWidget", lambda: QTableWidget))
        _l_(422975)
        _c_(422979, _a_(422978, _a_(422977, _n_(422976, "self", lambda: self), "table"), "setColumnCount"), 2)
        _l_(422980)
        _c_(422984, _a_(422983, _a_(422982, _n_(422981, "self", lambda: self), "table"), "setHorizontalHeaderLabels"), ["Description", "Price"])
        _l_(422985)
        _c_(422993, _a_(422990, _c_(422989, _a_(422988, _a_(422987, _n_(422986, "self", lambda: self), "table"), "horizontalHeader")), "setSectionResizeMode"), _a_(422992, _n_(422991, "QHeaderView", lambda: QHeaderView), "Stretch"))
        _l_(422994)

        # Chart
        _n_(422995, "self", lambda: self).chart_view = _c_(422997, _n_(422996, "QChartView", lambda: QChartView))
        _l_(422998)
        _c_(423004, _a_(423001, _a_(423000, _n_(422999, "self", lambda: self), "chart_view"), "setRenderHint"), _a_(423003, _n_(423002, "QPainter", lambda: QPainter), "Antialiasing"))
        _l_(423005)

        # Right Widget
        _n_(423006, "self", lambda: self).description = _c_(423008, _n_(423007, "QLineEdit", lambda: QLineEdit))
        _l_(423009)
        _n_(423010, "self", lambda: self).price = _c_(423012, _n_(423011, "QLineEdit", lambda: QLineEdit))
        _l_(423013)
        _n_(423014, "self", lambda: self).add = _c_(423016, _n_(423015, "QPushButton", lambda: QPushButton), "Add")
        _l_(423017)
        _n_(423018, "self", lambda: self).clear = _c_(423020, _n_(423019, "QPushButton", lambda: QPushButton), "Clear")
        _l_(423021)
        _n_(423022, "self", lambda: self).quit = _c_(423024, _n_(423023, "QPushButton", lambda: QPushButton), "Quit")
        _l_(423025)
        _n_(423026, "self", lambda: self).plot = _c_(423028, _n_(423027, "QPushButton", lambda: QPushButton), "Plot")
        _l_(423029)
        _n_(423030, "self", lambda: self).export = _c_(423032, _n_(423031, "QPushButton", lambda: QPushButton), "export")
        _l_(423033)

        # Disabling 'Add' button
        _c_(423037, _a_(423036, _a_(423035, _n_(423034, "self", lambda: self), "add"), "setEnabled"), False)
        _l_(423038)

        _n_(423039, "self", lambda: self).right = _c_(423041, _n_(423040, "QVBoxLayout", lambda: QVBoxLayout))
        _l_(423042)
        _c_(423048, _a_(423045, _a_(423044, _n_(423043, "self", lambda: self), "right"), "addWidget"), _c_(423047, _n_(423046, "QLabel", lambda: QLabel), "Description"))
        _l_(423049)
        _c_(423055, _a_(423052, _a_(423051, _n_(423050, "self", lambda: self), "right"), "addWidget"), _a_(423054, _n_(423053, "self", lambda: self), "description"))
        _l_(423056)
        _c_(423062, _a_(423059, _a_(423058, _n_(423057, "self", lambda: self), "right"), "addWidget"), _c_(423061, _n_(423060, "QLabel", lambda: QLabel), "Price"))
        _l_(423063)
        _c_(423069, _a_(423066, _a_(423065, _n_(423064, "self", lambda: self), "right"), "addWidget"), _a_(423068, _n_(423067, "self", lambda: self), "price"))
        _l_(423070)
        _c_(423076, _a_(423073, _a_(423072, _n_(423071, "self", lambda: self), "right"), "addWidget"), _a_(423075, _n_(423074, "self", lambda: self), "add"))
        _l_(423077)
        _c_(423083, _a_(423080, _a_(423079, _n_(423078, "self", lambda: self), "right"), "addWidget"), _a_(423082, _n_(423081, "self", lambda: self), "plot"))
        _l_(423084)
        _c_(423090, _a_(423087, _a_(423086, _n_(423085, "self", lambda: self), "right"), "addWidget"), _a_(423089, _n_(423088, "self", lambda: self), "chart_view"))
        _l_(423091)
        _c_(423097, _a_(423094, _a_(423093, _n_(423092, "self", lambda: self), "right"), "addWidget"), _a_(423096, _n_(423095, "self", lambda: self), "export"))
        _l_(423098)
        _c_(423104, _a_(423101, _a_(423100, _n_(423099, "self", lambda: self), "right"), "addWidget"), _a_(423103, _n_(423102, "self", lambda: self), "clear"))
        _l_(423105)
        _c_(423111, _a_(423108, _a_(423107, _n_(423106, "self", lambda: self), "right"), "addWidget"), _a_(423110, _n_(423109, "self", lambda: self), "quit"))
        _l_(423112)

        # QWidget Layout
        _n_(423113, "self", lambda: self).layout = _c_(423115, _n_(423114, "QHBoxLayout", lambda: QHBoxLayout))
        _l_(423116)

        #self.table_view.setSizePolicy(size)
        _c_(423122, _a_(423119, _a_(423118, _n_(423117, "self", lambda: self), "layout"), "addWidget"), _a_(423121, _n_(423120, "self", lambda: self), "table"))
        _l_(423123)
        _c_(423129, _a_(423126, _a_(423125, _n_(423124, "self", lambda: self), "layout"), "addLayout"), _a_(423128, _n_(423127, "self", lambda: self), "right"))
        _l_(423130)

        # Set the layout to the QWidget
        _c_(423135, _a_(423132, _n_(423131, "self", lambda: self), "setLayout"), _a_(423134, _n_(423133, "self", lambda: self), "layout"))
        _l_(423136)

        # Signals and Slots
        _c_(423143, _a_(423140, _a_(423139, _a_(423138, _n_(423137, "self", lambda: self), "add"), "clicked"), "connect"), _a_(423142, _n_(423141, "self", lambda: self), "add_element"))
        _l_(423144)
        _c_(423151, _a_(423148, _a_(423147, _a_(423146, _n_(423145, "self", lambda: self), "quit"), "clicked"), "connect"), _a_(423150, _n_(423149, "self", lambda: self), "quit_application"))
        _l_(423152)
        _c_(423159, _a_(423156, _a_(423155, _a_(423154, _n_(423153, "self", lambda: self), "plot"), "clicked"), "connect"), _a_(423158, _n_(423157, "self", lambda: self), "plot_data"))
        _l_(423160)
        _c_(423167, _a_(423164, _a_(423163, _a_(423162, _n_(423161, "self", lambda: self), "clear"), "clicked"), "connect"), _a_(423166, _n_(423165, "self", lambda: self), "clear_table"))
        _l_(423168)
        _c_(423175, _a_(423172, _a_(423171, _a_(423170, _n_(423169, "self", lambda: self), "export"), "clicked"), "connect"), _a_(423174, _n_(423173, "self", lambda: self), "clear_table"))
        _l_(423176)
        _c_(423184, _a_(423181, _a_(423179, _a_(423178, _n_(423177, "self", lambda: self), "description"), "textChanged")[_n_(423180, "str", lambda: str)], "connect"), _a_(423183, _n_(423182, "self", lambda: self), "check_disable"))
        _l_(423185)
        _c_(423193, _a_(423190, _a_(423188, _a_(423187, _n_(423186, "self", lambda: self), "price"), "textChanged")[_n_(423189, "str", lambda: str)], "connect"), _a_(423192, _n_(423191, "self", lambda: self), "check_disable"))
        _l_(423194)

        # Fill example data
        _c_(423197, _a_(423196, _n_(423195, "self", lambda: self), "fill_table"))
        _l_(423198)

    @_c_(423201, _n_(423200, "Slot", lambda: Slot))
    def add_element(self):
        _l_(423270)

        des = _c_(423205, _a_(423204, _a_(423203, _n_(423202, "self", lambda: self), "description"), "text"))
        _l_(423206)
        price = _c_(423210, _a_(423209, _a_(423208, _n_(423207, "self", lambda: self), "price"), "text"))
        _l_(423211)

        try:
            _l_(423269)

            price_item = _c_(423216, _n_(423212, "QTableWidgetItem", lambda: QTableWidgetItem), f"{_c_(423215, _n_(423213, 'float', lambda: float), _n_(423214, 'price', lambda: price)):.2f}")
            _l_(423217)
            _c_(423222, _a_(423219, _n_(423218, "price_item", lambda: price_item), "setTextAlignment"), _a_(423221, _n_(423220, "Qt", lambda: Qt), "AlignRight"))
            _l_(423223)

            _c_(423229, _a_(423226, _a_(423225, _n_(423224, "self", lambda: self), "table"), "insertRow"), _a_(423228, _n_(423227, "self", lambda: self), "items"))
            _l_(423230)
            description_item = _c_(423233, _n_(423231, "QTableWidgetItem", lambda: QTableWidgetItem), _n_(423232, "des", lambda: des))
            _l_(423234)

            _c_(423241, _a_(423237, _a_(423236, _n_(423235, "self", lambda: self), "table"), "setItem"), _a_(423239, _n_(423238, "self", lambda: self), "items"), 0, _n_(423240, "description_item", lambda: description_item))
            _l_(423242)
            _c_(423249, _a_(423245, _a_(423244, _n_(423243, "self", lambda: self), "table"), "setItem"), _a_(423247, _n_(423246, "self", lambda: self), "items"), 1, _n_(423248, "price_item", lambda: price_item))
            _l_(423250)

            _c_(423254, _a_(423253, _a_(423252, _n_(423251, "self", lambda: self), "description"), "setText"), "")
            _l_(423255)
            _c_(423259, _a_(423258, _a_(423257, _n_(423256, "self", lambda: self), "price"), "setText"), "")
            _l_(423260)

            _n_(423261, "self", lambda: self).items += 1
            _l_(423262)
        except _n_(423263, "ValueError", lambda: ValueError):
            _l_(423268)

            _c_(423266, _n_(423264, "print", lambda: print), "That is not an invalid input:", _n_(423265, "price", lambda: price), "Make sure to enter a price!")
            _l_(423267)


    @_c_(423272, _n_(423271, "Slot", lambda: Slot))
    def check_disable(self, x):
        _l_(423292)

        if not _c_(423276, _a_(423275, _a_(423274, _n_(423273, "self", lambda: self), "description"), "text")) or not _c_(423280, _a_(423279, _a_(423278, _n_(423277, "self", lambda: self), "price"), "text")):
            _l_(423291)

            _c_(423284, _a_(423283, _a_(423282, _n_(423281, "self", lambda: self), "add"), "setEnabled"), False)
            _l_(423285)
        else:
            _c_(423289, _a_(423288, _a_(423287, _n_(423286, "self", lambda: self), "add"), "setEnabled"), True)
            _l_(423290)

    @_c_(423294, _n_(423293, "Slot", lambda: Slot))
    def plot_data(self):
        _l_(423351)

        # Get table information
        series = _c_(423296, _n_(423295, "QPieSeries", lambda: QPieSeries))
        _l_(423297)
        for i in _c_(423303, _n_(423298, "range", lambda: range), _c_(423302, _a_(423301, _a_(423300, _n_(423299, "self", lambda: self), "table"), "rowCount"))):
            _l_(423328)

            text = _c_(423310, _a_(423309, _c_(423308, _a_(423306, _a_(423305, _n_(423304, "self", lambda: self), "table"), "item"), _n_(423307, "i", lambda: i), 0), "text"))
            _l_(423311)
            number = _c_(423320, _n_(423312, "float", lambda: float), _c_(423319, _a_(423318, _c_(423317, _a_(423315, _a_(423314, _n_(423313, "self", lambda: self), "table"), "item"), _n_(423316, "i", lambda: i), 1), "text")))
            _l_(423321)
            _c_(423326, _a_(423323, _n_(423322, "series", lambda: series), "append"), _n_(423324, "text", lambda: text), _n_(423325, "number", lambda: number))
            _l_(423327)

        chart = _c_(423330, _n_(423329, "QChart", lambda: QChart))
        _l_(423331)
        _c_(423335, _a_(423333, _n_(423332, "chart", lambda: chart), "addSeries"), _n_(423334, "series", lambda: series))
        _l_(423336)
        _c_(423343, _a_(423340, _c_(423339, _a_(423338, _n_(423337, "chart", lambda: chart), "legend")), "setAlignment"), _a_(423342, _n_(423341, "Qt", lambda: Qt), "AlignLeft"))
        _l_(423344)
        _c_(423349, _a_(423347, _a_(423346, _n_(423345, "self", lambda: self), "chart_view"), "setChart"), _n_(423348, "chart", lambda: chart))
        _l_(423350)

    @_c_(423353, _n_(423352, "Slot", lambda: Slot))
    def quit_application(self):
        _l_(423358)

        _c_(423356, _a_(423355, _n_(423354, "QApplication", lambda: QApplication), "quit"))
        _l_(423357)

    def fill_table(self, data=None):
        _l_(423407)

        data = _a_(423360, _n_(423359, "self", lambda: self), "_data") if not _n_(423361, "data", lambda: data) else _n_(423362, "data", lambda: data)
        _l_(423363)
        for desc, price in _c_(423366, _a_(423365, _n_(423364, "data", lambda: data), "items")):
            _l_(423406)

            description_item = _c_(423369, _n_(423367, "QTableWidgetItem", lambda: QTableWidgetItem), _n_(423368, "desc", lambda: desc))
            _l_(423370)
            price_item = _c_(423373, _n_(423371, "QTableWidgetItem", lambda: QTableWidgetItem), f"{_n_(423372, 'price', lambda: price):.2f}")
            _l_(423374)
            _c_(423379, _a_(423376, _n_(423375, "price_item", lambda: price_item), "setTextAlignment"), _a_(423378, _n_(423377, "Qt", lambda: Qt), "AlignRight"))
            _l_(423380)
            _c_(423386, _a_(423383, _a_(423382, _n_(423381, "self", lambda: self), "table"), "insertRow"), _a_(423385, _n_(423384, "self", lambda: self), "items"))
            _l_(423387)
            _c_(423394, _a_(423390, _a_(423389, _n_(423388, "self", lambda: self), "table"), "setItem"), _a_(423392, _n_(423391, "self", lambda: self), "items"), 0, _n_(423393, "description_item", lambda: description_item))
            _l_(423395)
            _c_(423402, _a_(423398, _a_(423397, _n_(423396, "self", lambda: self), "table"), "setItem"), _a_(423400, _n_(423399, "self", lambda: self), "items"), 1, _n_(423401, "price_item", lambda: price_item))
            _l_(423403)
            _n_(423404, "self", lambda: self).items += 1
            _l_(423405)

    @_c_(423409, _n_(423408, "Slot", lambda: Slot))
    def clear_table(self):
        _l_(423417)

        _c_(423413, _a_(423412, _a_(423411, _n_(423410, "self", lambda: self), "table"), "setRowCount"), 0)
        _l_(423414)
        _n_(423415, "self", lambda: self).items = 0
        _l_(423416)


class MainWindow(_n_(423419, "QMainWindow", lambda: QMainWindow)):
    _l_(423474)

    def __init__(self, widget):
        _l_(423466)

        _c_(423423, _a_(423421, _n_(423420, "QMainWindow", lambda: QMainWindow), "__init__"), _n_(423422, "self", lambda: self))
        _l_(423424)
        _c_(423427, _a_(423426, _n_(423425, "self", lambda: self), "setWindowTitle"), "The pynancial advisor")
        _l_(423428)

        # Menu
        _n_(423429, "self", lambda: self).menu = _c_(423432, _a_(423431, _n_(423430, "self", lambda: self), "menuBar"))
        _l_(423433)
        _n_(423434, "self", lambda: self).file_menu = _c_(423438, _a_(423437, _a_(423436, _n_(423435, "self", lambda: self), "menu"), "addMenu"), "File")
        _l_(423439)

        # Exit QAction
        exit_action = _c_(423442, _n_(423440, "QAction", lambda: QAction), "Exit", _n_(423441, "self", lambda: self))
        _l_(423443)
        _c_(423446, _a_(423445, _n_(423444, "exit_action", lambda: exit_action), "setShortcut"), "Ctrl+Q")
        _l_(423447)
        _c_(423453, _a_(423450, _a_(423449, _n_(423448, "exit_action", lambda: exit_action), "triggered"), "connect"), _a_(423452, _n_(423451, "self", lambda: self), "exit_app"))
        _l_(423454)

        _c_(423459, _a_(423457, _a_(423456, _n_(423455, "self", lambda: self), "file_menu"), "addAction"), _n_(423458, "exit_action", lambda: exit_action))
        _l_(423460)
        _c_(423464, _a_(423462, _n_(423461, "self", lambda: self), "setCentralWidget"), _n_(423463, "widget", lambda: widget))
        _l_(423465)

    @_c_(423468, _n_(423467, "Slot", lambda: Slot))
    def exit_app(self, checked):
        _l_(423473)

        _c_(423471, _a_(423470, _n_(423469, "QApplication", lambda: QApplication), "quit"))
        _l_(423472)


if _n_(423475, "__name__", lambda: __name__) == "__main__":
    _l_(423503)

    # Qt Application
    app = _c_(423479, _n_(423476, "QApplication", lambda: QApplication), _a_(423478, _n_(423477, "sys", lambda: sys), "argv"))
    _l_(423480)
    # QWidget
    widget = _c_(423482, _n_(423481, "Widget", lambda: Widget))
    _l_(423483)
    # QMainWindow using QWidget as central widget
    window = _c_(423486, _n_(423484, "MainWindow", lambda: MainWindow), _n_(423485, "widget", lambda: widget))
    _l_(423487)
    _c_(423490, _a_(423489, _n_(423488, "window", lambda: window), "resize"), 800, 600)
    _l_(423491)
    _c_(423494, _a_(423493, _n_(423492, "window", lambda: window), "show"))
    _l_(423495)

    # Execute application
    _c_(423501, _a_(423497, _n_(423496, "sys", lambda: sys), "exit"), _c_(423500, _a_(423499, _n_(423498, "app", lambda: app), "exec")))
    _l_(423502)