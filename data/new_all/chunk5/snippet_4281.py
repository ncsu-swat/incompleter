# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60345611/dont-understand-cause-of-this-typeerror-exception
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cc_gdps = {}
_l_(656406)
for gdp_dict  in _n_(656407, "gdp_data", lambda: gdp_data):
    _l_(656428)

    if _n_(656408, "gdp_dict", lambda: gdp_dict)['Year'] == 2014:
        _l_(656421)

        country_name = _n_(656409, "gdp_data", lambda: gdp_data)["Country Name"]
        _l_(656410)
        gdp = _c_(656415, _n_(656411, "int", lambda: int), _c_(656414, _n_(656412, "float", lambda: float), _n_(656413, "gdp_data", lambda: gdp_data)['Value']))
        _l_(656416)
        code = _c_(656419, _n_(656417, "get_country_code", lambda: get_country_code), _n_(656418, "country_name", lambda: country_name))
        _l_(656420)
    if _n_(656422, "code", lambda: code):
        _l_(656427)

        _n_(656423, "cc_gdps", lambda: cc_gdps)[_n_(656424, "code", lambda: code)] = _n_(656425, "gdp", lambda: gdp)
        _l_(656426)
#Group the countries into 3 gdp level
cc_gdps_1,cc_gdps_2,cc_gdps_3 = {},{},{}
_l_(656429)
for cc,gdp in _c_(656432, _a_(656431, _n_(656430, "cc_gdps", lambda: cc_gdps), "items")):
    _l_(656455)

    if _n_(656433, "gdp", lambda: gdp) < 5000000000:
        _l_(656454)

        _n_(656434, "cc_gdps_1", lambda: cc_gdps_1)[_n_(656435, "cc", lambda: cc)]=_c_(656438, _n_(656436, "round", lambda: round), _n_(656437, "gdp", lambda: gdp)/1000000000)
        _l_(656439)
    elif _n_(656440, "gdp", lambda: gdp) < 5000000000:
        _l_(656453)

        _n_(656441, "cc_gdps_2", lambda: cc_gdps_2)[_n_(656442, "cc", lambda: cc)] = _c_(656445, _n_(656443, "round", lambda: round), _n_(656444, "gdp", lambda: gdp)/1000000000)
        _l_(656446)
    else:
        _n_(656447, "cc_gdps_3", lambda: cc_gdps_3)[_n_(656448, "cc", lambda: cc)] = _c_(656451, _n_(656449, "round", lambda: round), _n_(656450, "gdp", lambda: gdp)/1000000000)
        _l_(656452)
#see how many countries are in each level
_c_(656466, _n_(656456, "print", lambda: print), _c_(656459, _n_(656457, "len", lambda: len), _n_(656458, "cc_gdps_1", lambda: cc_gdps_1)),_c_(656462, _n_(656460, "len", lambda: len), _n_(656461, "cc_gdps_2", lambda: cc_gdps_2)),_c_(656465, _n_(656463, "len", lambda: len), _n_(656464, "cc_gdps_3", lambda: cc_gdps_3)))
_l_(656467)
wm_style = _c_(656470, _n_(656468, "RC", lambda: RC), '#336699',base_style=_n_(656469, "LCS", lambda: LCS))
_l_(656471)
wm = _c_(656474, _n_(656472, "World", lambda: World), style = _n_(656473, "wm_style", lambda: wm_style))
_l_(656475)
_n_(656476, "wm", lambda: wm).title = 'Global GDP in 2014, by country.'
_l_(656477)
_c_(656481, _a_(656479, _n_(656478, "wm", lambda: wm), "add"), '0-5bln',_n_(656480, "cc_gdps_1", lambda: cc_gdps_1))
_l_(656482)
_c_(656486, _a_(656484, _n_(656483, "wm", lambda: wm), "add"), '5bln-50bln',_n_(656485, "cc_gdps_2", lambda: cc_gdps_2))
_l_(656487)
_c_(656491, _a_(656489, _n_(656488, "wm", lambda: wm), "add"), '>50bln', _n_(656490, "cc_gdps_3", lambda: cc_gdps_3))
_l_(656492)
_c_(656495, _a_(656494, _n_(656493, "wm", lambda: wm), "render_to_file"), 'global_gdp.svg')
_l_(656496)