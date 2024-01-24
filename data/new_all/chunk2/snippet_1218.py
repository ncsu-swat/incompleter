# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/21886641/printout-typeerror-bool
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import win32com.client
    _l_(437131)

except ImportError:
    pass

ExObj = _c_(437134, _a_(437133, _a_(437132, win32com, "client"), "Dispatch"), "Excel.Application")
_l_(437135)
_n_(437136, "ExObj", lambda: ExObj).Visible = 1
_l_(437137)
wb = _c_(437141, _a_(437140, _a_(437139, _n_(437138, "ExObj", lambda: ExObj), "Workbooks"), "Open"), '')
_l_(437142)
ws = _a_(437144, _n_(437143, "wb", lambda: wb), "Worksheets")[0]
_l_(437145)
_c_(437148, _a_(437147, _n_(437146, "ws", lambda: ws), "printout"))
_l_(437149)