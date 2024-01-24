# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/19877064/typeerror-unsupported-operand-types-for-dict-keys-and-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_LEAST_GREATER_ODD = lambda x: (_n_(413534, "x", lambda: x) + 1) | 1
_l_(413535)
_LEAST_GREATER_EVEN = lambda x: (_n_(413536, "x", lambda: x) + 2) & ~1
_l_(413537)

X2_X5_MAPPINGS = {
    'RLE': (_n_(413538, "_LEAST_GREATER_ODD", lambda: _LEAST_GREATER_ODD), 'N'),
    'LRE': (_n_(413539, "_LEAST_GREATER_EVEN", lambda: _LEAST_GREATER_EVEN), 'N'),
    'RLO': (_n_(413540, "_LEAST_GREATER_ODD", lambda: _LEAST_GREATER_ODD), 'R'),
    'LRO': (_n_(413541, "_LEAST_GREATER_EVEN", lambda: _LEAST_GREATER_EVEN), 'L'),
}
_l_(413542)

# Added 'B' so X6 won't execute in that case and X8 will run its course
X6_IGNORED = _c_(413545, _a_(413544, _n_(413543, "X2_X5_MAPPINGS", lambda: X2_X5_MAPPINGS), "keys")) + ['BN', 'PDF', 'B']
_l_(413546)
X9_REMOVED = _c_(413549, _a_(413548, _n_(413547, "X2_X5_MAPPINGS", lambda: X2_X5_MAPPINGS), "keys")) + ['BN', 'PDF']
_l_(413550)