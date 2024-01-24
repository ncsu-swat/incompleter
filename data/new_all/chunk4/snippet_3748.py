# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68660137/why-does-presidio-stanzanlpengine-throw-nameerror-name-stanzalanguage-is-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import stanza
    _l_(622141)

except ImportError:
    pass
_c_(622144, _a_(622143, _n_(622142, "stanza", lambda: stanza), "download"), "en")
_l_(622145)
try:
    from presidio_analyzer.nlp_engine import StanzaNlpEngine
    _l_(622147)

except ImportError:
    pass
_c_(622149, _n_(622148, "StanzaNlpEngine", lambda: StanzaNlpEngine), models={"en": "en"})
_l_(622150)