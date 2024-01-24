# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64506532/attributeerror-nonetype-object-has-no-attribute-coords
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(549711)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(549713)

except ImportError:
    pass
try:
    import astropy.units as u
    _l_(549715)

except ImportError:
    pass
try:
    from astropy.wcs import WCS
    _l_(549717)

except ImportError:
    pass
try:
    from astropy.io import fits
    _l_(549719)

except ImportError:
    pass
try:
    from astropy.utils.data import get_pkg_data_filename
    _l_(549721)

except ImportError:
    pass
try:
    from astropy.coordinates import SkyCoord
    _l_(549723)

except ImportError:
    pass
try:
    from astropy.coordinates import ICRS, Galactic, FK4, FK5
    _l_(549725)

except ImportError:
    pass
try:
    from astropy.coordinates import Angle, Latitude, Longitude
    _l_(549727)

except ImportError:
    pass
try:
    import astropy.units as u
    _l_(549729)

except ImportError:
    pass


filename = _c_(549731, _n_(549730, "get_pkg_data_filename", lambda: get_pkg_data_filename), 'jopi.fits')
_l_(549732)


hdu = _c_(549736, _a_(549734, _n_(549733, "fits", lambda: fits), "open"), _n_(549735, "filename", lambda: filename))[0]
_l_(549737)
wcs = _a_(549742, _c_(549741, _n_(549738, "WCS", lambda: WCS), _a_(549740, _n_(549739, "hdu", lambda: hdu), "header")), "celestial")
_l_(549743)
_a_(549745, _n_(549744, "wcs", lambda: wcs), "wcs").crval = [0,0]
_l_(549746)
_a_(549748, _n_(549747, "wcs", lambda: wcs), "wcs").ctype = [ 'XOFFSET' , 'YOFFSET' ]
_l_(549749)


fig = _c_(549752, _a_(549751, _n_(549750, "plt", lambda: plt), "figure"), figsize=(8,6))
_l_(549753)
ax = _c_(549757, _a_(549755, _n_(549754, "fig", lambda: fig), "add_subplot"), projection=_n_(549756, "wcs", lambda: wcs))
_l_(549758)
_c_(549763, _a_(549760, _n_(549759, "plt", lambda: plt), "imshow"), _a_(549762, _n_(549761, "hdu", lambda: hdu), "data")[0][0], origin='lower') 
_l_(549764) 
lon = _a_(549766, _n_(549765, "ax", lambda: ax), "coords")[0]
_l_(549767)
lat = _a_(549769, _n_(549768, "ax", lambda: ax), "coords")[1]
_l_(549770)
_c_(549773, _a_(549772, _n_(549771, "lon", lambda: lon), "set_major_formatter"), 'x')
_l_(549774)
_c_(549777, _a_(549776, _n_(549775, "lat", lambda: lat), "set_major_formatter"), 'x')
_l_(549778)
_c_(549783, _a_(549780, _n_(549779, "lon", lambda: lon), "set_format_unit"), _a_(549782, _n_(549781, "u", lambda: u), "milliarcsecond"))
_l_(549784)
_c_(549789, _a_(549786, _n_(549785, "lat", lambda: lat), "set_format_unit"), _a_(549788, _n_(549787, "u", lambda: u), "milliarcsecond"))
_l_(549790)
_c_(549793, _a_(549792, _n_(549791, "ax", lambda: ax), "set_xlim"), 200,800)
_l_(549794)
_c_(549797, _a_(549796, _n_(549795, "ax", lambda: ax), "set_ylim"), 200,800)
_l_(549798)
_c_(549801, _a_(549800, _n_(549799, "ax", lambda: ax), "set_xlabel"), 'Relative R.A ()')
_l_(549802)
_c_(549805, _a_(549804, _n_(549803, "ax", lambda: ax), "set_ylabel"), 'Relative Dec ()')
_l_(549806)