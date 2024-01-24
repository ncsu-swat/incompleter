# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35919525/type-error-in-python-3-expected-string-or-buffer-but-u-occured-at-index-0
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
token_pattern=r'(?u)\b\w\w+\b'
_l_(566152)
def preprocess(line,
           token_pattern=_n_(566153, "token_pattern", lambda: token_pattern),
           exclude_stoptword=_a_(566155, _n_(566154, "config", lambda: config), "cooccurrence_word_exclude_stopword"),
           encode_digit=False):
    _l_(566185)


    token_pattern=_c_(566161, _a_(566157, _n_(566156, "re", lambda: re), "compile"), _n_(566158, "token_pattern", lambda: token_pattern),_a_(566160, _n_(566159, "re", lambda: re), "UNICODE"))
    _l_(566162)
    tokens=[_c_(566165, _a_(566164, _n_(566163, "x", lambda: x), "lower")) for x in _c_(566169, _a_(566167, _n_(566166, "token_pattern", lambda: token_pattern), "findall"), _n_(566168, "line", lambda: line))]
    _l_(566170)

    tokens_stemmed=_c_(566174, _n_(566171, "stem_tokens", lambda: stem_tokens), _n_(566172, "tokens", lambda: tokens),_n_(566173, "english_stemmer", lambda: english_stemmer))
    _l_(566175)
    if _n_(566176, "exclude_stoptword", lambda: exclude_stoptword):
        _l_(566182)

        tokens_stemmed=[_n_(566177, "x", lambda: x) for x in _n_(566178, "tokens_stemmed", lambda: tokens_stemmed) if _n_(566179, "x", lambda: x)  not in _n_(566180, "stopwords", lambda: stopwords)]
        _l_(566181)
    aux = _n_(566183, "tokens_stemmed", lambda: tokens_stemmed)
    _l_(566184)
    return aux

def extract(df):
    _l_(566196)

    #Unigram Features 

    _n_(566186, "df", lambda: df)["query_unigram"]=_c_(566194, _n_(566187, "list", lambda: list), _c_(566193, _a_(566189, _n_(566188, "df", lambda: df), "apply"), lambda x:_c_(566192, _n_(566190, "preprocess", lambda: preprocess), _n_(566191, "df", lambda: df)["query"]),axis=1))
    _l_(566195)