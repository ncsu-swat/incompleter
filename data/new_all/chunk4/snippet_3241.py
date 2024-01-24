# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76864344/spire-xls-for-python-produces-attributeerror-nonetype-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from spire.xls import *
    _l_(622878)

except ImportError:
    pass
try:
    from spire.common import *
    _l_(622880)

except ImportError:
    pass


inputFile = "/Users/myname/Desktop/XYZ.xlsm"
_l_(622881)
outputFile = "/Users/myname/Library/Mobile      Documents/com~apple~CloudDocs/Development/CellRangeToPDF.pdf"
_l_(622882)

#create a workbook
workbook = _c_(622884, _n_(622883, "Workbook", lambda: Workbook))
_l_(622885)
#load a excel document
_c_(622889, _a_(622887, _n_(622886, "workbook", lambda: workbook), "LoadFromFile"), _n_(622888, "inputFile", lambda: inputFile))
_l_(622890)
_a_(622892, _n_(622891, "workbook", lambda: workbook), "ConverterSetting").SheetFitToPage = True
_l_(622893)
#convert to PDF file
_c_(622899, _a_(622895, _n_(622894, "workbook", lambda: workbook), "SaveToFile"), _n_(622896, "outputFile", lambda: outputFile), _a_(622898, _n_(622897, "FileFormat", lambda: FileFormat), "pdf"))
_l_(622900)
_c_(622903, _a_(622902, _n_(622901, "workbook", lambda: workbook), "Dispose"))
_l_(622904)