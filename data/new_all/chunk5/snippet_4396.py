# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58505289/stackplot-typeerror-ufunc-isfinite-not-supported-for-the-input-types
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
diet_projection = _c_(705727, _a_(705725, _n_(705724, "perc_contributions_WRAP", lambda: perc_contributions_WRAP), "percentage_contributions"), _n_(705726, "diet_props", lambda: diet_props), 2050, 1961, 2013)
_l_(705728)

_c_(705733, _n_(705729, "print", lambda: print), _a_(705732, _a_(705731, _n_(705730, "diet_projection", lambda: diet_projection), "iloc")[:], "values"))
_l_(705734)
_c_(705739, _n_(705735, "print", lambda: print), _c_(705738, _a_(705737, _n_(705736, "np", lambda: np), "arange"), 2013, 2051, 1))
_l_(705740)

_c_(705749, _a_(705742, _n_(705741, "plt", lambda: plt), "stackplot"), _c_(705745, _a_(705744, _n_(705743, "np", lambda: np), "arange"), 2013, 2051, 1), _a_(705748, _a_(705747, _n_(705746, "diet_projection", lambda: diet_projection), "iloc")[:], "values"))
_l_(705750)
# plt.legend(loc = "upper left")
# plt.ylabel("Diet makeup - kcal/capita/day")
# plt.xlabel("Year")
# plt.xticks(np.arange(2010, 2050, 5))
_c_(705753, _a_(705752, _n_(705751, "plt", lambda: plt), "show"))
_l_(705754)