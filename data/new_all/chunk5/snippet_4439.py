# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57742659/im-getting-an-error-while-adding-a-new-column-with-set-up-bins-typeerror
# set up bins
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
bins = [0, 585, 615, 645, 675]
_l_(655339)
group_name = ['0 - 584', '585 - 614', '615 - 644', '645 +']
_l_(655340)

# add a new column: spending range
_n_(655341, "score_by_school_spending", lambda: score_by_school_spending)["Spending Range"] = _c_(655347, _a_(655343, _n_(655342, "pd", lambda: pd), "cut"), _n_(655344, "score_by_school_spending", lambda: score_by_school_spending)["Per Student Budget"],_n_(655345, "bins", lambda: bins),labels=_n_(655346, "group_name", lambda: group_name))
_l_(655348)
_n_(655349, "score_by_school_spending", lambda: score_by_school_spending)
_l_(655350)