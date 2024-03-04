# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/180986/what-is-the-difference-between-re-search-and-re-match
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(62952, _a_(62951, _n_(62950, "re", lambda: re), "search"), 'test', ' test')      # returns a Truthy match object (because the search starts from any index) 
_l_(62953)      # returns a Truthy match object (because the search starts from any index) 

_c_(62956, _a_(62955, _n_(62954, "re", lambda: re), "match"), 'test', ' test')       # returns None (because the search start from 0 index)
_l_(62957)       # returns None (because the search start from 0 index)
_c_(62960, _a_(62959, _n_(62958, "re", lambda: re), "match"), 'test', 'test')        # returns a Truthy match object (match at 0 index)
_l_(62961)        # returns a Truthy match object (match at 0 index)

