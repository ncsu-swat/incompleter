# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54922007/trying-to-extract-links-from-fetching-link-from-csv-file-into-request-get-but-ge
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
      from bs4 import BeautifulSoup
      _l_(699246)

except ImportError:
      pass
try:
      import requests
      _l_(699248)

except ImportError:
      pass
try:
      import csv
      _l_(699250)

except ImportError:
      pass
try:
      import pandas as pd
      _l_(699252)

except ImportError:
      pass

links = _c_(699256, _a_(699254, _n_(699253, "pd", lambda: pd), "read_csv"), 'C:\\Users\\acer\\Desktop\\hindustan_pages.csv',encoding = 'latin',dtype=_n_(699255, "str", lambda: str))
_l_(699257)

for i in _c_(699259, _n_(699258, "range", lambda: range), 1,3):
      _l_(699290)


      link = _a_(699261, _n_(699260, "links", lambda: links), "iloc")[_n_(699262, "i", lambda: i),0]
      _l_(699263)

      r = _c_(699267, _a_(699265, _n_(699264, "requests", lambda: requests), "get"), _n_(699266, "link", lambda: link))
      _l_(699268)

      soup = _c_(699272, _n_(699269, "BeautifulSoup", lambda: BeautifulSoup), _a_(699271, _n_(699270, "r", lambda: r), "text"),'lxml')
      _l_(699273)

      div = _c_(699276, _a_(699275, _n_(699274, "soup", lambda: soup), "find"), 'div',{"id":"company_list_grid"})
      _l_(699277)
      for links in _c_(699280, _a_(699279, _n_(699278, "div", lambda: div), "find_all"), 'th',{"id":"c_name"}):
            _l_(699289)

            link = _c_(699283, _a_(699282, _n_(699281, "links", lambda: links), "find"), 'a')
            _l_(699284)
            _c_(699287, _n_(699285, "print", lambda: print), "https://www.hindustanyellowpages.in/Ahmedabad" + _n_(699286, "link", lambda: link)['href'][2:])
            _l_(699288)