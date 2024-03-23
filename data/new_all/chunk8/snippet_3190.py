# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77567020/attributeerror-nonetype-object-has-no-attribute-update-when-trying-to-add-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(616060)

except ImportError:
    pass
try:
    from PySide6.QtCore import Qt, Slot
    _l_(616062)

except ImportError:
    pass
try:
    from PySide6.QtGui import QAction , QPainter
    _l_(616064)

except ImportError:
    pass
try:
    from PySide6.QtWidgets import (QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit, 
                                   QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, 
                                   QWidget)
    _l_(616066)

except ImportError:
    pass
try:
    from PySide6.QtCharts import QChartView, QPieSeries, QChart
    _l_(616068)

except ImportError:
    pass





class Widget(_n_(616069, "QWidget", lambda: QWidget)):
    _l_(616609)

    def __init__(self):
        _l_(616327)

        _c_(616073, _a_(616071, _n_(616070, "QWidget", lambda: QWidget), "__init__"), _n_(616072, "self", lambda: self))
        _l_(616074)
        _n_(616075, "self", lambda: self).items = 0
        _l_(616076)
        _n_(616077, "self", lambda: self)._data = {}
        _l_(616078)
        
        with _c_(616080, _n_(616079, "open", lambda: open), 'aib_october.csv', encoding= 'utf-8-sig') as f:
            _l_(616094)

            reader = _c_(616084, _a_(616082, _n_(616081, "csv", lambda: csv), "DictReader"), _n_(616083, "f", lambda: f))
            _l_(616085)
            for record in _n_(616086, "reader", lambda: reader):
                _l_(616093)

                _c_(616091, _a_(616089, _a_(616088, _n_(616087, "self", lambda: self), "_data"), "update"), _n_(616090, "record", lambda: record))
                _l_(616092)

        _c_(616098, _n_(616095, "print", lambda: print), _a_(616097, _n_(616096, "self", lambda: self), "_data")) 
        _l_(616099) 

        # Left Widget
        _n_(616100, "self", lambda: self).table = _c_(616102, _n_(616101, "QTableWidget", lambda: QTableWidget))
        _l_(616103)
        _c_(616107, _a_(616106, _a_(616105, _n_(616104, "self", lambda: self), "table"), "setColumnCount"), 2)
        _l_(616108)
        _c_(616112, _a_(616111, _a_(616110, _n_(616109, "self", lambda: self), "table"), "setHorizontalHeaderLabels"), ["Description", "Price"])
        _l_(616113)
        _c_(616121, _a_(616118, _c_(616117, _a_(616116, _a_(616115, _n_(616114, "self", lambda: self), "table"), "horizontalHeader")), "setSectionResizeMode"), _a_(616120, _n_(616119, "QHeaderView", lambda: QHeaderView), "Stretch"))
        _l_(616122)

        # Chart
        _n_(616123, "self", lambda: self).chart_view = _c_(616125, _n_(616124, "QChartView", lambda: QChartView))
        _l_(616126)
        _c_(616132, _a_(616129, _a_(616128, _n_(616127, "self", lambda: self), "chart_view"), "setRenderHint"), _a_(616131, _n_(616130, "QPainter", lambda: QPainter), "Antialiasing"))
        _l_(616133)

        # Right Widget
        _n_(616134, "self", lambda: self).description = _c_(616136, _n_(616135, "QLineEdit", lambda: QLineEdit))
        _l_(616137)
        _n_(616138, "self", lambda: self).price = _c_(616140, _n_(616139, "QLineEdit", lambda: QLineEdit))
        _l_(616141)
        _n_(616142, "self", lambda: self).add = _c_(616144, _n_(616143, "QPushButton", lambda: QPushButton), "Add")
        _l_(616145)
        _n_(616146, "self", lambda: self).clear = _c_(616148, _n_(616147, "QPushButton", lambda: QPushButton), "Clear")
        _l_(616149)
        _n_(616150, "self", lambda: self).quit = _c_(616152, _n_(616151, "QPushButton", lambda: QPushButton), "Quit")
        _l_(616153)
        _n_(616154, "self", lambda: self).plot = _c_(616156, _n_(616155, "QPushButton", lambda: QPushButton), "Plot")
        _l_(616157)
        _n_(616158, "self", lambda: self).export = _c_(616160, _n_(616159, "QPushButton", lambda: QPushButton), "export")
        _l_(616161)

        # Disabling 'Add' button
        _c_(616165, _a_(616164, _a_(616163, _n_(616162, "self", lambda: self), "add"), "setEnabled"), False)
        _l_(616166)

        _n_(616167, "self", lambda: self).right = _c_(616169, _n_(616168, "QVBoxLayout", lambda: QVBoxLayout))
        _l_(616170)
        _c_(616176, _a_(616173, _a_(616172, _n_(616171, "self", lambda: self), "right"), "addWidget"), _c_(616175, _n_(616174, "QLabel", lambda: QLabel), "Description"))
        _l_(616177)
        _c_(616183, _a_(616180, _a_(616179, _n_(616178, "self", lambda: self), "right"), "addWidget"), _a_(616182, _n_(616181, "self", lambda: self), "description"))
        _l_(616184)
        _c_(616190, _a_(616187, _a_(616186, _n_(616185, "self", lambda: self), "right"), "addWidget"), _c_(616189, _n_(616188, "QLabel", lambda: QLabel), "Price"))
        _l_(616191)
        _c_(616197, _a_(616194, _a_(616193, _n_(616192, "self", lambda: self), "right"), "addWidget"), _a_(616196, _n_(616195, "self", lambda: self), "price"))
        _l_(616198)
        _c_(616204, _a_(616201, _a_(616200, _n_(616199, "self", lambda: self), "right"), "addWidget"), _a_(616203, _n_(616202, "self", lambda: self), "add"))
        _l_(616205)
        _c_(616211, _a_(616208, _a_(616207, _n_(616206, "self", lambda: self), "right"), "addWidget"), _a_(616210, _n_(616209, "self", lambda: self), "plot"))
        _l_(616212)
        _c_(616218, _a_(616215, _a_(616214, _n_(616213, "self", lambda: self), "right"), "addWidget"), _a_(616217, _n_(616216, "self", lambda: self), "chart_view"))
        _l_(616219)
        _c_(616225, _a_(616222, _a_(616221, _n_(616220, "self", lambda: self), "right"), "addWidget"), _a_(616224, _n_(616223, "self", lambda: self), "export"))
        _l_(616226)
        _c_(616232, _a_(616229, _a_(616228, _n_(616227, "self", lambda: self), "right"), "addWidget"), _a_(616231, _n_(616230, "self", lambda: self), "clear"))
        _l_(616233)
        _c_(616239, _a_(616236, _a_(616235, _n_(616234, "self", lambda: self), "right"), "addWidget"), _a_(616238, _n_(616237, "self", lambda: self), "quit"))
        _l_(616240)

        # QWidget Layout
        _n_(616241, "self", lambda: self).layout = _c_(616243, _n_(616242, "QHBoxLayout", lambda: QHBoxLayout))
        _l_(616244)

        #self.table_view.setSizePolicy(size)
        _c_(616250, _a_(616247, _a_(616246, _n_(616245, "self", lambda: self), "layout"), "addWidget"), _a_(616249, _n_(616248, "self", lambda: self), "table"))
        _l_(616251)
        _c_(616257, _a_(616254, _a_(616253, _n_(616252, "self", lambda: self), "layout"), "addLayout"), _a_(616256, _n_(616255, "self", lambda: self), "right"))
        _l_(616258)

        # Set the layout to the QWidget
        _c_(616263, _a_(616260, _n_(616259, "self", lambda: self), "setLayout"), _a_(616262, _n_(616261, "self", lambda: self), "layout"))
        _l_(616264)

        # Signals and Slots
        _c_(616271, _a_(616268, _a_(616267, _a_(616266, _n_(616265, "self", lambda: self), "add"), "clicked"), "connect"), _a_(616270, _n_(616269, "self", lambda: self), "add_element"))
        _l_(616272)
        _c_(616279, _a_(616276, _a_(616275, _a_(616274, _n_(616273, "self", lambda: self), "quit"), "clicked"), "connect"), _a_(616278, _n_(616277, "self", lambda: self), "quit_application"))
        _l_(616280)
        _c_(616287, _a_(616284, _a_(616283, _a_(616282, _n_(616281, "self", lambda: self), "plot"), "clicked"), "connect"), _a_(616286, _n_(616285, "self", lambda: self), "plot_data"))
        _l_(616288)
        _c_(616295, _a_(616292, _a_(616291, _a_(616290, _n_(616289, "self", lambda: self), "clear"), "clicked"), "connect"), _a_(616294, _n_(616293, "self", lambda: self), "clear_table"))
        _l_(616296)
        _c_(616303, _a_(616300, _a_(616299, _a_(616298, _n_(616297, "self", lambda: self), "export"), "clicked"), "connect"), _a_(616302, _n_(616301, "self", lambda: self), "export_data"))
        _l_(616304)
        _c_(616312, _a_(616309, _a_(616307, _a_(616306, _n_(616305, "self", lambda: self), "description"), "textChanged")[_n_(616308, "str", lambda: str)], "connect"), _a_(616311, _n_(616310, "self", lambda: self), "check_disable"))
        _l_(616313)
        _c_(616321, _a_(616318, _a_(616316, _a_(616315, _n_(616314, "self", lambda: self), "price"), "textChanged")[_n_(616317, "str", lambda: str)], "connect"), _a_(616320, _n_(616319, "self", lambda: self), "check_disable"))
        _l_(616322)

        # Fill example data
        _c_(616325, _a_(616324, _n_(616323, "self", lambda: self), "fill_table"))
        _l_(616326)

    @_c_(616329, _n_(616328, "Slot", lambda: Slot))

    def export_data(self):
        _l_(616352)

        with _c_(616331, _n_(616330, "open", lambda: open), "aib_october.csv", 'w', newline='') as file:
            _l_(616351)

            writer = _c_(616339, _a_(616333, _n_(616332, "csv", lambda: csv), "DictWriter"), _n_(616334, "file", lambda: file),fieldnames=_c_(616338, _a_(616337, _a_(616336, _n_(616335, "self", lambda: self), "_data"), "keys")))
            _l_(616340)
            _c_(616343, _a_(616342, _n_(616341, "writer", lambda: writer), "writeheader"))
            _l_(616344)
            _c_(616349, _a_(616346, _n_(616345, "writer", lambda: writer), "writerow"), _a_(616348, _n_(616347, "self", lambda: self), "_data"))
            _l_(616350)

    def add_element(self):
        _l_(616444)

        des = _c_(616356, _a_(616355, _a_(616354, _n_(616353, "self", lambda: self), "description"), "text"))
        _l_(616357)
        price = _c_(616361, _a_(616360, _a_(616359, _n_(616358, "self", lambda: self), "price"), "text"))
        _l_(616362)

        try:
            _l_(616443)

            price_item = _c_(616367, _n_(616363, "QTableWidgetItem", lambda: QTableWidgetItem), f"{_c_(616366, _n_(616364, 'float', lambda: float), _n_(616365, 'price', lambda: price)):.2f}")
            _l_(616368)
            _c_(616373, _a_(616370, _n_(616369, "price_item", lambda: price_item), "setTextAlignment"), _a_(616372, _n_(616371, "Qt", lambda: Qt), "AlignRight"))
            _l_(616374)

            _c_(616380, _a_(616377, _a_(616376, _n_(616375, "self", lambda: self), "table"), "insertRow"), _a_(616379, _n_(616378, "self", lambda: self), "items"))
            _l_(616381)
            description_item = _c_(616384, _n_(616382, "QTableWidgetItem", lambda: QTableWidgetItem), _n_(616383, "des", lambda: des))
            _l_(616385)

            _c_(616392, _a_(616388, _a_(616387, _n_(616386, "self", lambda: self), "table"), "setItem"), _a_(616390, _n_(616389, "self", lambda: self), "items"), 0, _n_(616391, "description_item", lambda: description_item))
            _l_(616393)
            _c_(616400, _a_(616396, _a_(616395, _n_(616394, "self", lambda: self), "table"), "setItem"), _a_(616398, _n_(616397, "self", lambda: self), "items"), 1, _n_(616399, "price_item", lambda: price_item))
            _l_(616401)

            _c_(616405, _a_(616404, _a_(616403, _n_(616402, "self", lambda: self), "description"), "setText"), "")
            _l_(616406)
            _c_(616410, _a_(616409, _a_(616408, _n_(616407, "self", lambda: self), "price"), "setText"), "")
            _l_(616411)

            _n_(616412, "self", lambda: self).items += 1
            _l_(616413)
            _c_(616421, _a_(616416, _a_(616415, _n_(616414, "self", lambda: self), "_data"), "update"), _c_(616420, _a_(616419, _a_(616418, _n_(616417, "self", lambda: self), "description"), "text")))
            _l_(616422)
            _c_(616430, _a_(616425, _a_(616424, _n_(616423, "self", lambda: self), "_data"), "update"), _c_(616429, _a_(616428, _a_(616427, _n_(616426, "self", lambda: self), "price"), "text")))
            _l_(616431)
            _c_(616435, _n_(616432, "print", lambda: print), _a_(616434, _n_(616433, "self", lambda: self), "_data"))
            _l_(616436)
        except _n_(616437, "ValueError", lambda: ValueError):
            _l_(616442)

            _c_(616440, _n_(616438, "print", lambda: print), "That is not an invalid input:", _n_(616439, "price", lambda: price), "Make sure to enter a price!")
            _l_(616441)


    @_c_(616446, _n_(616445, "Slot", lambda: Slot))
    def check_disable(self, x):
        _l_(616466)

        if not _c_(616450, _a_(616449, _a_(616448, _n_(616447, "self", lambda: self), "description"), "text")) or not _c_(616454, _a_(616453, _a_(616452, _n_(616451, "self", lambda: self), "price"), "text")):
            _l_(616465)

            _c_(616458, _a_(616457, _a_(616456, _n_(616455, "self", lambda: self), "add"), "setEnabled"), False)
            _l_(616459)
        else:
            _c_(616463, _a_(616462, _a_(616461, _n_(616460, "self", lambda: self), "add"), "setEnabled"), True)
            _l_(616464)

    @_c_(616468, _n_(616467, "Slot", lambda: Slot))
    def plot_data(self):
        _l_(616525)

        # Get table information
        series = _c_(616470, _n_(616469, "QPieSeries", lambda: QPieSeries))
        _l_(616471)
        for i in _c_(616477, _n_(616472, "range", lambda: range), _c_(616476, _a_(616475, _a_(616474, _n_(616473, "self", lambda: self), "table"), "rowCount"))):
            _l_(616502)

            text = _c_(616484, _a_(616483, _c_(616482, _a_(616480, _a_(616479, _n_(616478, "self", lambda: self), "table"), "item"), _n_(616481, "i", lambda: i), 0), "text"))
            _l_(616485)
            number = _c_(616494, _n_(616486, "float", lambda: float), _c_(616493, _a_(616492, _c_(616491, _a_(616489, _a_(616488, _n_(616487, "self", lambda: self), "table"), "item"), _n_(616490, "i", lambda: i), 1), "int")))
            _l_(616495)
            _c_(616500, _a_(616497, _n_(616496, "series", lambda: series), "append"), _n_(616498, "text", lambda: text), _n_(616499, "number", lambda: number))
            _l_(616501)

        chart = _c_(616504, _n_(616503, "QChart", lambda: QChart))
        _l_(616505)
        _c_(616509, _a_(616507, _n_(616506, "chart", lambda: chart), "addSeries"), _n_(616508, "series", lambda: series))
        _l_(616510)
        _c_(616517, _a_(616514, _c_(616513, _a_(616512, _n_(616511, "chart", lambda: chart), "legend")), "setAlignment"), _a_(616516, _n_(616515, "Qt", lambda: Qt), "AlignLeft"))
        _l_(616518)
        _c_(616523, _a_(616521, _a_(616520, _n_(616519, "self", lambda: self), "chart_view"), "setChart"), _n_(616522, "chart", lambda: chart))
        _l_(616524)

    @_c_(616527, _n_(616526, "Slot", lambda: Slot))
    def quit_application(self):
        _l_(616532)

        _c_(616530, _a_(616529, _n_(616528, "QApplication", lambda: QApplication), "quit"))
        _l_(616531)

    def fill_table(self, data=None):
        _l_(616596)

        data = _a_(616534, _n_(616533, "self", lambda: self), "_data") if not _n_(616535, "data", lambda: data) else _n_(616536, "data", lambda: data)
        _l_(616537)
        for desc, price in _c_(616540, _a_(616539, _n_(616538, "data", lambda: data), "items")):
            _l_(616595)

            description_item = _c_(616543, _n_(616541, "QTableWidgetItem", lambda: QTableWidgetItem), _n_(616542, "desc", lambda: desc))
            _l_(616544)
            price_item = _c_(616549, _n_(616545, "QTableWidgetItem", lambda: QTableWidgetItem), _c_(616548, _a_(616546, "{}", "format"), _n_(616547, "price", lambda: price)))
            _l_(616550)
            _c_(616555, _a_(616552, _n_(616551, "price_item", lambda: price_item), "setTextAlignment"), _a_(616554, _n_(616553, "Qt", lambda: Qt), "AlignRight"))
            _l_(616556)
            _c_(616562, _a_(616559, _a_(616558, _n_(616557, "self", lambda: self), "table"), "insertRow"), _a_(616561, _n_(616560, "self", lambda: self), "items"))
            _l_(616563)
            _c_(616570, _a_(616566, _a_(616565, _n_(616564, "self", lambda: self), "table"), "setItem"), _a_(616568, _n_(616567, "self", lambda: self), "items"), 0, _n_(616569, "description_item", lambda: description_item))
            _l_(616571)
            _c_(616578, _a_(616574, _a_(616573, _n_(616572, "self", lambda: self), "table"), "setItem"), _a_(616576, _n_(616575, "self", lambda: self), "items"), 1, _n_(616577, "price_item", lambda: price_item))
            _l_(616579)
            _n_(616580, "self", lambda: self).items += 1
            _l_(616581)
            _n_(616582, "self", lambda: self)._data = _c_(616588, _a_(616585, _a_(616584, _n_(616583, "self", lambda: self), "_data"), "update"), {_n_(616586, "desc", lambda: desc): _n_(616587, "price", lambda: price)})
            _l_(616589)
            _c_(616593, _n_(616590, "print", lambda: print), _a_(616592, _n_(616591, "self", lambda: self), "_data"))
            _l_(616594)

    @_c_(616598, _n_(616597, "Slot", lambda: Slot))
    def clear_table(self):
        _l_(616608)

        _c_(616602, _a_(616601, _a_(616600, _n_(616599, "self", lambda: self), "table"), "setRowCount"), 0)
        _l_(616603)
        _n_(616604, "self", lambda: self).items = 0
        _l_(616605)
        _n_(616606, "self", lambda: self)._data = {}
        _l_(616607)


