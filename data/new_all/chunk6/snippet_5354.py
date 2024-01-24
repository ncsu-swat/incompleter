# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62106106/typeerror-expected-string-or-bytes-like-object-tqdm
# Combining all the above statemennts 
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tqdm import tqdm
    _l_(358083)

except ImportError:
    pass
Other_skill = []
_l_(358084)
# tqdm is for printing the status bar
for sentance in _c_(358088, _n_(358085, "tqdm", lambda: tqdm), _a_(358087, _n_(358086, "project_data", lambda: project_data)['Other skills'], "values")):
    _l_(358128)

    sent = _c_(358091, _n_(358089, "decontracted", lambda: decontracted), _n_(358090, "sentance", lambda: sentance))
    _l_(358092)
    sent = _c_(358095, _a_(358094, _n_(358093, "sent", lambda: sent), "replace"), '\\r', ' ')
    _l_(358096)
    sent = _c_(358099, _a_(358098, _n_(358097, "sent", lambda: sent), "replace"), '\\"', ' ')
    _l_(358100)
    sent = _c_(358103, _a_(358102, _n_(358101, "sent", lambda: sent), "replace"), '\\n', ' ')
    _l_(358104)
    sent = _c_(358108, _a_(358106, _n_(358105, "re", lambda: re), "sub"), '[^A-Za-z0-9]+', ' ', _n_(358107, "sent", lambda: sent))
    _l_(358109)
    sent = _c_(358117, _a_(358110, ' ', "join"), (_n_(358111, "e", lambda: e) for e in _c_(358114, _a_(358113, _n_(358112, "sent", lambda: sent), "split")) if _n_(358115, "e", lambda: e) not in _n_(358116, "stopwords", lambda: stopwords)))
    _l_(358118)
    _c_(358126, _a_(358120, _n_(358119, "Other_skill", lambda: Other_skill), "append"), _c_(358125, _a_(358124, _c_(358123, _a_(358122, _n_(358121, "sent", lambda: sent), "lower")), "strip")))
    _l_(358127)