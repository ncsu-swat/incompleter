# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62139108/why-is-powershell-constantly-giving-me-an-attributeerror-for-this-class-based-pr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Song(_n_(656378, "object", lambda: object)):
    _l_(656391)


    def __init__(self, lyrics):
        _l_(656390)

        _n_(656379, "self", lambda: self).lyrics = _n_(656380, "lyrics", lambda: lyrics)
        _l_(656381)

        def sing_me_a_song(self):
            _l_(656389)

            for line in _a_(656383, _n_(656382, "self", lambda: self), "lyrics"):
                _l_(656388)

                _c_(656386, _n_(656384, "print", lambda: print), _n_(656385, "line", lambda: line))
                _l_(656387)

happy_bday = _c_(656393, _n_(656392, "Song", lambda: Song), ["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
_l_(656394)

bulls_on_parade = _c_(656396, _n_(656395, "Song", lambda: Song), ["They rally around tha family",
                        "With pockets full of shells"])
_l_(656397)

_c_(656400, _a_(656399, _n_(656398, "happy_bday", lambda: happy_bday), "sing_me_a_song"))
_l_(656401)

_c_(656404, _a_(656403, _n_(656402, "bulls_on_parade", lambda: bulls_on_parade), "sing_me_a_song"))
_l_(656405)