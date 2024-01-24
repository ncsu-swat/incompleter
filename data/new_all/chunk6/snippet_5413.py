# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54514394/typeerror-normalize-argument-2-must-be-str-not-series-with-a-dataframe-of-st
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
doc_data = {
  "size": 10,
  "query": {
    "bool": {
      "must" : [
       {"term":{"text":"gucci"}}
     ]
    }
  }
 }
_l_(342401)

docs = _c_(342404, _n_(342402, "create_doc", lambda: create_doc), "https://elastic:rKzWu2WbXI@db.luxurynsight.com/luxurynsight_v2/news/_search",_n_(342403, "doc_data", lambda: doc_data))
_l_(342405)


information_df = _c_(342412, _a_(342408, _a_(342407, _n_(342406, "pd", lambda: pd), "DataFrame"), "from_dict"), _c_(342411, _a_(342410, _n_(342409, "docs", lambda: docs), "json"))["hits"]["hits"])
_l_(342413)

# Reading the JSON file
df_news = _c_(342416, _a_(342415, _n_(342414, "pd", lambda: pd), "read_json"), 'data.json')
_l_(342417)

# Converting the element wise _source feature datatype to dictionary
_n_(342418, "df_news", lambda: df_news)._source = _c_(342425, _a_(342421, _a_(342420, _n_(342419, "df_news", lambda: df_news), "_source"), "apply"), lambda x: _c_(342424, _n_(342422, "dict", lambda: dict), _n_(342423, "x", lambda: x)))
_l_(342426)

# Creating name column
_n_(342427, "df_news", lambda: df_news)['name'] = _c_(342432, _a_(342430, _a_(342429, _n_(342428, "df_news", lambda: df_news), "_source"), "apply"), lambda x: _n_(342431, "x", lambda: x)['name'])
_l_(342433)

# Creating createdAt column
_n_(342434, "df_news", lambda: df_news)['createdAt'] = _c_(342439, _a_(342437, _a_(342436, _n_(342435, "df_news", lambda: df_news), "_source"), "apply"), lambda x: _n_(342438, "x", lambda: x)['createdAt'])
_l_(342440)

_n_(342441, "df_news", lambda: df_news)['createdAt'] =  _c_(342445, _a_(342443, _n_(342442, "pd", lambda: pd), "to_datetime"), _n_(342444, "df_news", lambda: df_news)['createdAt'], unit='ms')
_l_(342446)

_n_(342447, "df_news", lambda: df_news)['createdAt'] = _c_(342454, _a_(342453, _c_(342452, _a_(342449, _n_(342448, "pd", lambda: pd), "DatetimeIndex"), _a_(342451, _n_(342450, "df_news", lambda: df_news), "createdAt")), "normalize"))
_l_(342455)
#df_news.createdAt.dt.normalize()

_n_(342456, "df_news", lambda: df_news)['Date'] = _n_(342457, "df_news", lambda: df_news)['createdAt']
_l_(342458)

df_news = _n_(342459, "df_news", lambda: df_news)[['name','Date']]
_l_(342460)
df_news = _c_(342463, _a_(342462, _n_(342461, "df_news", lambda: df_news), "set_index"), 'Date')
_l_(342464)
_n_(342465, "information_df", lambda: information_df)._source = _c_(342471, _a_(342467, _n_(342466, "information_df", lambda: information_df), "apply"), lambda x: _c_(342470, _n_(342468, "dict", lambda: dict), _n_(342469, "x", lambda: x)))
_l_(342472)
_c_(342475, _a_(342474, _n_(342473, "df_news", lambda: df_news), "reset_index"))
_l_(342476)