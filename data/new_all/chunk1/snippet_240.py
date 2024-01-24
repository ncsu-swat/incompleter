# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56249161/typeerror-unsupported-operand-types-for-list-and-int-while-extractin
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy
    _l_(383178)

except ImportError:
    pass
try:
    import PyPDF2
    _l_(383180)

except ImportError:
    pass

fd = _c_(383182, _n_(383181, "open", lambda: open), './sample2.pdf', 'rb')
_l_(383183)
pdfreader = _c_(383187, _a_(383185, _n_(383184, "PyPDF2", lambda: PyPDF2), "PdfFileReader"), _n_(383186, "fd", lambda: fd))
_l_(383188)
page = _c_(383191, _a_(383190, _n_(383189, "pdfreader", lambda: pdfreader), "getPage"), 1)
_l_(383192)
content = _c_(383195, _a_(383194, _n_(383193, "page", lambda: page), "extractText"))
_l_(383196)
tableList = _c_(383199, _a_(383198, _n_(383197, "content", lambda: content), "split"), '\n')
_l_(383200)
#table has four columns
lines = _c_(383207, _a_(383202, _n_(383201, "numpy", lambda: numpy), "array_split"), _n_(383203, "tableList", lambda: tableList), _c_(383206, _n_(383204, "len", lambda: len), _n_(383205, "tableList", lambda: tableList)/4))
_l_(383208)
# displaying row by row 
for i in _c_(383210, _n_(383209, "range", lambda: range), 0,5):
    _l_(383216)

    _c_(383214, _n_(383211, "print", lambda: print), _n_(383212, "lines", lambda: lines)[_n_(383213, "i", lambda: i)])
    _l_(383215)