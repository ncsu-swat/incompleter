# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76841111/attributeerror-openpyxlwriter-object-has-no-setter-when-setting-writer-book
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
book = _c_(606033, _a_(606028, _n_(606027, "openpyxl", lambda: openpyxl), "load_workbook"), _c_(606032, _a_(606029, r'D:\Anto\Daily Work\Daily Reservoir Level\August\Plotting\Excel\{}.xlsx', "format"), _n_(606030, "my_list", lambda: my_list)[_n_(606031, "j", lambda: j)], data_only=True))
_l_(606034)
writer = _c_(606041, _a_(606036, _n_(606035, "pd", lambda: pd), "ExcelWriter"), _c_(606040, _a_(606037, r'D:\Anto\Daily Work\Daily Reservoir Level\August\Plotting\Excel\{}.xlsx', "format"), _n_(606038, "my_list", lambda: my_list)[_n_(606039, "j", lambda: j)]),engine='openpyxl', mode='a', if_sheet_exists='overlay')
_l_(606042)
_n_(606043, "writer", lambda: writer).book = _n_(606044, "book", lambda: book)
_l_(606045)