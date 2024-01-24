# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76690265/typeerror-a-bytes-like-object-is-required-not-str-when-trying-to-write-to-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(459238)

except ImportError:
    pass
try:
    import bz2
    _l_(459240)

except ImportError:
    pass
try:
    import csv
    _l_(459242)

except ImportError:
    pass
try:
    import traceback
    _l_(459244)

except ImportError:
    pass


tfile = '/tmp/test.csv.bz'
_l_(459245)
row = ['bc22jtr', 118324, None, 'contran', None, 11.5, 9.23, ]
_l_(459246)


def perr(err, bmode, fmode=None):
    _l_(459269)

    """Func for printing exception info in a less noisy manner."""
    _c_(459255, _n_(459247, "print", lambda: print), f"EXCEPTION: wt.writerow(row) → {_a_(459251, _c_(459250, _n_(459248, 'type', lambda: type), _n_(459249, 'err', lambda: err)), '__name__')}:"
        f" {_n_(459252, 'err', lambda: err)}; bmode='{_n_(459253, 'bmode', lambda: bmode)}', fmode='{_n_(459254, 'fmode', lambda: fmode)}'"
    )
    _l_(459256)
    _c_(459266, _n_(459257, "print", lambda: print), _c_(459265, _a_(459264, _c_(459263, _a_(459258, '', "join"), _c_(459262, _a_(459260, _n_(459259, "traceback", lambda: traceback), "format_exception"), _n_(459261, "err", lambda: err))[-2:-1]), "strip")))
    _l_(459267)
    aux = True
    _l_(459268)
    return aux


for fmode in ["w", "wt", "wb"]:
    _l_(459342)

    for bmode in ["w", "wb"]:
        _l_(459341)

        had_err = False
        _l_(459270)
        if _c_(459275, _a_(459273, _a_(459272, _n_(459271, "os", lambda: os), "path"), "exists"), _n_(459274, "tfile", lambda: tfile)):
            _l_(459281)

            _c_(459279, _a_(459277, _n_(459276, "os", lambda: os), "remove"), _n_(459278, "tfile", lambda: tfile))
            _l_(459280)
        fh = _c_(459285, _n_(459282, "open", lambda: open), _n_(459283, "tfile", lambda: tfile), _n_(459284, "fmode", lambda: fmode))
        _l_(459286)
        try:
            _l_(459301)

            bh = _c_(459291, _a_(459288, _n_(459287, "bz2", lambda: bz2), "BZ2File"), _n_(459289, "fh", lambda: fh), mode=_n_(459290, "bmode", lambda: bmode), compresslevel=9)
            _l_(459292)
        except _n_(459293, "ValueError", lambda: ValueError) as err:
            _l_(459300)

            had_err = _c_(459298, _n_(459294, "perr", lambda: perr), _n_(459295, "err", lambda: err), _n_(459296, "bmode", lambda: bmode), _n_(459297, "fmode", lambda: fmode))
            _l_(459299)
        wt = _c_(459305, _a_(459303, _n_(459302, "csv", lambda: csv), "writer"), _n_(459304, "fh", lambda: fh))
        _l_(459306)
        try:
            _l_(459320)

            _c_(459310, _a_(459308, _n_(459307, "wt", lambda: wt), "writerow"), _n_(459309, "row", lambda: row))
            _l_(459311)
        except _n_(459312, "TypeError", lambda: TypeError) as err:
            _l_(459319)

            had_err = _c_(459317, _n_(459313, "perr", lambda: perr), _n_(459314, "err", lambda: err), _n_(459315, "bmode", lambda: bmode), _n_(459316, "fmode", lambda: fmode))
            _l_(459318)
        try:
            _l_(459333)

            _c_(459323, _a_(459322, _n_(459321, "bh", lambda: bh), "close"))
            _l_(459324)
        except _n_(459325, "TypeError", lambda: TypeError) as err:
            _l_(459332)

            had_err = _c_(459330, _n_(459326, "perr", lambda: perr), _n_(459327, "err", lambda: err), _n_(459328, "bmode", lambda: bmode), _n_(459329, "fmode", lambda: fmode))
            _l_(459331)
        if not _n_(459334, "had_err", lambda: had_err):
            _l_(459340)

            _c_(459338, _n_(459335, "prnt", lambda: prnt), f"WAS OK: bmode={_n_(459336, 'bmode', lambda: bmode)}, fmode={_n_(459337, 'fmode', lambda: fmode)}")
            _l_(459339)
for bmode in ["w", "wb", "wt"]:
    _l_(459397)

    if _c_(459347, _a_(459345, _a_(459344, _n_(459343, "os", lambda: os), "path"), "exists"), _n_(459346, "tfile", lambda: tfile)):
        _l_(459353)

        _c_(459351, _a_(459349, _n_(459348, "os", lambda: os), "remove"), _n_(459350, "tfile", lambda: tfile))
        _l_(459352)
    bh = _c_(459358, _a_(459355, _n_(459354, "bz2", lambda: bz2), "open"), _n_(459356, "fh", lambda: fh), mode=_n_(459357, "bmode", lambda: bmode), compresslevel=9)
    _l_(459359)
    wt = _c_(459363, _a_(459361, _n_(459360, "csv", lambda: csv), "writer"), _n_(459362, "fh", lambda: fh))
    _l_(459364)
    had_err = False
    _l_(459365)
    try:
        _l_(459378)

        _c_(459369, _a_(459367, _n_(459366, "wt", lambda: wt), "writerow"), _n_(459368, "row", lambda: row))
        _l_(459370)
    except _n_(459371, "TypeError", lambda: TypeError) as err:
        _l_(459377)

        had_err = _c_(459375, _n_(459372, "perr", lambda: perr), _n_(459373, "err", lambda: err), _n_(459374, "bmode", lambda: bmode))
        _l_(459376)
    try:
        _l_(459390)

        _c_(459381, _a_(459380, _n_(459379, "bh", lambda: bh), "close"))
        _l_(459382)
    except _n_(459383, "TypeError", lambda: TypeError) as err:
        _l_(459389)

        had_err = _c_(459387, _n_(459384, "perr", lambda: perr), _n_(459385, "err", lambda: err), _n_(459386, "bmode", lambda: bmode))
        _l_(459388)
    if not _n_(459391, "had_err", lambda: had_err):
        _l_(459396)

        _c_(459394, _n_(459392, "prnt", lambda: prnt), f"WAS OK: bmode={_n_(459393, 'bmode', lambda: bmode)}")
        _l_(459395)
if _c_(459402, _a_(459400, _a_(459399, _n_(459398, "os", lambda: os), "path"), "exists"), _n_(459401, "tfile", lambda: tfile)):
    _l_(459408)

    _c_(459406, _a_(459404, _n_(459403, "os", lambda: os), "remove"), _n_(459405, "tfile", lambda: tfile))
    _l_(459407)