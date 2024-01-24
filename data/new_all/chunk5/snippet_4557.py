# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55577628/attributeerror-module-gensim-models-word2vec-has-no-attribute-load
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(669176)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(669178)

except ImportError:
    pass
try:
    import gensim
    _l_(669180)

except ImportError:
    pass
try:
    from matplotlib import pyplot as plt
    _l_(669182)

except ImportError:
    pass
try:
    from gensim.models import word2vec
    _l_(669184)

except ImportError:
    pass
try:
    from collections import defaultdict
    _l_(669186)

except ImportError:
    pass
try:
    from sklearn.cluster import KMeans
    _l_(669188)

except ImportError:
    pass

model = _c_(669191, _a_(669190, _n_(669189, "word2vec", lambda: word2vec), "Text8Corpus"), r'C:\Users\qlm\Desktop\globalwarming.txt')
_l_(669192)
model = _c_(669195, _a_(669194, _n_(669193, "word2vec", lambda: word2vec), "load"), r'C:\Users\qlm\Desktop\globalwarming.txt')
_l_(669196)