# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55865296/how-do-i-get-rid-of-the-typeerror
# html parsing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
page_soup = _c_(365746, _n_(365744, "soup", lambda: soup), _n_(365745, "page_html", lambda: page_html), "html.parser")
_l_(365747)

# grabs each appartment
containers = _c_(365750, _a_(365749, _n_(365748, "page_soup", lambda: page_soup), "findAll"), "div", {"class":"list-item-container"})
_l_(365751)

filename = "asunnot.csv"
_l_(365752)
f = _c_(365755, _n_(365753, "open", lambda: open), _n_(365754, "filename", lambda: filename), "w")
_l_(365756)

headers = "Kohdetta Vuokraa, Huoneistot, Talotyyppi ja Koko, Sijainti, Vapautuu, Vuokra"
_l_(365757)

_c_(365761, _a_(365759, _n_(365758, "f", lambda: f), "write"), _n_(365760, "headers", lambda: headers))
_l_(365762)
count = 0
_l_(365763)
for page in _c_(365765, _n_(365764, "range", lambda: range), 1,10):
    _l_(365816)

    my_url = "https://www.vuokraovi.com/vuokra-asunnot/Uusimaa?page={}&pageType="
    _l_(365766)
    for container in _n_(365767, "containers", lambda: containers):
        _l_(365815)


        Vuokranantaja = _a_(365771, _c_(365770, _a_(365769, _n_(365768, "container", lambda: container), "findAll"), "div", {"class":"hidden-xs col-sm-3 col-4"})[0], "img")["alt"]
        _l_(365772)

        Huoneistot = _a_(365776, _c_(365775, _a_(365774, _n_(365773, "container", lambda: container), "findAll"), "li", {"class":"semi-bold"})[1], "text")
        _l_(365777)

        Talotyyppi = _a_(365781, _c_(365780, _a_(365779, _n_(365778, "container", lambda: container), "findAll"), "li", {"class":"semi-bold"})[0], "text")
        _l_(365782)

        Sijainti = _c_(365798, _a_(365797, _c_(365796, _a_(365795, _c_(365794, _a_(365793, _c_(365792, _a_(365791, _c_(365790, _a_(365789, _a_(365788, _c_(365787, _a_(365786, _c_(365785, _a_(365784, _n_(365783, "container", lambda: container), "findAll"), "div", {"class":"hidden-xs col-sm-4 col-3"})[0], "findAll"), "span", {"class":"address"})[0], "text"), "strip")), "replace"), "\r", ""), "replace"), "\n", ""), "replace"), " ", ""), "replace"), ",", ", ")
        _l_(365799)

        Vapautuu = _a_(365806, _a_(365805, _c_(365804, _a_(365803, _c_(365802, _a_(365801, _n_(365800, "container", lambda: container), "findAll"), "div", {"class":"hidden-xs col-sm-4 col-3"})[0], "findAll"), "span", {"class":"showing-lease-container hidden-xs"})[0], "li"), "text")
        _l_(365807)

        Vuokra = _c_(365813, _a_(365812, _a_(365811, _c_(365810, _a_(365809, _n_(365808, "container", lambda: container), "findAll"), "li", {"class":"rent"})[0], "text"), "strip"))
        _l_(365814)