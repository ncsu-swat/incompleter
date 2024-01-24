# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75439120/drop-duplicates-groupby-typeerror-sequence-item-0-expected-str-instance
### Concat LI related columns
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
list_LI_concat_cols = ['LI_date_engr_sign', 'Subst_SSO', 'Subst_name', 'Subst_mang_SSO',
    'Subst_mang_name', 'Signoff_name']
_l_(618784)

### Convert to string
_a_(618786, _n_(618785, "df1", lambda: df1), "loc")[:, ['Subst_SSO','Subst_mang_SSO']] \
    = _c_(618796, _a_(618794, _c_(618793, _a_(618791, _c_(618790, _a_(618789, _a_(618788, _n_(618787, "df1", lambda: df1), "loc")[:, ['Subst_SSO','Subst_mang_SSO']], "fillna"), '0'), "astype"), _n_(618792, "int", lambda: int)), "astype"), _n_(618795, "str", lambda: str))
_l_(618797)

### Aggr data per MRB_LI
for col in _n_(618798, "list_LI_concat_cols", lambda: list_LI_concat_cols):
    _l_(618819)

    df_subst_concat = _c_(618812, _a_(618811, _c_(618810, _a_(618806, _c_(618804, _a_(618803, _c_(618802, _a_(618800, _n_(618799, "df1", lambda: df1), "drop_duplicates"), subset=['MRB_LI#', _n_(618801, "col", lambda: col)], keep='last'), "groupby"), 'MRB_LI#')[_n_(618805, "col", lambda: col)], "agg"), lambda x: _c_(618809, _a_(618807, ' | ', "join"), _n_(618808, "x", lambda: x))), "reset_index"))
    _l_(618813)
    df_LI = _c_(618817, _a_(618815, _n_(618814, "df_LI", lambda: df_LI), "merge"), _n_(618816, "df_subst_concat", lambda: df_subst_concat), how='left', on='MRB_LI#')
    _l_(618818)