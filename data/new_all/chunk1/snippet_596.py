# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49668387/type-error-cannot-convert-the-series-to-class-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
gmap = _c_(390572, _a_(390569, _n_(390568, "gmplot", lambda: gmplot), "GoogleMapPlotter"), _n_(390570, "rep_points", lambda: rep_points)['lat'][0], _n_(390571, "rep_points", lambda: rep_points)['long'][0], 11)
_l_(390573)
_c_(390580, _a_(390575, _n_(390574, "gmap", lambda: gmap), "plot"), _a_(390577, _n_(390576, "df_min", lambda: df_min), "lat"), _a_(390579, _n_(390578, "df_min", lambda: df_min), "lng"))
_l_(390581)
_c_(390586, _a_(390583, _n_(390582, "gmap", lambda: gmap), "scatter"), _n_(390584, "rep_points", lambda: rep_points)['lat'],_n_(390585, "rep_points", lambda: rep_points)['long'],c='aquamarine')
_l_(390587)
_c_(390592, _a_(390589, _n_(390588, "gmap", lambda: gmap), "circle"), _n_(390590, "rep_points", lambda: rep_points)['lat'],_n_(390591, "rep_points", lambda: rep_points)['long'], 100, color='yellow')  
_l_(390593)  
_c_(390596, _a_(390595, _n_(390594, "gmap", lambda: gmap), "draw"), "user001_clus_time.html")
_l_(390597)