# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60616722/typeerror-when-chunking-subtasks-in-grouped-tasks
#!/usr/bin/env python3

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from celery import Celery, group
    _l_(575547)

except ImportError:
    pass
try:
    from io import BytesIO
    _l_(575549)

except ImportError:
    pass
try:
    import time
    _l_(575551)

except ImportError:
    pass
try:
    import xlsxwriter
    _l_(575553)

except ImportError:
    pass
try:
    import argparse
    _l_(575555)

except ImportError:
    pass
try:
    import sys
    _l_(575557)

except ImportError:
    pass

# Celery related :

app = _c_(575559, _n_(575558, "Celery", lambda: Celery), 'tasks', broker='amqp://admin:mypass@rabbit', backend='rpc://')
_l_(575560)

def apply_power(entry, power):
    _l_(575568)

    _c_(575563, _a_(575562, _n_(575561, "time", lambda: time), "sleep"), 0.01)
    _l_(575564)
    aux = _n_(575565, "entry", lambda: entry) ** _n_(575566, "power", lambda: power)
    _l_(575567)
    return aux

def make_data_for_entry(entries, power):
    _l_(575576)

    aux = [(_n_(575569, "entry", lambda: entry), _c_(575573, _n_(575570, "apply_power", lambda: apply_power), _n_(575571, "entry", lambda: entry), _n_(575572, "power", lambda: power))) for entry in _n_(575574, "entries", lambda: entries)]
    _l_(575575)
    return aux

@_a_(575578, _n_(575577, "app", lambda: app), "task")
def decorated_make_data_for_entry(*args):
    _l_(575583)

    aux = _c_(575581, _n_(575579, "make_data_for_entry", lambda: make_data_for_entry), *_n_(575580, "args", lambda: args))
    _l_(575582)
    return aux

@_a_(575585, _n_(575584, "app", lambda: app), "task")
def make_worksheet_data(entries, power, header, chunks):
    _l_(575616)

    if _n_(575586, "chunks", lambda: chunks) is not None:
        _l_(575612)

        result = _c_(575595, _c_(575593, _a_(575588, _n_(575587, "decorated_make_data_for_entry", lambda: decorated_make_data_for_entry), "chunks"), _c_(575591, _n_(575589, "zip", lambda: zip), _n_(575590, "entries", lambda: entries)), _n_(575592, "chunks", lambda: chunks)), _n_(575594, "power", lambda: power))
        _l_(575596)
        result = _c_(575605, _c_(575603, _a_(575598, _n_(575597, "make_data_for_entry", lambda: make_data_for_entry), "chunks"), _c_(575601, _n_(575599, "zip", lambda: zip), _n_(575600, "entries", lambda: entries)), _n_(575602, "chunks", lambda: chunks)), _n_(575604, "power", lambda: power))
        _l_(575606)
    else:
        result = _c_(575610, _n_(575607, "make_data_for_entry", lambda: make_data_for_entry), _n_(575608, "entries", lambda: entries), _n_(575609, "power", lambda: power))
        _l_(575611)
    aux = [_n_(575613, "header", lambda: header)] + _n_(575614, "result", lambda: result)
    _l_(575615)
    return aux

@_a_(575618, _n_(575617, "app", lambda: app), "task")
def decorated_make_worksheet_data(*args):
    _l_(575623)

    aux = _c_(575621, _n_(575619, "make_worksheet_data", lambda: make_worksheet_data), *_n_(575620, "args", lambda: args))
    _l_(575622)
    return aux

def make_worksheet_from_data(workbook, worksheet_data, name):
    _l_(575644)

    worksheet = _c_(575627, _a_(575625, _n_(575624, "workbook", lambda: workbook), "add_worksheet"), _n_(575626, "name", lambda: name))
    _l_(575628)
    for i, row in _c_(575631, _n_(575629, "enumerate", lambda: enumerate), _n_(575630, "worksheet_data", lambda: worksheet_data)):
        _l_(575643)

        for j, cell in _c_(575634, _n_(575632, "enumerate", lambda: enumerate), _n_(575633, "row", lambda: row)):
            _l_(575642)

            _c_(575640, _a_(575636, _n_(575635, "worksheet", lambda: worksheet), "write"), _n_(575637, "i", lambda: i), _n_(575638, "j", lambda: j), _n_(575639, "cell", lambda: cell))
            _l_(575641)

