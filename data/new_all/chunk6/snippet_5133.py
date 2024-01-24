# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49515768/typeerror-can-only-concatenate-list-not-int-to-list-help-needed
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
path2 = (r'C:\Users\newsample.csv')
_l_(361501)
openfile2 = _c_(361505, _a_(361503, _n_(361502, "pd", lambda: pd), "read_csv"), _n_(361504, "path2", lambda: path2), header='infer')
_l_(361506)

# Convert Long and Lat rows to list
lon = _c_(361509, _n_(361507, "list", lambda: list), _n_(361508, "openfile2", lambda: openfile2)['Long'])
_l_(361510)
lat = _c_(361513, _n_(361511, "list", lambda: list), _n_(361512, "openfile2", lambda: openfile2)['Lat'])
_l_(361514)
latitude = []
_l_(361515)
longitude = []
_l_(361516)

for la in _n_(361517, "lat", lambda: lat):
    _l_(361528)

    la = _c_(361521, _a_(361519, _n_(361518, "pd", lambda: pd), "to_numeric"), _n_(361520, "openfile2", lambda: openfile2)['Lat'])
    _l_(361522)
    _c_(361526, _a_(361524, _n_(361523, "latitude", lambda: latitude), "append"), _n_(361525, "la", lambda: la))
    _l_(361527)

for lo in _n_(361529, "lon", lambda: lon):
    _l_(361540)

    lo = _c_(361533, _a_(361531, _n_(361530, "pd", lambda: pd), "to_numeric"), _n_(361532, "openfile2", lambda: openfile2)['Long'])
    _l_(361534)
    _c_(361538, _a_(361536, _n_(361535, "latitude", lambda: latitude), "append"), _n_(361537, "lo", lambda: lo))
    _l_(361539)

# compute UTM zone for the rows
def get_zone(lat, lon):
    _l_(361582)

    zone = _c_(361543, _n_(361541, "int", lambda: int), (_n_(361542, "lon", lambda: lon) + 186) / 6)
    _l_(361544)
    if _n_(361545, "lat", lambda: lat) >= 56.0 and _n_(361546, "lat", lambda: lat) < 64.0 and _n_(361547, "lon", lambda: lon) >= 3.0 and _n_(361548, "lon", lambda: lon) < 12.0:
        _l_(361550)

        zone = 32
        _l_(361549)
    if _n_(361551, "lat", lambda: lat) >= 72.0 and _n_(361552, "lat", lambda: lat) < 84.0:
        _l_(361569)

        if _n_(361553, "lon", lambda: lon) >= 0.0 and _n_(361554, "lon", lambda: lon) < 9.0:
            _l_(361568)

            zone = 31
            _l_(361555)
        elif _n_(361556, "lon", lambda: lon) >= 9.0 and _n_(361557, "lon", lambda: lon) < 21.0:
            _l_(361567)

            zone = 33
            _l_(361558)
        elif _n_(361559, "lon", lambda: lon) >= 21.0 and _n_(361560, "lon", lambda: lon) < 33.0:
            _l_(361566)

            zone = 35
            _l_(361561)
        elif _n_(361562, "lon", lambda: lon) >= 33.0 and _n_(361563, "lon", lambda: lon) < 42.0:
            _l_(361565)

            zone = 37
            _l_(361564)
    if _n_(361570, "lat", lambda: lat) > 0:
        _l_(361579)

        cs = "EPSG::326" + _c_(361573, _n_(361571, "str", lambda: str), _n_(361572, "zone", lambda: zone))
        _l_(361574)
    else:
        cs = "EPSG::327" + _c_(361577, _n_(361575, "str", lambda: str), _n_(361576, "zone", lambda: zone))
        _l_(361578)
    aux = _n_(361580, "cs", lambda: cs)
    _l_(361581)
    return aux

# Call function
newfile = _c_(361586, _n_(361583, "get_zone", lambda: get_zone), _n_(361584, "latitude", lambda: latitude), _n_(361585, "longitude", lambda: longitude))
_l_(361587)
_c_(361590, _n_(361588, "print", lambda: print), _n_(361589, "newfile", lambda: newfile))
_l_(361591)