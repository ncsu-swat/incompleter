# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68850727/how-to-get-resolve-of-attribute-error-when-web-scraping-google-for-wind-speed
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(553252, "current_weather", lambda: current_weather)['wind']=_a_(553256, _c_(553255, _a_(553254, _n_(553253, "soup", lambda: soup), "find"), "span",attrs={"id": "wob_ws"}), "text")
_l_(553257)