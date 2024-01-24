# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61810309/threading-error-nameerror-name-datelabelstringvar-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(362885)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(362887)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(362889)

except ImportError:
    pass
try:
    from numerize import numerize
    _l_(362891)

except ImportError:
    pass
try:
    import pygame
    _l_(362893)

except ImportError:
    pass
try:
    import os
    _l_(362895)

except ImportError:
    pass
try:
    import random
    _l_(362897)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(362899)

except ImportError:
    pass
try:
    import threading
    _l_(362901)

except ImportError:
    pass
try:
    import time
    _l_(362903)

except ImportError:
    pass

wholedate = _c_(362909, _a_(362905, _n_(362904, "datetime", lambda: datetime), "date"), _c_(362908, _a_(362907, _n_(362906, "datetime", lambda: datetime), "now")))
_l_(362910)
date = _c_(362913, _a_(362912, _n_(362911, "wholedate", lambda: wholedate), "strftime"), "%d")
_l_(362914)
month = _c_(362917, _a_(362916, _n_(362915, "wholedate", lambda: wholedate), "strftime"), "%m")
_l_(362918)
year = _c_(362921, _a_(362920, _n_(362919, "wholedate", lambda: wholedate), "strftime"), "%Y")
_l_(362922)

def advancetime():
    _l_(363061)

    global date
    _l_(362923)
    global month
    _l_(362924)
    global year
    _l_(362925)
    _c_(362931, _a_(362930, _c_(362929, _a_(362927, _n_(362926, "threading", lambda: threading), "Timer"), 5.0, _n_(362928, "advancetime", lambda: advancetime)), "start"))
    _l_(362932)
    if _n_(362933, "month", lambda: month) == "09" or _n_(362934, "month", lambda: month) == "04" or _n_(362935, "month", lambda: month) == "06" or _n_(362936, "month", lambda: month) == "11":
        _l_(362975)

        date = _c_(362939, _n_(362937, "int", lambda: int), _n_(362938, "date", lambda: date)) + 1
        _l_(362940)
        if _n_(362941, "date", lambda: date) > 30:
            _l_(362954)

            date = 1
            _l_(362942)
            month = _c_(362945, _n_(362943, "int", lambda: int), _n_(362944, "month", lambda: month)) + 1
            _l_(362946)
            if _n_(362947, "month", lambda: month) > 12:
                _l_(362953)

                month = 1
                _l_(362948)
                year = _c_(362951, _n_(362949, "int", lambda: int), _n_(362950, "year", lambda: year)) + 1
                _l_(362952)
        _c_(362956, _n_(362955, "fixdate", lambda: fixdate))
        _l_(362957)
        _c_(362959, _n_(362958, "fixmonth", lambda: fixmonth))
        _l_(362960)
        _c_(362972, _a_(362962, _n_(362961, "datelabelstringvar", lambda: datelabelstringvar), "set"), _c_(362965, _n_(362963, "str", lambda: str), _n_(362964, "date", lambda: date)) + "/" + _c_(362968, _n_(362966, "str", lambda: str), _n_(362967, "month", lambda: month)) + "/" + _c_(362971, _n_(362969, "str", lambda: str), _n_(362970, "year", lambda: year)))
        _l_(362973)
        aux = ""
        _l_(362974)
        return aux
    if _n_(362976, "month", lambda: month) == "01" or _n_(362977, "month", lambda: month) == "03" or _n_(362978, "month", lambda: month) == "05" or _n_(362979, "month", lambda: month) == "07" or _n_(362980, "month", lambda: month) == "08" or _n_(362981, "month", lambda: month) == "10" or _n_(362982, "month", lambda: month) == "12":
        _l_(363021)

        date = _c_(362985, _n_(362983, "int", lambda: int), _n_(362984, "date", lambda: date)) + 1
        _l_(362986)
        if _n_(362987, "date", lambda: date) > 31:
            _l_(363000)

            date = 1
            _l_(362988)
            month = _c_(362991, _n_(362989, "int", lambda: int), _n_(362990, "month", lambda: month)) + 1
            _l_(362992)
            if _n_(362993, "month", lambda: month) > 12:
                _l_(362999)

                month = 1
                _l_(362994)
                year = _c_(362997, _n_(362995, "int", lambda: int), _n_(362996, "year", lambda: year)) + 1
                _l_(362998)
        _c_(363002, _n_(363001, "fixdate", lambda: fixdate))
        _l_(363003)
        _c_(363005, _n_(363004, "fixmonth", lambda: fixmonth))
        _l_(363006)
        _c_(363018, _a_(363008, _n_(363007, "datelabelstringvar", lambda: datelabelstringvar), "set"), _c_(363011, _n_(363009, "str", lambda: str), _n_(363010, "date", lambda: date)) + "/" + _c_(363014, _n_(363012, "str", lambda: str), _n_(363013, "month", lambda: month)) + "/" + _c_(363017, _n_(363015, "str", lambda: str), _n_(363016, "year", lambda: year)))
        _l_(363019)
        aux = ""
        _l_(363020)
        return aux
    if _n_(363022, "month", lambda: month) == "02":
        _l_(363060)

        date = _c_(363025, _n_(363023, "int", lambda: int), _n_(363024, "date", lambda: date)) + 1
        _l_(363026)
        if _n_(363027, "date", lambda: date) > 31:
            _l_(363040)

            date = 1
            _l_(363028)
            month = _c_(363031, _n_(363029, "int", lambda: int), _n_(363030, "month", lambda: month)) + 1
            _l_(363032)
            if _n_(363033, "month", lambda: month) > 12:
                _l_(363039)

                month = 1
                _l_(363034)
                year = _c_(363037, _n_(363035, "int", lambda: int), _n_(363036, "year", lambda: year)) + 1
                _l_(363038)
        _c_(363042, _n_(363041, "fixdate", lambda: fixdate))
        _l_(363043)
        _c_(363045, _n_(363044, "fixmonth", lambda: fixmonth))
        _l_(363046)
        _c_(363058, _a_(363048, _n_(363047, "datelabelstringvar", lambda: datelabelstringvar), "set"), _c_(363051, _n_(363049, "str", lambda: str), _n_(363050, "date", lambda: date)) + "/" + _c_(363054, _n_(363052, "str", lambda: str), _n_(363053, "month", lambda: month)) + "/" + _c_(363057, _n_(363055, "str", lambda: str), _n_(363056, "year", lambda: year)))
        _l_(363059)

