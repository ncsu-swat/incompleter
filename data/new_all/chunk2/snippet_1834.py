# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49415195/typeerror-from-multinomialnb-float-argument-must-be-a-string-or-a-number
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
documents = [(_c_(468322, _n_(468317, "list", lambda: list), _c_(468321, _a_(468319, _n_(468318, "movie_reviews", lambda: movie_reviews), "words"), _n_(468320, "fileid", lambda: fileid))), _n_(468323, "category", lambda: category))
             for category in _c_(468326, _a_(468325, _n_(468324, "movie_reviews", lambda: movie_reviews), "categories"))
             for fileid in _c_(468330, _a_(468328, _n_(468327, "movie_reviews", lambda: movie_reviews), "fileids"), _n_(468329, "category", lambda: category))]
_l_(468331)

_c_(468335, _a_(468333, _n_(468332, "random", lambda: random), "shuffle"), _n_(468334, "documents", lambda: documents))
_l_(468336)

#print(documents[1])

all_words = []
_l_(468337)

for w in _c_(468340, _a_(468339, _n_(468338, "movie_reviews", lambda: movie_reviews), "words")):
    _l_(468348)

    _c_(468346, _a_(468342, _n_(468341, "all_words", lambda: all_words), "append"), _c_(468345, _a_(468344, _n_(468343, "w", lambda: w), "lower")))
    _l_(468347)

all_words = _c_(468352, _a_(468350, _n_(468349, "nltk", lambda: nltk), "FreqDist"), _n_(468351, "all_words", lambda: all_words))
_l_(468353)

word_features = _c_(468358, _n_(468354, "list", lambda: list), _c_(468357, _a_(468356, _n_(468355, "all_words", lambda: all_words), "keys")))[:3000]
_l_(468359)

def look_for_features(document):
    _l_(468374)

    words = _c_(468362, _n_(468360, "set", lambda: set), _n_(468361, "document", lambda: document))
    _l_(468363)
    features = {}
    _l_(468364)
    for x in _n_(468365, "word_features", lambda: word_features):
        _l_(468371)

        _n_(468366, "features", lambda: features)[_n_(468367, "x", lambda: x)] = {_n_(468368, "x", lambda: x) in _n_(468369, "words", lambda: words)}
        _l_(468370)
    aux = _n_(468372, "features", lambda: features)
    _l_(468373)
    return aux

#feature set will be finding features and category
featuresets = [(_c_(468377, _n_(468375, "look_for_features", lambda: look_for_features), _n_(468376, "rev", lambda: rev)), _n_(468378, "category", lambda: category)) for (rev, category) in _n_(468379, "documents", lambda: documents)]
_l_(468380)

training_set = _n_(468381, "featuresets", lambda: featuresets)[:1400]
_l_(468382)
testing_set = _n_(468383, "featuresets", lambda: featuresets)[1400:]
_l_(468384)

#Multinomial
MNB_classifier = _c_(468388, _n_(468385, "SklearnClassifier", lambda: SklearnClassifier), _c_(468387, _n_(468386, "MultinomialNB", lambda: MultinomialNB)))
_l_(468389)
_c_(468393, _a_(468391, _n_(468390, "MNB_classifier", lambda: MNB_classifier), "train"), _n_(468392, "training_set", lambda: training_set))
_l_(468394)
_c_(468402, _n_(468395, "print", lambda: print), "Accuracy: ", _c_(468401, _a_(468398, _a_(468397, _n_(468396, "nltk", lambda: nltk), "classify"), "accuracy"), _n_(468399, "MNB_classifier", lambda: MNB_classifier),_n_(468400, "testing_set", lambda: testing_set))*100)
_l_(468403)