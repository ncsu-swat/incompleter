# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61810309/threading-error-nameerror-name-datelabelstringvar-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(372251)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(372253)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(372255)

except ImportError:
    pass
try:
    from numerize import numerize
    _l_(372257)

except ImportError:
    pass
try:
    import pygame
    _l_(372259)

except ImportError:
    pass
try:
    import os
    _l_(372261)

except ImportError:
    pass
try:
    import random
    _l_(372263)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(372265)

except ImportError:
    pass
try:
    import threading
    _l_(372267)

except ImportError:
    pass
try:
    import time
    _l_(372269)

except ImportError:
    pass

wholedate = _c_(372275, _a_(372271, _n_(372270, "datetime", lambda: datetime), "date"), _c_(372274, _a_(372273, _n_(372272, "datetime", lambda: datetime), "now")))
_l_(372276)
date = _c_(372279, _a_(372278, _n_(372277, "wholedate", lambda: wholedate), "strftime"), "%d")
_l_(372280)
month = _c_(372283, _a_(372282, _n_(372281, "wholedate", lambda: wholedate), "strftime"), "%m")
_l_(372284)
year = _c_(372287, _a_(372286, _n_(372285, "wholedate", lambda: wholedate), "strftime"), "%Y")
_l_(372288)

def advancetime():
    _l_(372427)

    global date
    _l_(372289)
    global month
    _l_(372290)
    global year
    _l_(372291)
    _c_(372297, _a_(372296, _c_(372295, _a_(372293, _n_(372292, "threading", lambda: threading), "Timer"), 5.0, _n_(372294, "advancetime", lambda: advancetime)), "start"))
    _l_(372298)
    if _n_(372299, "month", lambda: month) == "09" or _n_(372300, "month", lambda: month) == "04" or _n_(372301, "month", lambda: month) == "06" or _n_(372302, "month", lambda: month) == "11":
        _l_(372341)

        date = _c_(372305, _n_(372303, "int", lambda: int), _n_(372304, "date", lambda: date)) + 1
        _l_(372306)
        if _n_(372307, "date", lambda: date) > 30:
            _l_(372320)

            date = 1
            _l_(372308)
            month = _c_(372311, _n_(372309, "int", lambda: int), _n_(372310, "month", lambda: month)) + 1
            _l_(372312)
            if _n_(372313, "month", lambda: month) > 12:
                _l_(372319)

                month = 1
                _l_(372314)
                year = _c_(372317, _n_(372315, "int", lambda: int), _n_(372316, "year", lambda: year)) + 1
                _l_(372318)
        _c_(372322, _n_(372321, "fixdate", lambda: fixdate))
        _l_(372323)
        _c_(372325, _n_(372324, "fixmonth", lambda: fixmonth))
        _l_(372326)
        _c_(372338, _a_(372328, _n_(372327, "datelabelstringvar", lambda: datelabelstringvar), "set"), _c_(372331, _n_(372329, "str", lambda: str), _n_(372330, "date", lambda: date)) + "/" + _c_(372334, _n_(372332, "str", lambda: str), _n_(372333, "month", lambda: month)) + "/" + _c_(372337, _n_(372335, "str", lambda: str), _n_(372336, "year", lambda: year)))
        _l_(372339)
        aux = ""
        _l_(372340)
        return aux
    if _n_(372342, "month", lambda: month) == "01" or _n_(372343, "month", lambda: month) == "03" or _n_(372344, "month", lambda: month) == "05" or _n_(372345, "month", lambda: month) == "07" or _n_(372346, "month", lambda: month) == "08" or _n_(372347, "month", lambda: month) == "10" or _n_(372348, "month", lambda: month) == "12":
        _l_(372387)

        date = _c_(372351, _n_(372349, "int", lambda: int), _n_(372350, "date", lambda: date)) + 1
        _l_(372352)
        if _n_(372353, "date", lambda: date) > 31:
            _l_(372366)

            date = 1
            _l_(372354)
            month = _c_(372357, _n_(372355, "int", lambda: int), _n_(372356, "month", lambda: month)) + 1
            _l_(372358)
            if _n_(372359, "month", lambda: month) > 12:
                _l_(372365)

                month = 1
                _l_(372360)
                year = _c_(372363, _n_(372361, "int", lambda: int), _n_(372362, "year", lambda: year)) + 1
                _l_(372364)
        _c_(372368, _n_(372367, "fixdate", lambda: fixdate))
        _l_(372369)
        _c_(372371, _n_(372370, "fixmonth", lambda: fixmonth))
        _l_(372372)
        _c_(372384, _a_(372374, _n_(372373, "datelabelstringvar", lambda: datelabelstringvar), "set"), _c_(372377, _n_(372375, "str", lambda: str), _n_(372376, "date", lambda: date)) + "/" + _c_(372380, _n_(372378, "str", lambda: str), _n_(372379, "month", lambda: month)) + "/" + _c_(372383, _n_(372381, "str", lambda: str), _n_(372382, "year", lambda: year)))
        _l_(372385)
        aux = ""
        _l_(372386)
        return aux
    if _n_(372388, "month", lambda: month) == "02":
        _l_(372426)

        date = _c_(372391, _n_(372389, "int", lambda: int), _n_(372390, "date", lambda: date)) + 1
        _l_(372392)
        if _n_(372393, "date", lambda: date) > 31:
            _l_(372406)

            date = 1
            _l_(372394)
            month = _c_(372397, _n_(372395, "int", lambda: int), _n_(372396, "month", lambda: month)) + 1
            _l_(372398)
            if _n_(372399, "month", lambda: month) > 12:
                _l_(372405)

                month = 1
                _l_(372400)
                year = _c_(372403, _n_(372401, "int", lambda: int), _n_(372402, "year", lambda: year)) + 1
                _l_(372404)
        _c_(372408, _n_(372407, "fixdate", lambda: fixdate))
        _l_(372409)
        _c_(372411, _n_(372410, "fixmonth", lambda: fixmonth))
        _l_(372412)
        _c_(372424, _a_(372414, _n_(372413, "datelabelstringvar", lambda: datelabelstringvar), "set"), _c_(372417, _n_(372415, "str", lambda: str), _n_(372416, "date", lambda: date)) + "/" + _c_(372420, _n_(372418, "str", lambda: str), _n_(372419, "month", lambda: month)) + "/" + _c_(372423, _n_(372421, "str", lambda: str), _n_(372422, "year", lambda: year)))
        _l_(372425)

