# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53755893/facing-attributeerror-for-tag-using-spacy-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(390130)

except ImportError:
    pass
read_data = _c_(390133, _a_(390132, _n_(390131, "pd", lambda: pd), "read_csv"), 'C:\\Users\\abc\\def\\pqr\\Data\\training_data.csv', encoding="utf-8")
_l_(390134)
entity = []
_l_(390135)
for parsed_doc in _n_(390136, "read_data", lambda: read_data)['Description']:
    _l_(390153)

    doc = _c_(390139, _n_(390137, "nlp", lambda: nlp), _n_(390138, "parsed_doc", lambda: parsed_doc))
    _l_(390140)
    a = [(_a_(390142, _n_(390141, "X", lambda: X), "text"), _a_(390144, _n_(390143, "X", lambda: X), "tag_")) for X in _a_(390146, _n_(390145, "doc", lambda: doc), "ents")]
    _l_(390147)
    _c_(390151, _a_(390149, _n_(390148, "entity", lambda: entity), "append"), _n_(390150, "a", lambda: a))
    _l_(390152)