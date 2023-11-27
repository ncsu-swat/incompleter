# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(1541243)

except ImportError:
    pass
try:
    import unicodedata
    _l_(1541245)

except ImportError:
    pass

def strip_accents(text):
    _l_(1541272)

    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        _l_(1541254)

        text = _c_(1541248, _n_(1541246, "unicode", lambda: unicode), _n_(1541247, "text", lambda: text), 'utf-8')
        _l_(1541249)
    except (_n_(1541250, "TypeError", lambda: TypeError), _n_(1541251, "NameError", lambda: NameError)):
        _l_(1541253)

        pass
        _l_(1541252)
    text = _c_(1541258, _a_(1541256, _n_(1541255, "unicodedata", lambda: unicodedata), "normalize"), 'NFD', _n_(1541257, "text", lambda: text))
    _l_(1541259)
    text = _c_(1541262, _a_(1541261, _n_(1541260, "text", lambda: text), "encode"), 'ascii', 'ignore')
    _l_(1541263)
    text = _c_(1541266, _a_(1541265, _n_(1541264, "text", lambda: text), "decode"), "utf-8")
    _l_(1541267)
    aux = _c_(1541270, _n_(1541268, "str", lambda: str), _n_(1541269, "text", lambda: text))
    _l_(1541271)
    return aux

def text_to_id(text):
    _l_(1541291)

    """
    Convert input text to id.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    text = _c_(1541277, _n_(1541273, "strip_accents", lambda: strip_accents), _c_(1541276, _a_(1541275, _n_(1541274, "text", lambda: text), "lower")))
    _l_(1541278)
    text = _c_(1541282, _a_(1541280, _n_(1541279, "re", lambda: re), "sub"), '[ ]+', '_', _n_(1541281, "text", lambda: text))
    _l_(1541283)
    text = _c_(1541287, _a_(1541285, _n_(1541284, "re", lambda: re), "sub"), '[^0-9a-zA-Z_-]', '', _n_(1541286, "text", lambda: text))
    _l_(1541288)
    aux = _n_(1541289, "text", lambda: text)
    _l_(1541290)
    return aux

_c_(1541293, _n_(1541292, "text_to_id", lambda: text_to_id), "Montréal, über, 12.89, Mère, Françoise, noël, 889")
_l_(1541294)
'montreal_uber_1289_mere_francoise_noel_889'
_l_(1541295)

