# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46841991/python-3-6-beautifulsoup4-parse-table-attributeerror-resultset-object-has-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(621331)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(621333)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(621335)

except ImportError:
    pass
try:
    import re
    _l_(621337)

except ImportError:
    pass

## Python 3.6
##BeautifulSoup4
def get_all_cities(html_soup):
    _l_(621379)

    """Scrape WIkipedia page for cities in California (https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_California)
    and returns a structured list of city names, county, population, area, and incorporation date"""
    cities_in_california = []
    _l_(621338)
    table_wiki = _c_(621341, _a_(621340, _n_(621339, "html_soup", lambda: html_soup), "findAll"), 'table', attrs={"class":"wikitable"})
    _l_(621342)
    table_wiki_rows = _c_(621345, _a_(621344, _n_(621343, "table_wiki", lambda: table_wiki), "findAll"), 'tr')
    _l_(621346)
    for rows in _n_(621347, "table_wiki", lambda: table_wiki):
        _l_(621376)

        table_rows_header = _c_(621350, _a_(621349, _n_(621348, "html_soup", lambda: html_soup), "findAll"), 'th')
        _l_(621351)
        table_rows = _c_(621354, _a_(621353, _n_(621352, "html_soup", lambda: html_soup), "findAll"), 'td')
        _l_(621355)
        city_entry = {
                'City_name' : _a_(621357, _n_(621356, "table_rows_header", lambda: table_rows_header)[0], "text"),
                'City_type' : _a_(621359, _n_(621358, "table_rows", lambda: table_rows)[1], "text"),
                'County' : _a_(621361, _n_(621360, "table_rows", lambda: table_rows)[2], "text"),
                'Population' : _a_(621363, _n_(621362, "table_rows", lambda: table_rows)[3], "text"),
                'Area_sqr_miles' : _a_(621365, _n_(621364, "table_rows", lambda: table_rows)[4], "text"),
                'Area_sqr_km' : _a_(621367, _n_(621366, "table_rows", lambda: table_rows)[5], "text"),
                'Incorporation_Date' : _a_(621369, _n_(621368, "table_rows", lambda: table_rows)[6], "text")                
                }
        _l_(621370)
        _c_(621374, _a_(621372, _n_(621371, "cities_in_california", lambda: cities_in_california), "append"), _n_(621373, "city_entry", lambda: city_entry))
        _l_(621375)
    aux = _n_(621377, "cities_in_california", lambda: cities_in_california)
    _l_(621378)
    return aux

html = _c_(621381, _n_(621380, "urlopen", lambda: urlopen), 'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_California')
_l_(621382)
html_soup = _c_(621385, _n_(621383, "BeautifulSoup", lambda: BeautifulSoup), _n_(621384, "html", lambda: html), 'html.parser')
_l_(621386)
city_list = _c_(621389, _n_(621387, "get_all_cities", lambda: get_all_cities), _n_(621388, "html_soup", lambda: html_soup))
_l_(621390)

df = _c_(621394, _a_(621392, _n_(621391, "pd", lambda: pd), "DataFrame"), _n_(621393, "city_list", lambda: city_list) )
_l_(621395)
_c_(621398, _a_(621397, _n_(621396, "df", lambda: df), "head"), 7)
_l_(621399)