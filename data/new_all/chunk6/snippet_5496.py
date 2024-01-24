# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62918174/typeerror-list-indices-must-be-integers-or-slices-not-str-when-i-trying-to-r
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
j = """
{
  "kind": "youtube#videoListResponse",       
  "items": [
    {
      "kind": "youtube#video",
      "id": "IEEhzQoKtQU",
      "statistics": {
        "viewCount": "171938",
        "likeCount": "5856",
        "dislikeCount": "38",
        "favoriteCount": "0",
        "commentCount": "368"
      }
    }
  ],
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 1
  }
}
"""
_l_(368578)
    
js = _c_(368582, _a_(368580, _n_(368579, "json", lambda: json), "loads"), _n_(368581, "j", lambda: j))
_l_(368583)
    
js = _n_(368584, "js", lambda: js)["items"]
_l_(368585)
    
js = _n_(368586, "js", lambda: js)["statistics"]
_l_(368587)
    
_c_(368590, _n_(368588, "print", lambda: print), _n_(368589, "js", lambda: js)["viewCount"])
_l_(368591)