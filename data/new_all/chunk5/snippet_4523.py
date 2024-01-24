# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56308858/typeerror-not-supported-between-instances-of-int-and-str-and-del-from-l
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
player_score = 3000
_l_(667261)
with _c_(667263, _n_(667262, "open", lambda: open), 'testscores.txt', 'r') as f:
    _l_(667340)

    for line in _n_(667264, "f", lambda: f):
        _l_(667269)

        highscores = _c_(667267, _a_(667266, _n_(667265, "line", lambda: line), "split"), ",")
        _l_(667268)
    _c_(667273, _a_(667271, _n_(667270, "highscores", lambda: highscores), "append"), _n_(667272, "player_score", lambda: player_score))
    _l_(667274)
    lowest_score = _c_(667277, _n_(667275, "int", lambda: int), _n_(667276, "highscores", lambda: highscores)[0])
    _l_(667278)
    for i in _c_(667283, _n_(667279, "range", lambda: range), 1, _c_(667282, _n_(667280, "len", lambda: len), _n_(667281, "highscores", lambda: highscores))):
        _l_(667295)

        if _c_(667287, _n_(667284, "int", lambda: int), _n_(667285, "highscores", lambda: highscores)[_n_(667286, "i", lambda: i)]) < _c_(667290, _n_(667288, "int", lambda: int), _n_(667289, "lowest_score", lambda: lowest_score)):
            _l_(667294)

            lowest_score = _n_(667291, "highscores", lambda: highscores)[_n_(667292, "i", lambda: i)]
            _l_(667293)
    lowest_score = _c_(667298, _n_(667296, "int", lambda: int), _n_(667297, "lowest_score", lambda: lowest_score))
    _l_(667299)
    del highscores[lowest_score]
    _l_(667300)
    highhelper = ''
    _l_(667301)
    for i in _c_(667306, _n_(667302, "range", lambda: range), 0, _c_(667305, _n_(667303, "len", lambda: len), _n_(667304, "highscores", lambda: highscores))-1):
        _l_(667312)

        highhelper += _c_(667310, _n_(667307, "str", lambda: str), _n_(667308, "highscores", lambda: highscores)[_n_(667309, "i", lambda: i)])+","
        _l_(667311)
    highhelper += _c_(667318, _n_(667313, "str", lambda: str), _n_(667314, "highscores", lambda: highscores)[_c_(667317, _n_(667315, "len", lambda: len), _n_(667316, "highscores", lambda: highscores))-1])
    _l_(667319)
    _c_(667322, _n_(667320, "print", lambda: print), _n_(667321, "highhelper", lambda: highhelper))
    _l_(667323)
    with _c_(667325, _n_(667324, "open", lambda: open), 'testscores.txt', 'w') as outF:
        _l_(667333)

        _c_(667331, _a_(667327, _n_(667326, "outF", lambda: outF), "write"), _c_(667330, _n_(667328, "str", lambda: str), _n_(667329, "highhelper", lambda: highhelper)))
        _l_(667332)
    _c_(667338, _n_(667334, "print", lambda: print), "kicking out score: "+_c_(667337, _n_(667335, "str", lambda: str), _n_(667336, "lowest_score", lambda: lowest_score)))
    _l_(667339)