class MainWindow(_n_(616610, "QMainWindow", lambda: QMainWindow)):
    _l_(616665)

    def __init__(self, widget):
        _l_(616657)

        _c_(616614, _a_(616612, _n_(616611, "QMainWindow", lambda: QMainWindow), "__init__"), _n_(616613, "self", lambda: self))
        _l_(616615)
        _c_(616618, _a_(616617, _n_(616616, "self", lambda: self), "setWindowTitle"), "The pynancial advisor")
        _l_(616619)

        # Menu
        _n_(616620, "self", lambda: self).menu = _c_(616623, _a_(616622, _n_(616621, "self", lambda: self), "menuBar"))
        _l_(616624)
        _n_(616625, "self", lambda: self).file_menu = _c_(616629, _a_(616628, _a_(616627, _n_(616626, "self", lambda: self), "menu"), "addMenu"), "File")
        _l_(616630)

        # Exit QAction
        exit_action = _c_(616633, _n_(616631, "QAction", lambda: QAction), "Exit", _n_(616632, "self", lambda: self))
        _l_(616634)
        _c_(616637, _a_(616636, _n_(616635, "exit_action", lambda: exit_action), "setShortcut"), "Ctrl+Q")
        _l_(616638)
        _c_(616644, _a_(616641, _a_(616640, _n_(616639, "exit_action", lambda: exit_action), "triggered"), "connect"), _a_(616643, _n_(616642, "self", lambda: self), "exit_app"))
        _l_(616645)

        _c_(616650, _a_(616648, _a_(616647, _n_(616646, "self", lambda: self), "file_menu"), "addAction"), _n_(616649, "exit_action", lambda: exit_action))
        _l_(616651)
        _c_(616655, _a_(616653, _n_(616652, "self", lambda: self), "setCentralWidget"), _n_(616654, "widget", lambda: widget))
        _l_(616656)

    @_c_(616659, _n_(616658, "Slot", lambda: Slot))
    def exit_app(self, checked):
        _l_(616664)

        _c_(616662, _a_(616661, _n_(616660, "QApplication", lambda: QApplication), "quit"))
        _l_(616663)


if _n_(616666, "__name__", lambda: __name__) == "__main__":
    _l_(616694)

    # Qt Application
    app = _c_(616670, _n_(616667, "QApplication", lambda: QApplication), _a_(616669, _n_(616668, "sys", lambda: sys), "argv"))
    _l_(616671)
    # QWidget
    widget = _c_(616673, _n_(616672, "Widget", lambda: Widget))
    _l_(616674)
    # QMainWindow using QWidget as central widget
    window = _c_(616677, _n_(616675, "MainWindow", lambda: MainWindow), _n_(616676, "widget", lambda: widget))
    _l_(616678)
    _c_(616681, _a_(616680, _n_(616679, "window", lambda: window), "resize"), 800, 600)
    _l_(616682)
    _c_(616685, _a_(616684, _n_(616683, "window", lambda: window), "show"))
    _l_(616686)

    # Execute application
    _c_(616692, _a_(616688, _n_(616687, "sys", lambda: sys), "exit"), _c_(616691, _a_(616690, _n_(616689, "app", lambda: app), "exec")))
    _l_(616693)