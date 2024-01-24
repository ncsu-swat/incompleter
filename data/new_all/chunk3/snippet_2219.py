# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57371575/attributeerror-word-application-documents-with-win32-com-in-a-flask-application
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import string
    _l_(536728)

except ImportError:
    pass
try:
    import win32com.client
    _l_(536730)

except ImportError:
    pass
try:
    import nltk
    _l_(536732)

except ImportError:
    pass
try:
    import os
    _l_(536734)

except ImportError:
    pass
try:
    from collections import Counter
    _l_(536736)

except ImportError:
    pass
try:
    from pywintypes import com_error
    _l_(536738)

except ImportError:
    pass
try:
    from flask import request, Flask, render_template, jsonify
    _l_(536740)

except ImportError:
    pass

word = _c_(536743, _a_(536742, _a_(536741, win32com, "client"), "Dispatch"), "Word.Application")
_l_(536744)
_n_(536745, "word", lambda: word).Visible = False
_l_(536746)

app = _c_(536749, _n_(536747, "Flask", lambda: Flask), _n_(536748, "__name__", lambda: __name__))
_l_(536750)
@_c_(536753, _a_(536752, _n_(536751, "app", lambda: app), "route"), '/')
def landingPage():
    _l_(536757)

    aux = _c_(536755, _n_(536754, "render_template", lambda: render_template), 'homepage.html')
    _l_(536756)
    return aux

@_c_(536760, _a_(536759, _n_(536758, "app", lambda: app), "route"), '/tokenizeDoc', methods = ['GET'])
def tokenizer():
    _l_(536829)

    if _a_(536762, _n_(536761, "request", lambda: request), "method") == 'GET':
        _l_(536828)

        pathToProc = _c_(536766, _a_(536765, _a_(536764, _n_(536763, "request", lambda: request), "values"), "get"), "doc")
        _l_(536767)
        sent_tokenizer = _c_(536771, _a_(536770, _a_(536769, _n_(536768, "nltk", lambda: nltk), "data"), "load"), 'tokenizers/punkt/italian.pickle')
        _l_(536772)
        it_stop_words = _c_(536777, _a_(536776, _a_(536775, _a_(536774, _n_(536773, "nltk", lambda: nltk), "corpus"), "stopwords"), "words"), 'italian') + ['\n', '\t', '']
        _l_(536778)
        trashes = _n_(536779, "it_stop_words", lambda: it_stop_words) + _c_(536783, _n_(536780, "list", lambda: list), _a_(536782, _n_(536781, "string", lambda: string), "punctuation"))
        _l_(536784)
        tokensTOT = []
        _l_(536785)
        try:
            _l_(536826)

            myDoc = _c_(536790, _a_(536788, _a_(536787, _n_(536786, "word", lambda: word), "Documents"), "Open"), _n_(536789, "pathToProc", lambda: pathToProc), False, False, True) #ERROR!!!
            _l_(536791) #ERROR!!!
            sentences = _c_(536799, _a_(536793, _n_(536792, "sent_tokenizer", lambda: sent_tokenizer), "tokenize"), _a_(536798, _c_(536797, _a_(536796, _a_(536795, _n_(536794, "word", lambda: word), "ActiveDocument"), "Range")), "Text"))
            _l_(536800)
            _c_(536803, _a_(536802, _n_(536801, "myDoc", lambda: myDoc), "Close"))
            _l_(536804)
            del myDoc
            _l_(536805)
            for sentence in _n_(536806, "sentences", lambda: sentences):
                _l_(536820)

                tokensTOT = _n_(536807, "tokensTOT", lambda: tokensTOT) + [_c_(536810, _a_(536809, _n_(536808, "t", lambda: t), "lower")) for t in _c_(536814, _a_(536812, _n_(536811, "nltk", lambda: nltk), "word_tokenize"), _n_(536813, "sentence", lambda: sentence)) 
                                         if _c_(536817, _a_(536816, _n_(536815, "t", lambda: t), "lower")) not in _n_(536818, "trashes", lambda: trashes)]
                _l_(536819)
        except _n_(536821, "com_error", lambda: com_error):
            _l_(536825)

            _c_(536823, _n_(536822, "print", lambda: print), 'IMPOSSIBILE DECIFRARE IL FILE')
            _l_(536824)
        aux = ''
        _l_(536827)
        return aux