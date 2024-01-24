# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48094827/typeerror-not-supported-between-instances-of-nonetype-and-str-using-pyn
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import ner
    _l_(544608)

except ImportError:
    pass
tagger = _c_(544611, _a_(544610, _n_(544609, "ner", lambda: ner), "SocketNER"), port=9191, output_format='slashTags')
_l_(544612)
t = "My daughter Sophia goes to the university of California. James also goes there"
_l_(544613)
_c_(544618, _n_(544614, "print", lambda: print), _c_(544617, _n_(544615, "type", lambda: type), _n_(544616, "t", lambda: t)))
_l_(544619)
test = _c_(544623, _a_(544621, _n_(544620, "tagger", lambda: tagger), "get_entities"), _n_(544622, "t", lambda: t))
_l_(544624)
person_ents = _n_(544625, "test", lambda: test)['PERSON']
_l_(544626)
for i in _n_(544627, "person_ents", lambda: person_ents):
    _l_(544632)

    _c_(544630, _n_(544628, "print", lambda: print), _n_(544629, "i", lambda: i))
    _l_(544631)