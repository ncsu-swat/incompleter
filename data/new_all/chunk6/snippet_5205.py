# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61302958/typeerror-not-supported-between-instances-of-int-and-dict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xlrd
    _l_(366084)

except ImportError:
    pass
try:
    from xlrd import xldate_as_tuple
    _l_(366086)

except ImportError:
    pass
try:
    import datetime
    _l_(366088)

except ImportError:
    pass


data1 = _c_(366091, _a_(366090, _n_(366089, "xlrd", lambda: xlrd), "open_workbook"), r'D:\\test.xlsx')
_l_(366092)
table = _c_(366095, _a_(366094, _n_(366093, "data1", lambda: data1), "sheets"))[0]
_l_(366096)

tables = []
_l_(366097)


def import_excel(excel):
    _l_(366129)

    for test in _c_(366101, _n_(366098, "range", lambda: range), _a_(366100, _n_(366099, "excel", lambda: excel), "nrows")):
        _l_(366128)

        array = [_c_(366105, _a_(366103, _n_(366102, "table", lambda: table), "cell_value"), _n_(366104, "test", lambda: test), 0), _c_(366109, _a_(366107, _n_(366106, "table", lambda: table), "cell_value"), _n_(366108, "test", lambda: test), 1),
                 _c_(366113, _a_(366111, _n_(366110, "table", lambda: table), "cell_value"), _n_(366112, "test", lambda: test), 2), _c_(366117, _a_(366115, _n_(366114, "table", lambda: table), "cell_value"), _n_(366116, "test", lambda: test), 3),
                 _c_(366121, _a_(366119, _n_(366118, "table", lambda: table), "cell_value"), _n_(366120, "test", lambda: test), 4)]
        _l_(366122)
        _c_(366126, _a_(366124, _n_(366123, "tables", lambda: tables), "append"), _n_(366125, "array", lambda: array))
        _l_(366127)


if _n_(366130, "__name__", lambda: __name__) == '__main__':
    _l_(366141)

    _c_(366133, _n_(366131, "import_excel", lambda: import_excel), _n_(366132, "table", lambda: table))
    _l_(366134)
    for i in _n_(366135, "tables", lambda: tables):
        _l_(366140)

        # pass
        _c_(366138, _n_(366136, "print", lambda: print), _n_(366137, "i", lambda: i))
        _l_(366139)

num1 = _n_(366142, "tables", lambda: tables)[0]
_l_(366143)
num2 = _n_(366144, "tables", lambda: tables)[1]
_l_(366145)
num3 = _n_(366146, "tables", lambda: tables)[2]
_l_(366147)
num4 = _n_(366148, "tables", lambda: tables)[3]
_l_(366149)
num5 = _n_(366150, "tables", lambda: tables)[4]
_l_(366151)

nu1 = 1
_l_(366152)
while _n_(366153, "nu1", lambda: nu1) < _n_(366154, "num2", lambda: num2):
    _l_(366165)

    _c_(366161, _n_(366155, "print", lambda: print), "%d\t%d\t%d\t%d\t%d" % (_n_(366156, "nu1", lambda: nu1), _n_(366157, "num2", lambda: num2), _n_(366158, "num3", lambda: num3), _n_(366159, "num4", lambda: num4), _n_(366160, "num5", lambda: num5)))
    _l_(366162)
    nu1 = _n_(366163, "nu1", lambda: nu1) + 1
    _l_(366164)