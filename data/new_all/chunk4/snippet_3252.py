# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76129300/typeerror-unhashable-type-csr-matrix-encoding-categorical-data-to-make-a-m
#importing the dataset 
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dataset = _c_(604147, _a_(604146, _n_(604145, "pd", lambda: pd), "read_csv"), '50_Startups.csv')
_l_(604148)
X = _a_(604151, _a_(604150, _n_(604149, "dataset", lambda: dataset), "iloc")[:,:-1], "values")
_l_(604152)
y = _a_(604155, _a_(604154, _n_(604153, "dataset", lambda: dataset), "iloc")[:, -1], "values")
_l_(604156)
try:
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    _l_(604158)

except ImportError:
    pass
enc = _c_(604160, _n_(604159, "OneHotEncoder", lambda: OneHotEncoder))
_l_(604161)
_n_(604162, "X", lambda: X)[:, :-1] = _c_(604166, _a_(604164, _n_(604163, "enc", lambda: enc), "fit_transform"), _n_(604165, "X", lambda: X)[:, :-1])
_l_(604167)

X = _c_(604173, _a_(604172, _c_(604171, _a_(604169, _n_(604168, "enc", lambda: enc), "fit_transform"), _n_(604170, "X", lambda: X)), "toarray")) 
_l_(604174) 
# Avoiding the Dummy Variable Trap
X = _n_(604175, "X", lambda: X)[:, 1:]
_l_(604176)