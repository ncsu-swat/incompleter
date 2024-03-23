# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27515882/csv-reader-close-raises-an-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(402019)

except ImportError:
    pass
try:
    import csv
    _l_(402021)

except ImportError:
    pass
try:
    import os
    _l_(402023)

except ImportError:
    pass
login = "bakerg"
_l_(402024)

def upgradetoadmin():
    _l_(402268)

    global masterpassword
    _l_(402025)
    masterpassword = []
    _l_(402026)
    def one():
        _l_(402034)

        _c_(402029, _a_(402028, _n_(402027, "masterpassword", lambda: masterpassword), "append"), "1")
        _l_(402030)
        _c_(402032, _n_(402031, "arraycheck", lambda: arraycheck))
        _l_(402033)
    def two():
        _l_(402042)

        _c_(402037, _a_(402036, _n_(402035, "masterpassword", lambda: masterpassword), "append"), "2")
        _l_(402038)
        _c_(402040, _n_(402039, "arraycheck", lambda: arraycheck))
        _l_(402041)
    def three():
        _l_(402050)

        _c_(402045, _a_(402044, _n_(402043, "masterpassword", lambda: masterpassword), "append"), "3")
        _l_(402046)
        _c_(402048, _n_(402047, "arraycheck", lambda: arraycheck))
        _l_(402049)
    def four():
        _l_(402058)

        _c_(402053, _a_(402052, _n_(402051, "masterpassword", lambda: masterpassword), "append"), "4")
        _l_(402054)
        _c_(402056, _n_(402055, "arraycheck", lambda: arraycheck))
        _l_(402057)
    def five():
        _l_(402066)

        _c_(402061, _a_(402060, _n_(402059, "masterpassword", lambda: masterpassword), "append"), "5")
        _l_(402062)
        _c_(402064, _n_(402063, "arraycheck", lambda: arraycheck))
        _l_(402065)
    def six():
        _l_(402074)

        _c_(402069, _a_(402068, _n_(402067, "masterpassword", lambda: masterpassword), "append"), "6")
        _l_(402070)
        _c_(402072, _n_(402071, "arraycheck", lambda: arraycheck))
        _l_(402073)
    def seven():
        _l_(402082)

        _c_(402077, _a_(402076, _n_(402075, "masterpassword", lambda: masterpassword), "append"), "7")
        _l_(402078)
        _c_(402080, _n_(402079, "arraycheck", lambda: arraycheck))
        _l_(402081)
    def eight():
        _l_(402090)

        _c_(402085, _a_(402084, _n_(402083, "masterpassword", lambda: masterpassword), "append"), "8")
        _l_(402086)
        _c_(402088, _n_(402087, "arraycheck", lambda: arraycheck))
        _l_(402089)
    def nine():
        _l_(402098)

        _c_(402093, _a_(402092, _n_(402091, "masterpassword", lambda: masterpassword), "append"), "9")
        _l_(402094)
        _c_(402096, _n_(402095, "arraycheck", lambda: arraycheck))
        _l_(402097)
    def zero():
        _l_(402106)

        _c_(402101, _a_(402100, _n_(402099, "masterpassword", lambda: masterpassword), "append"), "0")
        _l_(402102)
        _c_(402104, _n_(402103, "arraycheck", lambda: arraycheck))
        _l_(402105)
    def clear():
        _l_(402109)

        global masterpassword
        _l_(402107)
        masterpassword = []
        _l_(402108)
    def arraycheck():
        _l_(402175)

        global masterpassword
        _l_(402110)
        if _c_(402113, _n_(402111, "len", lambda: len), _n_(402112, "masterpassword", lambda: masterpassword)) == 4:
            _l_(402174)

            if _n_(402114, "masterpassword", lambda: masterpassword) == ['2','5','8','0']:
                _l_(402172)

                _c_(402116, _n_(402115, "print", lambda: print), "Success")
                _l_(402117)
                r = _c_(402122, _a_(402119, _n_(402118, "csv", lambda: csv), "reader"), _c_(402121, _n_(402120, "open", lambda: open), 'Student Data.csv'))
                _l_(402123)
                lines = [_n_(402124, "l", lambda: l) for l in _n_(402125, "r", lambda: r)]
                _l_(402126)
                _c_(402129, _n_(402127, "print", lambda: print), _n_(402128, "lines", lambda: lines))
                _l_(402130)
                i = 0
                _l_(402131)
                for item in _n_(402132, "lines", lambda: lines):
                    _l_(402164)

                    if _n_(402133, "item", lambda: item)[0] == _n_(402134, "login", lambda: login):
                        _l_(402163)

                        _c_(402137, _n_(402135, "print", lambda: print), _n_(402136, "item", lambda: item))
                        _l_(402138)
                        _c_(402140, _n_(402139, "print", lambda: print), "YAY")
                        _l_(402141)
                        _n_(402142, "item", lambda: item)[4] = "ADMIN"
                        _l_(402143)
                        _c_(402146, _n_(402144, "print", lambda: print), _n_(402145, "item", lambda: item))
                        _l_(402147)
                        _c_(402150, _a_(402149, _n_(402148, "os", lambda: os), "remove"), 'Student Data.csv')
                        _l_(402151)
                        writer = _c_(402156, _a_(402153, _n_(402152, "csv", lambda: csv), "writer"), _c_(402155, _n_(402154, "open", lambda: open), 'Student Data.csv', 'w'))
                        _l_(402157)
                        _c_(402161, _a_(402159, _n_(402158, "writer", lambda: writer), "writerows"), _n_(402160, "lines", lambda: lines))
                        _l_(402162)

                _c_(402167, _n_(402165, "print", lambda: print), _n_(402166, "login", lambda: login) + " is now an admin")
                _l_(402168)
            else:
                _c_(402170, _n_(402169, "print", lambda: print), "Invalid Code")
                _l_(402171)
            masterpassword = []
            _l_(402173)

    keypadwindow = _c_(402177, _n_(402176, "Tk", lambda: Tk))
    _l_(402178)
    _c_(402181, _a_(402180, _n_(402179, "keypadwindow", lambda: keypadwindow), "iconbitmap"), "hXYTZdJy.ico")
    _l_(402182)
    _c_(402185, _a_(402184, _n_(402183, "keypadwindow", lambda: keypadwindow), "title"), "ADMIN UPGRADER")
    _l_(402186)
    _c_(402192, _a_(402191, _c_(402190, _n_(402187, "Button", lambda: Button), _n_(402188, "keypadwindow", lambda: keypadwindow), text="1", height = 4, width = 10, command = _n_(402189, "one", lambda: one)), "grid"), column = 0, row = 0)
    _l_(402193)
    _c_(402199, _a_(402198, _c_(402197, _n_(402194, "Button", lambda: Button), _n_(402195, "keypadwindow", lambda: keypadwindow), text="2", height = 4, width = 10, command = _n_(402196, "two", lambda: two)), "grid"), column = 1, row = 0)
    _l_(402200)
    _c_(402206, _a_(402205, _c_(402204, _n_(402201, "Button", lambda: Button), _n_(402202, "keypadwindow", lambda: keypadwindow), text="3", height = 4, width = 10, command = _n_(402203, "three", lambda: three)), "grid"), column = 2, row = 0)
    _l_(402207)
    _c_(402213, _a_(402212, _c_(402211, _n_(402208, "Button", lambda: Button), _n_(402209, "keypadwindow", lambda: keypadwindow), text="4", height = 4, width = 10, command = _n_(402210, "four", lambda: four)), "grid"), column = 0, row = 1)
    _l_(402214)
    _c_(402220, _a_(402219, _c_(402218, _n_(402215, "Button", lambda: Button), _n_(402216, "keypadwindow", lambda: keypadwindow), text="5", height = 4, width = 10, command = _n_(402217, "five", lambda: five)), "grid"), column = 1, row = 1)
    _l_(402221)
    _c_(402227, _a_(402226, _c_(402225, _n_(402222, "Button", lambda: Button), _n_(402223, "keypadwindow", lambda: keypadwindow), text="6", height = 4, width = 10, command = _n_(402224, "six", lambda: six)), "grid"), column = 2, row = 1)
    _l_(402228)
    _c_(402234, _a_(402233, _c_(402232, _n_(402229, "Button", lambda: Button), _n_(402230, "keypadwindow", lambda: keypadwindow), text="7", height = 4, width = 10, command = _n_(402231, "seven", lambda: seven)), "grid"), column = 0, row = 2)
    _l_(402235)
    _c_(402241, _a_(402240, _c_(402239, _n_(402236, "Button", lambda: Button), _n_(402237, "keypadwindow", lambda: keypadwindow), text="8", height = 4, width = 10, command = _n_(402238, "eight", lambda: eight)), "grid"), column = 1, row = 2)
    _l_(402242)
    _c_(402248, _a_(402247, _c_(402246, _n_(402243, "Button", lambda: Button), _n_(402244, "keypadwindow", lambda: keypadwindow), text="9", height = 4, width = 10, command = _n_(402245, "nine", lambda: nine)), "grid"), column = 2, row = 2)
    _l_(402249)
    _c_(402255, _a_(402254, _c_(402253, _n_(402250, "Button", lambda: Button), _n_(402251, "keypadwindow", lambda: keypadwindow), text="0", height = 4, width = 10, command = _n_(402252, "zero", lambda: zero)), "grid"), column = 1, row = 3)
    _l_(402256)
    _c_(402262, _a_(402261, _c_(402260, _n_(402257, "Button", lambda: Button), _n_(402258, "keypadwindow", lambda: keypadwindow), text="CLEAR", height = 4, width = 10, command = _n_(402259, "clear", lambda: clear)), "grid"), column = 2, row = 3)
    _l_(402263)
    _c_(402266, _a_(402265, _n_(402264, "keypadwindow", lambda: keypadwindow), "mainloop"))
    _l_(402267)

_c_(402270, _n_(402269, "upgradetoadmin", lambda: upgradetoadmin))
_l_(402271)