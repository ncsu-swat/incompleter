# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41422386/python-3-5-2-openpyxl-v-2-4-1-get-highest-row-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
WorkBook = _c_(406802, _a_(406801, _n_(406800, "openpyxl", lambda: openpyxl), "load_workbook"), "G:\\Python_Created\\DS.xlsx")
_l_(406803)
#I have a Sheet named "Original" in my Excell Workbook
Sheet = _c_(406806, _a_(406805, _n_(406804, "WorkBook", lambda: WorkBook), "get_sheet_by_name"), "Original")
_l_(406807)
_c_(406810, _a_(406809, _n_(406808, "Sheet", lambda: Sheet), "get_highest_row"))
_l_(406811)