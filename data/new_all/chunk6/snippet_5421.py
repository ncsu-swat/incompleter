# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54514394/typeerror-normalize-argument-2-must-be-str-not-series-with-a-dataframe-of-st
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    _l_(371663)

except ImportError:
    pass
try:
    import unicodedata
    _l_(371665)

except ImportError:
    pass
sid = _c_(371667, _n_(371666, "SentimentIntensityAnalyzer", lambda: SentimentIntensityAnalyzer))
_l_(371668)
for date, row in _c_(371672, _a_(371671, _a_(371670, _n_(371669, "df_news", lambda: df_news), "T"), "iteritems")):
    _l_(371726)

    try:
        _l_(371725)

        sentence = _c_(371680, _a_(371679, _c_(371678, _a_(371674, _n_(371673, "unicodedata", lambda: unicodedata), "normalize"), 'NFKD', _a_(371676, _n_(371675, "df_news", lambda: df_news), "loc")[_n_(371677, "date", lambda: date), 'name']), "encode"), 'ascii','ignore')
        _l_(371681)
        #print((sentence))
        ss = _c_(371687, _a_(371683, _n_(371682, "sid", lambda: sid), "polarity_scores"), _c_(371686, _n_(371684, "str", lambda: str), _n_(371685, "sentence", lambda: sentence)))
        _l_(371688)
        _c_(371693, _a_(371690, _n_(371689, "df_news", lambda: df_news), "set_value"), _n_(371691, "date", lambda: date), 'compound', _n_(371692, "ss", lambda: ss)['compound'])
        _l_(371694)
        _c_(371699, _a_(371696, _n_(371695, "df_news", lambda: df_news), "set_value"), _n_(371697, "date", lambda: date), 'neg', _n_(371698, "ss", lambda: ss)['neg'])
        _l_(371700)
        _c_(371705, _a_(371702, _n_(371701, "df_news", lambda: df_news), "set_value"), _n_(371703, "date", lambda: date), 'neu', _n_(371704, "ss", lambda: ss)['neu'])
        _l_(371706)
        _c_(371711, _a_(371708, _n_(371707, "df_news", lambda: df_news), "set_value"), _n_(371709, "date", lambda: date), 'pos', _n_(371710, "ss", lambda: ss)['pos'])
        _l_(371712)
    except _n_(371713, "TypeError", lambda: TypeError):
        _l_(371724)

        _c_(371718, _n_(371714, "print", lambda: print), _a_(371716, _n_(371715, "df_news", lambda: df_news), "loc")[_n_(371717, "date", lambda: date), 'name'])
        _l_(371719)
        _c_(371722, _n_(371720, "print", lambda: print), _n_(371721, "date", lambda: date))
        _l_(371723)