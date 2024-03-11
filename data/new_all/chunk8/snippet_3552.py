# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72333214/attributeerror-nonetype-object-has-no-attribute-get-and-the-knn-step-is-ri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    _l_(593299)

except ImportError:
    pass
try:
    from sklearn.multiclass import OneVsRestClassifier
    _l_(593301)

except ImportError:
    pass
try:
    from sklearn.neighbors import KNeighborsClassifier
    _l_(593303)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(593305)

except ImportError:
    pass
top = _c_(593307, _n_(593306, "Tk", lambda: Tk), '300','300')
_l_(593308)
box= _c_(593313, _a_(593312, _c_(593311, _n_(593309, "Text", lambda: Text), _n_(593310, "top", lambda: top)), "grid"), row=1,column=1)
_l_(593314)
p = _c_(593316, _n_(593315, "TfidfVectorizer", lambda: TfidfVectorizer), sublinear_tf=True, stop_words='english')
_l_(593317)
_c_(593324, _a_(593319, _n_(593318, "p", lambda: p), "fit"), _c_(593323, _a_(593321, _n_(593320, "box", lambda: box), "get"), "1.0",_n_(593322, "END", lambda: END)))
_l_(593325)
wordOfp = _c_(593329, _a_(593327, _n_(593326, "p", lambda: p), "transform"), _n_(593328, "p", lambda: p))
_l_(593330)

x_train,x_test,y_train,y_test = _c_(593334, _n_(593331, "train_test_split", lambda: train_test_split), _n_(593332, "wordOfp", lambda: wordOfp),_n_(593333, "y", lambda: y),random_state = 42, test_size = 0.2)# y is target
_l_(593335)# y is target
model = _c_(593339, _n_(593336, "OneVsRestClassifier", lambda: OneVsRestClassifier), _c_(593338, _n_(593337, "KNeighborsClassifier", lambda: KNeighborsClassifier), n_neighbors=5, metric= 'euclidean'  ))
_l_(593340)
_c_(593345, _a_(593342, _n_(593341, "model", lambda: model), "fit"), _n_(593343, "x_train", lambda: x_train),_n_(593344, "y_train", lambda: y_train))
_l_(593346)
prediction = _c_(593350, _a_(593348, _n_(593347, "model", lambda: model), "predict"), _n_(593349, "x_test", lambda: x_test))
_l_(593351)