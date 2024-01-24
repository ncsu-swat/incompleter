# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51717503/python3-x-typeerror-expected-str-bytes-or-os-pathlike-object-not-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
     import xlwt
     _l_(427239)

except ImportError:
     pass
try:
     import os
     _l_(427241)

except ImportError:
     pass
try:
     import fnmatch
     _l_(427243)

except ImportError:
     pass

path='Z:\Data\13-output'
_l_(427244)
wbk = _c_(427247, _a_(427246, _n_(427245, "xlwt", lambda: xlwt), "Workbook"))
_l_(427248)
sheet = _c_(427251, _a_(427250, _n_(427249, "wbk", lambda: wbk), "add_sheet"), 'data')
_l_(427252)
row = 0
_l_(427253)


for files in _c_(427257, _a_(427255, _n_(427254, "os", lambda: os), "walk"), _n_(427256, "path", lambda: path)):
     _l_(427282)

     for file in _n_(427258, "files", lambda: files):
          _l_(427281)

          if _c_(427262, _a_(427260, _n_(427259, "fnmatch", lambda: fnmatch), "fnmatch"), _n_(427261, "file", lambda: file), '*.txt'):
               _l_(427280)

               L = _c_(427271, _a_(427270, _c_(427269, _n_(427263, "open", lambda: open), _c_(427268, _a_(427266, _a_(427265, _n_(427264, "os", lambda: os), "path"), "join"), _n_(427267, "file", lambda: file)), "r"), "read"))
               _l_(427272)
               _c_(427277, _a_(427274, _n_(427273, "sheet", lambda: sheet), "write"), _n_(427275, "row", lambda: row),5,_n_(427276, "L", lambda: L))
               _l_(427278)
               row += 1
               _l_(427279)

_c_(427285, _a_(427284, _n_(427283, "wbk", lambda: wbk), "save"), 'all_values_in_txt.xls')
_l_(427286)