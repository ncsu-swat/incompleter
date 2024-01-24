# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/25985508/typeerror-argument-of-type-nonetype-is-not-iterable-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(471216)

except ImportError:
    pass
def CreateDictionary ():
    _l_(471234)

    fo = _c_(471218, _n_(471217, "open", lambda: open), "textToEnglish2014.csv" , "r")
    _l_(471219)
    dictonary = {}
    _l_(471220)
    reader = _c_(471224, _a_(471222, _n_(471221, "csv", lambda: csv), "reader"), _n_(471223, "fo", lambda: fo))
    _l_(471225)
    for row in _n_(471226, "reader", lambda: reader):
        _l_(471233)

        _n_(471227, "dictionary", lambda: dictionary)[_n_(471228, "row", lambda: row)[0]] = _n_(471229, "row", lambda: row)[1]
        _l_(471230)
        aux = _n_(471231, "dictionary", lambda: dictionary)
        _l_(471232)
        return aux

def main():
    _l_(471278)

    dictionary = _c_(471236, _n_(471235, "CreateDictionary", lambda: CreateDictionary))
    _l_(471237)
    y = "y"
    _l_(471238)
    while _n_(471239, "y", lambda: y) == "y":
        _l_(471277)

        text = _c_(471241, _n_(471240, "input", lambda: input), "Enter text to which you would like conversion: ")
        _l_(471242)
        text = _c_(471245, _a_(471244, _n_(471243, "text", lambda: text), "lower"))
        _l_(471246)
        ntext = _c_(471249, _a_(471248, _n_(471247, "text", lambda: text), "split"), " ")
        _l_(471250)
        new_text = ""
        _l_(471251)
        x = 0
        _l_(471252)
        while _n_(471253, "x", lambda: x) < _c_(471256, _n_(471254, "len", lambda: len), _n_(471255, "ntext", lambda: ntext)):
            _l_(471269)

            if _n_(471257, "ntext", lambda: ntext)[_n_(471258, "x", lambda: x)] in _n_(471259, "dictionary", lambda: dictionary):
                _l_(471267)

                new_text = _n_(471260, "new_text", lambda: new_text) + _n_(471261, "dictionary", lambda: dictionary)[_n_(471262, "ntext", lambda: ntext)[_n_(471263, "x", lambda: x)]] + " "
                _l_(471264)
            else:
                export = _n_(471265, "export", lambda: export) + "NF "
                _l_(471266)
            x += 1
            _l_(471268)
        _c_(471272, _n_(471270, "print", lambda: print), _n_(471271, "new_text", lambda: new_text))
        _l_(471273)
        y = _c_(471275, _n_(471274, "input", lambda: input), "Continue conversion? y or q ")
        _l_(471276)

_c_(471280, _n_(471279, "main", lambda: main))
_l_(471281)