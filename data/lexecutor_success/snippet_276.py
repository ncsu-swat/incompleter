# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data = [
('betty', 1),
('bought', 1),
('a', 1),
('bit', 1),
('of', 1),
('butter', 2),
('but', 1),
('the', 1),
('was', 1),
('bitter', 1)]
_l_(1538898)

_c_(1538903, _n_(1538899, "sorted", lambda: sorted), _n_(1538900, "data", lambda: data), key=lambda tup:(-_n_(1538901, "tup", lambda: tup)[1], _n_(1538902, "tup", lambda: tup)[0]))
_l_(1538904)

[('butter', 2),
('a', 1),
('betty', 1),
('bit', 1),
('bitter', 1),
('bought', 1),
('but', 1),
('of', 1),
('the', 1),
('was', 1)]
_l_(1538905)

