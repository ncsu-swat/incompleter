# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55765498/attributeerror-can-only-use-dt-accessor-with-datetimelike-values-in-0yrs-0mon
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(367158, "train", lambda: train)['AVERAGE_ACCT_AGE']=_c_(367162, _a_(367160, _n_(367159, "pd", lambda: pd), "to_datetime"), _n_(367161, "train", lambda: train)['AVERAGE.ACCT.AGE'], format='%Y%m',errors='ignore',infer_datetime_format=True)
_l_(367163)