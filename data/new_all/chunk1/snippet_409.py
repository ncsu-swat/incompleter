# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70097223/adding-image-to-legend-in-matplotlib-returns-error-attributeerror-barcontaine
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
emoji_dataset = _c_(420095, _a_(420092, _a_(420091, _n_(420090, "os", lambda: os), "path"), "join"), _a_(420094, _n_(420093, "os", lambda: os), "environ")['HOME'], 'Datasets', 'Emojis')
_l_(420096)
h1 = _c_(420098, _n_(420097, "ImageHandler", lambda: ImageHandler))
_l_(420099)
h2 = _c_(420101, _n_(420100, "ImageHandler", lambda: ImageHandler))
_l_(420102)

_c_(420110, _a_(420104, _n_(420103, "h1", lambda: h1), "set_image"), _c_(420109, _a_(420107, _a_(420106, _n_(420105, "os", lambda: os), "path"), "join"), _n_(420108, "emoji_dataset", lambda: emoji_dataset), 'man.png'), image_stretch=(0, 20))
_l_(420111)
_c_(420119, _a_(420113, _n_(420112, "h2", lambda: h2), "set_image"), _c_(420118, _a_(420116, _a_(420115, _n_(420114, "os", lambda: os), "path"), "join"), _n_(420117, "emoji_dataset", lambda: emoji_dataset), 'woman.png'), image_stretch=(0, 20))
_l_(420120)

_c_(420127, _a_(420122, _n_(420121, "ax", lambda: ax), "legend"), handler_map={_n_(420123, "rects1", lambda: rects1): _n_(420124, "h1", lambda: h1), _n_(420125, "rects2", lambda: rects2): _n_(420126, "h2", lambda: h2)}, 
                        handlelength=2, labelspacing=0.0, 
                        fontsize=36, borderpad=0.15, loc='best', 
                        handletextpad=0.2, borderaxespad=0.15)
_l_(420128)