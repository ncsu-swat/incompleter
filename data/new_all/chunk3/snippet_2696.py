# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66302949/pandas-to-sql-typeerror-unsupported-operand-type
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df = _c_(546801, _a_(546796, _n_(546795, "pd", lambda: pd), "read_csv"), "test_repositories.csv", 
        header=0, 
        sep=',',
        quotechar='"',
        dtype={'column_one': _n_(546797, "str", lambda: str),
            'column_two': _n_(546798, "str", lambda: str),
            'column_three': _n_(546799, "str", lambda: str),
            'column_four': _n_(546800, "int", lambda: int)},
            error_bad_lines=False)
_l_(546802)
df = _c_(546809, _a_(546804, _n_(546803, "df", lambda: df), "where"), _c_(546808, _a_(546806, _n_(546805, "pd", lambda: pd), "notnull"), _n_(546807, "df", lambda: df)), None)
_l_(546810)
_c_(546819, _a_(546812, _n_(546811, "df", lambda: df), "to_sql"), _a_(546814, _n_(546813, "self", lambda: self), "staging_table"), _a_(546816, _n_(546815, "db", lambda: db), "engine"), _a_(546818, _n_(546817, "self", lambda: self), "chunksize"), method='multi')
_l_(546820)