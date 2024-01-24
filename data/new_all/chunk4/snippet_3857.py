# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66462158/tkinter-giving-typeerror-when-calling-function-same-function-gave-no-error-befo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(595781)

except ImportError:
    pass
try:
    import re
    _l_(595783)

except ImportError:
    pass
try:
    import xlsxwriter
    _l_(595785)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(595787)

except ImportError:
    pass
try:
    from PIL import Image, ImageTk
    _l_(595789)

except ImportError:
    pass


outWorkbook = _c_(595792, _a_(595791, _n_(595790, "xlsxwriter", lambda: xlsxwriter), "Workbook"), 'Wages.xlsx')  # Creates the link to the linked Excel file
_l_(595793)  # Creates the link to the linked Excel file

outSheet = _c_(595796, _a_(595795, _n_(595794, "outWorkbook", lambda: outWorkbook), "add_worksheet"))  # Creates a sheet within that excel file
_l_(595797)  # Creates a sheet within that excel file

_c_(595800, _a_(595799, _n_(595798, "outSheet", lambda: outSheet), "write"), 'A1', 'Day')  # Names the columns
_l_(595801)  # Names the columns
_c_(595804, _a_(595803, _n_(595802, "outSheet", lambda: outSheet), "write"), 'B1', 'Hours')
_l_(595805)


def proceed_to_input():
    _l_(595809)

    _c_(595807, _n_(595806, "ask_start_time", lambda: ask_start_time))
    _l_(595808)


def ask_start_time(day_name, attempts=25):
    _l_(595836)

    for a in _c_(595812, _n_(595810, "range", lambda: range), _n_(595811, "attempts", lambda: attempts)):
        _l_(595835)

        start = _c_(595815, _n_(595813, "input", lambda: input), f'What time did you start on {_n_(595814, "day_name", lambda: day_name)}?')
        _l_(595816)
        if 'na' in _n_(595817, 'start', lambda: start):
            _l_(595819)

            aux = '00:00'
            _l_(595818)
            return aux
        validation = _c_(595823, _a_(595821, _n_(595820, 're', lambda: re), 'match'), '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', _n_(595822, 'start', lambda: start))
        _l_(595824)
        if _n_(595825, 'validation', lambda: validation):
            _l_(595828)

            aux = _n_(595826, 'start', lambda: start)
            _l_(595827)
            return aux
        _c_(595830, _n_(595829, 'print', lambda: print), 'Please use a HH:MM format only.')
        _l_(595831)
    else:
        _c_(595833, _n_(595832, 'print', lambda: print), '25 wrong attempts and you still don\'t understand that it\'s HH:MM?!')
        _l_(595834)


def ask_finish_time(day_name, attempts=25):
    _l_(595860)

    for a in _c_(595839, _n_(595837, 'range', lambda: range), _n_(595838, 'attempts', lambda: attempts)):
        _l_(595859)

        finish = _c_(595842, _n_(595840, 'input', lambda: input), f'What time did you finish on {_n_(595841, "day_name", lambda: day_name)}?')
        _l_(595843)
        if 'na' in _n_(595844, 'finish', lambda: finish):
            _l_(595846)

            aux = '00:00'
            _l_(595845)
            return aux
        validation = _c_(595850, _a_(595848, _n_(595847, 're', lambda: re), 'match'), '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', _n_(595849, 'finish', lambda: finish))
        _l_(595851)
        if _n_(595852, 'validation', lambda: validation):
            _l_(595855)

            aux = _n_(595853, 'finish', lambda: finish)
            _l_(595854)
            return aux
        _c_(595857, _n_(595856, 'print', lambda: print), 'Please use a HH:MM format only.')
        _l_(595858)


def hourly_wage(attempts=25):
    _l_(595880)

    for a in _c_(595863, _n_(595861, 'range', lambda: range), _n_(595862, 'attempts', lambda: attempts)):
        _l_(595879)

        wage = _c_(595865, _n_(595864, 'input', lambda: input), f'What is your hourly rate of pay?')
        _l_(595866)
        validation = _c_(595870, _a_(595868, _n_(595867, 're', lambda: re), 'match'), '^[0-9].[0-9]|[0-9]*$', _n_(595869, 'wage', lambda: wage))
        _l_(595871)
        if _n_(595872, 'validation', lambda: validation):
            _l_(595878)

            aux = _n_(595873, 'wage', lambda: wage)
            _l_(595874)
            return aux
        else:
            _c_(595876, _n_(595875, 'print', lambda: print), 'Please use a N:NN format only.')
            _l_(595877)


