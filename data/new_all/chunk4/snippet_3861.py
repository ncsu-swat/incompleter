# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66462158/tkinter-giving-typeerror-when-calling-function-same-function-gave-no-error-befo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(641757)

except ImportError:
    pass
try:
    import re
    _l_(641759)

except ImportError:
    pass
try:
    import xlsxwriter
    _l_(641761)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(641763)

except ImportError:
    pass
try:
    from PIL import Image, ImageTk
    _l_(641765)

except ImportError:
    pass


outWorkbook = _c_(641768, _a_(641767, _n_(641766, "xlsxwriter", lambda: xlsxwriter), "Workbook"), 'Wages.xlsx')  # Creates the link to the linked Excel file
_l_(641769)  # Creates the link to the linked Excel file

outSheet = _c_(641772, _a_(641771, _n_(641770, "outWorkbook", lambda: outWorkbook), "add_worksheet"))  # Creates a sheet within that excel file
_l_(641773)  # Creates a sheet within that excel file

_c_(641776, _a_(641775, _n_(641774, "outSheet", lambda: outSheet), "write"), 'A1', 'Day')  # Names the columns
_l_(641777)  # Names the columns
_c_(641780, _a_(641779, _n_(641778, "outSheet", lambda: outSheet), "write"), 'B1', 'Hours')
_l_(641781)


def proceed_to_input():
    _l_(641785)

    _c_(641783, _n_(641782, "ask_start_time", lambda: ask_start_time))
    _l_(641784)


def ask_start_time(day_name, attempts=25):
    _l_(641812)

    for a in _c_(641788, _n_(641786, "range", lambda: range), _n_(641787, "attempts", lambda: attempts)):
        _l_(641811)

        start = _c_(641791, _n_(641789, "input", lambda: input), f'What time did you start on {_n_(641790, "day_name", lambda: day_name)}?')
        _l_(641792)
        if 'na' in _n_(641793, 'start', lambda: start):
            _l_(641795)

            aux = '00:00'
            _l_(641794)
            return aux
        validation = _c_(641799, _a_(641797, _n_(641796, 're', lambda: re), 'match'), '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', _n_(641798, 'start', lambda: start))
        _l_(641800)
        if _n_(641801, 'validation', lambda: validation):
            _l_(641804)

            aux = _n_(641802, 'start', lambda: start)
            _l_(641803)
            return aux
        _c_(641806, _n_(641805, 'print', lambda: print), 'Please use a HH:MM format only.')
        _l_(641807)
    else:
        _c_(641809, _n_(641808, 'print', lambda: print), '25 wrong attempts and you still don\'t understand that it\'s HH:MM?!')
        _l_(641810)


def ask_finish_time(day_name, attempts=25):
    _l_(641836)

    for a in _c_(641815, _n_(641813, 'range', lambda: range), _n_(641814, 'attempts', lambda: attempts)):
        _l_(641835)

        finish = _c_(641818, _n_(641816, 'input', lambda: input), f'What time did you finish on {_n_(641817, "day_name", lambda: day_name)}?')
        _l_(641819)
        if 'na' in _n_(641820, 'finish', lambda: finish):
            _l_(641822)

            aux = '00:00'
            _l_(641821)
            return aux
        validation = _c_(641826, _a_(641824, _n_(641823, 're', lambda: re), 'match'), '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', _n_(641825, 'finish', lambda: finish))
        _l_(641827)
        if _n_(641828, 'validation', lambda: validation):
            _l_(641831)

            aux = _n_(641829, 'finish', lambda: finish)
            _l_(641830)
            return aux
        _c_(641833, _n_(641832, 'print', lambda: print), 'Please use a HH:MM format only.')
        _l_(641834)


def hourly_wage(attempts=25):
    _l_(641856)

    for a in _c_(641839, _n_(641837, 'range', lambda: range), _n_(641838, 'attempts', lambda: attempts)):
        _l_(641855)

        wage = _c_(641841, _n_(641840, 'input', lambda: input), f'What is your hourly rate of pay?')
        _l_(641842)
        validation = _c_(641846, _a_(641844, _n_(641843, 're', lambda: re), 'match'), '^[0-9].[0-9]|[0-9]*$', _n_(641845, 'wage', lambda: wage))
        _l_(641847)
        if _n_(641848, 'validation', lambda: validation):
            _l_(641854)

            aux = _n_(641849, 'wage', lambda: wage)
            _l_(641850)
            return aux
        else:
            _c_(641852, _n_(641851, 'print', lambda: print), 'Please use a N:NN format only.')
            _l_(641853)


