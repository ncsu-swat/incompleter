# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59044361/typeerror-an-integer-is-required-got-type-datetime-datetime-when-trying-to-co
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
     import datetime
     _l_(411285)

except ImportError:
     pass

dic = {'Select start date': _c_(411288, _a_(411287, _n_(411286, "datetime", lambda: datetime), "datetime"), 2019, 11, 7, 0, 0)}
_l_(411289)

for key, value in _c_(411292, _a_(411291, _n_(411290, "dic", lambda: dic), "items")):
     _l_(411302)

     d = _c_(411296, _a_(411294, _n_(411293, "datetime", lambda: datetime), "datetime"), _n_(411295, "value", lambda: value))
     _l_(411297)
     _c_(411300, _a_(411299, _n_(411298, "d", lambda: d), "strftime"), "%d %b %Y")   
     _l_(411301)   