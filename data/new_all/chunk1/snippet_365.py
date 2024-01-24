# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67212594/attributeerror-pathdistribution-object-has-no-attribute-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(382869)

except ImportError:
    pass
try:
    import json
    _l_(382871)

except ImportError:
    pass
try:
    import spacy
    _l_(382873)

except ImportError:
    pass
try:
    import logging
    _l_(382875)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(382877)

except ImportError:
    pass
try:
    from celeryapp import app
    _l_(382879)

except ImportError:
    pass

sp = _c_(382882, _a_(382881, _n_(382880, "spacy", lambda: spacy), "load"), 'en_core_web_sm')
_l_(382883)

@_c_(382886, _a_(382885, _n_(382884, "app", lambda: app), "task"), bind=True)
def extract(self, filename):
    _l_(382907)

    file_path = _c_(382894, _a_(382889, _a_(382888, _n_(382887, "os", lambda: os), "path"), "join"), _c_(382892, _a_(382891, _n_(382890, "os", lambda: os), "getcwd")), 'data', _n_(382893, "filename", lambda: filename))
    _l_(382895)
    doc = _c_(382900, _a_(382899, _c_(382898, _n_(382896, "open", lambda: open), _n_(382897, "file_path", lambda: file_path)), "read"))
    _l_(382901)
    _c_(382903, _n_(382902, "print", lambda: print), 'Extract called')
    _l_(382904)
    aux = _n_(382905, "doc", lambda: doc)
    _l_(382906)
    return aux

@_c_(382910, _a_(382909, _n_(382908, "app", lambda: app), "task"), bind=True)
def transform_tokenize_doc(self, doc:_n_(382911, "str", lambda: str)):
    _l_(382929)

    sentences = []
    _l_(382912)

    for sent in _a_(382916, _c_(382915, _n_(382913, "sp", lambda: sp), _n_(382914, "doc", lambda: doc)), "sents"):
        _l_(382926)

        _c_(382924, _a_(382918, _n_(382917, "sentences", lambda: sentences), "append"), _c_(382923, _a_(382922, _c_(382921, _n_(382919, "str", lambda: str), _n_(382920, "sent", lambda: sent)), "strip")))
        _l_(382925)
    aux = _n_(382927, "sentences", lambda: sentences)
    _l_(382928)

    return aux

@_c_(382932, _a_(382931, _n_(382930, "app", lambda: app), "task"), bind=True)
def load(self, filename, *args):
    _l_(382952)

    with _c_(382942, _n_(382933, "open", lambda: open), _c_(382941, _a_(382936, _a_(382935, _n_(382934, "os", lambda: os), "path"), "join"), _c_(382939, _a_(382938, _n_(382937, "os", lambda: os), "getcwd")), 'output', _n_(382940, "filename", lambda: filename)), 'a+') as file:
        _l_(382951)

        _c_(382949, _a_(382944, _n_(382943, "file", lambda: file), "write"), _c_(382948, _a_(382946, _n_(382945, "json", lambda: json), "dumps"), _n_(382947, "args", lambda: args), indent=4))
        _l_(382950)


if _n_(382953, "__name__", lambda: __name__) == '__main__':
    _l_(382995)

    tasks = []
    _l_(382954)

    for filename in _c_(382964, _a_(382956, _n_(382955, "os", lambda: os), "listdir"), _c_(382963, _a_(382959, _a_(382958, _n_(382957, "os", lambda: os), "path"), "join"), _c_(382962, _a_(382961, _n_(382960, "os", lambda: os), "getcwd")), 'data'))[:10]:
        _l_(382988)

        _c_(382967, _n_(382965, "print", lambda: print), f'filename is {_n_(382966, "filename", lambda: filename)}')
        _l_(382968)
        etl = _c_(382981, _a_(382980, (_c_(382972, _a_(382970, _n_(382969, 'extract', lambda: extract), 's'), _n_(382971, 'filename', lambda: filename)) | _c_(382975, _a_(382974, _n_(382973, 'transform_tokenize_doc', lambda: transform_tokenize_doc), 's')) | _c_(382979, _a_(382977, _n_(382976, 'load', lambda: load), 's'), _n_(382978, 'filename', lambda: filename))), 'apply_async'))
        _l_(382982)
        _c_(382986, _a_(382984, _n_(382983, 'tasks', lambda: tasks), 'append'), _n_(382985, 'etl', lambda: etl))
        _l_(382987)

    for task in _n_(382989, 'tasks', lambda: tasks):
        _l_(382994)

        _c_(382992, _a_(382991, _n_(382990, 'task', lambda: task), 'get'))
        _l_(382993)