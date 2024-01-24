# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58275685/attributeerror-type-object-pandana-cyaccess-cyaccess-has-no-attribute-redu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandana, time, os, pandas as pd, numpy as np
    _l_(427307)

except ImportError:
    pass
try:
    from pandana.loaders import osm
    _l_(427309)

except ImportError:
    pass

# define your selected amenities and bounding box
# configure search at a max distance of 1 km for up to the 10 nearest points-of-interest
amenities = ['restaurant', 'bar', 'food']
_l_(427310)
distance = 1000
_l_(427311)
num_pois = 10
_l_(427312)
num_categories = _c_(427315, _n_(427313, "len", lambda: len), _n_(427314, "amenities", lambda: amenities)) + 1 #one for each amenity, plus one extra for all of them combined
_l_(427316) #one for each amenity, plus one extra for all of them combined

# bounding box as a list of llcrnrlat, llcrnrlng, urcrnrlat, urcrnrlng
# Bounding box for a Edinburgh, Scotland
west, south, east, north = (-3.449533, 55.818792, -3.074951, 56.004084)
_l_(427317)
bbox = [_n_(427318, "west", lambda: west), _n_(427319, "south", lambda: south), _n_(427320, "east", lambda: east), _n_(427321, "north", lambda: north)] #lat-long bounding box for Edinburgh, Scotland
_l_(427322) #lat-long bounding box for Edinburgh, Scotland