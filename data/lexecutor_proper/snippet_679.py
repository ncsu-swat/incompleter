# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/31594549/how-to-change-the-figure-size-of-a-seaborn-axes-or-figure-level-plot
# Sets the figure size temporarily but has to be set again the next plot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(64198, _a_(64197, _n_(64196, "plt", lambda: plt), "figure"), figsize=(18,18))
_l_(64199)

_c_(64206, _a_(64201, _n_(64200, "sns", lambda: sns), "barplot"), x=_a_(64203, _n_(64202, "housing", lambda: housing), "ocean_proximity"), y=_a_(64205, _n_(64204, "housing", lambda: housing), "median_house_value"))
_l_(64207)
_c_(64210, _a_(64209, _n_(64208, "plt", lambda: plt), "show"))
_l_(64211)

