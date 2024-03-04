# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1059559/split-strings-into-words-with-multiple-word-boundary-delimiters
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
join = lambda x: _c_(62351, _n_(62349, "sum", lambda: sum), _n_(62350, "x", lambda: x),[])  # a.k.a. flatten1([[1],[2,3],[4]]) -> [1,2,3,4]
_l_(62352)  # a.k.a. flatten1([[1],[2,3],[4]]) -> [1,2,3,4]
# ...alternatively...
join = lambda lists: [_n_(62353, "x", lambda: x) for l in _n_(62354, "lists", lambda: lists) for x in _n_(62355, "l", lambda: l)]
_l_(62356)

fragments = [_n_(62357, "text", lambda: text)]
_l_(62358)
for token in _n_(62359, "tokens", lambda: tokens):
    _l_(62368)

    fragments = _c_(62366, _n_(62360, "join", lambda: join), (_c_(62364, _a_(62362, _n_(62361, "f", lambda: f), "split"), _n_(62363, "token", lambda: token)) for f in _n_(62365, "fragments", lambda: fragments)))
    _l_(62367)

