# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56470356/cant-tell-why-im-getting-typeerror-cant-convert-int-object-to-str-implici
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def search(text_body, phrase):
    _l_(530644)

    count = 0
    _l_(530628)
    word_length = _c_(530631, _n_(530629, "len", lambda: len), _n_(530630, "phrase", lambda: phrase))
    _l_(530632)
    for i in _n_(530633, "text_body", lambda: text_body):
        _l_(530641)

        if _n_(530634, "phrase", lambda: phrase) == _n_(530635, "text_body", lambda: text_body)[_n_(530636, "i", lambda: i):_n_(530637, "i", lambda: i)+_n_(530638, "word_length", lambda: word_length)]:
            _l_(530640)

            count +=1 
            _l_(530639) 
    aux = _n_(530642, "count", lambda: count)
    _l_(530643)
    return aux

text_body = "text text text text text"
_l_(530645)
phrase = _c_(530647, _n_(530646, "input", lambda: input), "Search for: ")
_l_(530648)
final_count = _c_(530652, _n_(530649, "search", lambda: search), _n_(530650, "text_body", lambda: text_body), _n_(530651, "phrase", lambda: phrase))
_l_(530653)

_c_(530656, _n_(530654, "print", lambda: print), _n_(530655, "final_count", lambda: final_count))
_l_(530657)