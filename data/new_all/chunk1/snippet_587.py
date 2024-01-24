# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63479213/attributeerror-nonetype-object-has-no-attribute-lower
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
vectorizer = _c_(390243, _n_(390239, "CountVectorizer", lambda: CountVectorizer), tokenizer = lambda x: _c_(390242, _a_(390241, _n_(390240, "x", lambda: x), "split"), " "))
_l_(390244)

tag_dtm = _c_(390248, _a_(390246, _n_(390245, "vectorizer", lambda: vectorizer), "fit_transform"), _n_(390247, "tag_data", lambda: tag_data)['Tags'])
_l_(390249)