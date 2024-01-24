# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55764232/typeerror-write-object-cannot-be-interpreted-as-an-integer-write-is-the-na
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from xlwt import Workbook
    _l_(533378)

except ImportError:
    pass
try:
    import random
    _l_(533380)

except ImportError:
    pass
try:
    import string
    _l_(533382)

except ImportError:
    pass


class write_to_excel():
    _l_(533403)




    wb = _c_(533384, _n_(533383, "Workbook", lambda: Workbook))
    _l_(533385)

    # add_sheet is used to create sheet.
    sheet1 = _c_(533387, _a_(533386, wb, "add_sheet"), 'Sheet 1')
    _l_(533388)

    def randomString(stringLength=10):
        _l_(533402)

        """Generate a random string of fixed length """
        letters = _a_(533390, _n_(533389, "string", lambda: string), "ascii_lowercase")
        _l_(533391)
        aux = _c_(533400, _a_(533392, '', "join"), (_c_(533396, _a_(533394, _n_(533393, "random", lambda: random), "choice"), _n_(533395, "letters", lambda: letters)) for i in _c_(533399, _n_(533397, "range", lambda: range), _n_(533398, "stringLength", lambda: stringLength))))
        _l_(533401)
        return aux


s = _c_(533405, _n_(533404, "write_to_excel", lambda: write_to_excel))
_l_(533406)
r = _c_(533409, _a_(533408, _n_(533407, "s", lambda: s), "randomString"))
_l_(533410)
_c_(533413, _n_(533411, "print", lambda: print), _n_(533412, "r", lambda: r))
_l_(533414)