def days():
    _l_(595890)

    work_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    _l_(595881)
    start_times = {_n_(595882, 'day', lambda: day): _n_(595883, 'ask_start_time', lambda: ask_start_time) for day in _n_(595884, 'work_days', lambda: work_days)}
    _l_(595885)
    _c_(595888, _n_(595886, 'print', lambda: print), _n_(595887, 'start_times', lambda: start_times))
    _l_(595889)


def ask_user(days):
    _l_(595914)

    start = _c_(595893, _n_(595891, 'ask_start_time', lambda: ask_start_time), _n_(595892, 'days', lambda: days))
    _l_(595894)
    finish = _c_(595897, _n_(595895, 'ask_finish_time', lambda: ask_finish_time), _n_(595896, 'days', lambda: days))
    _l_(595898)
    day_start = _c_(595903, _a_(595901, _a_(595900, _n_(595899, 'datetime', lambda: datetime), 'datetime'), 'strptime'), _n_(595902, 'start', lambda: start), '%H:%M')
    _l_(595904)
    day_fin = _c_(595909, _a_(595907, _a_(595906, _n_(595905, 'datetime', lambda: datetime), 'datetime'), 'strptime'), _n_(595908, 'finish', lambda: finish), '%H:%M')
    _l_(595910)
    aux = _n_(595911, 'day_fin', lambda: day_fin) - _n_(595912, 'day_start', lambda: day_start)
    _l_(595913)
    return aux


root = _c_(595917, _a_(595916, _n_(595915, 'tk', lambda: tk), 'Tk'))  # Creates GUI
_l_(595918)  # Creates GUI
canvas = _c_(595922, _a_(595920, _n_(595919, 'tk', lambda: tk), 'Canvas'), _n_(595921, 'root', lambda: root), width=500, height=500)
_l_(595923)
_c_(595926, _a_(595925, _n_(595924, 'canvas', lambda: canvas), 'grid'), columnspan=3, rowspan=3)
_l_(595927)

logo = _c_(595930, _a_(595929, _n_(595928, 'Image', lambda: Image), 'open'), 'titleofcalc.png')  # Adds text logo for GUI
_l_(595931)  # Adds text logo for GUI
logo = _c_(595935, _a_(595933, _n_(595932, 'ImageTk', lambda: ImageTk), 'PhotoImage'), _n_(595934, 'logo', lambda: logo))
_l_(595936)
logo_label = _c_(595940, _a_(595938, _n_(595937, 'tk', lambda: tk), 'Label'), image=_n_(595939, 'logo', lambda: logo))
_l_(595941)
_n_(595942, 'logo_label', lambda: logo_label).image = _n_(595943, 'logo', lambda: logo)
_l_(595944)
_c_(595947, _a_(595946, _n_(595945, 'logo_label', lambda: logo_label), 'grid'), column=2, row=0)
_l_(595948)

instructions = _c_(595952, _a_(595950, _n_(595949, 'tk', lambda: tk), 'Label'), _n_(595951, 'root', lambda: root), text='Please input your hourly wage.')  # Instructions for user on GUI
_l_(595953)  # Instructions for user on GUI
_c_(595956, _a_(595955, _n_(595954, 'instructions', lambda: instructions), 'grid'), columnspan=1, column=2, row=1)
_l_(595957)

entry1 = _c_(595961, _a_(595959, _n_(595958, 'tk', lambda: tk), 'Entry'), _n_(595960, 'root', lambda: root))
_l_(595962)
_c_(595966, _a_(595964, _n_(595963, 'canvas', lambda: canvas), 'create_window'), 200, 140, window=_n_(595965, 'entry1', lambda: entry1))
_l_(595967)

proceed_text = _c_(595970, _a_(595969, _n_(595968, 'tk', lambda: tk), 'StringVar'))  # Creates proceed button for GUI
_l_(595971)  # Creates proceed button for GUI
proceed_button = _c_(595979, _a_(595973, _n_(595972, 'tk', lambda: tk), 'Button'), _n_(595974, 'root', lambda: root), textvariable=_n_(595975, 'proceed_text', lambda: proceed_text), command=lambda: _c_(595978, _n_(595976, 'proceed_to_input', lambda: proceed_to_input), _n_(595977, 'days', lambda: days)), bg='#858485',
                           fg='white', height=2, width=15)
_l_(595980)

