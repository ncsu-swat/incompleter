# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63564183/nameerror-name-pydotplus-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas
    _l_(395581)

except ImportError:
    pass
try:
    from sklearn import tree
    _l_(395583)

except ImportError:
    pass
try:
    import pydotplus
    _l_(395585)

except ImportError:
    pass
try:
    from sklearn.tree import DecisionTreeClassifier
    _l_(395587)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(395589)

except ImportError:
    pass
try:
    import matplotlib.image as pltimg
    _l_(395591)

except ImportError:
    pass

df = _c_(395594, _a_(395593, _n_(395592, "pandas", lambda: pandas), "read_csv"), "shows.csv")
_l_(395595)

d = {'UK': 0, 'USA': 1, 'N': 2}
_l_(395596)
_n_(395597, "df", lambda: df)['Nationality'] = _c_(395601, _a_(395599, _n_(395598, "df", lambda: df)['Nationality'], "map"), _n_(395600, "d", lambda: d))
_l_(395602)
d = {'YES': 1, 'NO': 0}
_l_(395603)
_n_(395604, "df", lambda: df)['Go'] = _c_(395608, _a_(395606, _n_(395605, "df", lambda: df)['Go'], "map"), _n_(395607, "d", lambda: d))
_l_(395609)

features = ['Age', 'Experience', 'Rank', 'Nationality']
_l_(395610)

X = _n_(395611, "df", lambda: df)[_n_(395612, "features", lambda: features)]
_l_(395613)
y = _n_(395614, "df", lambda: df)['Go']
_l_(395615)

dtree = _c_(395617, _n_(395616, "DecisionTreeClassifier", lambda: DecisionTreeClassifier))
_l_(395618)
dtree = _c_(395623, _a_(395620, _n_(395619, "dtree", lambda: dtree), "fit"), _n_(395621, "X", lambda: X), _n_(395622, "y", lambda: y))
_l_(395624)
data = _c_(395629, _a_(395626, _n_(395625, "tree", lambda: tree), "export_graphviz"), _n_(395627, "dtree", lambda: dtree), out_file=None, feature_names=_n_(395628, "features", lambda: features))
_l_(395630)
graph = _c_(395634, _a_(395632, _n_(395631, "pydotplus", lambda: pydotplus), "graph_from_dot_data"), _n_(395633, "data", lambda: data))
_l_(395635)
_c_(395638, _a_(395637, _n_(395636, "graph", lambda: graph), "write_png"), 'mydecisiontree.png')
_l_(395639)

img=_c_(395642, _a_(395641, _n_(395640, "pltimg", lambda: pltimg), "imread"), 'mydecisiontree.png')
_l_(395643)
imgplot = _c_(395647, _a_(395645, _n_(395644, "plt", lambda: plt), "imshow"), _n_(395646, "img", lambda: img))
_l_(395648)
_c_(395651, _a_(395650, _n_(395649, "plt", lambda: plt), "show"))
_l_(395652)