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
_l_(344000)

docs = _c_(344003, _n_(344001, "create_doc", lambda: create_doc), "https://elastic:rKzWu2WbXI@db.luxurynsight.com/luxurynsight_v2/news/_search",_n_(344002, "doc_data", lambda: doc_data))
_l_(344004)


information_df = _c_(344011, _a_(344007, _a_(344006, _n_(344005, "pd", lambda: pd), "DataFrame"), "from_dict"), _c_(344010, _a_(344009, _n_(344008, "docs", lambda: docs), "json"))["hits"]["hits"])
_l_(344012)

# Reading the JSON file
df_news = _c_(344015, _a_(344014, _n_(344013, "pd", lambda: pd), "read_json"), 'data.json')
_l_(344016)

# Converting the element wise _source feature datatype to dictionary
_n_(344017, "df_news", lambda: df_news)._source = _c_(344024, _a_(344020, _a_(344019, _n_(344018, "df_news", lambda: df_news), "_source"), "apply"), lambda x: _c_(344023, _n_(344021, "dict", lambda: dict), _n_(344022, "x", lambda: x)))
_l_(344025)

# Creating name column
_n_(344026, "df_news", lambda: df_news)['name'] = _c_(344031, _a_(344029, _a_(344028, _n_(344027, "df_news", lambda: df_news), "_source"), "apply"), lambda x: _n_(344030, "x", lambda: x)['name'])
_l_(344032)

# Creating createdAt column
_n_(344033, "df_news", lambda: df_news)['createdAt'] = _c_(344038, _a_(344036, _a_(344035, _n_(344034, "df_news", lambda: df_news), "_source"), "apply"), lambda x: _n_(344037, "x", lambda: x)['createdAt'])
_l_(344039)

_n_(344040, "df_news", lambda: df_news)['createdAt'] =  _c_(344044, _a_(344042, _n_(344041, "pd", lambda: pd), "to_datetime"), _n_(344043, "df_news", lambda: df_news)['createdAt'], unit='ms')
_l_(344045)

_n_(344046, "df_news", lambda: df_news)['createdAt'] = _c_(344053, _a_(344052, _c_(344051, _a_(344048, _n_(344047, "pd", lambda: pd), "DatetimeIndex"), _a_(344050, _n_(344049, "df_news", lambda: df_news), "createdAt")), "normalize"))
_l_(344054)
#df_news.createdAt.dt.normalize()

_n_(344055, "df_news", lambda: df_news)['Date'] = _n_(344056, "df_news", lambda: df_news)['createdAt']
_l_(344057)

df_news = _n_(344058, "df_news", lambda: df_news)[['name','Date']]
_l_(344059)
df_news = _c_(344062, _a_(344061, _n_(344060, "df_news", lambda: df_news), "set_index"), 'Date')
_l_(344063)
_n_(344064, "information_df", lambda: information_df)._source = _c_(344070, _a_(344066, _n_(344065, "information_df", lambda: information_df), "apply"), lambda x: _c_(344069, _n_(344067, "dict", lambda: dict), _n_(344068, "x", lambda: x)))
_l_(344071)
_c_(344074, _a_(344073, _n_(344072, "df_news", lambda: df_news), "reset_index"))
_l_(344075)