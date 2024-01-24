# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54514394/typeerror-normalize-argument-2-must-be-str-not-series-with-a-dataframe-of-st
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    _l_(334758)

except ImportError:
    pass
try:
    import unicodedata
    _l_(334760)

except ImportError:
    pass
sid = _c_(334762, _n_(334761, "SentimentIntensityAnalyzer", lambda: SentimentIntensityAnalyzer))
_l_(334763)
for date, row in _c_(334767, _a_(334766, _a_(334765, _n_(334764, "df_news", lambda: df_news), "T"), "iteritems")):
    _l_(334821)

    try:
        _l_(334820)

        sentence = _c_(334775, _a_(334774, _c_(334773, _a_(334769, _n_(334768, "unicodedata", lambda: unicodedata), "normalize"), 'NFKD', _a_(334771, _n_(334770, "df_news", lambda: df_news), "loc")[_n_(334772, "date", lambda: date), 'name']), "encode"), 'ascii','ignore')
        _l_(334776)
        #print((sentence))
        ss = _c_(334782, _a_(334778, _n_(334777, "sid", lambda: sid), "polarity_scores"), _c_(334781, _n_(334779, "str", lambda: str), _n_(334780, "sentence", lambda: sentence)))
        _l_(334783)
        _c_(334788, _a_(334785, _n_(334784, "df_news", lambda: df_news), "set_value"), _n_(334786, "date", lambda: date), 'compound', _n_(334787, "ss", lambda: ss)['compound'])
        _l_(334789)
        _c_(334794, _a_(334791, _n_(334790, "df_news", lambda: df_news), "set_value"), _n_(334792, "date", lambda: date), 'neg', _n_(334793, "ss", lambda: ss)['neg'])
        _l_(334795)
        _c_(334800, _a_(334797, _n_(334796, "df_news", lambda: df_news), "set_value"), _n_(334798, "date", lambda: date), 'neu', _n_(334799, "ss", lambda: ss)['neu'])
        _l_(334801)
        _c_(334806, _a_(334803, _n_(334802, "df_news", lambda: df_news), "set_value"), _n_(334804, "date", lambda: date), 'pos', _n_(334805, "ss", lambda: ss)['pos'])
        _l_(334807)
    except _n_(334808, "TypeError", lambda: TypeError):
        _l_(334819)

        _c_(334813, _n_(334809, "print", lambda: print), _a_(334811, _n_(334810, "df_news", lambda: df_news), "loc")[_n_(334812, "date", lambda: date), 'name'])
        _l_(334814)
        _c_(334817, _n_(334815, "print", lambda: print), _n_(334816, "date", lambda: date))
        _l_(334818)