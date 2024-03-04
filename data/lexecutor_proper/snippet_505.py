# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14770735/how-do-i-change-the-figure-size-with-subplots
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(63328, _a_(63327, _n_(63326, "plt", lambda: plt), "figure"), figsize=(16, 8)) 
_l_(63329) 
for i in _c_(63331, _n_(63330, "range", lambda: range), 1, 7):
    _l_(63352)

    _c_(63335, _a_(63333, _n_(63332, "plt", lambda: plt), "subplot"), 2, 3, _n_(63334, "i", lambda: i))
    _l_(63336)
    _c_(63344, _a_(63338, _n_(63337, "plt", lambda: plt), "title"), _c_(63343, _a_(63339, 'Histogram of {}', "format"), _c_(63342, _n_(63340, "str", lambda: str), _n_(63341, "i", lambda: i))))
    _l_(63345)
    _c_(63350, _a_(63347, _n_(63346, "plt", lambda: plt), "hist"), _n_(63348, "x", lambda: x)[:,_n_(63349, "i", lambda: i)-1], bins=60)
    _l_(63351)

