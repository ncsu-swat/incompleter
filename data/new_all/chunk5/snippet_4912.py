# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40916386/typeerror-when-searching-google-with-the-google-api-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import requests, urllib, json
  _l_(671437)

except ImportError:
  pass

def search(search_string):
  _l_(671490)

  query = _c_(671442, _a_(671440, _a_(671439, _n_(671438, "urllib", lambda: urllib), "parse"), "urlencode"), {'q': _n_(671441, "search_string", lambda: search_string)})
  _l_(671443)
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % _n_(671444, "query", lambda: query)
  _l_(671445)
  search_response = _c_(671450, _a_(671448, _a_(671447, _n_(671446, "urllib", lambda: urllib), "request"), "urlopen"), _n_(671449, "url", lambda: url))
  _l_(671451)
  search_results = _c_(671456, _a_(671455, _c_(671454, _a_(671453, _n_(671452, "search_response", lambda: search_response), "read")), "decode"), "utf8")
  _l_(671457)
  results = _c_(671461, _a_(671459, _n_(671458, "json", lambda: json), "loads"), _n_(671460, "search_results", lambda: search_results))
  _l_(671462)
  data = _n_(671463, "results", lambda: results)['responseData']
  _l_(671464)
  _c_(671467, _n_(671465, "print", lambda: print), 'Total results: %s' % _n_(671466, "data", lambda: data)['cursor']['estimatedResultCount'])
  _l_(671468)
  hits = _n_(671469, "data", lambda: data)['results']
  _l_(671470)
  _c_(671475, _n_(671471, "print", lambda: print), 'Top %d hits:' % _c_(671474, _n_(671472, "len", lambda: len), _n_(671473, "hits", lambda: hits)))
  _l_(671476)
  for h in _n_(671477, "hits", lambda: hits):
    _l_(671481)

_c_(671480, _n_(671478, "print", lambda: print), ' ', _n_(671479, "h", lambda: h)['url'])  _c_(671484, _n_(671482, "print", lambda: print), 'For more results, see %s' % _n_(671483, "data", lambda: data)['cursor']['moreResultsUrl'])
  _l_(671485)
  _c_(671488, _n_(671486, "print", lambda: print), _n_(671487, "hits", lambda: hits))
  _l_(671489)

_c_(671494, _n_(671491, "search", lambda: search), _c_(671493, _n_(671492, "input", lambda: input), 'Enter search query:'))
_l_(671495)