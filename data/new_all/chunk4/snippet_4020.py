# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63678164/pandas-reset-index-gives-typeerror-cannot-compare-types-ndarraydtype-float64
# get all csv files, append to list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
file_list = _c_(587977, _n_(587976, "list", lambda: list))
_l_(587978)
for file in _n_(587979, "table_files", lambda: table_files):
    _l_(587991)

    df_file = _c_(587984, _a_(587981, _n_(587980, "pd", lambda: pd), "read_csv"), _n_(587982, "pdf_data_path", lambda: pdf_data_path) + _n_(587983, "file", lambda: file), header=None)
    _l_(587985)
    _c_(587989, _a_(587987, _n_(587986, "file_list", lambda: file_list), "append"), _n_(587988, "df_file", lambda: df_file))
    _l_(587990)

# create new df from file list
df_raw = _c_(587995, _a_(587993, _n_(587992, "pd", lambda: pd), "concat"), _n_(587994, "file_list", lambda: file_list), axis=0, ignore_index=True)
_l_(587996)

# remove trailing spaces entire df 
df_all = _c_(588007, _a_(587998, _n_(587997, "df_raw", lambda: df_raw), "applymap"), lambda x: _c_(588001, _a_(588000, _n_(587999, "x", lambda: x), "rstrip")) if _c_(588004, _n_(588002, "type", lambda: type), _n_(588003, "x", lambda: x))==_n_(588005, "str", lambda: str) else _n_(588006, "x", lambda: x))
_l_(588008)

# exclude top 2 rows
df_all = _a_(588010, _n_(588009, "df_all", lambda: df_all), "iloc")[2:]
_l_(588011)

# drop empty rows
_c_(588014, _a_(588013, _n_(588012, "df_all", lambda: df_all), "dropna"), how='all', inplace = True) 
_l_(588015) 