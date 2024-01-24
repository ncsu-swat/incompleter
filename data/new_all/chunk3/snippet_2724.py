# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65500142/how-do-i-fix-this-python-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(535302)

except ImportError:
    pass

# starting values for day, month and year
parent_dir = 'C:\\Users\\locale\\Desktop\\DIRS\\'
_l_(535303)
day_int = 16
_l_(535304)
month_int = 9
_l_(535305)
year_int = 2020
_l_(535306)


def gen_day_str():
    _l_(535333)

    if _c_(535311, _n_(535307, "len", lambda: len), _c_(535310, _n_(535308, "str", lambda: str), _n_(535309, "day_int", lambda: day_int))) == 1:
        _l_(535332)

        day_str = '0' + _c_(535314, _n_(535312, "str", lambda: str), _n_(535313, "day_int", lambda: day_int))
        _l_(535315)
    elif _c_(535320, _n_(535316, "len", lambda: len), _c_(535319, _n_(535317, "str", lambda: str), _n_(535318, "day_int", lambda: day_int))) == 2:
        _l_(535331)

        day_str = _c_(535323, _n_(535321, "str", lambda: str), _n_(535322, "day_int", lambda: day_int))
        _l_(535324)
    else:
        _c_(535326, _n_(535325, "print", lambda: print), 'error! exiting...')
        _l_(535327)
        aux = ""
        _l_(535330)
        exit(aux)
def gen_month_str():
    _l_(535360)

    if _c_(535338, _n_(535334, "len", lambda: len), _c_(535337, _n_(535335, "str", lambda: str), _n_(535336, "month_int", lambda: month_int))) == 1:
        _l_(535359)

        month_str = '0' + _c_(535341, _n_(535339, "str", lambda: str), _n_(535340, "month_int", lambda: month_int))
        _l_(535342)
    elif _c_(535347, _n_(535343, "len", lambda: len), _c_(535346, _n_(535344, "str", lambda: str), _n_(535345, "month_int", lambda: month_int))) == 2:
        _l_(535358)

        month_str = _c_(535350, _n_(535348, "str", lambda: str), _n_(535349, "month_int", lambda: month_int))
        _l_(535351)
    else:
        _c_(535353, _n_(535352, "print", lambda: print), 'error! exiting...')
        _l_(535354)
        aux = ""
        _l_(535357)
        exit(aux)
def gen_year_str():
    _l_(535365)

    year_str = _c_(535363, _n_(535361, "str", lambda: str), _n_(535362, "year_int", lambda: year_int))
    _l_(535364)
def gen_dir_name():
    _l_(535379)

    _c_(535367, _n_(535366, "gen_day_str", lambda: gen_day_str))
    _l_(535368)
    _c_(535370, _n_(535369, "gen_month_str", lambda: gen_month_str))
    _l_(535371)
    _c_(535373, _n_(535372, "gen_year_str", lambda: gen_year_str))
    _l_(535374)
    dir_name = _n_(535375, "day_str", lambda: day_str) + '-' + _n_(535376, "month_str", lambda: month_str) + '-' + _n_(535377, "year_str", lambda: year_str)
    _l_(535378)


while _n_(535380, "day_int", lambda: day_int) <= 30:
    _l_(535391)

    _c_(535382, _n_(535381, "gen_dir_name", lambda: gen_dir_name))
    _l_(535383)
    _c_(535388, _a_(535385, _n_(535384, "os", lambda: os), "mkdir"), _n_(535386, "parent_dir", lambda: parent_dir) + _n_(535387, "dir_name", lambda: dir_name))
    _l_(535389)
    day_int += 1
    _l_(535390)
day_int = 1
_l_(535392)
month_int = 10
_l_(535393)
while _n_(535394, "day_int", lambda: day_int) <= 16:
    _l_(535405)

    _c_(535396, _n_(535395, "gen_dir_name", lambda: gen_dir_name))
    _l_(535397)
    _c_(535402, _a_(535399, _n_(535398, "os", lambda: os), "mkdir"), _n_(535400, "parent_dir", lambda: parent_dir) + _n_(535401, "dir_name", lambda: dir_name))
    _l_(535403)
    day_int += 1
    _l_(535404)

_c_(535407, _n_(535406, "print", lambda: print), 'folders created successfully!')
_l_(535408)
aux = ""
_l_(535411)
exit(aux)