# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50146402/why-is-this-nameerror-happening
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib
    _l_(532662)

except ImportError:
    pass


def read_text():
    _l_(532682)

    quotes = _c_(532664, _n_(532663, "open", lambda: open), "C:\\Udacity Python\\Lesson 4\\movie_quotes.txt", "r")
    _l_(532665)
    contents = _c_(532668, _a_(532667, _n_(532666, "quotes", lambda: quotes), "read"))
    _l_(532669)
    _c_(532672, _n_(532670, "print", lambda: print), _n_(532671, "contents", lambda: contents))
    _l_(532673)
    _c_(532676, _a_(532675, _n_(532674, "quotes", lambda: quotes), "close"))
    _l_(532677)
    _c_(532680, _n_(532678, "check_profanity", lambda: check_profanity), _n_(532679, "contents", lambda: contents))
    _l_(532681)


_c_(532684, _n_(532683, "read_text", lambda: read_text))
_l_(532685)


def check_profanity(contents_of_file):
    _l_(532706)

    text_to_check = _a_(532687, _n_(532686, "read_text", lambda: read_text), "contents_of_file")
    _l_(532688)
    connection = _c_(532692, _a_(532690, _n_(532689, "urllib", lambda: urllib), "urlopen"), "http://www.wdylike.appspot.com/?q="+_n_(532691, "text_to_check", lambda: text_to_check))
    _l_(532693)
    output = _c_(532696, _a_(532695, _n_(532694, "connection", lambda: connection), "read"))
    _l_(532697)
    _c_(532700, _n_(532698, "print", lambda: print), _n_(532699, "output", lambda: output))
    _l_(532701)
    _c_(532704, _a_(532703, _n_(532702, "connection", lambda: connection), "close"))
    _l_(532705)


_c_(532708, _n_(532707, "check_profanity", lambda: check_profanity))
_l_(532709)