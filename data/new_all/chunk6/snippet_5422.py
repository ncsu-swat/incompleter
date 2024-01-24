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
_l_(335186)

docs = _c_(335189, _n_(335187, "create_doc", lambda: create_doc), "https://elastic:rKzWu2WbXI@db.luxurynsight.com/luxurynsight_v2/news/_search",_n_(335188, "doc_data", lambda: doc_data))
_l_(335190)


information_df = _c_(335197, _a_(335193, _a_(335192, _n_(335191, "pd", lambda: pd), "DataFrame"), "from_dict"), _c_(335196, _a_(335195, _n_(335194, "docs", lambda: docs), "json"))["hits"]["hits"])
_l_(335198)

# Reading the JSON file
df_news = _c_(335201, _a_(335200, _n_(335199, "pd", lambda: pd), "read_json"), 'data.json')
_l_(335202)

# Converting the element wise _source feature datatype to dictionary
_n_(335203, "df_news", lambda: df_news)._source = _c_(335210, _a_(335206, _a_(335205, _n_(335204, "df_news", lambda: df_news), "_source"), "apply"), lambda x: _c_(335209, _n_(335207, "dict", lambda: dict), _n_(335208, "x", lambda: x)))
_l_(335211)

# Creating name column
_n_(335212, "df_news", lambda: df_news)['name'] = _c_(335217, _a_(335215, _a_(335214, _n_(335213, "df_news", lambda: df_news), "_source"), "apply"), lambda x: _n_(335216, "x", lambda: x)['name'])
_l_(335218)

# Creating createdAt column
_n_(335219, "df_news", lambda: df_news)['createdAt'] = _c_(335224, _a_(335222, _a_(335221, _n_(335220, "df_news", lambda: df_news), "_source"), "apply"), lambda x: _n_(335223, "x", lambda: x)['createdAt'])
_l_(335225)

_n_(335226, "df_news", lambda: df_news)['createdAt'] =  _c_(335230, _a_(335228, _n_(335227, "pd", lambda: pd), "to_datetime"), _n_(335229, "df_news", lambda: df_news)['createdAt'], unit='ms')
_l_(335231)

_n_(335232, "df_news", lambda: df_news)['createdAt'] = _c_(335239, _a_(335238, _c_(335237, _a_(335234, _n_(335233, "pd", lambda: pd), "DatetimeIndex"), _a_(335236, _n_(335235, "df_news", lambda: df_news), "createdAt")), "normalize"))
_l_(335240)
#df_news.createdAt.dt.normalize()

_n_(335241, "df_news", lambda: df_news)['Date'] = _n_(335242, "df_news", lambda: df_news)['createdAt']
_l_(335243)

df_news = _n_(335244, "df_news", lambda: df_news)[['name','Date']]
_l_(335245)
df_news = _c_(335248, _a_(335247, _n_(335246, "df_news", lambda: df_news), "set_index"), 'Date')
_l_(335249)
_n_(335250, "information_df", lambda: information_df)._source = _c_(335256, _a_(335252, _n_(335251, "information_df", lambda: information_df), "apply"), lambda x: _c_(335255, _n_(335253, "dict", lambda: dict), _n_(335254, "x", lambda: x)))
_l_(335257)
_c_(335260, _a_(335259, _n_(335258, "df_news", lambda: df_news), "reset_index"))
_l_(335261)