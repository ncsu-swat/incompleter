# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70981856/how-do-i-fix-the-typeerror-load-missing-1-required-positional-argument-load
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from openai.embeddings_utils import get_embedding
    _l_(620140)

except ImportError:
    pass

# This will take just under 10 minutes
_n_(620141, "df", lambda: df)['babbage_similarity'] = _c_(620148, _a_(620144, _a_(620143, _n_(620142, "df", lambda: df), "combined"), "apply"), lambda x: _c_(620147, _n_(620145, "get_embedding", lambda: get_embedding), _n_(620146, "x", lambda: x), engine='text-similarity-babbage-001'))
_l_(620149)
_n_(620150, "df", lambda: df)['babbage_search'] = _c_(620157, _a_(620153, _a_(620152, _n_(620151, "df", lambda: df), "combined"), "apply"), lambda x: _c_(620156, _n_(620154, "get_embedding", lambda: get_embedding), _n_(620155, "x", lambda: x), engine='text-search-babbage-doc-001'))
_l_(620158)
_c_(620161, _a_(620160, _n_(620159, "df", lambda: df), "to_csv"), '/content/documents.csv')
_l_(620162)