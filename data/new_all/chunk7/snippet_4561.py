# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55577628/attributeerror-module-gensim-models-word2vec-has-no-attribute-load
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(693456)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(693458)

except ImportError:
    pass
try:
    import gensim
    _l_(693460)

except ImportError:
    pass
try:
    from matplotlib import pyplot as plt
    _l_(693462)

except ImportError:
    pass
try:
    from gensim.models import word2vec
    _l_(693464)

except ImportError:
    pass
try:
    from collections import defaultdict
    _l_(693466)

except ImportError:
    pass
try:
    from sklearn.cluster import KMeans
    _l_(693468)

except ImportError:
    pass

model = _c_(693471, _a_(693470, _n_(693469, "word2vec", lambda: word2vec), "Text8Corpus"), r'C:\Users\qlm\Desktop\globalwarming.txt')
_l_(693472)
model = _c_(693475, _a_(693474, _n_(693473, "word2vec", lambda: word2vec), "load"), r'C:\Users\qlm\Desktop\globalwarming.txt')
_l_(693476)