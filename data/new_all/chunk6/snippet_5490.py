# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51925123/nameerror-name-fit-classifier-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(337107)

except ImportError:
    pass
try:
    import pandas
    _l_(337109)

except ImportError:
    pass
try:
    from sklearn import svm
    _l_(337111)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(337113)

except ImportError:
    pass
try:
    from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
    _l_(337115)

except ImportError:
    pass
try:
    import numpy as np
    _l_(337117)

except ImportError:
    pass
try:
    from sklearn.feature_extraction.text import CountVectorizer
    _l_(337119)

except ImportError:
    pass
try:
    from sklearn.feature_extraction.text import TfidfTransformer
    _l_(337121)

except ImportError:
    pass
try:
    from sklearn.multiclass import OneVsOneClassifier
    _l_(337123)

except ImportError:
    pass
try:
    from sklearn.svm import SVC
    _l_(337125)

except ImportError:
    pass
try:
    from sklearn import cross_validation
    _l_(337127)

except ImportError:
    pass
try:
    from sklearn.metrics import confusion_matrix
    _l_(337129)

except ImportError:
    pass

dataset = _c_(337132, _a_(337131, _n_(337130, "pd", lambda: pd), "read_csv"), 'data.csv', encoding = 'utf-8')
_l_(337133)
data = _n_(337134, "dataset", lambda: dataset)['text']
_l_(337135)
labels = _n_(337136, "dataset", lambda: dataset)['label']
_l_(337137)

X_train, X_test, y_train, y_test = _c_(337141, _n_(337138, "train_test_split", lambda: train_test_split), _n_(337139, "data", lambda: data), _n_(337140, "labels", lambda: labels), test_size = 0.2, random_state = 0)
_l_(337142)

count_vector = _c_(337144, _n_(337143, "CountVectorizer", lambda: CountVectorizer))
_l_(337145)
tfidf = _c_(337147, _n_(337146, "TfidfTransformer", lambda: TfidfTransformer))
_l_(337148)

classifier = _c_(337152, _n_(337149, "OneVsOneClassifier", lambda: OneVsOneClassifier), _c_(337151, _n_(337150, "SVC", lambda: SVC), kernel = 'linear', random_state = 84))
_l_(337153)

train_counts = _c_(337157, _a_(337155, _n_(337154, "count_vector", lambda: count_vector), "fit_transform"), _n_(337156, "X_train", lambda: X_train))
_l_(337158)
train_tfidf = _c_(337162, _a_(337160, _n_(337159, "tfidf", lambda: tfidf), "fit_transform"), _n_(337161, "train_counts", lambda: train_counts))
_l_(337163)
_c_(337168, _a_(337165, _n_(337164, "classifier", lambda: classifier), "fit"), _n_(337166, "train_tfidf", lambda: train_tfidf), _n_(337167, "y_train", lambda: y_train))
_l_(337169)

test_counts = _c_(337173, _a_(337171, _n_(337170, "count_vector", lambda: count_vector), "transform"), _n_(337172, "X_test", lambda: X_test))
_l_(337174)
test_tfidf = _c_(337178, _a_(337176, _n_(337175, "tfidf", lambda: tfidf), "transform"), _n_(337177, "test_counts", lambda: test_counts))
_l_(337179)
_c_(337183, _a_(337181, _n_(337180, "classifier", lambda: classifier), "predict"), _n_(337182, "test_tfidf", lambda: test_tfidf))
_l_(337184)

_c_(337188, _n_(337185, "fit_classifier", lambda: fit_classifier), _n_(337186, "X_train", lambda: X_train), _n_(337187, "y_train", lambda: y_train))
_l_(337189)
predicted = _c_(337192, _n_(337190, "predict", lambda: predict), _n_(337191, "X_test", lambda: X_test))
_l_(337193)

_c_(337195, _n_(337194, "print", lambda: print), "confusion matrix")
_l_(337196)
_c_(337203, _n_(337197, "print", lambda: print), _c_(337202, _n_(337198, "confusion_matrix", lambda: confusion_matrix), _n_(337199, "X_test", lambda: X_test), _n_(337200, "predicted", lambda: predicted), labels = _n_(337201, "labels", lambda: labels)))
_l_(337204)

_c_(337206, _n_(337205, "print", lambda: print), "cross validation")
_l_(337207)
test_counts = _c_(337211, _a_(337209, _n_(337208, "count_vector", lambda: count_vector), "fit_transform"), _n_(337210, "data", lambda: data))
_l_(337212)
test_tfidf = _c_(337216, _a_(337214, _n_(337213, "tfidf", lambda: tfidf), "fit_transform"), _n_(337215, "test_counts", lambda: test_counts))
_l_(337217)

scores = _c_(337223, _a_(337219, _n_(337218, "cross_validation", lambda: cross_validation), "cross_val_score"), _n_(337220, "classifier", lambda: classifier), _n_(337221, "test_tfidf", lambda: test_tfidf), _n_(337222, "labels", lambda: labels), cv = 10)
_l_(337224)
_c_(337227, _n_(337225, "print", lambda: print), _n_(337226, "scores", lambda: scores))
_l_(337228)
_c_(337238, _n_(337229, "print", lambda: print), _c_(337237, _a_(337230, "Accuracy: {} +/- {}", "format"), _c_(337233, _a_(337232, _n_(337231, "scores", lambda: scores), "mean")), _c_(337236, _a_(337235, _n_(337234, "scores", lambda: scores), "std")) * 2))
_l_(337239)