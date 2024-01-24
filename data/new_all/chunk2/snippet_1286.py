# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55668134/how-do-i-fix-the-attributeerror-nonetype-object-has-no-attribute-text-whe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(454926)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(454928)

except ImportError:
    pass
try:
    import csv
    _l_(454930)

except ImportError:
    pass
try:
    import lxml
    _l_(454932)

except ImportError:
    pass


# Lists to store the scraped data in

addresses = []
_l_(454933)
geographies = []
_l_(454934)
rents = []
_l_(454935)
units = []
_l_(454936)
availabilities = []
_l_(454937)

# Scraping all pages

pages_url = _c_(454940, _a_(454939, _n_(454938, "requests", lambda: requests), "get"), 'https://www.rent.com/new-york/tuckahoe-apartments')
_l_(454941)

pages_soup = _c_(454945, _n_(454942, "BeautifulSoup", lambda: BeautifulSoup), _a_(454944, _n_(454943, "pages_url", lambda: pages_url), "text"), 'html.parser')
_l_(454946)

list_nums = _a_(454950, _c_(454949, _a_(454948, _n_(454947, "pages_soup", lambda: pages_soup), "find"), 'div', class_='_1y05u'), "text")
_l_(454951)

_c_(454954, _n_(454952, "print", lambda: print), _n_(454953, "list_nums", lambda: list_nums))
_l_(454955)

pages = [_c_(454958, _n_(454956, "str", lambda: str), _n_(454957, "i", lambda: i)) for i in _c_(454960, _n_(454959, "range", lambda: range), 1,8)]
_l_(454961)

for page in _n_(454962, "pages", lambda: pages):
    _l_(455055)


    response = _a_(454967, _c_(454966, _a_(454964, _n_(454963, "requests", lambda: requests), "get"), 'https://www.rent.com/new-york/tuckahoe-apartments?page=' + _n_(454965, "page", lambda: page)), "text")
    _l_(454968)

    html_soup = _c_(454971, _n_(454969, "BeautifulSoup", lambda: BeautifulSoup), _n_(454970, "response", lambda: response), 'lxml')
    _l_(454972)


    # Extract data from individual listing containers

    listing_containers = _c_(454975, _a_(454974, _n_(454973, "html_soup", lambda: html_soup), "find_all"), 'div', class_='_3PdAH')
    _l_(454976)
    _c_(454981, _n_(454977, "print", lambda: print), _c_(454980, _n_(454978, "type", lambda: type), _n_(454979, "listing_containers", lambda: listing_containers)))
    _l_(454982)
    _c_(454987, _n_(454983, "print", lambda: print), _c_(454986, _n_(454984, "len", lambda: len), _n_(454985, "listing_containers", lambda: listing_containers)))
    _l_(454988)



    for container in _n_(454989, "listing_containers", lambda: listing_containers):
        _l_(455054)

        address = _a_(454992, _a_(454991, _n_(454990, "container", lambda: container), "a"), "text")
        _l_(454993)
        _c_(454997, _a_(454995, _n_(454994, "addresses", lambda: addresses), "append"), _n_(454996, "address", lambda: address))
        _l_(454998)

        geography = _a_(455002, _c_(455001, _a_(455000, _n_(454999, "container", lambda: container), "find"), 'div', class_='_1dhrl'), "text")
        _l_(455003)
        _c_(455007, _a_(455005, _n_(455004, "geographies", lambda: geographies), "append"), _n_(455006, "geography", lambda: geography))
        _l_(455008)

        rent = _a_(455012, _c_(455011, _a_(455010, _n_(455009, "container", lambda: container), "find"), 'div', class_='_3e12V'), "text")
        _l_(455013)
        _c_(455017, _a_(455015, _n_(455014, "rents", lambda: rents), "append"), _n_(455016, "rent", lambda: rent))
        _l_(455018)

        unit = _a_(455022, _c_(455021, _a_(455020, _n_(455019, "container", lambda: container), "find"), 'div', class_='_2tApa'), "text")
        _l_(455023)
        _c_(455027, _a_(455025, _n_(455024, "units", lambda: units), "append"), _n_(455026, "unit", lambda: unit))
        _l_(455028)

        availability = _a_(455032, _c_(455031, _a_(455030, _n_(455029, "container", lambda: container), "find"), 'div', class_='_2P6xE'), "text")
        _l_(455033)
        _c_(455037, _a_(455035, _n_(455034, "availabilities", lambda: availabilities), "append"), _n_(455036, "availability", lambda: availability))
        _l_(455038)
        try:
            import pandas as pd
            _l_(455040)

        except ImportError:
            pass
        test_df = _c_(455048, _a_(455042, _n_(455041, "pd", lambda: pd), "DataFrame"), {'Street' : _n_(455043, "addresses", lambda: addresses),
                                'City-State-Zip' : _n_(455044, "geographies", lambda: geographies),
                                'Rent' : _n_(455045, "rents", lambda: rents),
                                'BR/BA' : _n_(455046, "units", lambda: units),
                                'Units Available' : _n_(455047, "availabilities", lambda: availabilities)

        })
        _l_(455049)
        _c_(455052, _n_(455050, "print", lambda: print), _n_(455051, "test_df", lambda: test_df))
        _l_(455053)