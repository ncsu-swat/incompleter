# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53145882/typeerror-kmeans-got-an-unexpected-keyword-argument-n-clusters
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(534255)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(534257)

except ImportError:
    pass
try:
    from sklearn.datasets import make_blobs
    _l_(534259)

except ImportError:
    pass
try:
    from sklearn.cluster import KMeans
    _l_(534261)

except ImportError:
    pass


def KMeans():
    _l_(534387)

    n = 4
    _l_(534262)
    data = _c_(534264, _n_(534263, "open", lambda: open), "testSet.txt", "r")
    _l_(534265)
    nums = []
    _l_(534266)
    arr = _c_(534270, _a_(534268, _n_(534267, "np", lambda: np), "empty"), (0,2), _n_(534269, "float", lambda: float))
    _l_(534271)

    #Gets dataset from file
    for x in _c_(534276, _a_(534275, _c_(534274, _a_(534273, _n_(534272, "data", lambda: data), "read")), "split"), ' '):
        _l_(534284)

        _c_(534282, _a_(534278, _n_(534277, "nums", lambda: nums), "append"), _c_(534281, _n_(534279, "float", lambda: float), _n_(534280, "x", lambda: x)))
        _l_(534283)
    _c_(534287, _a_(534286, _n_(534285, "data", lambda: data), "close"))
    _l_(534288)
    _c_(534291, _n_(534289, "print", lambda: print), _n_(534290, "nums", lambda: nums))
    _l_(534292)

    #Stores numbers in a 2D array (X, Y axis)
    for x in _c_(534297, _n_(534293, "range", lambda: range), 0, _c_(534296, _n_(534294, "len", lambda: len), _n_(534295, "nums", lambda: nums)), 2):
        _l_(534310)

        arr = _c_(534308, _a_(534299, _n_(534298, "np", lambda: np), "append"), _n_(534300, "arr", lambda: arr), _c_(534307, _a_(534302, _n_(534301, "np", lambda: np), "array"), [[_n_(534303, "nums", lambda: nums)[_n_(534304, "x", lambda: x)],_n_(534305, "nums", lambda: nums)[_n_(534306, "x", lambda: x)+1]]]), axis=0)
        _l_(534309)

    _c_(534313, _n_(534311, "print", lambda: print), _n_(534312, "arr", lambda: arr))
    _l_(534314)

    kmeans = _c_(534319, _a_(534317, _c_(534316, _n_(534315, "KMeans", lambda: KMeans), n_clusters = 2), "fit"), _n_(534318, "arr", lambda: arr))
    _l_(534320)

    #Example 2, using make blobs to create random data
    X, y = _c_(534322, _n_(534321, "make_blobs", lambda: make_blobs), n_samples=13, centers=5)
    _l_(534323)
    _c_(534329, _n_(534324, "print", lambda: print), "Shape:", _a_(534326, _n_(534325, "X", lambda: X), "shape"), _a_(534328, _n_(534327, "y", lambda: y), "shape"))
    _l_(534330)


    #Plotting the data
    _c_(534333, _a_(534332, _n_(534331, "plt", lambda: plt), "figure"), 0)
    _l_(534334)
    _c_(534337, _a_(534336, _n_(534335, "plt", lambda: plt), "grid"), True)
    _l_(534338)
    _c_(534343, _a_(534340, _n_(534339, "plt", lambda: plt), "scatter"), _n_(534341, "X", lambda: X)[:, 0], _n_(534342, "X", lambda: X)[:, 1])
    _l_(534344)
    _c_(534347, _a_(534346, _n_(534345, "plt", lambda: plt), "show"))
    _l_(534348)


    clf = _c_(534350, _n_(534349, "KMeans", lambda: KMeans), n_clusters=5)
    _l_(534351)
    _c_(534355, _a_(534353, _n_(534352, "clf", lambda: clf), "fit"), _n_(534354, "X", lambda: X))
    _l_(534356)

    _c_(534360, _n_(534357, "print", lambda: print), _a_(534359, _n_(534358, "clf", lambda: clf), "labels_"))
    _l_(534361)

    z = _a_(534363, _n_(534362, "clf", lambda: clf), "cluster_centers_")
    _l_(534364)
    _c_(534367, _n_(534365, "print", lambda: print), _n_(534366, "z", lambda: z))
    _l_(534368)


    _c_(534375, _a_(534370, _n_(534369, "plt", lambda: plt), "scatter"), _n_(534371, "X", lambda: X)[:,0], _n_(534372, "X", lambda: X)[:,1], _a_(534374, _n_(534373, "clf", lambda: clf), "labels_"))
    _l_(534376)
    _c_(534381, _a_(534378, _n_(534377, "plt", lambda: plt), "scatter"), _n_(534379, "z", lambda: z)[:,0],_n_(534380, "z", lambda: z)[:,1], c='blue')
    _l_(534382)
    _c_(534385, _a_(534384, _n_(534383, "plt", lambda: plt), "show"))
    _l_(534386)
_c_(534389, _n_(534388, "KMeans", lambda: KMeans))
_l_(534390)