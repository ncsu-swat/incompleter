# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45965493/labelencoder-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
onehot = _c_(557617, _a_(557616, _n_(557615, "pd", lambda: pd), "DataFrame"))
_l_(557618)
encoders = []
_l_(557619)
for column in _a_(557621, _n_(557620, "df_resolved", lambda: df_resolved), "loc")[:, ((_a_(557623, _n_(557622, "df_resolved", lambda: df_resolved), "dtypes") != _a_(557625, _n_(557624, "np", lambda: np), "int64"))&(_a_(557627, _n_(557626, "df_resolved", lambda: df_resolved), "dtypes") != _a_(557629, _n_(557628, "np", lambda: np), "int32")))]:
    _l_(557647)

    enc = _c_(557632, _a_(557631, _n_(557630, "preprocessing", lambda: preprocessing), "LabelEncoder"))
    _l_(557633)
    _c_(557637, _a_(557635, _n_(557634, "encoders", lambda: encoders), "append"), _n_(557636, "enc", lambda: enc))
    _l_(557638)
    _n_(557639, "onehot", lambda: onehot)[_n_(557640, "column", lambda: column)] = _c_(557645, _a_(557642, _n_(557641, "enc", lambda: enc), "fit_transform"), _n_(557643, "df_resolved", lambda: df_resolved)[_n_(557644, "column", lambda: column)])
    _l_(557646)