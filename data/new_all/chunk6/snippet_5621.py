# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61810309/threading-error-nameerror-name-datelabelstringvar-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(342881)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(342883)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(342885)

except ImportError:
    pass
try:
    from numerize import numerize
    _l_(342887)

except ImportError:
    pass
try:
    import pygame
    _l_(342889)

except ImportError:
    pass
try:
    import os
    _l_(342891)

except ImportError:
    pass
try:
    import random
    _l_(342893)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(342895)

except ImportError:
    pass
try:
    import threading
    _l_(342897)

except ImportError:
    pass
try:
    import time
    _l_(342899)

except ImportError:
    pass

wholedate = _c_(342905, _a_(342901, _n_(342900, "datetime", lambda: datetime), "date"), _c_(342904, _a_(342903, _n_(342902, "datetime", lambda: datetime), "now")))
_l_(342906)
date = _c_(342909, _a_(342908, _n_(342907, "wholedate", lambda: wholedate), "strftime"), "%d")
_l_(342910)
month = _c_(342913, _a_(342912, _n_(342911, "wholedate", lambda: wholedate), "strftime"), "%m")
_l_(342914)
year = _c_(342917, _a_(342916, _n_(342915, "wholedate", lambda: wholedate), "strftime"), "%Y")
_l_(342918)

def advancetime():
    _l_(343057)

    global date
    _l_(342919)
    global month
    _l_(342920)
    global year
    _l_(342921)
    _c_(342927, _a_(342926, _c_(342925, _a_(342923, _n_(342922, "threading", lambda: threading), "Timer"), 5.0, _n_(342924, "advancetime", lambda: advancetime)), "start"))
    _l_(342928)
    if _n_(342929, "month", lambda: month) == "09" or _n_(342930, "month", lambda: month) == "04" or _n_(342931, "month", lambda: month) == "06" or _n_(342932, "month", lambda: month) == "11":
        _l_(342971)

        date = _c_(342935, _n_(342933, "int", lambda: int), _n_(342934, "date", lambda: date)) + 1
        _l_(342936)
        if _n_(342937, "date", lambda: date) > 30:
            _l_(342950)

            date = 1
            _l_(342938)
            month = _c_(342941, _n_(342939, "int", lambda: int), _n_(342940, "month", lambda: month)) + 1
            _l_(342942)
            if _n_(342943, "month", lambda: month) > 12:
                _l_(342949)

                month = 1
                _l_(342944)
                year = _c_(342947, _n_(342945, "int", lambda: int), _n_(342946, "year", lambda: year)) + 1
                _l_(342948)
        _c_(342952, _n_(342951, "fixdate", lambda: fixdate))
        _l_(342953)
        _c_(342955, _n_(342954, "fixmonth", lambda: fixmonth))
        _l_(342956)
        _c_(342968, _a_(342958, _n_(342957, "datelabelstringvar", lambda: datelabelstringvar), "set"), _c_(342961, _n_(342959, "str", lambda: str), _n_(342960, "date", lambda: date)) + "/" + _c_(342964, _n_(342962, "str", lambda: str), _n_(342963, "month", lambda: month)) + "/" + _c_(342967, _n_(342965, "str", lambda: str), _n_(342966, "year", lambda: year)))
        _l_(342969)
        aux = ""
        _l_(342970)
        return aux
    if _n_(342972, "month", lambda: month) == "01" or _n_(342973, "month", lambda: month) == "03" or _n_(342974, "month", lambda: month) == "05" or _n_(342975, "month", lambda: month) == "07" or _n_(342976, "month", lambda: month) == "08" or _n_(342977, "month", lambda: month) == "10" or _n_(342978, "month", lambda: month) == "12":
        _l_(343017)

        date = _c_(342981, _n_(342979, "int", lambda: int), _n_(342980, "date", lambda: date)) + 1
        _l_(342982)
        if _n_(342983, "date", lambda: date) > 31:
            _l_(342996)

            date = 1
            _l_(342984)
            month = _c_(342987, _n_(342985, "int", lambda: int), _n_(342986, "month", lambda: month)) + 1
            _l_(342988)
            if _n_(342989, "month", lambda: month) > 12:
                _l_(342995)

                month = 1
                _l_(342990)
                year = _c_(342993, _n_(342991, "int", lambda: int), _n_(342992, "year", lambda: year)) + 1
                _l_(342994)
        _c_(342998, _n_(342997, "fixdate", lambda: fixdate))
        _l_(342999)
        _c_(343001, _n_(343000, "fixmonth", lambda: fixmonth))
        _l_(343002)
        _c_(343014, _a_(343004, _n_(343003, "datelabelstringvar", lambda: datelabelstringvar), "set"), _c_(343007, _n_(343005, "str", lambda: str), _n_(343006, "date", lambda: date)) + "/" + _c_(343010, _n_(343008, "str", lambda: str), _n_(343009, "month", lambda: month)) + "/" + _c_(343013, _n_(343011, "str", lambda: str), _n_(343012, "year", lambda: year)))
        _l_(343015)
        aux = ""
        _l_(343016)
        return aux
    if _n_(343018, "month", lambda: month) == "02":
        _l_(343056)

        date = _c_(343021, _n_(343019, "int", lambda: int), _n_(343020, "date", lambda: date)) + 1
        _l_(343022)
        if _n_(343023, "date", lambda: date) > 31:
            _l_(343036)

            date = 1
            _l_(343024)
            month = _c_(343027, _n_(343025, "int", lambda: int), _n_(343026, "month", lambda: month)) + 1
            _l_(343028)
            if _n_(343029, "month", lambda: month) > 12:
                _l_(343035)

                month = 1
                _l_(343030)
                year = _c_(343033, _n_(343031, "int", lambda: int), _n_(343032, "year", lambda: year)) + 1
                _l_(343034)
        _c_(343038, _n_(343037, "fixdate", lambda: fixdate))
        _l_(343039)
        _c_(343041, _n_(343040, "fixmonth", lambda: fixmonth))
        _l_(343042)
        _c_(343054, _a_(343044, _n_(343043, "datelabelstringvar", lambda: datelabelstringvar), "set"), _c_(343047, _n_(343045, "str", lambda: str), _n_(343046, "date", lambda: date)) + "/" + _c_(343050, _n_(343048, "str", lambda: str), _n_(343049, "month", lambda: month)) + "/" + _c_(343053, _n_(343051, "str", lambda: str), _n_(343052, "year", lambda: year)))
        _l_(343055)

