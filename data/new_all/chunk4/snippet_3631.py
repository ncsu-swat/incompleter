# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70981856/how-do-i-fix-the-typeerror-load-missing-1-required-positional-argument-load
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from openai.embeddings_utils import get_embedding
    _l_(580966)

except ImportError:
    pass

# This will take just under 10 minutes
_n_(580967, "df", lambda: df)['babbage_similarity'] = _c_(580974, _a_(580970, _a_(580969, _n_(580968, "df", lambda: df), "combined"), "apply"), lambda x: _c_(580973, _n_(580971, "get_embedding", lambda: get_embedding), _n_(580972, "x", lambda: x), engine='text-similarity-babbage-001'))
_l_(580975)
_n_(580976, "df", lambda: df)['babbage_search'] = _c_(580983, _a_(580979, _a_(580978, _n_(580977, "df", lambda: df), "combined"), "apply"), lambda x: _c_(580982, _n_(580980, "get_embedding", lambda: get_embedding), _n_(580981, "x", lambda: x), engine='text-search-babbage-doc-001'))
_l_(580984)
_c_(580987, _a_(580986, _n_(580985, "df", lambda: df), "to_csv"), '/content/documents.csv')
_l_(580988)