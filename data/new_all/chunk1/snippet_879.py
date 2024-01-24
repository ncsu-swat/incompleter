# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57291797/dask-attributeerror-dataframe-object-has-no-attribute-getitem-array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
train_churn = _n_(409108, "train", lambda: train)[_n_(409109, "train", lambda: train)['CON_CHURN_DECLARATION'] == 1]
_l_(409110)
_c_(409113, _a_(409112, _n_(409111, "train_churn", lambda: train_churn), "compute"))
_l_(409114)