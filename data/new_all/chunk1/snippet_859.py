# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60087408/python-pandas-and-nltk-type-error-int-object-is-not-callable-when-calling-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(414604)

except ImportError:
    pass
try:
    import numpy as np
    _l_(414606)

except ImportError:
    pass
try:
    import nltk
    _l_(414608)

except ImportError:
    pass
try:
    import string
    _l_(414610)

except ImportError:
    pass
try:
    import collections
    _l_(414612)

except ImportError:
    pass
try:
    from collections import Counter
    _l_(414614)

except ImportError:
    pass
_c_(414617, _a_(414616, _n_(414615, "nltk", lambda: nltk), "download"), 'stopwords')
_l_(414618)
sw= _c_(414625, _n_(414619, "set", lambda: set), _c_(414624, _a_(414623, _a_(414622, _a_(414621, _n_(414620, "nltk", lambda: nltk), "corpus"), "stopwords"), "words"), 'english'))
_l_(414626)
punctuation = _c_(414630, _n_(414627, "set", lambda: set), _a_(414629, _n_(414628, "string", lambda: string), "punctuation"))
_l_(414631)
data= _c_(414634, _a_(414633, _n_(414632, "pd", lambda: pd), "read_csv"), '~/Desktop/tweets.csv.zip', compression='zip')
_l_(414635)

_c_(414639, _n_(414636, "print", lambda: print), _a_(414638, _n_(414637, "data", lambda: data), "columns"))
_l_(414640)
_c_(414644, _n_(414641, "print", lambda: print), _a_(414643, _n_(414642, "data", lambda: data), "text"))
_l_(414645)
_n_(414646, "data", lambda: data)['text'] = [_c_(414649, _a_(414648, _n_(414647, "str", lambda: str), "lower")) for str in _a_(414651, _n_(414650, "data", lambda: data), "text") if _c_(414654, _a_(414653, _n_(414652, "str", lambda: str), "lower")) not in _n_(414655, "sw", lambda: sw) and _c_(414658, _a_(414657, _n_(414656, "str", lambda: str), "lower")) not in _n_(414659, "punctuation", lambda: punctuation)] 
_l_(414660) 
_c_(414664, _n_(414661, "print", lambda: print), _a_(414663, _n_(414662, "data", lambda: data), "text"))
_l_(414665)
_n_(414666, "data", lambda: data)["text"] = _c_(414670, _a_(414669, _a_(414668, _n_(414667, "data", lambda: data)["text"], "str"), "split"))
_l_(414671)
_n_(414672, "data", lambda: data)['text'] = _c_(414679, _a_(414674, _n_(414673, "data", lambda: data)['text'], "apply"), lambda x: [_n_(414675, "item", lambda: item) for item in _n_(414676, "x", lambda: x) if _n_(414677, "item", lambda: item) not in _n_(414678, "sw", lambda: sw)])
_l_(414680)
_c_(414684, _n_(414681, "print", lambda: print), _a_(414683, _n_(414682, "data", lambda: data), "text"))
_l_(414685)
_n_(414686, "data", lambda: data)['text'] = _c_(414691, _a_(414689, _a_(414688, _n_(414687, "data", lambda: data), "text"), "astype"), _n_(414690, "str", lambda: str))
_l_(414692)
_c_(414698, _n_(414693, "print", lambda: print), _c_(414697, _n_(414694, "type", lambda: type), _a_(414696, _n_(414695, "data", lambda: data), "text")))
_l_(414699)
tweets=_a_(414701, _n_(414700, "data", lambda: data), "text")
_l_(414702)

_n_(414703, "data", lambda: data)['words']= _c_(414710, _a_(414705, _n_(414704, "tweets", lambda: tweets), "apply"), _c_(414709, _a_(414707, _n_(414706, "nltk", lambda: nltk), "FreqDist"), _n_(414708, "tweets", lambda: tweets)))
_l_(414711)
_c_(414715, _n_(414712, "print", lambda: print), _a_(414714, _n_(414713, "data", lambda: data), "words"))
_l_(414716)