# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/19104771/attribute-error-none-type-object-has-no-attribute-insert-inserting-into-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(605672)

except ImportError:
    pass
try:
    from tkinter.ttk import *
    _l_(605674)

except ImportError:
    pass
try:
    import math, os
    _l_(605676)

except ImportError:
    pass

try:
    _l_(605684)

    _c_(605679, _a_(605678, _n_(605677, "os", lambda: os), "remove"), "temp.txt")
    _l_(605680)
except _n_(605681, "OSError", lambda: OSError):
    _l_(605683)

    pass
    _l_(605682)

def Calculate():
    _l_(605887)

    h1 = _c_(605689, _n_(605685, "float", lambda: float), _c_(605688, _a_(605687, _n_(605686, "LongHeight", lambda: LongHeight), "get")))
    _l_(605690)
    h2 = _c_(605695, _n_(605691, "float", lambda: float), _c_(605694, _a_(605693, _n_(605692, "ShortHeight", lambda: ShortHeight), "get")))
    _l_(605696)
    aj = _c_(605701, _n_(605697, "float", lambda: float), _c_(605700, _a_(605699, _n_(605698, "Width", lambda: Width), "get")))
    _l_(605702)
    d = _c_(605707, _n_(605703, "float", lambda: float), _c_(605706, _a_(605705, _n_(605704, "Depth", lambda: Depth), "get")))
    _l_(605708)

    opc = _n_(605709, "h1", lambda: h1) - _n_(605710, "h2", lambda: h2)
    _l_(605711)
    Opc_Width = _n_(605712, "opc", lambda: opc) / _n_(605713, "aj", lambda: aj)
    _l_(605714)
    Radians = _c_(605719, _a_(605716, _n_(605715, "math", lambda: math), "atan"), _n_(605717, "opc", lambda: opc) / _n_(605718, "aj", lambda: aj))
    _l_(605720)
    Pitch = _c_(605728, _a_(605722, _n_(605721, "math", lambda: math), "degrees"), _c_(605727, _a_(605724, _n_(605723, "math", lambda: math), "atan"), _n_(605725, "opc", lambda: opc) / _n_(605726, "aj", lambda: aj)))
    _l_(605729)
    Width_And_Height_Squared = (_n_(605730, "opc", lambda: opc) * _n_(605731, "opc", lambda: opc)) + (_n_(605732, "aj", lambda: aj) * _n_(605733, "aj", lambda: aj))
    _l_(605734)
    Square_Root = _c_(605741, _a_(605736, _n_(605735, "math", lambda: math), "sqrt"), (_n_(605737, "opc", lambda: opc) * _n_(605738, "opc", lambda: opc)) + (_n_(605739, "aj", lambda: aj) * _n_(605740, "aj", lambda: aj)))
    _l_(605742)
    Roof_Area = _c_(605749, _a_(605744, _n_(605743, "math", lambda: math), "sqrt"), (_n_(605745, "opc", lambda: opc) * _n_(605746, "opc", lambda: opc)) + (_n_(605747, "aj", lambda: aj) * _n_(605748, "aj", lambda: aj)))*_n_(605750, "d", lambda: d)
    _l_(605751)

    text_file = _c_(605753, _n_(605752, "open", lambda: open), "temp.txt", "a")
    _l_(605754)
    _c_(605757, _a_(605756, _n_(605755, "text_file", lambda: text_file), "write"), "Longest Height: ")
    _l_(605758)
    _c_(605764, _a_(605760, _n_(605759, "text_file", lambda: text_file), "write"), _c_(605763, _n_(605761, "str", lambda: str), _n_(605762, "h1", lambda: h1)))
    _l_(605765)
    _c_(605768, _a_(605767, _n_(605766, "text_file", lambda: text_file), "write"), "\n")
    _l_(605769)
    _c_(605772, _a_(605771, _n_(605770, "text_file", lambda: text_file), "write"), "Shortest Height: ")
    _l_(605773)
    _c_(605779, _a_(605775, _n_(605774, "text_file", lambda: text_file), "write"), _c_(605778, _n_(605776, "str", lambda: str), _n_(605777, "h2", lambda: h2)))
    _l_(605780)
    _c_(605783, _a_(605782, _n_(605781, "text_file", lambda: text_file), "write"), "\n")
    _l_(605784)
    _c_(605787, _a_(605786, _n_(605785, "text_file", lambda: text_file), "write"), "Width: ")
    _l_(605788)
    _c_(605794, _a_(605790, _n_(605789, "text_file", lambda: text_file), "write"), _c_(605793, _n_(605791, "str", lambda: str), _n_(605792, "aj", lambda: aj)))
    _l_(605795)
    _c_(605798, _a_(605797, _n_(605796, "text_file", lambda: text_file), "write"), "\n")
    _l_(605799)
    _c_(605802, _a_(605801, _n_(605800, "text_file", lambda: text_file), "write"), "Depth: ")
    _l_(605803)
    _c_(605809, _a_(605805, _n_(605804, "text_file", lambda: text_file), "write"), _c_(605808, _n_(605806, "str", lambda: str), _n_(605807, "d", lambda: d)))
    _l_(605810)
    _c_(605813, _a_(605812, _n_(605811, "text_file", lambda: text_file), "write"), "\n")
    _l_(605814)
    _c_(605817, _a_(605816, _n_(605815, "text_file", lambda: text_file), "write"), "Pitch: ")
    _l_(605818)
    _c_(605824, _a_(605820, _n_(605819, "text_file", lambda: text_file), "write"), _c_(605823, _n_(605821, "str", lambda: str), _n_(605822, "Pitch", lambda: Pitch)))
    _l_(605825)
    _c_(605828, _a_(605827, _n_(605826, "text_file", lambda: text_file), "write"), "\n")
    _l_(605829)
    _c_(605832, _a_(605831, _n_(605830, "text_file", lambda: text_file), "write"), "Roof Area: ")
    _l_(605833)
    _c_(605839, _a_(605835, _n_(605834, "text_file", lambda: text_file), "write"), _c_(605838, _n_(605836, "str", lambda: str), _n_(605837, "Roof_Area", lambda: Roof_Area)))
    _l_(605840)
    _c_(605843, _a_(605842, _n_(605841, "text_file", lambda: text_file), "write"), "\n")
    _l_(605844)
    _c_(605847, _a_(605846, _n_(605845, "text_file", lambda: text_file), "write"), "\n")
    _l_(605848)
    _c_(605851, _a_(605850, _n_(605849, "text_file", lambda: text_file), "close"))
    _l_(605852)

    text_file = _c_(605854, _n_(605853, "open", lambda: open), "temp.txt")
    _l_(605855)
    contents = ""
    _l_(605856)

    for i in _n_(605857, "text_file", lambda: text_file):
        _l_(605860)

        contents += _n_(605858, "i", lambda: i)
        _l_(605859)

    _c_(605865, _a_(605862, _n_(605861, "ResultsBox", lambda: ResultsBox), "insert"), _n_(605863, "END", lambda: END), _n_(605864, "contents", lambda: contents))
    _l_(605866)
    _c_(605869, _a_(605868, _n_(605867, "text_file", lambda: text_file), "close"))
    _l_(605870)

    _c_(605873, _a_(605872, _n_(605871, "ShortHeight", lambda: ShortHeight), "set"), "")
    _l_(605874)
    _c_(605877, _a_(605876, _n_(605875, "LongHeight", lambda: LongHeight), "set"), "")
    _l_(605878)
    _c_(605881, _a_(605880, _n_(605879, "Depth", lambda: Depth), "set"), "")
    _l_(605882)
    _c_(605885, _a_(605884, _n_(605883, "Width", lambda: Width), "set"), "")
    _l_(605886)


