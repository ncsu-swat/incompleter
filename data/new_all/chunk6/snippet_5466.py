# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35026280/curangle-throwing-this-error-typeerror-float-argument-must-be-a-string-or
    #Update the solar file for reporting
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
logsolar = _c_(343768, _n_(343767, "open", lambda: open), '/tools/inputs/solarvalues.txt','w')
_l_(343769)
writeline=("[myvars]\n")
_l_(343770)
_c_(343774, _a_(343772, _n_(343771, "logsolar", lambda: logsolar), "write"), _n_(343773, "writeline", lambda: writeline))
_l_(343775)
writeline=("solar_heading: " + _c_(343783, _n_(343776, "str", lambda: str), _c_(343782, _n_(343777, "round", lambda: round), _c_(343781, _n_(343778, "float", lambda: float), _c_(343780, _n_(343779, "getsolarheading", lambda: getsolarheading))),1)) + "\n")
_l_(343784)
_c_(343788, _a_(343786, _n_(343785, "logsolar", lambda: logsolar), "write"), _n_(343787, "writeline", lambda: writeline))
_l_(343789)
writeline=("solar_elevation: " + _c_(343797, _n_(343790, "str", lambda: str), _c_(343796, _n_(343791, "round", lambda: round), _c_(343795, _n_(343792, "float", lambda: float), _c_(343794, _n_(343793, "getsolarangle", lambda: getsolarangle))),1))+ "\n")
_l_(343798)
_c_(343802, _a_(343800, _n_(343799, "logsolar", lambda: logsolar), "write"), _n_(343801, "writeline", lambda: writeline))
_l_(343803)
writeline=("actual_elevation: " + _c_(343811, _n_(343804, "str", lambda: str), _c_(343810, _n_(343805, "round", lambda: round), _c_(343809, _n_(343806, "float", lambda: float), _c_(343808, _n_(343807, "getcurangle", lambda: getcurangle))),1))+ "\n")
_l_(343812)
_c_(343816, _a_(343814, _n_(343813, "logsolar", lambda: logsolar), "write"), _n_(343815, "writeline", lambda: writeline))
_l_(343817)
writeline=("actual_heading: " + _c_(343825, _n_(343818, "str", lambda: str), _c_(343824, _n_(343819, "round", lambda: round), _c_(343823, _n_(343820, "float", lambda: float), _c_(343822, _n_(343821, "getcurheading", lambda: getcurheading))),1))+ "\n")
_l_(343826)
_c_(343830, _a_(343828, _n_(343827, "logsolar", lambda: logsolar), "write"), _n_(343829, "writeline", lambda: writeline))
_l_(343831)
_c_(343834, _a_(343833, _n_(343832, "logsolar", lambda: logsolar), "close"))
_l_(343835)