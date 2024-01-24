# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56847143/typeerror-not-supported-between-instances-of-builtin-function-or-method-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Yatzy:
    _l_(397046)

    def __init__(self, humans_num, bots_num):
        _l_(396943)

(...)
    @_n_(396944, "property", lambda: property)
    def players_scores(self):
        _l_(396995)

        scores = {}
        _l_(396945)
        for i in _c_(396951, _n_(396946, "range", lambda: range), _c_(396950, _n_(396947, "len", lambda: len), _a_(396949, _n_(396948, "self", lambda: self), "humans"))):
            _l_(396962)

            _n_(396952, "scores", lambda: scores)[_a_(396956, _a_(396954, _n_(396953, "self", lambda: self), "humans")[_n_(396955, "i", lambda: i)], "name")] = _a_(396960, _a_(396958, _n_(396957, "self", lambda: self), "humans")[_n_(396959, "i", lambda: i)], "total_score")
            _l_(396961)
        for i in _c_(396968, _n_(396963, "range", lambda: range), _c_(396967, _n_(396964, "len", lambda: len), _a_(396966, _n_(396965, "self", lambda: self), "bots"))):
            _l_(396979)

            _n_(396969, "scores", lambda: scores)[_a_(396973, _a_(396971, _n_(396970, "self", lambda: self), "bots")[_n_(396972, "i", lambda: i)], "name")] = _a_(396977, _a_(396975, _n_(396974, "self", lambda: self), "bots")[_n_(396976, "i", lambda: i)], "total_score")
            _l_(396978)
        _c_(396991, _n_(396980, "print", lambda: print), _c_(396985, _n_(396981, "type", lambda: type), _a_(396984, _a_(396983, _n_(396982, "self", lambda: self), "bots")[0], "name")), _c_(396990, _n_(396986, "type", lambda: type), _a_(396989, _a_(396988, _n_(396987, "self", lambda: self), "bots")[0], "total_score")))
        _l_(396992)
        aux = _n_(396993, "scores", lambda: scores)
        _l_(396994)
        return aux

    def game_loop(self):
        _l_(397045)

        _c_(396997, _n_(396996, "print", lambda: print), 'Welcome to Yatzy game!')
        _l_(396998)
        round_counter = 1
        _l_(396999)
        while _n_(397000, "round_counter", lambda: round_counter) <= _a_(397002, _n_(397001, "self", lambda: self), "MAX_ROUNDS"):
            _l_(397003)

(...)        _c_(397007, _n_(397004, "print", lambda: print), "Final score:", _a_(397006, _n_(397005, "self", lambda: self), "players_scores"))
        _l_(397008)
        _c_(397026, _n_(397009, "print", lambda: print), _c_(397013, _n_(397010, "type", lambda: type), _a_(397012, _n_(397011, "self", lambda: self), "players_scores")), _c_(397019, _n_(397014, "type", lambda: type), _c_(397018, _a_(397017, _a_(397016, _n_(397015, "self", lambda: self), "players_scores"), "keys"))), _c_(397025, _n_(397020, "type", lambda: type), _c_(397024, _a_(397023, _a_(397022, _n_(397021, "self", lambda: self), "players_scores"), "values"))))
        _l_(397027)
        best_player = _c_(397034, _n_(397028, "max", lambda: max), _a_(397030, _n_(397029, "self", lambda: self), "players_scores"), _a_(397033, _a_(397032, _n_(397031, "self", lambda: self), "players_scores"), "get"))
        _l_(397035)
        _c_(397043, _n_(397036, "print", lambda: print), _c_(397042, _a_(397037, "{} won with {}", "format"), _n_(397038, "best_player", lambda: best_player), _a_(397040, _n_(397039, "self", lambda: self), "players_scores")[_n_(397041, "best_player", lambda: best_player)]))
        _l_(397044)

game = _c_(397048, _n_(397047, "Yatzy", lambda: Yatzy), humans_num=0, bots_num=4)
_l_(397049)
_c_(397052, _a_(397051, _n_(397050, "game", lambda: game), "game_loop"))
_l_(397053)