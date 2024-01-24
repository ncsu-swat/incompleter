# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/22121108/encoding-type-error-python-3-x
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
inputfilename = "a.txt"
_l_(391032)
outputfilename = _n_(391033, "inputfilename", lambda: inputfilename)[0:-4]+"_fixed"+".txt"
_l_(391034)

inputfile = _c_(391037, _n_(391035, "open", lambda: open), _n_(391036, "inputfilename", lambda: inputfilename), 'r')
_l_(391038)

str = _c_(391041, _a_(391040, _n_(391039, "inputfile", lambda: inputfile), "read")) #name for the file
_l_(391042) #name for the file

newstring = _c_(391059, _a_(391058, _c_(391057, _a_(391056, _c_(391055, _a_(391054, _c_(391053, _a_(391052, _c_(391051, _a_(391050, _c_(391049, _a_(391048, _c_(391047, _a_(391046, _c_(391045, _a_(391044, _n_(391043, "str", lambda: str), "replace"), "œ", "s"), "replace"), "ê","e"), "replace"), "³","l"), "replace"), "¹","a"), "replace"), "¿","z"), "replace"), "ñ","n"), "replace"), "Ÿ","z"), "replace"), "æ","c")
_l_(391060)

outputfile = _c_(391063, _n_(391061, "open", lambda: open), _n_(391062, "outputfilename", lambda: outputfilename), "w")
_l_(391064)
_c_(391068, _a_(391066, _n_(391065, "outputfile", lambda: outputfile), "write"), _n_(391067, "newstring", lambda: newstring))
_l_(391069)
_c_(391072, _a_(391071, _n_(391070, "outputfile", lambda: outputfile), "close"))
_l_(391073)