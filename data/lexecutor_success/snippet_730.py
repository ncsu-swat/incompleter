# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import glob
    _l_(1538651)

except ImportError:
    pass
try:
    import re
    _l_(1538653)

except ImportError:
    pass

mapfile = _c_(1538655, _n_(1538654, "input", lambda: input), "Enter map file name with extension eg. codifica.txt: ")
_l_(1538656)
sep = _c_(1538658, _n_(1538657, "input", lambda: input), "Enter map file column separator eg. |: ")
_l_(1538659)
mask = _c_(1538661, _n_(1538660, "input", lambda: input), "Enter search mask with extension eg. 2010*txt for all files to be processed: ")
_l_(1538662)
suff = _c_(1538664, _n_(1538663, "input", lambda: input), "Enter suffix with extension eg. _NEW.txt for newly generated files: ")
_l_(1538665)

rep = {} # creation of empy dictionary
_l_(1538666) # creation of empy dictionary

with _c_(1538669, _n_(1538667, "open", lambda: open), _n_(1538668, "mapfile", lambda: mapfile)) as temprep:
    _l_(1538683)

    for line in _n_(1538670, "temprep", lambda: temprep):
        _l_(1538682)

        (key, val) = _c_(1538676, _a_(1538674, _c_(1538673, _a_(1538672, _n_(1538671, "line", lambda: line), "strip"), '\n'), "split"), _n_(1538675, "sep", lambda: sep))
        _l_(1538677)
        _n_(1538678, "rep", lambda: rep)[_n_(1538679, "key", lambda: key)] = _n_(1538680, "val", lambda: val)
        _l_(1538681)

for filename in _c_(1538687, _a_(1538685, _n_(1538684, "glob", lambda: glob), "iglob"), _n_(1538686, "mask", lambda: mask)):
    _l_(1538727)


    with _c_(1538690, _n_(1538688, "open", lambda: open), _n_(1538689, "filename", lambda: filename), "r") as textfile:
        _l_(1538726)

        text = _c_(1538693, _a_(1538692, _n_(1538691, "textfile", lambda: textfile), "read"))
        _l_(1538694)

        # start replacement
        #rep = dict((re.escape(k), v) for k, v in rep.items()) commented to enable the use in the mapping of re reserved characters
        pattern = _c_(1538702, _a_(1538696, _n_(1538695, "re", lambda: re), "compile"), _c_(1538701, _a_(1538697, "|", "join"), _c_(1538700, _a_(1538699, _n_(1538698, "rep", lambda: rep), "keys"))))
        _l_(1538703)
        text = _c_(1538711, _a_(1538705, _n_(1538704, "pattern", lambda: pattern), "sub"), lambda m: _n_(1538706, "rep", lambda: rep)[_c_(1538709, _a_(1538708, _n_(1538707, "m", lambda: m), "group"), 0)], _n_(1538710, "text", lambda: text))
        _l_(1538712)

        #write of te output files with the prompted suffice
        target = _c_(1538715, _n_(1538713, "open", lambda: open), _n_(1538714, "filename", lambda: filename)[:-4]+"_NEW.txt", "w")
        _l_(1538716)
        _c_(1538720, _a_(1538718, _n_(1538717, "target", lambda: target), "write"), _n_(1538719, "text", lambda: text))
        _l_(1538721)
        _c_(1538724, _a_(1538723, _n_(1538722, "target", lambda: target), "close"))
        _l_(1538725)

