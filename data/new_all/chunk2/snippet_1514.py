# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66293109/in-pafy-i-got-that-error-best-resolution-best-extensionres-format-typeerro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pafy import *
    _l_(465258)

except ImportError:
    pass
url = _c_(465262, _n_(465259, "str", lambda: str), _c_(465261, _n_(465260, "input", lambda: input), "Videonun Youtube linkini girin"))
_l_(465263)
video = _c_(465267, _a_(465265, _n_(465264, "pafy", lambda: pafy), "new"), _n_(465266, "url", lambda: url))
_l_(465268)
streams = _a_(465270, _n_(465269, "video", lambda: video), "streams")
_l_(465271)
for s in _n_(465272, "streams", lambda: streams):
    _l_(465285)

    _c_(465283, _n_(465273, "print", lambda: print), _a_(465275, _n_(465274, "s", lambda: s), "resolution"), _a_(465277, _n_(465276, "s", lambda: s), "extension"), _c_(465280, _a_(465279, _n_(465278, "s", lambda: s), "get_filesize")), _a_(465282, _n_(465281, "s", lambda: s), "url"))
    _l_(465284)

format = _c_(465287, _n_(465286, "input", lambda: input), "indirilecek turu seçin")
_l_(465288)
res = _c_(465290, _n_(465289, "input", lambda: input), "lutfen sectiginiz ture uygun cozunurluk yazın")
_l_(465291)

best = _c_(465295, _a_(465293, _n_(465292, "video", lambda: video), "getbest"), preftype=_n_(465294, "format", lambda: format))
_l_(465296)
_a_(465298, _n_(465297, "best", lambda: best), "resolution"), _c_(465303, _a_(465300, _n_(465299, "best", lambda: best), "extension"), _n_(465301, "res", lambda: res), _n_(465302, "format", lambda: format))
_l_(465304)

konum = _c_(465308, _n_(465305, "str", lambda: str), _c_(465307, _n_(465306, "input", lambda: input), "indirilecek yeri seçin"))
_l_(465309)
_c_(465313, _a_(465311, _n_(465310, "best", lambda: best), "download"), quiet=False,filepath=_n_(465312, "konum", lambda: konum))
_l_(465314)