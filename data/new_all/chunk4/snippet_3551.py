# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72333214/attributeerror-nonetype-object-has-no-attribute-get-and-the-knn-step-is-ri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    _l_(632721)

except ImportError:
    pass
try:
    from sklearn.multiclass import OneVsRestClassifier
    _l_(632723)

except ImportError:
    pass
try:
    from sklearn.neighbors import KNeighborsClassifier
    _l_(632725)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(632727)

except ImportError:
    pass
top = _c_(632729, _n_(632728, "Tk", lambda: Tk), '300','300')
_l_(632730)
box= _c_(632735, _a_(632734, _c_(632733, _n_(632731, "Text", lambda: Text), _n_(632732, "top", lambda: top)), "grid"), row=1,column=1)
_l_(632736)
p = _c_(632738, _n_(632737, "TfidfVectorizer", lambda: TfidfVectorizer), sublinear_tf=True, stop_words='english')
_l_(632739)
_c_(632746, _a_(632741, _n_(632740, "p", lambda: p), "fit"), _c_(632745, _a_(632743, _n_(632742, "box", lambda: box), "get"), "1.0",_n_(632744, "END", lambda: END)))
_l_(632747)
wordOfp = _c_(632751, _a_(632749, _n_(632748, "p", lambda: p), "transform"), _n_(632750, "p", lambda: p))
_l_(632752)

x_train,x_test,y_train,y_test = _c_(632756, _n_(632753, "train_test_split", lambda: train_test_split), _n_(632754, "wordOfp", lambda: wordOfp),_n_(632755, "y", lambda: y),random_state = 42, test_size = 0.2)# y is target
_l_(632757)# y is target
model = _c_(632761, _n_(632758, "OneVsRestClassifier", lambda: OneVsRestClassifier), _c_(632760, _n_(632759, "KNeighborsClassifier", lambda: KNeighborsClassifier), n_neighbors=5, metric= 'euclidean'  ))
_l_(632762)
_c_(632767, _a_(632764, _n_(632763, "model", lambda: model), "fit"), _n_(632765, "x_train", lambda: x_train),_n_(632766, "y_train", lambda: y_train))
_l_(632768)
prediction = _c_(632772, _a_(632770, _n_(632769, "model", lambda: model), "predict"), _n_(632771, "x_test", lambda: x_test))
_l_(632773)