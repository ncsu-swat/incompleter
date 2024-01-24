# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48277354/typeerror-a-bytes-like-object-is-required-not-str-how-can-i-fix-this
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib.request
    _l_(419535)

except ImportError:
    pass
try:
    import urllib.parse
    _l_(419537)

except ImportError:
    pass

def read_text():
    _l_(419557)

    quotes = _c_(419539, _n_(419538, "open", lambda: open), "C:\Check Profanity\movie_quotes.txt")
    _l_(419540)
    contents_of_file = _c_(419543, _a_(419542, _n_(419541, "quotes", lambda: quotes), "read"))
    _l_(419544)
    _c_(419547, _n_(419545, "print", lambda: print), _n_(419546, "contents_of_file", lambda: contents_of_file))
    _l_(419548)
    _c_(419551, _a_(419550, _n_(419549, "quotes", lambda: quotes), "close"))
    _l_(419552)
    _c_(419555, _n_(419553, "check_profanity", lambda: check_profanity), _n_(419554, "contents_of_file", lambda: contents_of_file))
    _l_(419556)

def check_profanity(text_to_check):
    _l_(419595)

    encoded_text = _c_(419561, _a_(419559, _a_(419558, urllib, "parse"), "quote"), _n_(419560, "text_to_check", lambda: text_to_check), 'utf-8')
    _l_(419562)
    address = "http://www.wdylike.appspot.com/?q="+_n_(419563, "encoded_text", lambda: encoded_text)
    _l_(419564)
    connection = _c_(419568, _a_(419566, _a_(419565, urllib, "request"), "urlopen"), _n_(419567, "address", lambda: address))
    _l_(419569)
    output = _c_(419572, _a_(419571, _n_(419570, "connection", lambda: connection), "read"))
    _l_(419573)
    _c_(419576, _n_(419574, "print", lambda: print), _n_(419575, "output", lambda: output))
    _l_(419577)
    _c_(419580, _a_(419579, _n_(419578, "connection", lambda: connection), "close"))
    _l_(419581)
    if "true" in _n_(419582, "output", lambda: output):
        _l_(419594)

        _c_(419584, _n_(419583, "print", lambda: print), "Profanity Alert!")
        _l_(419585)
    elif "false" in _n_(419586, "output", lambda: output):
        _l_(419593)

        _c_(419588, _n_(419587, "print", lambda: print), "This document has no curse words!")
        _l_(419589)
    else:
        _c_(419591, _n_(419590, "print", lambda: print), "Could not scan the document properly.")
        _l_(419592)

_c_(419597, _n_(419596, "read_text", lambda: read_text))
_l_(419598)