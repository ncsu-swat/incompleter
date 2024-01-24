# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54922007/trying-to-extract-links-from-fetching-link-from-csv-file-into-request-get-but-ge
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
      from bs4 import BeautifulSoup
      _l_(664181)

except ImportError:
      pass
try:
      import requests
      _l_(664183)

except ImportError:
      pass
try:
      import csv
      _l_(664185)

except ImportError:
      pass
try:
      import pandas as pd
      _l_(664187)

except ImportError:
      pass

links = _c_(664191, _a_(664189, _n_(664188, "pd", lambda: pd), "read_csv"), 'C:\\Users\\acer\\Desktop\\hindustan_pages.csv',encoding = 'latin',dtype=_n_(664190, "str", lambda: str))
_l_(664192)

for i in _c_(664194, _n_(664193, "range", lambda: range), 1,3):
      _l_(664225)


      link = _a_(664196, _n_(664195, "links", lambda: links), "iloc")[_n_(664197, "i", lambda: i),0]
      _l_(664198)

      r = _c_(664202, _a_(664200, _n_(664199, "requests", lambda: requests), "get"), _n_(664201, "link", lambda: link))
      _l_(664203)

      soup = _c_(664207, _n_(664204, "BeautifulSoup", lambda: BeautifulSoup), _a_(664206, _n_(664205, "r", lambda: r), "text"),'lxml')
      _l_(664208)

      div = _c_(664211, _a_(664210, _n_(664209, "soup", lambda: soup), "find"), 'div',{"id":"company_list_grid"})
      _l_(664212)
      for links in _c_(664215, _a_(664214, _n_(664213, "div", lambda: div), "find_all"), 'th',{"id":"c_name"}):
            _l_(664224)

            link = _c_(664218, _a_(664217, _n_(664216, "links", lambda: links), "find"), 'a')
            _l_(664219)
            _c_(664222, _n_(664220, "print", lambda: print), "https://www.hindustanyellowpages.in/Ahmedabad" + _n_(664221, "link", lambda: link)['href'][2:])
            _l_(664223)