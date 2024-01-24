# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62364735/how-to-fix-typeerror-data-type-not-understood-with-a-datetime-object-in-pandas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
user_groups = _c_(702727, _a_(702726, _n_(702725, "df1", lambda: df1), "groupby"), "customer_id")["month"]
_l_(702728)

_n_(702729, "df1", lambda: df1)["Cohort_month"] = _c_(702732, _a_(702731, _n_(702730, "user_groups", lambda: user_groups), "transform"), "min")
_l_(702733)