_c_(595983, _a_(595982, _n_(595981, 'proceed_text', lambda: proceed_text), 'set'), 'Next')
_l_(595984)
_c_(595987, _a_(595986, _n_(595985, 'proceed_button', lambda: proceed_button), 'grid'), column=2, row=2)
_l_(595988)

_c_(595991, _a_(595990, _n_(595989, 'root', lambda: root), 'mainloop'))  # Closes GUI instructions
_l_(595992)  # Closes GUI instructions

_c_(595994, _n_(595993, 'print', lambda: print), 'Please enter \'na\' on days you didn\'t work')
_l_(595995)
_c_(595997, _n_(595996, 'print', lambda: print), '')
_l_(595998)

wage = _c_(596002, _n_(595999, 'float', lambda: float), _c_(596001, _n_(596000, 'hourly_wage', lambda: hourly_wage)))
_l_(596003)

mon = _c_(596005, _n_(596004, 'ask_user', lambda: ask_user), 'Monday')
_l_(596006)
tue = _c_(596008, _n_(596007, 'ask_user', lambda: ask_user), 'Tuesday')
_l_(596009)
wed = _c_(596011, _n_(596010, 'ask_user', lambda: ask_user), 'Wednesday')
_l_(596012)
thu = _c_(596014, _n_(596013, 'ask_user', lambda: ask_user), 'Thursday')
_l_(596015)
fri = _c_(596017, _n_(596016, 'ask_user', lambda: ask_user), 'Friday')
_l_(596018)
sat = _c_(596020, _n_(596019, 'ask_user', lambda: ask_user), 'Saturday')
_l_(596021)
sun = _c_(596023, _n_(596022, 'ask_user', lambda: ask_user), 'Sunday')
_l_(596024)

hours_worked = (
    ['Mon', _n_(596025, 'mon', lambda: mon)],
    ['Tue', _n_(596026, 'tue', lambda: tue)],
    ['Wed', _n_(596027, 'wed', lambda: wed)],
    ['Thu', _n_(596028, 'thu', lambda: thu)],
    ['Fri', _n_(596029, 'fri', lambda: fri)],
    ['Sat', _n_(596030, 'sat', lambda: sat)],
    ['Sun', _n_(596031, 'sun', lambda: sun)],
)
_l_(596032)

row = 1
_l_(596033)
col = 0
_l_(596034)

for day, hours in _n_(596035, 'hours_worked', lambda: hours_worked):
    _l_(596051)

    _c_(596041, _a_(596037, _n_(596036, 'outSheet', lambda: outSheet), 'write'), _n_(596038, 'row', lambda: row), _n_(596039, 'col', lambda: col), _n_(596040, 'day', lambda: day))
    _l_(596042)
    _c_(596048, _a_(596044, _n_(596043, 'outSheet', lambda: outSheet), 'write'), _n_(596045, 'row', lambda: row), _n_(596046, 'col', lambda: col) + 1, _n_(596047, 'hours', lambda: hours) * 24)
    _l_(596049)
    row += 1
    _l_(596050)

week_hours = (_n_(596052, 'mon', lambda: mon) + _n_(596053, 'tue', lambda: tue) + _n_(596054, 'wed', lambda: wed) + _n_(596055, 'thu', lambda: thu) + _n_(596056, 'fri', lambda: fri) + _n_(596057, 'sat', lambda: sat) + _n_(596058, 'sun', lambda: sun))
_l_(596059)

total_seconds = _c_(596062, _a_(596061, _n_(596060, 'week_hours', lambda: week_hours), 'total_seconds'))
_l_(596063)

hours = ((_n_(596064, 'total_seconds', lambda: total_seconds) / 60) / 60)
_l_(596065)

pay = _c_(596069, _n_(596066, 'float', lambda: float), _n_(596067, 'hours', lambda: hours) * _n_(596068, 'wage', lambda: wage))
_l_(596070)

_c_(596073, _a_(596072, _n_(596071, 'outSheet', lambda: outSheet), 'write'), 'A10', 'Wages')
_l_(596074)
_c_(596078, _a_(596076, _n_(596075, 'outSheet', lambda: outSheet), 'write'), 'B10', _n_(596077, 'pay', lambda: pay))
_l_(596079)

_c_(596082, _a_(596081, _n_(596080, 'outWorkbook', lambda: outWorkbook), 'close'))  # Closes and saves Excel spreadsheet
_l_(596083)  # Closes and saves Excel spreadsheet