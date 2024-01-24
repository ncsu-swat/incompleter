# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61537231/what-could-cause-this-error-filenotfounderror-errno-2-no-such-file-or-direc
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pathlib
    _l_(653803)

except ImportError:
    pass

directory = _c_(653806, _a_(653805, _n_(653804, "pathlib", lambda: pathlib), "Path"), '/Users/karl/files/Code')
_l_(653807)

stats ={}
_l_(653808)

for path in _c_(653811, _a_(653810, _n_(653809, "directory", lambda: directory), "iterdir")):
    _l_(653846)

    file = _c_(653816, _n_(653812, "open", lambda: open), _c_(653815, _n_(653813, "str", lambda: str), _n_(653814, "path", lambda: path)))
    _l_(653817)
    text = _c_(653822, _a_(653821, _c_(653820, _a_(653819, _n_(653818, "file", lambda: file), "read")), "lower"))
    _l_(653823)

    punctuation  = (";", ".")
    _l_(653824)
    for mark in _n_(653825, "punctuation", lambda: punctuation):
        _l_(653831)

        text = _c_(653829, _a_(653827, _n_(653826, "text", lambda: text), "replace"), _n_(653828, "mark", lambda: mark), "")
        _l_(653830)


    for word in _a_(653833, _n_(653832, "text", lambda: text), "split"):
        _l_(653845)

        if _n_(653834, "word", lambda: word) in _n_(653835, "stats", lambda: stats):
            _l_(653844)


            _n_(653836, "stats", lambda: stats)[_n_(653837, "word", lambda: word)] = _n_(653838, "stats", lambda: stats)[_n_(653839, "word", lambda: word)] + 1
            _l_(653840)
        else:
            _n_(653841, "stats", lambda: stats)[_n_(653842, "word", lambda: word)] = 1
            _l_(653843)

most_used_word = None
_l_(653847)
score_max = 0
_l_(653848)
for word, score in _c_(653851, _a_(653850, _n_(653849, "stats", lambda: stats), "items")):
    _l_(653859)

    if _n_(653852, "score", lambda: score) > _n_(653853, "score_max", lambda: score_max):
        _l_(653858)

        score_max = _n_(653854, "score", lambda: score)
        _l_(653855)
        most_used_word = _n_(653856, "word", lambda: word)
        _l_(653857)

_c_(653863, _n_(653860, "print", lambda: print), _n_(653861, "word", lambda: word),"The most used word is : ", _n_(653862, "score_max", lambda: score_max)) 
_l_(653864) 