def calendarOnClose():
    _l_(343066)

    _c_(343060, _a_(343059, _n_(343058, "root", lambda: root), "deiconify"))
    _l_(343061)
    _c_(343064, _a_(343063, _n_(343062, "calendarwindow", lambda: calendarwindow), "destroy"))
    _l_(343065)

def calendar():
    _l_(343136)

    global datelabelstringvar
    _l_(343067)
    global calendarwindow
    _l_(343068)
    _c_(343071, _a_(343070, _n_(343069, "root", lambda: root), "withdraw"))
    _l_(343072)
    calendarwindow = _c_(343074, _n_(343073, "Toplevel", lambda: Toplevel))
    _l_(343075)
    _c_(343078, _a_(343077, _n_(343076, "calendarwindow", lambda: calendarwindow), "title"), "Calendar")
    _l_(343079)
    _c_(343082, _a_(343081, _n_(343080, "calendarwindow", lambda: calendarwindow), "geometry"), "400x350+300+100")
    _l_(343083)
    _c_(343087, _a_(343085, _n_(343084, "calendarwindow", lambda: calendarwindow), "protocol"), "WM_DELETE_WINDOW", _n_(343086, "calendarOnClose", lambda: calendarOnClose))
    _l_(343088)
    datelabelstringvar = _c_(343090, _n_(343089, "StringVar", lambda: StringVar))
    _l_(343091)
    _c_(343103, _a_(343093, _n_(343092, "datelabelstringvar", lambda: datelabelstringvar), "set"), _c_(343096, _n_(343094, "str", lambda: str), _n_(343095, "date", lambda: date)) + "/" + _c_(343099, _n_(343097, "str", lambda: str), _n_(343098, "month", lambda: month)) + "/" + _c_(343102, _n_(343100, "str", lambda: str), _n_(343101, "year", lambda: year)))
    _l_(343104)
    datelabel = _c_(343110, _a_(343109, _c_(343108, _n_(343105, "Label", lambda: Label), _n_(343106, "calendarwindow", lambda: calendarwindow), textvariable=_n_(343107, "datelabelstringvar", lambda: datelabelstringvar)), "grid"), row="0", column="0")
    _l_(343111)
    _c_(343117, _a_(343116, _c_(343115, _n_(343112, "Button", lambda: Button), _n_(343113, "calendarwindow", lambda: calendarwindow), text="Advance Time", command=_n_(343114, "advancetime", lambda: advancetime)), "grid"), row="1", column="0")
    _l_(343118)
    totalfruitclickerstringvar = _c_(343120, _n_(343119, "StringVar", lambda: StringVar))
    _l_(343121)
    _c_(343127, _a_(343123, _n_(343122, "totalfruitclickerstringvar", lambda: totalfruitclickerstringvar), "set"), "Fruit Clicked: " + _c_(343126, _n_(343124, "str", lambda: str), _n_(343125, "totalfruitclicked", lambda: totalfruitclicked)))
    _l_(343128)
    _c_(343134, _a_(343133, _c_(343132, _n_(343129, "Label", lambda: Label), _n_(343130, "calendarwindow", lambda: calendarwindow), textvariable=_n_(343131, "totalfruitclickerstringvar", lambda: totalfruitclickerstringvar)), "grid"), row="2", column="0")
    _l_(343135)

root = _c_(343138, _n_(343137, "Tk", lambda: Tk))
_l_(343139)
_c_(343142, _a_(343141, _n_(343140, "root", lambda: root), "title"), "Fruit Clicker")
_l_(343143)
_c_(343146, _a_(343145, _n_(343144, "root", lambda: root), "geometry"), "400x350+300+100")
_l_(343147)

calendarbutton = _c_(343151, _n_(343148, "Button", lambda: Button), _n_(343149, "root", lambda: root), text="Calendar", fg="White", bg="Black", width="11", command=_n_(343150, "calendar", lambda: calendar))
_l_(343152)
_c_(343155, _a_(343154, _n_(343153, "calendarbutton", lambda: calendarbutton), "grid"), row="8", column="0")
_l_(343156)

_c_(343158, _n_(343157, "advancetime", lambda: advancetime))
_l_(343159)

_c_(343162, _a_(343161, _n_(343160, "root", lambda: root), "mainloop"))
_l_(343163)