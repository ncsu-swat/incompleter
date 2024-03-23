# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51615388/retrieve-data-from-db-set-to-textinput-fields-and-image-widget-in-kivy-for-a-m
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sqlite3
    _l_(411418)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(411420)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(411422)

except ImportError:
    pass
try:
    from kivy.uix.recycleview.views import RecycleDataViewBehavior
    _l_(411424)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(411426)

except ImportError:
    pass
try:
    from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
    _l_(411428)

except ImportError:
    pass
try:
    from kivy.uix.recyclegridlayout import RecycleGridLayout
    _l_(411430)

except ImportError:
    pass
try:
    from kivy.uix.behaviors import FocusBehavior
    _l_(411432)

except ImportError:
    pass
try:
    from kivy.uix.recycleview.layout import LayoutSelectionBehavior
    _l_(411434)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(411436)

except ImportError:
    pass
try:
    from kivy.uix.accordion import Accordion
    _l_(411438)

except ImportError:
    pass
try:
    from kivy.clock import Clock
    _l_(411440)

except ImportError:
    pass
try:
    from tkinter.filedialog import askopenfilename
    _l_(411442)

except ImportError:
    pass
try:
    from tkinter import Tk
    _l_(411444)

except ImportError:
    pass

class Manager(_n_(411445, "ScreenManager", lambda: ScreenManager)):
    _l_(411452)

    screen_one = _c_(411447, _n_(411446, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(411448)
    screen_two = _c_(411450, _n_(411449, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(411451)

class ScreenTwo(_n_(411453, "BoxLayout", lambda: BoxLayout), _n_(411454, "Screen", lambda: Screen), _n_(411455, "Accordion", lambda: Accordion)):
    _l_(411668)

    data_items = _c_(411457, _n_(411456, "ListProperty", lambda: ListProperty), [])
    _l_(411458)

    def __init__(self, **kwargs):
        _l_(411478)

        _c_(411464, _a_(411462, _n_(411459, "super", lambda: super)(_n_(411460, "ScreenTwo", lambda: ScreenTwo), _n_(411461, "self", lambda: self)), "__init__"), **_n_(411463, "kwargs", lambda: kwargs))
        _l_(411465)
        # Clock.schedule_once(self.populate_fields)
        _c_(411468, _a_(411467, _n_(411466, "self", lambda: self), "create_table"))
        _l_(411469)
        _c_(411472, _a_(411471, _n_(411470, "self", lambda: self), "get_table_column_headings"))
        _l_(411473)
        _c_(411476, _a_(411475, _n_(411474, "self", lambda: self), "get_users"))
        _l_(411477)

    def populate_fields(self, instance):
        _l_(411497)

        columns = _a_(411480, _n_(411479, "self", lambda: self), "data_items")[_a_(411482, _n_(411481, "instance", lambda: instance), "index")]['range']
        _l_(411483)
        _a_(411486, _a_(411485, _n_(411484, "self", lambda: self), "ids"), "no").text = _a_(411488, _n_(411487, "self", lambda: self), "data_items")[_n_(411489, "columns", lambda: columns)[0]]['text']
        _l_(411490)
        _a_(411492, _n_(411491, "self", lambda: self), "user_name_text_input").text = _a_(411494, _n_(411493, "self", lambda: self), "data_items")[_n_(411495, "columns", lambda: columns)[1]]['text']
        _l_(411496)

    def get_table_column_headings(self):
        _l_(411521)

        connection = _c_(411500, _a_(411499, _n_(411498, "sqlite3", lambda: sqlite3), "connect"), "demo.db")
        _l_(411501)
        with _n_(411502, "connection", lambda: connection):
            _l_(411520)

            cursor = _c_(411505, _a_(411504, _n_(411503, "connection", lambda: connection), "cursor"))
            _l_(411506)
            _c_(411509, _a_(411508, _n_(411507, "cursor", lambda: cursor), "execute"), "PRAGMA table_info(Users)")
            _l_(411510)
            col_headings = _c_(411513, _a_(411512, _n_(411511, "cursor", lambda: cursor), "fetchall"))
            _l_(411514)
            _n_(411515, "self", lambda: self).total_col_headings = _c_(411518, _n_(411516, "len", lambda: len), _n_(411517, "col_headings", lambda: col_headings))
            _l_(411519)

    def filechooser(self):
        _l_(411541)

        _c_(411525, _a_(411524, _c_(411523, _n_(411522, "Tk", lambda: Tk)), "withdraw"))
        _l_(411526)
        _n_(411527, "self", lambda: self).image_path = _c_(411529, _n_(411528, "askopenfilename", lambda: askopenfilename), initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        _l_(411530)
        _a_(411532, _n_(411531, "self", lambda: self), "image").source = _a_(411534, _n_(411533, "self", lambda: self), "image_path")
        _l_(411535)
        image_path = _a_(411537, _n_(411536, "self", lambda: self), "image_path")
        _l_(411538)
        aux = _n_(411539, "image_path", lambda: image_path)
        _l_(411540)
        return aux

    def create_table(self):
        _l_(411560)

        connection = _c_(411544, _a_(411543, _n_(411542, "sqlite3", lambda: sqlite3), "connect"), "demo.db")
        _l_(411545)
        cursor = _c_(411548, _a_(411547, _n_(411546, "connection", lambda: connection), "cursor"))
        _l_(411549)
        sql = """CREATE TABLE IF NOT EXISTS Employees(
        EmpID integer PRIMARY KEY,
        EmpName text NOT NULL,
        EmpPhoto blob NOT NULL)"""
        _l_(411550)
        _c_(411554, _a_(411552, _n_(411551, "cursor", lambda: cursor), "execute"), _n_(411553, "sql", lambda: sql))
        _l_(411555)
        _c_(411558, _a_(411557, _n_(411556, "connection", lambda: connection), "close"))
        _l_(411559)

    def get_users(self):
        _l_(411610)

        connection = _c_(411563, _a_(411562, _n_(411561, "sqlite3", lambda: sqlite3), "connect"), "demo.db")
        _l_(411564)
        cursor = _c_(411567, _a_(411566, _n_(411565, "connection", lambda: connection), "cursor"))
        _l_(411568)

        _c_(411571, _a_(411570, _n_(411569, "cursor", lambda: cursor), "execute"), "SELECT * FROM Employees ORDER BY EmpID ASC")
        _l_(411572)
        rows = _c_(411575, _a_(411574, _n_(411573, "cursor", lambda: cursor), "fetchall"))
        _l_(411576)

        # create list with db column, db primary key, and db column range
        data = []
        _l_(411577)
        low = 0
        _l_(411578)
        high = _a_(411580, _n_(411579, "self", lambda: self), "total_col_headings") - 1
        _l_(411581)
        # Using database column range for populating the TextInput widgets with values from the row clicked/pressed.
        _n_(411582, "self", lambda: self).data_items = []
        _l_(411583)
        for row in _n_(411584, "rows", lambda: rows):
            _l_(411599)

            for col in _n_(411585, "row", lambda: row):
                _l_(411594)

                _c_(411592, _a_(411587, _n_(411586, "data", lambda: data), "append"), [_n_(411588, "col", lambda: col), _n_(411589, "row", lambda: row)[0], [_n_(411590, "low", lambda: low), _n_(411591, "high", lambda: high)]])
                _l_(411593)
            low += _n_(411595, "self", lambda: self).total_col_headings
            _l_(411596)
            high += _n_(411597, "self", lambda: self).total_col_headings
            _l_(411598)

        # create data_items
        _n_(411600, "self", lambda: self).data_items = [{'text': _c_(411603, _n_(411601, "str", lambda: str), _n_(411602, "x", lambda: x)[0]), 'Index': _c_(411606, _n_(411604, "str", lambda: str), _n_(411605, "x", lambda: x)[1]), 'range': _n_(411607, "x", lambda: x)[2]} for x in _n_(411608, "data", lambda: data)]
        _l_(411609)

    def save(self):
        _l_(411667)

        connection = _c_(411613, _a_(411612, _n_(411611, "sqlite3", lambda: sqlite3), "connect"), "demo.db")
        _l_(411614)
        cursor = _c_(411617, _a_(411616, _n_(411615, "connection", lambda: connection), "cursor"))
        _l_(411618)

        EmpID = _a_(411622, _a_(411621, _a_(411620, _n_(411619, "self", lambda: self), "ids"), "no"), "text")
        _l_(411623)
        EmpName = _a_(411627, _a_(411626, _a_(411625, _n_(411624, "self", lambda: self), "ids"), "name"), "text")
        _l_(411628)
        image_path = _a_(411630, _n_(411629, "self", lambda: self), "image_path") # -- > return value from fielchooser
        _l_(411631) # -- > return value from fielchooser

        EmpPhoto = _c_(411636, _a_(411635, _c_(411634, _n_(411632, "open", lambda: open), _n_(411633, "image_path", lambda: image_path), "rb"), "read"))
        _l_(411637)

        try:
            _l_(411662)

            save_sql="INSERT INTO Employees (EmpID, EmpName, EmpPhoto) VALUES (?,?,?)"
            _l_(411638)
            _c_(411645, _a_(411640, _n_(411639, "connection", lambda: connection), "execute"), _n_(411641, "save_sql", lambda: save_sql),(_n_(411642, "EmpID", lambda: EmpID), _n_(411643, "EmpName", lambda: EmpName), _n_(411644, "EmpPhoto", lambda: EmpPhoto)))
            _l_(411646)
            _c_(411649, _a_(411648, _n_(411647, "connection", lambda: connection), "commit"))
            _l_(411650)
            _c_(411653, _a_(411652, _n_(411651, "connection", lambda: connection), "close"))
            _l_(411654)
        except _a_(411656, _n_(411655, "sqlite3", lambda: sqlite3), "IntegrityError") as e:
            _l_(411661)

            _c_(411659, _n_(411657, "print", lambda: print), "Error: ",_n_(411658, "e", lambda: e))
            _l_(411660)

        _c_(411665, _a_(411664, _n_(411663, "self", lambda: self), "get_users")) #NEW
        _l_(411666) #NEW

class ScreenOne(_n_(411669, "Screen", lambda: Screen)):
    _l_(411673)

    var = _c_(411671, _n_(411670, "ScreenTwo", lambda: ScreenTwo))
    _l_(411672)

class SelectableRecycleGridLayout(_n_(411674, "FocusBehavior", lambda: FocusBehavior), _n_(411675, "LayoutSelectionBehavior", lambda: LayoutSelectionBehavior),
                                  _n_(411676, "RecycleGridLayout", lambda: RecycleGridLayout)):
    _l_(411678)

    ''' Adds selection and focus behaviour to the view. '''
    _l_(411677)

class SelectableButton(_n_(411679, "RecycleDataViewBehavior", lambda: RecycleDataViewBehavior), _n_(411680, "Button", lambda: Button)):
    _l_(411737)

    ''' Add selection support to the Button '''
    _l_(411681)

    var = _c_(411683, _n_(411682, "ScreenTwo", lambda: ScreenTwo))
    _l_(411684)
    index = None
    _l_(411685)
    selected = _c_(411687, _n_(411686, "BooleanProperty", lambda: BooleanProperty), False)
    _l_(411688)
    selectable = _c_(411690, _n_(411689, "BooleanProperty", lambda: BooleanProperty), True)
    _l_(411691)

    def refresh_view_attrs(self, rv, index, data):
        _l_(411705)

        ''' Catch and handle the view changes '''
        _l_(411692)
        _n_(411693, "self", lambda: self).index = _n_(411694, "index", lambda: index)
        _l_(411695)
        aux = _c_(411703, _a_(411699, _n_(411696, "super", lambda: super)(_n_(411697, "SelectableButton", lambda: SelectableButton), _n_(411698, "self", lambda: self)), "refresh_view_attrs"), _n_(411700, "rv", lambda: rv), _n_(411701, "index", lambda: index), _n_(411702, "data", lambda: data))
        _l_(411704)
        return aux

    def on_touch_down(self, touch):
        _l_(411731)

        ''' Add selection on touch down '''
        _l_(411706)
        if _c_(411712, _a_(411710, _n_(411707, "super", lambda: super)(_n_(411708, "SelectableButton", lambda: SelectableButton), _n_(411709, "self", lambda: self)), "on_touch_down"), _n_(411711, "touch", lambda: touch)):
            _l_(411714)

            aux = True
            _l_(411713)
            return aux
        if _c_(411719, _a_(411716, _n_(411715, "self", lambda: self), "collide_point"), *_a_(411718, _n_(411717, "touch", lambda: touch), "pos")) and _a_(411721, _n_(411720, "self", lambda: self), "selectable"):
            _l_(411730)

            aux = _c_(411728, _a_(411724, _a_(411723, _n_(411722, "self", lambda: self), "parent"), "select_with_touch"), _a_(411726, _n_(411725, "self", lambda: self), "index"), _n_(411727, "touch", lambda: touch))
            _l_(411729)
            return aux

    def apply_selection(self, rv, index, is_selected):
        _l_(411736)

        ''' Respond to the selection of items in the view. '''
        _l_(411732)
        _n_(411733, "self", lambda: self).selected = _n_(411734, "is_selected", lambda: is_selected)
        _l_(411735)

class OneApp(_n_(411738, "App", lambda: App)):
    _l_(411743)

    def build(self):
        _l_(411742)

        aux = _c_(411740, _n_(411739, "Manager", lambda: Manager))
        _l_(411741)
        return aux

if _n_(411744, "__name__", lambda: __name__) =="__main__":
    _l_(411750)

    _c_(411748, _a_(411747, _c_(411746, _n_(411745, "OneApp", lambda: OneApp)), "run"))
    _l_(411749)