# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69648331/unable-to-load-workbook-typeerror-expected-class-openpyxl-chart-axis-numeri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import openpyxl
    _l_(457936)

except ImportError:
    pass

wb = _c_(457939, _a_(457938, _n_(457937, "openpyxl", lambda: openpyxl), "load_workbook"), 'test.xlsm', data_only=True)
_l_(457940)
sheets = _a_(457942, _n_(457941, "wb", lambda: wb), "sheetnames")
_l_(457943)
x = _n_(457944, "wb", lambda: wb)[_n_(457945, "sheets", lambda: sheets)[0]]
_l_(457946)