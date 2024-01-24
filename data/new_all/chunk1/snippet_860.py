# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60087408/python-pandas-and-nltk-type-error-int-object-is-not-callable-when-calling-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(392816)

except ImportError:
    pass
try:
    import numpy as np
    _l_(392818)

except ImportError:
    pass
try:
    import nltk
    _l_(392820)

except ImportError:
    pass
try:
    import string
    _l_(392822)

except ImportError:
    pass
try:
    import collections
    _l_(392824)

except ImportError:
    pass
try:
    from collections import Counter
    _l_(392826)

except ImportError:
    pass
_c_(392829, _a_(392828, _n_(392827, "nltk", lambda: nltk), "download"), 'stopwords')
_l_(392830)
sw= _c_(392837, _n_(392831, "set", lambda: set), _c_(392836, _a_(392835, _a_(392834, _a_(392833, _n_(392832, "nltk", lambda: nltk), "corpus"), "stopwords"), "words"), 'english'))
_l_(392838)
punctuation = _c_(392842, _n_(392839, "set", lambda: set), _a_(392841, _n_(392840, "string", lambda: string), "punctuation"))
_l_(392843)
data= _c_(392846, _a_(392845, _n_(392844, "pd", lambda: pd), "read_csv"), '~/Desktop/tweets.csv.zip', compression='zip')
_l_(392847)

_c_(392851, _n_(392848, "print", lambda: print), _a_(392850, _n_(392849, "data", lambda: data), "columns"))
_l_(392852)
_c_(392858, _n_(392853, "print", lambda: print), _c_(392857, _n_(392854, "len", lambda: len), _a_(392856, _n_(392855, "data", lambda: data), "tweet_id")))
_l_(392859)
tweets = _a_(392861, _n_(392860, "data", lambda: data), "text")
_l_(392862)
test = _c_(392866, _a_(392864, _n_(392863, "pd", lambda: pd), "DataFrame"), _n_(392865, "data", lambda: data))
_l_(392867)
_n_(392868, "test", lambda: test).column = ["text"]
_l_(392869)
# Exclude stopwords with Python's list comprehension and pandas.DataFrame.apply.
_n_(392870, "test", lambda: test)['tweet_without_stopwords'] = _c_(392887, _a_(392872, _n_(392871, "test", lambda: test)['text'], "apply"), lambda x: _c_(392886, _a_(392873, ' ', "join"), [_n_(392874, "word", lambda: word) for word in _c_(392877, _a_(392876, _n_(392875, "x", lambda: x), "split")) if _n_(392878, "word", lambda: word) not in _n_(392879, "sw", lambda: (sw)) and _n_(392880, "word", lambda: word) for word in _c_(392883, _a_(392882, _n_(392881, "x", lambda: x), "split")) if _n_(392884, "word", lambda: word) not in _n_(392885, "punctuation", lambda: punctuation)]))
_l_(392888)
_c_(392891, _n_(392889, "print", lambda: print), _n_(392890, "test", lambda: test))
_l_(392892)
chirps = _a_(392894, _n_(392893, "test", lambda: test), "text")
_l_(392895)
splitwords = [ _c_(392901, _a_(392897, _n_(392896, "nltk", lambda: nltk), "word_tokenize"), _c_(392900, _n_(392898, "str", lambda: str), _n_(392899, "c", lambda: c)) ) for c in _n_(392902, "chirps", lambda: chirps) ]
_l_(392903)
allWords = []
_l_(392904)
for wordList in _n_(392905, "splitwords", lambda: splitwords):
    _l_(392908)

    allWords += _n_(392906, "wordList", lambda: wordList)
    _l_(392907)
allWords_clean = [_c_(392911, _a_(392910, _n_(392909, "w", lambda: w), "lower")) for w in _n_(392912, "allWords", lambda: allWords) if _c_(392915, _a_(392914, _n_(392913, "w", lambda: w), "lower")) not in _n_(392916, "sw", lambda: sw) and _c_(392919, _a_(392918, _n_(392917, "w", lambda: w), "lower")) not in _n_(392920, "punctuation", lambda: punctuation)]   
_l_(392921)   
tweets2 = _c_(392925, _a_(392923, _n_(392922, "pd", lambda: pd), "Series"), _n_(392924, "allWords", lambda: allWords))
_l_(392926)

words = _c_(392930, _a_(392928, _n_(392927, "nltk", lambda: nltk), "FreqDist"), _n_(392929, "tweets2", lambda: tweets2))
_l_(392931)