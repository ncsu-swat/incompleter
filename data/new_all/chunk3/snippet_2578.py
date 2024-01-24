# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70946230/need-to-filter-some-strings-elements-but-i-get-typeerror-unsupported-operand-ty
# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
bdegree = _c_(533866, _a_(533865, _n_(533862, "df", lambda: df)[(_n_(533863, "df", lambda: df)["education"] == "Bachelors") & (_n_(533864, "df", lambda: df)["salary"] >= "50K")], "count"))
_l_(533867)
mdegree = _c_(533872, _a_(533871, _n_(533868, "df", lambda: df)[(_n_(533869, "df", lambda: df)["education"] == "Masters") & (_n_(533870, "df", lambda: df)["salary"] >= "50K")], "count"))
_l_(533873)
phddegree = _c_(533878, _a_(533877, _n_(533874, "df", lambda: df)[(_n_(533875, "df", lambda: df)["education"] == "Doctorate") & (_n_(533876, "df", lambda: df)["salary"] >= "50K")], "count"))
_l_(533879)
all_degrees = _n_(533880, "bdegree", lambda: bdegree) + _n_(533881, "mdegree", lambda: mdegree) + _n_(533882, "phddegree", lambda: phddegree)
_l_(533883)
_c_(533886, _n_(533884, "print", lambda: print), _n_(533885, "all_degrees", lambda: all_degrees))
_l_(533887)
percentaje_of_more50 = (_n_(533888, "all_degrees", lambda: all_degrees) / _c_(533891, _a_(533890, _n_(533889, "df", lambda: df)["education" == "Bachelors"|"Masters"|"Doctorate"], "count")))*100
_l_(533892)
_c_(533897, _n_(533893, "print", lambda: print), "The percentaje of people with bla bla bla is", _c_(533896, _a_(533895, _n_(533894, "percentaje_of_more50", lambda: percentaje_of_more50)["education"], "round"), 1))
_l_(533898)