def days():
    _l_(641866)

    work_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    _l_(641857)
    start_times = {_n_(641858, 'day', lambda: day): _n_(641859, 'ask_start_time', lambda: ask_start_time) for day in _n_(641860, 'work_days', lambda: work_days)}
    _l_(641861)
    _c_(641864, _n_(641862, 'print', lambda: print), _n_(641863, 'start_times', lambda: start_times))
    _l_(641865)


def ask_user(days):
    _l_(641890)

    start = _c_(641869, _n_(641867, 'ask_start_time', lambda: ask_start_time), _n_(641868, 'days', lambda: days))
    _l_(641870)
    finish = _c_(641873, _n_(641871, 'ask_finish_time', lambda: ask_finish_time), _n_(641872, 'days', lambda: days))
    _l_(641874)
    day_start = _c_(641879, _a_(641877, _a_(641876, _n_(641875, 'datetime', lambda: datetime), 'datetime'), 'strptime'), _n_(641878, 'start', lambda: start), '%H:%M')
    _l_(641880)
    day_fin = _c_(641885, _a_(641883, _a_(641882, _n_(641881, 'datetime', lambda: datetime), 'datetime'), 'strptime'), _n_(641884, 'finish', lambda: finish), '%H:%M')
    _l_(641886)
    aux = _n_(641887, 'day_fin', lambda: day_fin) - _n_(641888, 'day_start', lambda: day_start)
    _l_(641889)
    return aux


root = _c_(641893, _a_(641892, _n_(641891, 'tk', lambda: tk), 'Tk'))  # Creates GUI
_l_(641894)  # Creates GUI
canvas = _c_(641898, _a_(641896, _n_(641895, 'tk', lambda: tk), 'Canvas'), _n_(641897, 'root', lambda: root), width=500, height=500)
_l_(641899)
_c_(641902, _a_(641901, _n_(641900, 'canvas', lambda: canvas), 'grid'), columnspan=3, rowspan=3)
_l_(641903)

logo = _c_(641906, _a_(641905, _n_(641904, 'Image', lambda: Image), 'open'), 'titleofcalc.png')  # Adds text logo for GUI
_l_(641907)  # Adds text logo for GUI
logo = _c_(641911, _a_(641909, _n_(641908, 'ImageTk', lambda: ImageTk), 'PhotoImage'), _n_(641910, 'logo', lambda: logo))
_l_(641912)
logo_label = _c_(641916, _a_(641914, _n_(641913, 'tk', lambda: tk), 'Label'), image=_n_(641915, 'logo', lambda: logo))
_l_(641917)
_n_(641918, 'logo_label', lambda: logo_label).image = _n_(641919, 'logo', lambda: logo)
_l_(641920)
_c_(641923, _a_(641922, _n_(641921, 'logo_label', lambda: logo_label), 'grid'), column=2, row=0)
_l_(641924)

instructions = _c_(641928, _a_(641926, _n_(641925, 'tk', lambda: tk), 'Label'), _n_(641927, 'root', lambda: root), text='Please input your hourly wage.')  # Instructions for user on GUI
_l_(641929)  # Instructions for user on GUI
_c_(641932, _a_(641931, _n_(641930, 'instructions', lambda: instructions), 'grid'), columnspan=1, column=2, row=1)
_l_(641933)

entry1 = _c_(641937, _a_(641935, _n_(641934, 'tk', lambda: tk), 'Entry'), _n_(641936, 'root', lambda: root))
_l_(641938)
_c_(641942, _a_(641940, _n_(641939, 'canvas', lambda: canvas), 'create_window'), 200, 140, window=_n_(641941, 'entry1', lambda: entry1))
_l_(641943)

proceed_text = _c_(641946, _a_(641945, _n_(641944, 'tk', lambda: tk), 'StringVar'))  # Creates proceed button for GUI
_l_(641947)  # Creates proceed button for GUI
proceed_button = _c_(641955, _a_(641949, _n_(641948, 'tk', lambda: tk), 'Button'), _n_(641950, 'root', lambda: root), textvariable=_n_(641951, 'proceed_text', lambda: proceed_text), command=lambda: _c_(641954, _n_(641952, 'proceed_to_input', lambda: proceed_to_input), _n_(641953, 'days', lambda: days)), bg='#858485',
                           fg='white', height=2, width=15)
_l_(641956)

