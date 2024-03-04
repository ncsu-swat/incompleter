# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/47152691/how-can-i-pivot-a-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(63378, _a_(63376, _c_(63375, _a_(63373, _c_(63371, _a_(63368, _n_(63367, "df", lambda: df), "groupby"), _n_(63369, "rows", lambda: rows)+_n_(63370, "cols", lambda: cols))[_n_(63372, "vals", lambda: vals)], "agg"), _n_(63374, "aggfuncs", lambda: aggfuncs)), "unstack"), _n_(63377, "cols", lambda: cols))
_l_(63379)
# equivalently,
_c_(63386, _a_(63381, _n_(63380, "df", lambda: df), "pivot_table"), _n_(63382, "vals", lambda: vals), _n_(63383, "rows", lambda: rows), _n_(63384, "cols", lambda: cols), _n_(63385, "aggfuncs", lambda: aggfuncs))
_l_(63387)

_c_(63396, _a_(63394, _c_(63392, _a_(63389, _n_(63388, "df", lambda: df), "set_index"), _n_(63390, "rows", lambda: rows)+_n_(63391, "cols", lambda: cols))[_n_(63393, "vals", lambda: vals)], "unstack"), _n_(63395, "cols", lambda: cols))
_l_(63397)
# equivalently, 
_c_(63403, _a_(63399, _n_(63398, "df", lambda: df), "pivot"), _n_(63400, "rows", lambda: rows), _n_(63401, "cols", lambda: cols), _n_(63402, "vals", lambda: vals))
_l_(63404)

df = _c_(63407, _a_(63406, _n_(63405, "pd", lambda: pd), "DataFrame"), {'A': [1, 1, 1, 2, 2, 2], 'B': [*'xxyyzz'], 
                   'C': [*'CCDCDD'], 'E': [100, 200, 300, 400, 500, 600]})
_l_(63408)
rows, cols, vals = ['A', 'B'], ['C'], 'E'
_l_(63409)

# using pivot syntax
df1 = _c_(63432, _a_(63431, _c_(63430, _a_(63429, _c_(63428, _a_(63427, _c_(63426, _a_(63425, _c_(63424, _a_(63420, _c_(63419, _a_(63411, _n_(63410, "df", lambda: df), "assign"), ix=_c_(63418, _a_(63417, _c_(63416, _a_(63413, _n_(63412, "df", lambda: df), "groupby"), _n_(63414, "rows", lambda: rows)+_n_(63415, "cols", lambda: cols)), "cumcount"))), "pivot"), [*_n_(63421, "rows", lambda: rows), 'ix'], _n_(63422, "cols", lambda: cols), _n_(63423, "vals", lambda: vals)), "fillna"), 0, downcast='infer'), "droplevel"), -1), "reset_index")), "rename_axis"), columns=None)
_l_(63433)

# equivalently, using set_index + unstack syntax
df1 = _c_(63454, _a_(63453, _c_(63452, _a_(63451, _c_(63450, _a_(63449, _c_(63448, _a_(63447, _c_(63445, _a_(63435, _n_(63434, "df", lambda: df), "set_index"), [*_n_(63436, "rows", lambda: rows), _c_(63443, _a_(63442, _c_(63441, _a_(63438, _n_(63437, "df", lambda: df), "groupby"), _n_(63439, "rows", lambda: rows)+_n_(63440, "cols", lambda: cols)), "cumcount")), *_n_(63444, "cols", lambda: cols)])[_n_(63446, "vals", lambda: vals)], "unstack"), fill_value=0), "droplevel"), -1), "reset_index")), "rename_axis"), columns=None)
_l_(63455)

df1 = _c_(63472, _a_(63471, _c_(63469, _a_(63466, _c_(63465, _a_(63457, _n_(63456, "df", lambda: df), "assign"), ix=_c_(63464, _a_(63463, _c_(63462, _a_(63459, _n_(63458, "df", lambda: df), "groupby"), _n_(63460, "rows", lambda: rows)+_n_(63461, "cols", lambda: cols)), "cumcount"))), "pivot"), _n_(63467, "rows", lambda: rows), [*_n_(63468, "cols", lambda: cols), 'ix'])[_n_(63470, "vals", lambda: vals)], "fillna"), 0, downcast='infer')
_l_(63473)
df1 = _c_(63481, _a_(63480, _c_(63479, _a_(63475, _n_(63474, "df1", lambda: df1), "set_axis"), [f"{_n_(63476, 'c', lambda: c)[0]}_{_n_(63477, 'c', lambda: c)[1]}" for c in _n_(63478, "df1", lambda: df1)], axis=1), "reset_index"))
_l_(63482)

# equivalently, using the set_index + unstack syntax
df1 = _c_(63502, _a_(63496, _c_(63494, _a_(63484, _n_(63483, "df", lambda: df), "set_index"), [*_n_(63485, "rows", lambda: rows), _c_(63492, _a_(63491, _c_(63490, _a_(63487, _n_(63486, "df", lambda: df), "groupby"), _n_(63488, "rows", lambda: rows)+_n_(63489, "cols", lambda: cols)), "cumcount")), *_n_(63493, "cols", lambda: cols)])[_n_(63495, "vals", lambda: vals)], "unstack"), [-1, *_c_(63501, _n_(63497, "range", lambda: range), -2, -_c_(63500, _n_(63498, "len", lambda: len), _n_(63499, "cols", lambda: cols))-2, -1)], fill_value=0)
_l_(63503)
df1 = _c_(63511, _a_(63510, _c_(63509, _a_(63505, _n_(63504, "df1", lambda: df1), "set_axis"), [f"{_n_(63506, 'c', lambda: c)[0]}_{_n_(63507, 'c', lambda: c)[1]}" for c in _n_(63508, "df1", lambda: df1)], axis=1), "reset_index"))
_l_(63512)

df1 = _c_(63526, _a_(63525, _c_(63524, _a_(63523, _c_(63522, _a_(63521, _c_(63520, _a_(63514, _n_(63513, "df", lambda: df), "set_index"), ['A', _c_(63519, _a_(63518, _c_(63517, _a_(63516, _n_(63515, "df", lambda: df), "groupby"), 'A'), "cumcount"))])['E'], "unstack"), fill_value=0), "add_prefix"), 'Col'), "reset_index"))
_l_(63527)

pv_1 = _c_(63534, _a_(63529, _n_(63528, "df", lambda: df), "pivot_table"), index=_n_(63530, "rows", lambda: rows), columns=_n_(63531, "cols", lambda: cols), values=_n_(63532, "vals", lambda: vals), aggfunc=_n_(63533, "aggfuncs", lambda: aggfuncs), fill_value=0)
_l_(63535)
# internal operation of `pivot_table()`
gb_1 = _c_(63549, _a_(63548, _c_(63547, _a_(63545, _c_(63544, _a_(63542, _c_(63540, _a_(63537, _n_(63536, "df", lambda: df), "groupby"), _n_(63538, "rows", lambda: rows)+_n_(63539, "cols", lambda: cols))[_n_(63541, "vals", lambda: vals)], "agg"), _n_(63543, "aggfuncs", lambda: aggfuncs)), "unstack"), _n_(63546, "cols", lambda: cols)), "fillna"), 0, downcast="infer")
_l_(63550)
_c_(63554, _a_(63552, _n_(63551, "pv_1", lambda: pv_1), "equals"), _n_(63553, "gb_1", lambda: gb_1)) # True
_l_(63555) # True

