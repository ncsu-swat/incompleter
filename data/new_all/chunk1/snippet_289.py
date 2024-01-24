# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54629368/pandas-attributeerror-dataframe-object-has-no-attribute-dt-when-using-apply
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df_code_grp_by = _c_(390502, _a_(390501, _n_(390500, "df", lambda: df), "groupby"), ['code'])
_l_(390503)

_c_(390516, _a_(390515, _c_(390514, _a_(390513, _a_(390512, _a_(390511, _c_(390510, _a_(390505, _n_(390504, "df_code_grp_by", lambda: df_code_grp_by), "apply"), lambda x: _a_(390507, _n_(390506, "x", lambda: x), "date2") - _a_(390509, _n_(390508, "x", lambda: x), "date1")), "dt"), "days"), "sum"), level=0), "reset_index"), name='date_diff_sum')
_l_(390517)