def calendarOnClose():
    _l_(363070)

    _c_(363064, _a_(363063, _n_(363062, "root", lambda: root), "deiconify"))
    _l_(363065)
    _c_(363068, _a_(363067, _n_(363066, "calendarwindow", lambda: calendarwindow), "destroy"))
    _l_(363069)

def calendar():
    _l_(363140)

    global datelabelstringvar
    _l_(363071)
    global calendarwindow
    _l_(363072)
    _c_(363075, _a_(363074, _n_(363073, "root", lambda: root), "withdraw"))
    _l_(363076)
    calendarwindow = _c_(363078, _n_(363077, "Toplevel", lambda: Toplevel))
    _l_(363079)
    _c_(363082, _a_(363081, _n_(363080, "calendarwindow", lambda: calendarwindow), "title"), "Calendar")
    _l_(363083)
    _c_(363086, _a_(363085, _n_(363084, "calendarwindow", lambda: calendarwindow), "geometry"), "400x350+300+100")
    _l_(363087)
    _c_(363091, _a_(363089, _n_(363088, "calendarwindow", lambda: calendarwindow), "protocol"), "WM_DELETE_WINDOW", _n_(363090, "calendarOnClose", lambda: calendarOnClose))
    _l_(363092)
    datelabelstringvar = _c_(363094, _n_(363093, "StringVar", lambda: StringVar))
    _l_(363095)
    _c_(363107, _a_(363097, _n_(363096, "datelabelstringvar", lambda: datelabelstringvar), "set"), _c_(363100, _n_(363098, "str", lambda: str), _n_(363099, "date", lambda: date)) + "/" + _c_(363103, _n_(363101, "str", lambda: str), _n_(363102, "month", lambda: month)) + "/" + _c_(363106, _n_(363104, "str", lambda: str), _n_(363105, "year", lambda: year)))
    _l_(363108)
    datelabel = _c_(363114, _a_(363113, _c_(363112, _n_(363109, "Label", lambda: Label), _n_(363110, "calendarwindow", lambda: calendarwindow), textvariable=_n_(363111, "datelabelstringvar", lambda: datelabelstringvar)), "grid"), row="0", column="0")
    _l_(363115)
    _c_(363121, _a_(363120, _c_(363119, _n_(363116, "Button", lambda: Button), _n_(363117, "calendarwindow", lambda: calendarwindow), text="Advance Time", command=_n_(363118, "advancetime", lambda: advancetime)), "grid"), row="1", column="0")
    _l_(363122)
    totalfruitclickerstringvar = _c_(363124, _n_(363123, "StringVar", lambda: StringVar))
    _l_(363125)
    _c_(363131, _a_(363127, _n_(363126, "totalfruitclickerstringvar", lambda: totalfruitclickerstringvar), "set"), "Fruit Clicked: " + _c_(363130, _n_(363128, "str", lambda: str), _n_(363129, "totalfruitclicked", lambda: totalfruitclicked)))
    _l_(363132)
    _c_(363138, _a_(363137, _c_(363136, _n_(363133, "Label", lambda: Label), _n_(363134, "calendarwindow", lambda: calendarwindow), textvariable=_n_(363135, "totalfruitclickerstringvar", lambda: totalfruitclickerstringvar)), "grid"), row="2", column="0")
    _l_(363139)

root = _c_(363142, _n_(363141, "Tk", lambda: Tk))
_l_(363143)
_c_(363146, _a_(363145, _n_(363144, "root", lambda: root), "title"), "Fruit Clicker")
_l_(363147)
_c_(363150, _a_(363149, _n_(363148, "root", lambda: root), "geometry"), "400x350+300+100")
_l_(363151)

calendarbutton = _c_(363155, _n_(363152, "Button", lambda: Button), _n_(363153, "root", lambda: root), text="Calendar", fg="White", bg="Black", width="11", command=_n_(363154, "calendar", lambda: calendar))
_l_(363156)
_c_(363159, _a_(363158, _n_(363157, "calendarbutton", lambda: calendarbutton), "grid"), row="8", column="0")
_l_(363160)

_c_(363162, _n_(363161, "advancetime", lambda: advancetime))
_l_(363163)

_c_(363166, _a_(363165, _n_(363164, "root", lambda: root), "mainloop"))
_l_(363167)