window = _c_(605889, _n_(605888, "Tk", lambda: Tk))
_l_(605890)
_c_(605893, _a_(605892, _n_(605891, "window", lambda: window), "geometry"), "600x400+200+200")
_l_(605894)
_c_(605897, _a_(605896, _n_(605895, "window", lambda: window), "title"), "Roof Pitch Calculator")
_l_(605898)
_c_(605901, _a_(605900, _n_(605899, "window", lambda: window), "wm_resizable"), 0,0)
_l_(605902)

TitleLabel = _c_(605907, _a_(605906, _c_(605905, _n_(605903, "Label", lambda: Label), _n_(605904, "window", lambda: window), font = "Comic 30", foreground = "deep sky blue", text = "Roof Pitch Calculator"), "pack"))
_l_(605908)

CalculateButton = _c_(605915, _a_(605913, _c_(605912, _n_(605909, "Button", lambda: Button), _n_(605910, "window", lambda: window), text = "Calculate", command = _n_(605911, "Calculate", lambda: Calculate)), "pack"), side = _n_(605914, "BOTTOM", lambda: BOTTOM), pady = 5)
_l_(605916)
ResultsBox = _c_(605922, _a_(605920, _c_(605919, _n_(605917, "Text", lambda: Text), _n_(605918, "window", lambda: window), height = 13, width = 70), "pack"), side = _n_(605921, "BOTTOM", lambda: BOTTOM))
_l_(605923)
ShortHeightLabel = _c_(605928, _a_(605927, _c_(605926, _n_(605924, "Label", lambda: Label), _n_(605925, "window", lambda: window), text = "Short Height"), "place"), x = 190, y = 50)
_l_(605929)
LongHeightLabel = _c_(605934, _a_(605933, _c_(605932, _n_(605930, "Label", lambda: Label), _n_(605931, "window", lambda: window), text = "Long Height"), "place"), x = 330, y = 50)
_l_(605935)
DepthLabel = _c_(605940, _a_(605939, _c_(605938, _n_(605936, "Label", lambda: Label), _n_(605937, "window", lambda: window), text = "Depth"), "place"), x = 207, y = 100)
_l_(605941)
WidthLabel = _c_(605946, _a_(605945, _c_(605944, _n_(605942, "Label", lambda: Label), _n_(605943, "window", lambda: window), text = "Width"), "place"), x = 345, y = 100)
_l_(605947)

