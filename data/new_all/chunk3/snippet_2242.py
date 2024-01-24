# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56119642/is-there-a-solution-for-attributeerror-nonetype-object-has-no-attribute-wor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import openpyxl
    _l_(522851)

except ImportError:
    pass

wb = _c_(522854, _a_(522853, _n_(522852, "openpyxl", lambda: openpyxl), "load_workbook"), 'test1.xlsx' )
_l_(522855)

_a_(522858, _a_(522857, _n_(522856, "wb", lambda: wb), "security"), "workbookPassword").value = 'test_password'
_l_(522859)
_a_(522861, _n_(522860, "wb", lambda: wb), "security").lockStructure = True
_l_(522862)