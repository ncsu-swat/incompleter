# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61773112/attributeerror-tuple-object-has-no-attribute-asjson
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if not _n_(652327, "filename", lambda: filename) or _n_(652328, "filename", lambda: filename) == '-':
    _l_(652342)

    text = _c_(652332, _a_(652331, _a_(652330, _n_(652329, "sys", lambda: sys), "stdin"), "read"))
    _l_(652333)
else:
    with _c_(652336, _n_(652334, "open", lambda: open), _n_(652335, "filename", lambda: filename)) as f:
        _l_(652341)

        text = _c_(652339, _a_(652338, _n_(652337, "f", lambda: f), "read"))
        _l_(652340)

grammarname = 'grammars/CTEST.ebnf'
_l_(652343)
grammarData = _c_(652348, _a_(652347, _c_(652346, _n_(652344, "open", lambda: open), _n_(652345, "grammarname", lambda: grammarname)), "read"))
_l_(652349)
parser = _c_(652353, _a_(652351, _n_(652350, "tatsu", lambda: tatsu), "compile"), _n_(652352, "grammarData", lambda: grammarData), asmodel=True)
_l_(652354)

model = _c_(652358, _a_(652356, _n_(652355, "parser", lambda: parser), "parse"), _n_(652357, "text", lambda: text))
_l_(652359)
_c_(652361, _n_(652360, "print", lambda: print))
_l_(652362)
_c_(652368, _n_(652363, "print", lambda: print), '# MODEL TYPE IS:', _a_(652367, _c_(652366, _n_(652364, "type", lambda: type), _n_(652365, "model", lambda: model)), "__name__"))
_l_(652369)
_c_(652377, _n_(652370, "print", lambda: print), _c_(652376, _a_(652372, _n_(652371, "json", lambda: json), "dumps"), _c_(652375, _a_(652374, _n_(652373, "model", lambda: model), "asjson")), indent=4))
_l_(652378)
_c_(652380, _n_(652379, "print", lambda: print))
_l_(652381)