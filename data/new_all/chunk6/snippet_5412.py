# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54514394/typeerror-normalize-argument-2-must-be-str-not-series-with-a-dataframe-of-st
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    _l_(339710)

except ImportError:
    pass
try:
    import unicodedata
    _l_(339712)

except ImportError:
    pass
sid = _c_(339714, _n_(339713, "SentimentIntensityAnalyzer", lambda: SentimentIntensityAnalyzer))
_l_(339715)
for date, row in _c_(339719, _a_(339718, _a_(339717, _n_(339716, "df_news", lambda: df_news), "T"), "iteritems")):
    _l_(339773)

    try:
        _l_(339772)

        sentence = _c_(339727, _a_(339726, _c_(339725, _a_(339721, _n_(339720, "unicodedata", lambda: unicodedata), "normalize"), 'NFKD', _a_(339723, _n_(339722, "df_news", lambda: df_news), "loc")[_n_(339724, "date", lambda: date), 'name']), "encode"), 'ascii','ignore')
        _l_(339728)
        #print((sentence))
        ss = _c_(339734, _a_(339730, _n_(339729, "sid", lambda: sid), "polarity_scores"), _c_(339733, _n_(339731, "str", lambda: str), _n_(339732, "sentence", lambda: sentence)))
        _l_(339735)
        _c_(339740, _a_(339737, _n_(339736, "df_news", lambda: df_news), "set_value"), _n_(339738, "date", lambda: date), 'compound', _n_(339739, "ss", lambda: ss)['compound'])
        _l_(339741)
        _c_(339746, _a_(339743, _n_(339742, "df_news", lambda: df_news), "set_value"), _n_(339744, "date", lambda: date), 'neg', _n_(339745, "ss", lambda: ss)['neg'])
        _l_(339747)
        _c_(339752, _a_(339749, _n_(339748, "df_news", lambda: df_news), "set_value"), _n_(339750, "date", lambda: date), 'neu', _n_(339751, "ss", lambda: ss)['neu'])
        _l_(339753)
        _c_(339758, _a_(339755, _n_(339754, "df_news", lambda: df_news), "set_value"), _n_(339756, "date", lambda: date), 'pos', _n_(339757, "ss", lambda: ss)['pos'])
        _l_(339759)
    except _n_(339760, "TypeError", lambda: TypeError):
        _l_(339771)

        _c_(339765, _n_(339761, "print", lambda: print), _a_(339763, _n_(339762, "df_news", lambda: df_news), "loc")[_n_(339764, "date", lambda: date), 'name'])
        _l_(339766)
        _c_(339769, _n_(339767, "print", lambda: print), _n_(339768, "date", lambda: date))
        _l_(339770)