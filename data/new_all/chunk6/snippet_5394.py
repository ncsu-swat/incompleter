# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56902630/attributeerror-nonetype-object-has-no-attribute-find-all
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(354749)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(354751)

except ImportError:
    pass


# Collect and parse first page
page = _c_(354754, _a_(354753, _n_(354752, "requests", lambda: requests), "get"), 'https://www.jiosaavn.com/album/vijayashanti-birthday-telugu-hits/A05RmafpUiI_')
_l_(354755)
soup = _c_(354759, _n_(354756, "BeautifulSoup", lambda: BeautifulSoup), _a_(354758, _n_(354757, "page", lambda: page), "text"), 'html.parser')
_l_(354760)

# Pull all text from the BodyText div
artist_name_list = _c_(354763, _a_(354762, _n_(354761, "soup", lambda: soup), "find"), class_='song-wrap')
_l_(354764)

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = _c_(354767, _a_(354766, _n_(354765, "artist_name_list", lambda: artist_name_list), "find_all"), 'a')
_l_(354768)

for artist_name in _n_(354769, "artist_name_list_items", lambda: artist_name_list_items):
    _l_(354776)

    _c_(354774, _n_(354770, "print", lambda: print), _c_(354773, _a_(354772, _n_(354771, "artist_name", lambda: artist_name), "prettify")))
    _l_(354775)