ShortHeight = _c_(605949, _n_(605948, "StringVar", lambda: StringVar))
_l_(605950)
ShortHeightEntry = _c_(605954, _n_(605951, "Entry", lambda: Entry), _n_(605952, "window", lambda: window), textvariable = _n_(605953, "ShortHeight", lambda: ShortHeight))
_l_(605955)
_c_(605958, _a_(605957, _n_(605956, "ShortHeightEntry", lambda: ShortHeightEntry), "place"), x = 161, y = 71)
_l_(605959)

LongHeight = _c_(605961, _n_(605960, "StringVar", lambda: StringVar))
_l_(605962)
LongHeightEntry = _c_(605966, _n_(605963, "Entry", lambda: Entry), _n_(605964, "window", lambda: window), textvariable = _n_(605965, "LongHeight", lambda: LongHeight))
_l_(605967)
_c_(605970, _a_(605969, _n_(605968, "LongHeightEntry", lambda: LongHeightEntry), "place"), x = 300, y = 71)
_l_(605971)

Depth = _c_(605973, _n_(605972, "StringVar", lambda: StringVar))
_l_(605974)
DepthEntry = _c_(605978, _n_(605975, "Entry", lambda: Entry), _n_(605976, "window", lambda: window), textvariable = _n_(605977, "Depth", lambda: Depth))
_l_(605979)
_c_(605982, _a_(605981, _n_(605980, "DepthEntry", lambda: DepthEntry), "place"), x = 161, y = 120)
_l_(605983)

Width = _c_(605985, _n_(605984, "StringVar", lambda: StringVar))
_l_(605986)
WidthEntry = _c_(605990, _n_(605987, "Entry", lambda: Entry), _n_(605988, "window", lambda: window), textvariable = _n_(605989, "Width", lambda: Width))
_l_(605991)
_c_(605994, _a_(605993, _n_(605992, "WidthEntry", lambda: WidthEntry), "place"), x = 300, y = 120)
_l_(605995)

_c_(605998, _a_(605997, _n_(605996, "window", lambda: window), "mainloop"))
_l_(605999)