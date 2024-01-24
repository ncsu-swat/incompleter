# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61773112/attributeerror-tuple-object-has-no-attribute-asjson
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if not _n_(667872, "filename", lambda: filename) or _n_(667873, "filename", lambda: filename) == '-':
    _l_(667887)

    text = _c_(667877, _a_(667876, _a_(667875, _n_(667874, "sys", lambda: sys), "stdin"), "read"))
    _l_(667878)
else:
    with _c_(667881, _n_(667879, "open", lambda: open), _n_(667880, "filename", lambda: filename)) as f:
        _l_(667886)

        text = _c_(667884, _a_(667883, _n_(667882, "f", lambda: f), "read"))
        _l_(667885)

grammarname = 'grammars/CTEST.ebnf'
_l_(667888)
grammarData = _c_(667893, _a_(667892, _c_(667891, _n_(667889, "open", lambda: open), _n_(667890, "grammarname", lambda: grammarname)), "read"))
_l_(667894)
parser = _c_(667898, _a_(667896, _n_(667895, "tatsu", lambda: tatsu), "compile"), _n_(667897, "grammarData", lambda: grammarData), asmodel=True)
_l_(667899)

model = _c_(667903, _a_(667901, _n_(667900, "parser", lambda: parser), "parse"), _n_(667902, "text", lambda: text))
_l_(667904)
_c_(667906, _n_(667905, "print", lambda: print))
_l_(667907)
_c_(667913, _n_(667908, "print", lambda: print), '# MODEL TYPE IS:', _a_(667912, _c_(667911, _n_(667909, "type", lambda: type), _n_(667910, "model", lambda: model)), "__name__"))
_l_(667914)
_c_(667922, _n_(667915, "print", lambda: print), _c_(667921, _a_(667917, _n_(667916, "json", lambda: json), "dumps"), _c_(667920, _a_(667919, _n_(667918, "model", lambda: model), "asjson")), indent=4))
_l_(667923)
_c_(667925, _n_(667924, "print", lambda: print))
_l_(667926)