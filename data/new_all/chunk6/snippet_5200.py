# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61302958/typeerror-not-supported-between-instances-of-int-and-dict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xlrd
    _l_(361389)

except ImportError:
    pass
try:
    from xlrd import xldate_as_tuple
    _l_(361391)

except ImportError:
    pass
try:
    import datetime
    _l_(361393)

except ImportError:
    pass


data1 = _c_(361396, _a_(361395, _n_(361394, "xlrd", lambda: xlrd), "open_workbook"), r'D:\\test.xlsx')
_l_(361397)
table = _c_(361400, _a_(361399, _n_(361398, "data1", lambda: data1), "sheets"))[0]
_l_(361401)

tables = []
_l_(361402)


def import_excel(excel):
    _l_(361434)

    for test in _c_(361406, _n_(361403, "range", lambda: range), _a_(361405, _n_(361404, "excel", lambda: excel), "nrows")):
        _l_(361433)

        array = [_c_(361410, _a_(361408, _n_(361407, "table", lambda: table), "cell_value"), _n_(361409, "test", lambda: test), 0), _c_(361414, _a_(361412, _n_(361411, "table", lambda: table), "cell_value"), _n_(361413, "test", lambda: test), 1),
                 _c_(361418, _a_(361416, _n_(361415, "table", lambda: table), "cell_value"), _n_(361417, "test", lambda: test), 2), _c_(361422, _a_(361420, _n_(361419, "table", lambda: table), "cell_value"), _n_(361421, "test", lambda: test), 3),
                 _c_(361426, _a_(361424, _n_(361423, "table", lambda: table), "cell_value"), _n_(361425, "test", lambda: test), 4)]
        _l_(361427)
        _c_(361431, _a_(361429, _n_(361428, "tables", lambda: tables), "append"), _n_(361430, "array", lambda: array))
        _l_(361432)


if _n_(361435, "__name__", lambda: __name__) == '__main__':
    _l_(361446)

    _c_(361438, _n_(361436, "import_excel", lambda: import_excel), _n_(361437, "table", lambda: table))
    _l_(361439)
    for i in _n_(361440, "tables", lambda: tables):
        _l_(361445)

        # pass
        _c_(361443, _n_(361441, "print", lambda: print), _n_(361442, "i", lambda: i))
        _l_(361444)

num1 = _n_(361447, "tables", lambda: tables)[0]
_l_(361448)
num2 = _n_(361449, "tables", lambda: tables)[1]
_l_(361450)
num3 = _n_(361451, "tables", lambda: tables)[2]
_l_(361452)
num4 = _n_(361453, "tables", lambda: tables)[3]
_l_(361454)
num5 = _n_(361455, "tables", lambda: tables)[4]
_l_(361456)

nu1 = 1
_l_(361457)
while _n_(361458, "nu1", lambda: nu1) < _n_(361459, "num2", lambda: num2):
    _l_(361470)

    _c_(361466, _n_(361460, "print", lambda: print), "%d\t%d\t%d\t%d\t%d" % (_n_(361461, "nu1", lambda: nu1), _n_(361462, "num2", lambda: num2), _n_(361463, "num3", lambda: num3), _n_(361464, "num4", lambda: num4), _n_(361465, "num5", lambda: num5)))
    _l_(361467)
    nu1 = _n_(361468, "nu1", lambda: nu1) + 1
    _l_(361469)