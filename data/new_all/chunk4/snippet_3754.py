# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68638629/json-dump-typeerror-object-of-type-int64-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ldamodel = _c_(596086, _n_(596084, "LDA_Model", lambda: LDA_Model), _n_(596085, "data_words", lambda: data_words))
_l_(596087)
coherence = _c_(596090, _a_(596089, _n_(596088, "ldamodel", lambda: ldamodel), "build_models"), start = 5, limit= 71, step= 5, runs=10)
_l_(596091)