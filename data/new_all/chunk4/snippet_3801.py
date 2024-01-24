# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67757892/typeerror-cannot-convert-the-series-to-class-int-in-to-date
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(631402)

except ImportError:
    pass
try:
    import glob
    _l_(631404)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(631406)

except ImportError:
    pass
try:
    from pymongo import MongoClient
    _l_(631408)

except ImportError:
    pass

client = _c_(631410, _n_(631409, "MongoClient", lambda: MongoClient))
_l_(631411)
col = _n_(631412, "client", lambda: client)['right']['abcde']
_l_(631413)

listFileNames = _c_(631416, _a_(631415, _n_(631414, "glob", lambda: glob), "glob"), r"C:\Users\%username%\Desktop\Book1.csv")
_l_(631417)

# print(len(listFileNames))

cols = ["start_time", "end_time", "source_Ip", "source_Mac", "destination_Ip", "destination_Mac"]
_l_(631418)


def get_merged_data_frame(list_file_names, p_index_col=False, p_header=None, columns=None):
    _l_(631451)

    if _n_(631419, "columns", lambda: columns) is None:
        _l_(631422)

        columns = _n_(631420, "cols", lambda: cols)
        _l_(631421)
    if _c_(631425, _n_(631423, "len", lambda: len), _n_(631424, "list_file_names", lambda: list_file_names)) == 1:
        _l_(631450)

        aux = _c_(631432, _a_(631427, _n_(631426, "pd", lambda: pd), "read_csv"), _n_(631428, "list_file_names", lambda: list_file_names)[0], index_col=_n_(631429, "p_index_col", lambda: p_index_col), header=_n_(631430, "p_header", lambda: p_header), low_memory=False,
                           names=_n_(631431, "columns", lambda: columns),
                           usecols=[6, 7, 8, 9, 10, 11])
        _l_(631433)
        return aux
    else:
        df_from_each_file = (_c_(631440, _a_(631435, _n_(631434, "pd", lambda: pd), "read_csv"), _n_(631436, "f", lambda: f), index_col=_n_(631437, "p_index_col", lambda: p_index_col), header=_n_(631438, "p_header", lambda: p_header), low_memory=False, names=_n_(631439, "columns", lambda: columns),
                                         usecols=[6, 7, 8, 9, 10, 11])
                             for f in _n_(631441, "list_file_names", lambda: list_file_names))
        _l_(631442)
        concatenated_df = _c_(631446, _a_(631444, _n_(631443, "pd", lambda: pd), "concat"), _n_(631445, "df_from_each_file", lambda: df_from_each_file), ignore_index=True)
        _l_(631447)
        aux = _n_(631448, "concatenated_df", lambda: concatenated_df)
        _l_(631449)
        return aux


def to_date(x):
    _l_(631464)

    aux = _c_(631462, _a_(631453, _n_(631452, "datetime", lambda: datetime), "strftime"), _c_(631461, _a_(631460, _c_(631459, _a_(631455, _n_(631454, "datetime", lambda: datetime), "fromtimestamp"), _c_(631458, _n_(631456, "int", lambda: int), _n_(631457, "x", lambda: x))/1000), "strftime"), "%d-%b-%Y"), "%d-%b-%Y")
    _l_(631463)
    return aux




df = _c_(631467, _n_(631465, "get_merged_data_frame", lambda: get_merged_data_frame), _n_(631466, "listFileNames", lambda: listFileNames))
_l_(631468)
_c_(631471, _n_(631469, "print", lambda: print), _n_(631470, "df", lambda: df))
_l_(631472)
_n_(631473, "df", lambda: df)['start_data'] = _c_(631477, _a_(631475, _n_(631474, "df", lambda: df)['start_time'], "apply"), _n_(631476, "to_date", lambda: to_date))
_l_(631478)
_c_(631483, _n_(631479, "print", lambda: print), _c_(631482, _n_(631480, "to_date", lambda: to_date), _n_(631481, "df", lambda: df)['start_time']))
_l_(631484)
_c_(631489, _n_(631485, "print", lambda: print), _c_(631488, _n_(631486, "type", lambda: type), _n_(631487, "df", lambda: df)))
_l_(631490)
_c_(631493, _n_(631491, "print", lambda: print), _n_(631492, "df", lambda: df))
_l_(631494)
data = _c_(631497, _a_(631496, _n_(631495, "df", lambda: df), "to_dict"), orient='records')
_l_(631498)
_c_(631501, _n_(631499, "print", lambda: print), _n_(631500, "data", lambda: data))
_l_(631502)
_c_(631506, _a_(631504, _n_(631503, "col", lambda: col), "insert_many"), _n_(631505, "data", lambda: data))
_l_(631507)