def generate_output(parsed_args, output):
    _l_(575716)

    workbook = _c_(575648, _a_(575646, _n_(575645, "xlsxwriter", lambda: xlsxwriter), "Workbook"), _n_(575647, "output", lambda: output))
    _l_(575649)
    entries = _c_(575653, _n_(575650, "range", lambda: range), _a_(575652, _n_(575651, "parsed_args", lambda: parsed_args), "entries"))
    _l_(575654)
    if _a_(575656, _n_(575655, "parsed_args", lambda: parsed_args), "multi") is not None:
        _l_(575701)

        g = _c_(575674, _n_(575657, "group", lambda: group), [
            _c_(575665, _a_(575659, _n_(575658, "decorated_make_worksheet_data", lambda: decorated_make_worksheet_data), "s"), _c_(575662, _n_(575660, "list", lambda: list), _n_(575661, "entries", lambda: entries)), 2, ["value", "square"], _a_(575664, _n_(575663, "parsed_args", lambda: parsed_args), "chunks")),
            _c_(575673, _a_(575667, _n_(575666, "decorated_make_worksheet_data", lambda: decorated_make_worksheet_data), "s"), _c_(575670, _n_(575668, "list", lambda: list), _n_(575669, "entries", lambda: entries)), 3, ["value", "cube"], _a_(575672, _n_(575671, "parsed_args", lambda: parsed_args), "chunks")),
        ])  # also tried without the []
        _l_(575675)  # also tried without the []
        result = _c_(575677, _n_(575676, "g", lambda: g))
        _l_(575678)
        result_get = _c_(575681, _a_(575680, _n_(575679, "result", lambda: result), "get"))
        _l_(575682)
        worksheet_square_data, worksheet_cube_data = _n_(575683, "result_get", lambda: result_get)
        _l_(575684)
    else:
        worksheet_square_data = _c_(575691, _n_(575685, "make_worksheet_data", lambda: make_worksheet_data), _c_(575688, _n_(575686, "list", lambda: list), _n_(575687, "entries", lambda: entries)), 2, ["value", "square"], _a_(575690, _n_(575689, "parsed_args", lambda: parsed_args), "chunks"))
        _l_(575692)
        worksheet_cube_data = _c_(575699, _n_(575693, "make_worksheet_data", lambda: make_worksheet_data), _c_(575696, _n_(575694, "list", lambda: list), _n_(575695, "entries", lambda: entries)), 3, ["value", "cube"], _a_(575698, _n_(575697, "parsed_args", lambda: parsed_args), "chunks"))
        _l_(575700)
    _c_(575705, _n_(575702, "make_worksheet_from_data", lambda: make_worksheet_from_data), _n_(575703, "workbook", lambda: workbook), _n_(575704, "worksheet_square_data", lambda: worksheet_square_data), "square")
    _l_(575706)
    _c_(575710, _n_(575707, "make_worksheet_from_data", lambda: make_worksheet_from_data), _n_(575708, "workbook", lambda: workbook), _n_(575709, "worksheet_cube_data", lambda: worksheet_cube_data), "cube")
    _l_(575711)
    _c_(575714, _a_(575713, _n_(575712, "workbook", lambda: workbook), "close"))
    _l_(575715)

@_a_(575718, _n_(575717, "app", lambda: app), "task")
def generate_file_from_output(parsed_args):
    _l_(575741)

    output = _c_(575720, _n_(575719, "BytesIO", lambda: BytesIO))
    _l_(575721)
    _c_(575725, _n_(575722, "generate_output", lambda: generate_output), _n_(575723, "parsed_args", lambda: parsed_args), _n_(575724, "output", lambda: output))
    _l_(575726)
    with _c_(575728, _n_(575727, "open", lambda: open), "/dump/file.xlsx", "wb") as f:
        _l_(575740)

        _c_(575731, _a_(575730, _n_(575729, "output", lambda: output), "seek"), 0)
        _l_(575732)
        _c_(575738, _a_(575734, _n_(575733, "f", lambda: f), "write"), _c_(575737, _a_(575736, _n_(575735, "output", lambda: output), "read")))
        _l_(575739)

def main():
    _l_(575745)

    _c_(575743, _n_(575742, "generate_file_from_output", lambda: generate_file_from_output))
    _l_(575744)

if _n_(575746, "__name__", lambda: __name__) == "__main__":
    _l_(575750)

    _c_(575748, _n_(575747, "main", lambda: main))
    _l_(575749)