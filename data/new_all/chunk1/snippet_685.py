# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57577132/python-3-7-attributeerror-list-object-has-no-attribute-split
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
analyser = _c_(396192, _n_(396191, "SentimentIntensityAnalyzer", lambda: SentimentIntensityAnalyzer))
_l_(396193)

def print_sentiment_scores(sentence):
    _l_(396208)

    snt = _c_(396197, _a_(396195, _n_(396194, "analyser", lambda: analyser), "polarity_scores"), _n_(396196, "sentence", lambda: sentence))
    _l_(396198)
    _c_(396206, _n_(396199, "print", lambda: print), _c_(396205, _a_(396200, "{:-<40} {}", "format"), _n_(396201, "sentence", lambda: sentence), _c_(396204, _n_(396202, "str", lambda: str), _n_(396203, "snt", lambda: snt))))
    _l_(396207)


_c_(396211, _n_(396209, "print_sentiment_scores", lambda: print_sentiment_scores), _n_(396210, "your_list", lambda: your_list))
_l_(396212)