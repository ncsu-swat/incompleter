# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71272910/attributeerror-spacy-tokenizer-tokenizer-object-has-no-attribute-tokens-from
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import spacy
    _l_(595671)

except ImportError:
    pass
try:
    import re
    _l_(595673)

except ImportError:
    pass

regexp = _c_(595676, _a_(595675, _n_(595674, "re", lambda: re), "compile"), '(?u)\\b\\w\\w+\\b')
_l_(595677)
en_nlp = _c_(595680, _a_(595679, _n_(595678, "spacy", lambda: spacy), "load"), "en_core_web_sm", disable=['parser', 'ner'])
_l_(595681)
old_tokenizer = _a_(595683, _n_(595682, "en_nlp", lambda: en_nlp), "tokenizer")
_l_(595684)

_n_(595685, "en_nlp", lambda: en_nlp).tokenizer = lambda string: _c_(595692, _a_(595687, _n_(595686, "old_tokenizer", lambda: old_tokenizer), "tokens_from_list"), _c_(595691, _a_(595689, _n_(595688, "regexp", lambda: regexp), "findall"), _n_(595690, "string", lambda: string)))
_l_(595693)

def custom_tokenizer(document):
    _l_(595702)

    doc_spacy = _c_(595696, _n_(595694, "en_nlp", lambda: en_nlp), _n_(595695, "document", lambda: document))
    _l_(595697)
    aux = [_a_(595699, _n_(595698, "token", lambda: token), "lemma_") for token in _n_(595700, "doc_spacy", lambda: doc_spacy)]
    _l_(595701)
    return aux

lemma_vect = _c_(595705, _n_(595703, "CountVectorizer", lambda: CountVectorizer), tokenizer=_n_(595704, "custom_tokenizer", lambda: custom_tokenizer), min_df=5)
_l_(595706)