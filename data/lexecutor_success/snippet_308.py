# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/104420/how-do-i-generate-all-permutations-of-a-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def getPermutations(array):
    _l_(1545433)

    if _c_(1545404, _n_(1545402, "len", lambda: len), _n_(1545403, "array", lambda: array)) == 1:
        _l_(1545407)

        aux = [_n_(1545405, "array", lambda: array)]
        _l_(1545406)
        return aux
    permutations = []
    _l_(1545408)
    for i in _c_(1545413, _n_(1545409, "range", lambda: range), _c_(1545412, _n_(1545410, "len", lambda: len), _n_(1545411, "array", lambda: array))):
        _l_(1545430)

        # get all perm's of subarray w/o current item
        perms = _c_(1545419, _n_(1545414, "getPermutations", lambda: getPermutations), _n_(1545415, "array", lambda: array)[:_n_(1545416, "i", lambda: i)] + _n_(1545417, "array", lambda: array)[_n_(1545418, "i", lambda: i)+1:])  
        _l_(1545420)  
        for p in _n_(1545421, "perms", lambda: perms):
            _l_(1545429)

            _c_(1545427, _a_(1545423, _n_(1545422, "permutations", lambda: permutations), "append"), [_n_(1545424, "array", lambda: array)[_n_(1545425, "i", lambda: i)], *_n_(1545426, "p", lambda: p)])
            _l_(1545428)
    aux = _n_(1545431, "permutations", lambda: permutations)
    _l_(1545432)
    return aux

def getPermutations(array):
    _l_(1545459)

    if _c_(1545436, _n_(1545434, "len", lambda: len), _n_(1545435, "array", lambda: array)) == 1:
        _l_(1545458)

        yield _n_(1545437, "array", lambda: array)
        _l_(1545438)
    else:
        for i in _c_(1545443, _n_(1545439, "range", lambda: range), _c_(1545442, _n_(1545440, "len", lambda: len), _n_(1545441, "array", lambda: array))):
            _l_(1545457)

            perms = _c_(1545449, _n_(1545444, "getPermutations", lambda: getPermutations), _n_(1545445, "array", lambda: array)[:_n_(1545446, "i", lambda: i)] + _n_(1545447, "array", lambda: array)[_n_(1545448, "i", lambda: i)+1:])
            _l_(1545450)
            for p in _n_(1545451, "perms", lambda: perms):
                _l_(1545456)

                yield [_n_(1545452, "array", lambda: array)[_n_(1545453, "i", lambda: i)], *_n_(1545454, "p", lambda: p)]
                _l_(1545455)

