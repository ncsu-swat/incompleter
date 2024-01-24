# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40916386/typeerror-when-searching-google-with-the-google-api-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import requests, urllib, json
  _l_(695721)

except ImportError:
  pass

def search(search_string):
  _l_(695774)

  query = _c_(695726, _a_(695724, _a_(695723, _n_(695722, "urllib", lambda: urllib), "parse"), "urlencode"), {'q': _n_(695725, "search_string", lambda: search_string)})
  _l_(695727)
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % _n_(695728, "query", lambda: query)
  _l_(695729)
  search_response = _c_(695734, _a_(695732, _a_(695731, _n_(695730, "urllib", lambda: urllib), "request"), "urlopen"), _n_(695733, "url", lambda: url))
  _l_(695735)
  search_results = _c_(695740, _a_(695739, _c_(695738, _a_(695737, _n_(695736, "search_response", lambda: search_response), "read")), "decode"), "utf8")
  _l_(695741)
  results = _c_(695745, _a_(695743, _n_(695742, "json", lambda: json), "loads"), _n_(695744, "search_results", lambda: search_results))
  _l_(695746)
  data = _n_(695747, "results", lambda: results)['responseData']
  _l_(695748)
  _c_(695751, _n_(695749, "print", lambda: print), 'Total results: %s' % _n_(695750, "data", lambda: data)['cursor']['estimatedResultCount'])
  _l_(695752)
  hits = _n_(695753, "data", lambda: data)['results']
  _l_(695754)
  _c_(695759, _n_(695755, "print", lambda: print), 'Top %d hits:' % _c_(695758, _n_(695756, "len", lambda: len), _n_(695757, "hits", lambda: hits)))
  _l_(695760)
  for h in _n_(695761, "hits", lambda: hits):
    _l_(695765)

_c_(695764, _n_(695762, "print", lambda: print), ' ', _n_(695763, "h", lambda: h)['url'])  _c_(695768, _n_(695766, "print", lambda: print), 'For more results, see %s' % _n_(695767, "data", lambda: data)['cursor']['moreResultsUrl'])
  _l_(695769)
  _c_(695772, _n_(695770, "print", lambda: print), _n_(695771, "hits", lambda: hits))
  _l_(695773)

_c_(695778, _n_(695775, "search", lambda: search), _c_(695777, _n_(695776, "input", lambda: input), 'Enter search query:'))
_l_(695779)