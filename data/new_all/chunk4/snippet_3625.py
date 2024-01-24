# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71067529/beautiful-soup-attributeerror-nonetype-object-has-no-attribute-get-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(586430, _n_(586429, "open", lambda: open), 'source.html') as f:
   _l_(586437)

   soup = _c_(586435, _n_(586431, "BeautifulSoup", lambda: BeautifulSoup), _c_(586434, _a_(586433, _n_(586432, "f", lambda: f), "read")), "html.parser")
   _l_(586436)

# Extract script and style elements
for s in _c_(586439, _n_(586438, "soup", lambda: soup), ["script", "style"]):
   _l_(586444)

   _c_(586442, _a_(586441, _n_(586440, "s", lambda: s), "extract"))
   _l_(586443)

tr = _c_(586447, _a_(586446, _n_(586445, "soup", lambda: soup), "find_all"), "tr")
_l_(586448)
for t in _n_(586449, "tr", lambda: tr):
   _l_(586456)

   location = _c_(586454, _a_(586453, _c_(586452, _a_(586451, _n_(586450, "t", lambda: t), "find"), 'span', itemprop='name'), "get_text")) # ERROR
   _l_(586455) # ERROR