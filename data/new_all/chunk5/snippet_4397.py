# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58505289/stackplot-typeerror-ufunc-isfinite-not-supported-for-the-input-types
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
diet_projection = _c_(697711, _a_(697709, _n_(697708, "perc_contributions_WRAP", lambda: perc_contributions_WRAP), "percentage_contributions"), _n_(697710, "diet_props", lambda: diet_props), 2050, 1961, 2013)
_l_(697712)

_c_(697717, _n_(697713, "print", lambda: print), _a_(697716, _a_(697715, _n_(697714, "diet_projection", lambda: diet_projection), "iloc")[:], "values"))
_l_(697718)
_c_(697723, _n_(697719, "print", lambda: print), _c_(697722, _a_(697721, _n_(697720, "np", lambda: np), "arange"), 2013, 2051, 1))
_l_(697724)

_c_(697733, _a_(697726, _n_(697725, "plt", lambda: plt), "stackplot"), _c_(697729, _a_(697728, _n_(697727, "np", lambda: np), "arange"), 2013, 2051, 1), _a_(697732, _a_(697731, _n_(697730, "diet_projection", lambda: diet_projection), "iloc")[:], "values"))
_l_(697734)
# plt.legend(loc = "upper left")
# plt.ylabel("Diet makeup - kcal/capita/day")
# plt.xlabel("Year")
# plt.xticks(np.arange(2010, 2050, 5))
_c_(697737, _a_(697736, _n_(697735, "plt", lambda: plt), "show"))
_l_(697738)