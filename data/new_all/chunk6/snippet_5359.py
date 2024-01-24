# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61591232/typeerror-unorderable-types-str-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(344981)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(344983)

except ImportError:
    pass
try:
    import re
    _l_(344985)

except ImportError:
    pass
try:
    import nltk
    _l_(344987)

except ImportError:
    pass
_c_(344990, _a_(344989, _n_(344988, "nltk", lambda: nltk), "download"), 'stopwords')  
_l_(344991)  
try:
    from nltk.corpus import stopwords
    _l_(344993)

except ImportError:
    pass
tweets = _c_(344996, _a_(344995, _n_(344994, "pd", lambda: pd), "read_csv"), "C:\\Users\\data.csv")
_l_(344997)
_a_(344999, _n_(344998, "tweets", lambda: tweets), "shape")
_l_(345000)