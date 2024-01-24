# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76171687/save-dictionary-with-value-of-type-nltk-corpus-reader-wordnet-synset-encount
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(637816, _n_(637815, "open", lambda: open), 'dict1.pickle', 'wb') as handle:
    _l_(637825)

    _c_(637823, _a_(637818, _n_(637817, "pickle", lambda: pickle), "dump"), _n_(637819, "hypernyms", lambda: hypernyms), _n_(637820, "handle", lambda: handle), protocol=_a_(637822, _n_(637821, "pickle", lambda: pickle), "HIGHEST_PROTOCOL"))
    _l_(637824)