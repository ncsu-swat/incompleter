# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56308858/typeerror-not-supported-between-instances-of-int-and-str-and-del-from-l
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
player_score = 3000
_l_(658000)
with _c_(658002, _n_(658001, "open", lambda: open), 'testscores.txt', 'r') as f:
    _l_(658079)

    for line in _n_(658003, "f", lambda: f):
        _l_(658008)

        highscores = _c_(658006, _a_(658005, _n_(658004, "line", lambda: line), "split"), ",")
        _l_(658007)
    _c_(658012, _a_(658010, _n_(658009, "highscores", lambda: highscores), "append"), _n_(658011, "player_score", lambda: player_score))
    _l_(658013)
    lowest_score = _c_(658016, _n_(658014, "int", lambda: int), _n_(658015, "highscores", lambda: highscores)[0])
    _l_(658017)
    for i in _c_(658022, _n_(658018, "range", lambda: range), 1, _c_(658021, _n_(658019, "len", lambda: len), _n_(658020, "highscores", lambda: highscores))):
        _l_(658034)

        if _c_(658026, _n_(658023, "int", lambda: int), _n_(658024, "highscores", lambda: highscores)[_n_(658025, "i", lambda: i)]) < _c_(658029, _n_(658027, "int", lambda: int), _n_(658028, "lowest_score", lambda: lowest_score)):
            _l_(658033)

            lowest_score = _n_(658030, "highscores", lambda: highscores)[_n_(658031, "i", lambda: i)]
            _l_(658032)
    lowest_score = _c_(658037, _n_(658035, "int", lambda: int), _n_(658036, "lowest_score", lambda: lowest_score))
    _l_(658038)
    del highscores[lowest_score]
    _l_(658039)
    highhelper = ''
    _l_(658040)
    for i in _c_(658045, _n_(658041, "range", lambda: range), 0, _c_(658044, _n_(658042, "len", lambda: len), _n_(658043, "highscores", lambda: highscores))-1):
        _l_(658051)

        highhelper += _c_(658049, _n_(658046, "str", lambda: str), _n_(658047, "highscores", lambda: highscores)[_n_(658048, "i", lambda: i)])+","
        _l_(658050)
    highhelper += _c_(658057, _n_(658052, "str", lambda: str), _n_(658053, "highscores", lambda: highscores)[_c_(658056, _n_(658054, "len", lambda: len), _n_(658055, "highscores", lambda: highscores))-1])
    _l_(658058)
    _c_(658061, _n_(658059, "print", lambda: print), _n_(658060, "highhelper", lambda: highhelper))
    _l_(658062)
    with _c_(658064, _n_(658063, "open", lambda: open), 'testscores.txt', 'w') as outF:
        _l_(658072)

        _c_(658070, _a_(658066, _n_(658065, "outF", lambda: outF), "write"), _c_(658069, _n_(658067, "str", lambda: str), _n_(658068, "highhelper", lambda: highhelper)))
        _l_(658071)
    _c_(658077, _n_(658073, "print", lambda: print), "kicking out score: "+_c_(658076, _n_(658074, "str", lambda: str), _n_(658075, "lowest_score", lambda: lowest_score)))
    _l_(658078)