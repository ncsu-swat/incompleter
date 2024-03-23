# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56659854/typeerror-nonetype-object-is-not-subscriptable-only-showing-on-second-iterati
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while True:
    _l_(366838)

    _c_(366814, _n_(366813, "print_menu", lambda: print_menu));
    _l_(366815)

    try:
        _l_(366826)

        choice = _c_(366819, _n_(366816, "int", lambda: int), _c_(366818, _n_(366817, "input", lambda: input), "What is your choice?: "));
        _l_(366820)

    except:
        _l_(366825)

        _c_(366822, _n_(366821, "print", lambda: print), "Please enter an integer only");
        _l_(366823)
        continue;
        _l_(366824)

    if _n_(366827, "choice", lambda: choice) == 1:
        _l_(366837)

        _c_(366830, _n_(366828, "Process_a_new_data_file", lambda: Process_a_new_data_file), _n_(366829, "current_set", lambda: current_set));
        _l_(366831)

    elif _n_(366832, "choice", lambda: choice) == 2:
        _l_(366836)

        _c_(366834, _n_(366833, "Choose_units", lambda: Choose_units));
        _l_(366835)


def Choose_units():
    _l_(366887)

    global current_units
    _l_(366839)
    if _n_(366840, "current_units", lambda: current_units) is not None:
        _l_(366844)

        _c_(366842, _n_(366841, "print", lambda: print), "a")
        _l_(366843)
    _c_(366847, _n_(366845, "print", lambda: print), _n_(366846, "current_units", lambda: current_units))
    _l_(366848)
    units_used = _c_(366852, _a_(366850, _n_(366849, "UNITS", lambda: UNITS), "get"), _n_(366851, "current_units", lambda: current_units))[0]
    _l_(366853)
    _c_(366856, _n_(366854, "print", lambda: print), "Current units in " + _n_(366855, "units_used", lambda: units_used))
    _l_(366857)
    _c_(366859, _n_(366858, "print", lambda: print), "Choose new units:\n")
    _l_(366860)
    for i in _n_(366861, "UNITS", lambda: UNITS):
        _l_(366870)

        _c_(366868, _n_(366862, "print", lambda: print), _c_(366865, _n_(366863, "str", lambda: str), _n_(366864, "i", lambda: i)) + " - " + _n_(366866, "UNITS", lambda: UNITS)[_n_(366867, "i", lambda: i)][0])
        _l_(366869)
    while True:
        _l_(366886)

        current_units = _c_(366872, _n_(366871, "input", lambda: input), "Which unit?\n")
        _l_(366873)
        for i in _n_(366874, "UNITS", lambda: UNITS):
            _l_(366881)

            if(_c_(366877, _n_(366875, "int", lambda: int), _n_(366876, "current_units", lambda: current_units)) == _n_(366878, "i", lambda: i)):
                _l_(366880)

                aux = ""
                _l_(366879)
                return aux
        _c_(366883, _n_(366882, "print", lambda: print), "Please choose a unit from the list")
        _l_(366884)
        continue
        _l_(366885)