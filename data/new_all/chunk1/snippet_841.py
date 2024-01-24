# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63926412/nameerror-name-number-is-not-defined-using-css-selector-as-nth-childn-with
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
basecss = '#ctl00_ContentPlaceHolder1_Estadocombo > option'
_l_(385543)
events = _c_(385548, _a_(385546, _a_(385545, _n_(385544, "self", lambda: self), "driver_web_browser"), "find_elements_by_css_selector"), _n_(385547, "basecss", lambda: basecss))
_l_(385549)


for index, val in _c_(385552, _n_(385550, "enumerate", lambda: enumerate), _n_(385551, "events", lambda: events), 1):
    _l_(385588)

    name = _c_(385560, _a_(385555, _a_(385554, _n_(385553, "self", lambda: self), "driver_web_browser"), "find_elements_by_css_selector"), _c_(385559, _a_(385556, "{}:nth-child({})", "format"), _n_(385557, "basecss", lambda: basecss),_n_(385558, "index", lambda: index)))
    _l_(385561)

    _c_(385566, _n_(385562, "print", lambda: print), _n_(385563, "index", lambda: index),_a_(385565, _n_(385564, "val", lambda: val), "text"))
    _l_(385567)

    if _a_(385569, _n_(385568, "self", lambda: self), "state") == _a_(385571, _n_(385570, "val", lambda: val), "text"):
        _l_(385587)

        #event = self.driver_web_browser.find_element_by_css_selector(basecss + ("{}:nth-child({})").click())
        click = _c_(385578, _a_(385577, _c_(385576, _a_(385574, _a_(385573, _n_(385572, "self", lambda: self), "driver_web_browser"), "find_element_by_css_selector"), '#ctl00_ContentPlaceHolder1_Estadocombo > option:nth-child('+ _n_(385575, "index", lambda: index) +')'), "click"))
        _l_(385579)
        _c_(385584, _n_(385580, "print", lambda: print), _c_(385583, _n_(385581, "type", lambda: type), _n_(385582, "click", lambda: click)))
        _l_(385585)
        break 
        _l_(385586) 