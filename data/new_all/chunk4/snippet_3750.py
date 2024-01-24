# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68660137/why-does-presidio-stanzanlpengine-throw-nameerror-name-stanzalanguage-is-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import stanza
    _l_(591909)

except ImportError:
    pass
_c_(591912, _a_(591911, _n_(591910, "stanza", lambda: stanza), "download"), "en")
_l_(591913)
try:
    from presidio_analyzer.nlp_engine import StanzaNlpEngine
    _l_(591915)

except ImportError:
    pass
_c_(591917, _n_(591916, "StanzaNlpEngine", lambda: StanzaNlpEngine), models={"en": "en"})
_l_(591918)