def calendarOnClose():
    _l_(372436)

    _c_(372430, _a_(372429, _n_(372428, "root", lambda: root), "deiconify"))
    _l_(372431)
    _c_(372434, _a_(372433, _n_(372432, "calendarwindow", lambda: calendarwindow), "destroy"))
    _l_(372435)

def calendar():
    _l_(372506)

    global datelabelstringvar
    _l_(372437)
    global calendarwindow
    _l_(372438)
    _c_(372441, _a_(372440, _n_(372439, "root", lambda: root), "withdraw"))
    _l_(372442)
    calendarwindow = _c_(372444, _n_(372443, "Toplevel", lambda: Toplevel))
    _l_(372445)
    _c_(372448, _a_(372447, _n_(372446, "calendarwindow", lambda: calendarwindow), "title"), "Calendar")
    _l_(372449)
    _c_(372452, _a_(372451, _n_(372450, "calendarwindow", lambda: calendarwindow), "geometry"), "400x350+300+100")
    _l_(372453)
    _c_(372457, _a_(372455, _n_(372454, "calendarwindow", lambda: calendarwindow), "protocol"), "WM_DELETE_WINDOW", _n_(372456, "calendarOnClose", lambda: calendarOnClose))
    _l_(372458)
    datelabelstringvar = _c_(372460, _n_(372459, "StringVar", lambda: StringVar))
    _l_(372461)
    _c_(372473, _a_(372463, _n_(372462, "datelabelstringvar", lambda: datelabelstringvar), "set"), _c_(372466, _n_(372464, "str", lambda: str), _n_(372465, "date", lambda: date)) + "/" + _c_(372469, _n_(372467, "str", lambda: str), _n_(372468, "month", lambda: month)) + "/" + _c_(372472, _n_(372470, "str", lambda: str), _n_(372471, "year", lambda: year)))
    _l_(372474)
    datelabel = _c_(372480, _a_(372479, _c_(372478, _n_(372475, "Label", lambda: Label), _n_(372476, "calendarwindow", lambda: calendarwindow), textvariable=_n_(372477, "datelabelstringvar", lambda: datelabelstringvar)), "grid"), row="0", column="0")
    _l_(372481)
    _c_(372487, _a_(372486, _c_(372485, _n_(372482, "Button", lambda: Button), _n_(372483, "calendarwindow", lambda: calendarwindow), text="Advance Time", command=_n_(372484, "advancetime", lambda: advancetime)), "grid"), row="1", column="0")
    _l_(372488)
    totalfruitclickerstringvar = _c_(372490, _n_(372489, "StringVar", lambda: StringVar))
    _l_(372491)
    _c_(372497, _a_(372493, _n_(372492, "totalfruitclickerstringvar", lambda: totalfruitclickerstringvar), "set"), "Fruit Clicked: " + _c_(372496, _n_(372494, "str", lambda: str), _n_(372495, "totalfruitclicked", lambda: totalfruitclicked)))
    _l_(372498)
    _c_(372504, _a_(372503, _c_(372502, _n_(372499, "Label", lambda: Label), _n_(372500, "calendarwindow", lambda: calendarwindow), textvariable=_n_(372501, "totalfruitclickerstringvar", lambda: totalfruitclickerstringvar)), "grid"), row="2", column="0")
    _l_(372505)

root = _c_(372508, _n_(372507, "Tk", lambda: Tk))
_l_(372509)
_c_(372512, _a_(372511, _n_(372510, "root", lambda: root), "title"), "Fruit Clicker")
_l_(372513)
_c_(372516, _a_(372515, _n_(372514, "root", lambda: root), "geometry"), "400x350+300+100")
_l_(372517)

calendarbutton = _c_(372521, _n_(372518, "Button", lambda: Button), _n_(372519, "root", lambda: root), text="Calendar", fg="White", bg="Black", width="11", command=_n_(372520, "calendar", lambda: calendar))
_l_(372522)
_c_(372525, _a_(372524, _n_(372523, "calendarbutton", lambda: calendarbutton), "grid"), row="8", column="0")
_l_(372526)

_c_(372528, _n_(372527, "advancetime", lambda: advancetime))
_l_(372529)

_c_(372532, _a_(372531, _n_(372530, "root", lambda: root), "mainloop"))
_l_(372533)