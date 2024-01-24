# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55975955/attributeerror-tuple-object-has-no-attribute-translate
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
mycursor = _c_(547700, _a_(547699, _n_(547698, "mydb", lambda: mydb), "cursor"))
_l_(547701)
_c_(547704, _a_(547703, _n_(547702, "mycursor", lambda: mycursor), "execute"), "SELECT content FROM news_tb")
_l_(547705)
myresult = _c_(547708, _a_(547707, _n_(547706, "mycursor", lambda: mycursor), "fetchall"))
_l_(547709)
for row in _n_(547710, "myresult", lambda: myresult):
    _l_(547747)

    row = _c_(547720, _a_(547719, _c_(547718, _a_(547712, _n_(547711, "row", lambda: row), "translate"), _c_(547717, _a_(547714, _n_(547713, "str", lambda: str), "maketrans"), '', '', _a_(547716, _n_(547715, "string", lambda: string), "punctuation"))), "lower"))
    _l_(547721)


    tokens = _c_(547724, _n_(547722, "word_tokenize", lambda: word_tokenize), _n_(547723, "row", lambda: row))
    _l_(547725)
    listStopword = _c_(547730, _n_(547726, "set", lambda: set), _c_(547729, _a_(547728, _n_(547727, "stopwords", lambda: stopwords), "words"), 'indonesian'))
    _l_(547731)
    wordsFiltered = []
    _l_(547732)

    for t in _n_(547733, "tokens", lambda: tokens):
        _l_(547742)

        if _n_(547734, "t", lambda: t) not in _n_(547735, "listStopword", lambda: listStopword):
            _l_(547741)

            _c_(547739, _a_(547737, _n_(547736, "wordsFiltered", lambda: wordsFiltered), "append"), _n_(547738, "t", lambda: t))
            _l_(547740)
    _c_(547745, _n_(547743, "print", lambda: print), _n_(547744, "wordsFiltered", lambda: wordsFiltered))
    _l_(547746)