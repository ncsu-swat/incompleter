# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67333170/python-nameerror-after-introduction-of-if-clause
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
process_time_dfs = []
_l_(639005)
status_dfs = []
_l_(639006)

for string in _n_(639007, "filestrings", lambda: filestrings):
    _l_(639037)

    
    #read in command with apropriate delimiter and engine starting from a nmc-specific line in the excel doc
    EIS_TS_csv = _c_(639015, _a_(639009, _n_(639008, "pd", lambda: pd), "read_csv"), _c_(639013, _a_(639011, _n_(639010, "DATA_DIR", lambda: DATA_DIR), "joinpath"), _n_(639012, "string", lambda: string)), engine = 'python', delimiter = ';', skiprows = _n_(639014, "startposition", lambda: startposition))
    _l_(639016)

    #drop [descriptor] row
    _c_(639019, _a_(639018, _n_(639017, "EIS_TS_csv", lambda: EIS_TS_csv), "drop"), index = 0, axis = 0, inplace = True)
    _l_(639020)

    #add to dataframe
    _c_(639024, _a_(639022, _n_(639021, "status_dfs", lambda: status_dfs), "append"), _n_(639023, "EIS_TS_csv", lambda: EIS_TS_csv)['Status'])
    _l_(639025)
    _c_(639035, _a_(639027, _n_(639026, "process_time_dfs", lambda: process_time_dfs), "append"), _c_(639034, _a_(639032, _c_(639031, _a_(639030, _a_(639029, _n_(639028, "EIS_TS_csv", lambda: EIS_TS_csv)['Progr. Zeit'], "str"), "replace"), '.', ''), "astype"), _n_(639033, "float", lambda: float)))
    _l_(639036)