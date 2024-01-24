# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/7447284/how-to-troubleshoot-an-attributeerror-exit-in-multiproccesing-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(401617)

except ImportError:
    pass
try:
    import time
    _l_(401619)

except ImportError:
    pass
try:
    import datetime
    _l_(401621)

except ImportError:
    pass
try:
    import re
    _l_(401623)

except ImportError:
    pass
try:
    from operator import itemgetter
    _l_(401625)

except ImportError:
    pass
try:
    from multiprocessing import Pool
    _l_(401627)

except ImportError:
    pass
try:
    import itertools
    _l_(401629)

except ImportError:
    pass

def chunks(l,n):
    _l_(401648)

    """Divide a list of nodes `l` in `n` chunks"""
    l_c = _c_(401632, _n_(401630, "iter", lambda: iter), _n_(401631, "l", lambda: l))
    _l_(401633)
    while 1:
        _l_(401647)

        x = _c_(401640, _n_(401634, "tuple", lambda: tuple), _c_(401639, _a_(401636, _n_(401635, "itertools", lambda: itertools), "islice"), _n_(401637, "l_c", lambda: l_c),_n_(401638, "n", lambda: n)))
        _l_(401641)
        if not _n_(401642, "x", lambda: x):
            _l_(401644)

            aux = ""
            _l_(401643)
            return aux
        yield _n_(401645, "x", lambda: x)
        _l_(401646)

def csv2nodes(r):
    _l_(401706)

    strptime = _a_(401650, _n_(401649, "time", lambda: time), "strptime")
    _l_(401651)
    mktime = _a_(401653, _n_(401652, "time", lambda: time), "mktime")
    _l_(401654)
    l = []
    _l_(401655)
    ppl = _c_(401657, _n_(401656, "set", lambda: set))
    _l_(401658)
    pattern = _c_(401661, _a_(401660, _n_(401659, "re", lambda: re), "compile"), r"""[A-Za-z0-9"/]+?(?=[,\n])""")
    _l_(401662)
    for row in _n_(401663, "r", lambda: r):
        _l_(401702)

        with _c_(401667, _a_(401665, _n_(401664, "pattern", lambda: pattern), "findall"), _n_(401666, "row", lambda: row)) as f:
            _l_(401688)

            cell = _c_(401670, _n_(401668, "int", lambda: int), _n_(401669, "f", lambda: f)[3])
            _l_(401671)
            id = _c_(401674, _n_(401672, "int", lambda: int), _n_(401673, "f", lambda: f)[2])
            _l_(401675)
            st = _c_(401680, _n_(401676, "mktime", lambda: mktime), _c_(401679, _n_(401677, "strptime", lambda: strptime), _n_(401678, "f", lambda: f)[0],'%d/%m/%Y'))
            _l_(401681)
            ed = _c_(401686, _n_(401682, "mktime", lambda: mktime), _c_(401685, _n_(401683, "strptime", lambda: strptime), _n_(401684, "f", lambda: f)[1],'%d/%m/%Y'))
            _l_(401687)
        # collect list
        _c_(401695, _a_(401690, _n_(401689, "l", lambda: l), "append"), [(_n_(401691, "id", lambda: id),_n_(401692, "cell", lambda: cell),{1:_n_(401693, "st", lambda: st),2: _n_(401694, "ed", lambda: ed)})])
        _l_(401696)
        # collect separate sets
        _c_(401700, _a_(401698, _n_(401697, "ppl", lambda: ppl), "add"), _n_(401699, "id", lambda: id))
        _l_(401701)
    aux = (_n_(401703, "l", lambda: l),_n_(401704, "ppl", lambda: ppl))
    _l_(401705)
    return aux

def csv2graph(source):
    _l_(401767)

    MG=_c_(401709, _a_(401708, _n_(401707, "nx", lambda: nx), "MultiGraph"))
    _l_(401710)
    # Remember that I use integers for edge attributes, to save space! Dic above.
    # start: 1
    # end: 2
    p = _c_(401712, _n_(401711, "Pool", lambda: Pool))
    _l_(401713)
    node_divisor = _c_(401717, _n_(401714, "len", lambda: len), _a_(401716, _n_(401715, "p", lambda: p), "_pool"))
    _l_(401718)
    node_chunks = _c_(401731, _n_(401719, "list", lambda: list), _c_(401730, _n_(401720, "chunks", lambda: chunks), _n_(401721, "source", lambda: source),_c_(401729, _n_(401722, "int", lambda: int), _c_(401725, _n_(401723, "len", lambda: len), _n_(401724, "source", lambda: source))/_c_(401728, _n_(401726, "int", lambda: int), _n_(401727, "node_divisor", lambda: node_divisor)))))
    _l_(401732)
    num_chunks = _c_(401735, _n_(401733, "len", lambda: len), _n_(401734, "node_chunks", lambda: node_chunks))
    _l_(401736)
    pedgelists = _c_(401741, _a_(401738, _n_(401737, "p", lambda: p), "map"), _n_(401739, "csv2nodes", lambda: csv2nodes),
                       _n_(401740, "node_chunks", lambda: node_chunks))
    _l_(401742)
    ll = []
    _l_(401743)
    ppl = _c_(401745, _n_(401744, "set", lambda: set))
    _l_(401746)
    for l in _n_(401747, "pedgelists", lambda: pedgelists):
        _l_(401758)

        _c_(401751, _a_(401749, _n_(401748, "ll", lambda: ll), "append"), _n_(401750, "l", lambda: l)[0])
        _l_(401752)
        _c_(401756, _a_(401754, _n_(401753, "ppl", lambda: ppl), "update"), _n_(401755, "l", lambda: l)[1])
        _l_(401757)
    _c_(401762, _a_(401760, _n_(401759, "MG", lambda: MG), "add_edges_from"), _n_(401761, "ll", lambda: ll))
    _l_(401763)
    aux = (_n_(401764, "MG", lambda: MG),_n_(401765, "ppl", lambda: ppl))
    _l_(401766)
    return aux

with _c_(401769, _n_(401768, "open", lambda: open), '/Users/laszlosandor/Dropbox/peers_prisons/python/codetenus_test.txt','r') as source:
    _l_(401778)

    r = _c_(401772, _a_(401771, _n_(401770, "source", lambda: source), "readlines"))
    _l_(401773)
    MG,ppl = _c_(401776, _n_(401774, "csv2graph", lambda: csv2graph), _n_(401775, "r", lambda: r))
    _l_(401777)