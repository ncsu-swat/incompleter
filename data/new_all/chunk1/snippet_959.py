# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64636058/attributeerror-line2d-object-has-no-property-cmap
#create x,y coordinates
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = _c_(414802, _a_(414801, _a_(414800, _n_(414799, "numpy", lambda: numpy), "random"), "choice"), 10,10)
_l_(414803)
y = _c_(414807, _a_(414806, _a_(414805, _n_(414804, "numpy", lambda: numpy), "random"), "choice"), 10,10)
_l_(414808)

#create an array of colors based on direction of line (0=r, 1=g, 2=b)
colors = []
_l_(414809)
#create an array that is one position away from original 
#to determine direction of line 
yCopy = _c_(414812, _n_(414810, "list", lambda: list), _n_(414811, "y", lambda: y)[1:])
_l_(414813)
for y1,y2 in _c_(414817, _n_(414814, "zip", lambda: zip), _n_(414815, "y", lambda: y),_n_(414816, "yCopy", lambda: yCopy)):
    _l_(414836)

    if _n_(414818, "y1", lambda: y1) > _n_(414819, "y2", lambda: y2):
        _l_(414835)

        _c_(414822, _a_(414821, _n_(414820, "colors", lambda: colors), "append"), 0)
        _l_(414823)
    elif _n_(414824, "y1", lambda: y1) < _n_(414825, "y2", lambda: y2):
        _l_(414834)

        _c_(414828, _a_(414827, _n_(414826, "colors", lambda: colors), "append"), 1)
        _l_(414829)
    else:
        _c_(414832, _a_(414831, _n_(414830, "colors", lambda: colors), "append"), 2)
        _l_(414833)
#add tenth spot to array as loop only does nine
_c_(414839, _a_(414838, _n_(414837, "colors", lambda: colors), "append"), 2)
_l_(414840)

#create a numpy array of colors
categories = _c_(414844, _a_(414842, _n_(414841, "numpy", lambda: numpy), "array"), _n_(414843, "colors", lambda: colors))
_l_(414845)

#create a color map with the three colors
colormap = _c_(414863, _a_(414847, _n_(414846, "numpy", lambda: numpy), "array"), [_c_(414852, _a_(414851, _a_(414850, _a_(414849, _n_(414848, "matplotlib", lambda: matplotlib), "colors"), "colorConverter"), "to_rgb"), 'r'),_c_(414857, _a_(414856, _a_(414855, _a_(414854, _n_(414853, "matplotlib", lambda: matplotlib), "colors"), "colorConverter"), "to_rgb"), 'g'),_c_(414862, _a_(414861, _a_(414860, _a_(414859, _n_(414858, "matplotlib", lambda: matplotlib), "colors"), "colorConverter"), "to_rgb"), 'b')])
_l_(414864)

#plot line
_c_(414872, _a_(414867, _a_(414866, _n_(414865, "matplotlib", lambda: matplotlib), "axes"), "plot"), _n_(414868, "x", lambda: x),_n_(414869, "y", lambda: y),color=_n_(414870, "colormap", lambda: colormap)[_n_(414871, "categories", lambda: categories)])
_l_(414873)