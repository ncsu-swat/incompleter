# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67333170/python-nameerror-after-introduction-of-if-clause
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
process_time_dfs = []
_l_(632853)
status_dfs = []
_l_(632854)

for string in _n_(632855, "filestrings", lambda: filestrings):
    _l_(632897)

    
    #read in command with apropriate delimiter and engine starting from a nmc-specific line in the excel doc
    EIS_TS_csv = _c_(632863, _a_(632857, _n_(632856, "pd", lambda: pd), "read_csv"), _c_(632861, _a_(632859, _n_(632858, "DATA_DIR", lambda: DATA_DIR), "joinpath"), _n_(632860, "string", lambda: string)), engine = 'python', delimiter = ';', skiprows = _n_(632862, "startposition", lambda: startposition))
    _l_(632864)

    #drop [descriptor] row
    _c_(632867, _a_(632866, _n_(632865, "EIS_TS_csv", lambda: EIS_TS_csv), "drop"), index = 0, axis = 0, inplace = True)
    _l_(632868)

    #add to dataframe
    _c_(632872, _a_(632870, _n_(632869, "status_dfs", lambda: status_dfs), "append"), _n_(632871, "EIS_TS_csv", lambda: EIS_TS_csv)['Status'])
    _l_(632873)
    
    if _a_(632875, _n_(632874, "EIS_TS_csv", lambda: EIS_TS_csv)['Progr. Zeit'], "dtype") == _n_(632876, "object", lambda: object):
        _l_(632896)

        _c_(632886, _a_(632878, _n_(632877, "process_time_dfs", lambda: process_time_dfs), "append"), _c_(632885, _a_(632883, _c_(632882, _a_(632881, _a_(632880, _n_(632879, "EIS_TS_csv", lambda: EIS_TS_csv)['Progr. Zeit'], "str"), "replace"), '.', ''), "astype"), _n_(632884, "float", lambda: float)))
        _l_(632887)
    else:
        _c_(632894, _a_(632889, _n_(632888, "process_time_dfs", lambda: process_time_dfs), "append"), _c_(632893, _a_(632891, _n_(632890, "EIS_TS_csv", lambda: EIS_TS_csv)['Progr. Zeit'], "astype"), _n_(632892, "float", lambda: float)))
        _l_(632895)