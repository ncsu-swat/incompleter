# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65372742/python-kivy-attributeerror-nonetype-object-has-no-attribute-text
#exel database
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xlrd, xlwt
    _l_(639657)

except ImportError:
    pass
try:
    from xlutils.copy import copy
    _l_(639659)

except ImportError:
    pass
try:
    import datetime
    _l_(639661)

except ImportError:
    pass

class DataBase:
    _l_(639783)

    def __init__(self, filename):
        _l_(639673)

        _n_(639662, "self", lambda: self).filename = _n_(639663, "filename", lambda: filename)
        _l_(639664)
        _n_(639665, "self", lambda: self).loadinfo = None
        _l_(639666)
        _n_(639667, "self", lambda: self).file = None
        _l_(639668)
        _c_(639671, _a_(639670, _n_(639669, "self", lambda: self), "load"))
        _l_(639672)

    def load(self):
        _l_(639708)

        _n_(639674, "self", lambda: self).file = _c_(639678, _n_(639675, "open", lambda: open), _a_(639677, _n_(639676, "self", lambda: self), "filename"), "r")
        _l_(639679)
        _n_(639680, "self", lambda: self).loadinfo = {}
        _l_(639681)

        for line in _a_(639683, _n_(639682, "self", lambda: self), "file"):
            _l_(639702)

            invoice, purpose, carrier, cost, local, outcal, Driver, Dispatcher = _c_(639688, _a_(639687, _c_(639686, _a_(639685, _n_(639684, "line", lambda: line), "strip")), "split"), ";")
            _l_(639689)
            _a_(639691, _n_(639690, "self", lambda: self), "loadinfo")[_n_(639692, "invoice", lambda: invoice)] = (_n_(639693, "invoice", lambda: invoice), _n_(639694, "purpose", lambda: purpose), _n_(639695, "carrier", lambda: carrier), _n_(639696, "cost", lambda: cost), _n_(639697, "local", lambda: local), _n_(639698, "outcal", lambda: outcal), _n_(639699, "Driver", lambda: Driver), _n_(639700, "Dispatcher", lambda: Dispatcher))
            _l_(639701)

        _c_(639706, _a_(639705, _a_(639704, _n_(639703, "self", lambda: self), "file"), "close"))
        _l_(639707)

    def top_right(self, invoice, purpose):
        _l_(639710)

        pass
        _l_(639709)

    def add_loadinfo(self, invoice, purpose, carrier, cost, local, outcal, Driver, Dispatcher):
        _l_(639748)

        _a_(639712, _n_(639711, "self", lambda: self), "loadinfo")[_c_(639715, _a_(639714, _n_(639713, "invoice", lambda: invoice), "strip"))] = (_c_(639718, _a_(639717, _n_(639716, "invoice", lambda: invoice), "strip")), _c_(639721, _a_(639720, _n_(639719, "purpose", lambda: purpose), "strip")), _c_(639724, _a_(639723, _n_(639722, "carrier", lambda: carrier), "strip")), _c_(639727, _a_(639726, _n_(639725, "cost", lambda: cost), "strip")), _c_(639730, _a_(639729, _n_(639728, "local", lambda: local), "strip")), _c_(639733, _a_(639732, _n_(639731, "outcal", lambda: outcal), "strip")), _c_(639736, _a_(639735, _n_(639734, "Driver", lambda: Driver), "strip")), _c_(639739, _a_(639738, _n_(639737, "Dispatcher", lambda: Dispatcher), "strip")), _c_(639742, _a_(639741, _n_(639740, "DataBase", lambda: DataBase), "get_date")))
        _l_(639743)
        _c_(639746, _a_(639745, _n_(639744, "self", lambda: self), "save"))
        _l_(639747)

    
    def save(self):
        _l_(639771)

        with _c_(639752, _n_(639749, "open", lambda: open), _a_(639751, _n_(639750, "self", lambda: self), "filename"), "w") as f:
            _l_(639770)

            for loadinfo in _a_(639754, _n_(639753, "self", lambda: self), "loadinfo"):
                _l_(639769)

                _c_(639767, _a_(639756, _n_(639755, "f", lambda: f), "write"), _n_(639757, "loadinfo", lambda: loadinfo) + ";" + _a_(639759, _n_(639758, "self", lambda: self), "loadinfo")[_n_(639760, "invoice", lambda: invoice)][0] + ";" + _a_(639762, _n_(639761, "self", lambda: self), "loadinfo")[_n_(639763, "invoice", lambda: invoice)][1] + ";" + _a_(639765, _n_(639764, "self", lambda: self), "loadinfo")[_n_(639766, "invoice", lambda: invoice)][2] + "\n")
                _l_(639768)

    @_n_(639772, "staticmethod", lambda: staticmethod)
    def get_date():
        _l_(639782)

        aux = _c_(639780, _a_(639779, _c_(639778, _n_(639773, "str", lambda: str), _c_(639777, _a_(639776, _a_(639775, _n_(639774, "datetime", lambda: datetime), "datetime"), "now"))), "split"), " ")[0]
        _l_(639781)
        return aux

#code to put it into excel

# read_book = xlrd.open_workbook("Invoice.xls", formatting_info=True) #Make Readable Copy
# write_book = copy(read_book) #Make Writeable Copy

# write_sheet1 = write_book.get_sheet(1) #Get sheet 1 in writeable copy
# write_sheet1.write(1, 11, self.invoice.text) #Write 'test' to cell (1, 11)

# write_sheet2 = write_book.get_sheet(2) #Get sheet 2 in writeable copy
# write_sheet2.write(3, 14, '135') #Write '135' to cell (3, 14)

# write_book.save("New/File/Path") #Save the newly written copy. Enter the same as the old path to write over