_c_(641959, _a_(641958, _n_(641957, 'proceed_text', lambda: proceed_text), 'set'), 'Next')
_l_(641960)
_c_(641963, _a_(641962, _n_(641961, 'proceed_button', lambda: proceed_button), 'grid'), column=2, row=2)
_l_(641964)

_c_(641967, _a_(641966, _n_(641965, 'root', lambda: root), 'mainloop'))  # Closes GUI instructions
_l_(641968)  # Closes GUI instructions

_c_(641970, _n_(641969, 'print', lambda: print), 'Please enter \'na\' on days you didn\'t work')
_l_(641971)
_c_(641973, _n_(641972, 'print', lambda: print), '')
_l_(641974)

wage = _c_(641978, _n_(641975, 'float', lambda: float), _c_(641977, _n_(641976, 'hourly_wage', lambda: hourly_wage)))
_l_(641979)

mon = _c_(641981, _n_(641980, 'ask_user', lambda: ask_user), 'Monday')
_l_(641982)
tue = _c_(641984, _n_(641983, 'ask_user', lambda: ask_user), 'Tuesday')
_l_(641985)
wed = _c_(641987, _n_(641986, 'ask_user', lambda: ask_user), 'Wednesday')
_l_(641988)
thu = _c_(641990, _n_(641989, 'ask_user', lambda: ask_user), 'Thursday')
_l_(641991)
fri = _c_(641993, _n_(641992, 'ask_user', lambda: ask_user), 'Friday')
_l_(641994)
sat = _c_(641996, _n_(641995, 'ask_user', lambda: ask_user), 'Saturday')
_l_(641997)
sun = _c_(641999, _n_(641998, 'ask_user', lambda: ask_user), 'Sunday')
_l_(642000)

hours_worked = (
    ['Mon', _n_(642001, 'mon', lambda: mon)],
    ['Tue', _n_(642002, 'tue', lambda: tue)],
    ['Wed', _n_(642003, 'wed', lambda: wed)],
    ['Thu', _n_(642004, 'thu', lambda: thu)],
    ['Fri', _n_(642005, 'fri', lambda: fri)],
    ['Sat', _n_(642006, 'sat', lambda: sat)],
    ['Sun', _n_(642007, 'sun', lambda: sun)],
)
_l_(642008)

row = 1
_l_(642009)
col = 0
_l_(642010)

for day, hours in _n_(642011, 'hours_worked', lambda: hours_worked):
    _l_(642027)

    _c_(642017, _a_(642013, _n_(642012, 'outSheet', lambda: outSheet), 'write'), _n_(642014, 'row', lambda: row), _n_(642015, 'col', lambda: col), _n_(642016, 'day', lambda: day))
    _l_(642018)
    _c_(642024, _a_(642020, _n_(642019, 'outSheet', lambda: outSheet), 'write'), _n_(642021, 'row', lambda: row), _n_(642022, 'col', lambda: col) + 1, _n_(642023, 'hours', lambda: hours) * 24)
    _l_(642025)
    row += 1
    _l_(642026)

week_hours = (_n_(642028, 'mon', lambda: mon) + _n_(642029, 'tue', lambda: tue) + _n_(642030, 'wed', lambda: wed) + _n_(642031, 'thu', lambda: thu) + _n_(642032, 'fri', lambda: fri) + _n_(642033, 'sat', lambda: sat) + _n_(642034, 'sun', lambda: sun))
_l_(642035)

total_seconds = _c_(642038, _a_(642037, _n_(642036, 'week_hours', lambda: week_hours), 'total_seconds'))
_l_(642039)

hours = ((_n_(642040, 'total_seconds', lambda: total_seconds) / 60) / 60)
_l_(642041)

pay = _c_(642045, _n_(642042, 'float', lambda: float), _n_(642043, 'hours', lambda: hours) * _n_(642044, 'wage', lambda: wage))
_l_(642046)

_c_(642049, _a_(642048, _n_(642047, 'outSheet', lambda: outSheet), 'write'), 'A10', 'Wages')
_l_(642050)
_c_(642054, _a_(642052, _n_(642051, 'outSheet', lambda: outSheet), 'write'), 'B10', _n_(642053, 'pay', lambda: pay))
_l_(642055)

_c_(642058, _a_(642057, _n_(642056, 'outWorkbook', lambda: outWorkbook), 'close'))  # Closes and saves Excel spreadsheet
_l_(642059)  # Closes and saves Excel spreadsheet