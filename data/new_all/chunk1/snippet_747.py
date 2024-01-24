# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61996710/labelencoder-typeerror-argument-must-be-a-string-or-number
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(390751)

except ImportError:
    pass
try:
    from sklearn.preprocessing import LabelEncoder
    _l_(390753)

except ImportError:
    pass
_c_(390756, _a_(390755, _n_(390754, "pd", lambda: pd), "set_option"), 'display.max_columns', 500)
_l_(390757)
df=_c_(390760, _a_(390759, _n_(390758, "pd", lambda: pd), "read_csv"), "https://media-doselect.s3.amazonaws.com/generic/831JKKEkW7kqd5M4evNva9LyB/insurance_grouped.csv")
_l_(390761)
le = _c_(390763, _n_(390762, "LabelEncoder", lambda: LabelEncoder))#use this encoder to encod
_l_(390764)#use this encoder to encod
_n_(390765, "df", lambda: df).BMI_group = _c_(390771, _a_(390767, _n_(390766, "le", lambda: le), "fit_transform"), _a_(390770, _a_(390769, _n_(390768, "df", lambda: df), "BMI_group"), "values"))
_l_(390772)
_c_(390777, _n_(390773, "print", lambda: print), _c_(390776, _a_(390775, _n_(390774, "df", lambda: df), "head")))
_l_(390778)