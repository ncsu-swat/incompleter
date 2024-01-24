# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70097223/adding-image-to-legend-in-matplotlib-returns-error-attributeerror-barcontaine
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from matplotlib.transforms import Bbox, TransformedBbox
    _l_(412292)

except ImportError:
    pass
try:
    from matplotlib.legend_handler import HandlerBase
    _l_(412294)

except ImportError:
    pass
try:
    from matplotlib.image import BboxImage
    _l_(412296)

except ImportError:
    pass

class ImageHandler(_n_(412297, "HandlerBase", lambda: HandlerBase)):
    _l_(412348)

    def create_artists(self, legend, orig_handle, Xd_, Yd_, W_, H_, fontsize, trans):
        _l_(412337)

        # enlarge the image by these margins
        sx, sy = _a_(412299, _n_(412298, "self", lambda: self), "image_stretch") 
        _l_(412300) 

        # create a bounding box to house the image
        bb = _c_(412311, _a_(412302, _n_(412301, "Bbox", lambda: Bbox), "from_bounds"), _n_(412303, "Xd_", lambda: Xd_) - _n_(412304, "sx", lambda: sx), _n_(412305, "Yd_", lambda: Yd_) - _n_(412306, "sy", lambda: sy), _n_(412307, "W_", lambda: W_) + _n_(412308, "sx", lambda: sx), _n_(412309, "H_", lambda: H_) + _n_(412310, "sy", lambda: sy) )
        _l_(412312)
        tbb = _c_(412316, _n_(412313, "TransformedBbox", lambda: TransformedBbox), _n_(412314, "bb", lambda: bb), _n_(412315, "trans", lambda: trans))
        _l_(412317)
        image = _c_(412320, _n_(412318, "BboxImage", lambda: BboxImage), _n_(412319, "tbb", lambda: tbb))
        _l_(412321)
        _c_(412326, _a_(412323, _n_(412322, "image", lambda: image), "set_data"), _a_(412325, _n_(412324, "self", lambda: self), "image_data"))
        _l_(412327)
        _c_(412333, _a_(412329, _n_(412328, "self", lambda: self), "update_prop"), _n_(412330, "image", lambda: image), _n_(412331, "orig_handle", lambda: orig_handle), _n_(412332, "legend", lambda: legend))
        _l_(412334)
        aux = [_n_(412335, "image", lambda: image)]
        _l_(412336)
        return aux

    def set_image(self, image_path, image_stretch=(0, 0)):
        _l_(412347)

        _n_(412338, "self", lambda: self).image_data = _c_(412342, _a_(412340, _n_(412339, "plt", lambda: plt), "imread"), _n_(412341, "image_path", lambda: image_path))
        _l_(412343)
        _n_(412344, "self", lambda: self).image_stretch = _n_(412345, "image_stretch", lambda: image_stretch)
        _l_(412346)