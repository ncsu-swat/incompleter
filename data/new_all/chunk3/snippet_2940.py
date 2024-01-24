# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57540372/typeerror-unhashable-type-numpy-ndarray-when-merging-pandas-datframes-from-b
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from google.cloud import bigquery
    _l_(562775)

except ImportError:
    pass
try:
    from google.oauth2 import service_account
    _l_(562777)

except ImportError:
    pass
try:
    from google.cloud import bigquery_storage_v1beta1
    _l_(562779)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(562781)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(562783)

except ImportError:
    pass

credentials = _c_(562787, _a_(562786, _a_(562785, _n_(562784, "service_account", lambda: service_account), "Credentials"), "from_service_account_file"), 'XXXXXXXXX.json')
_l_(562788)
project_id = 'XXXXXX'
_l_(562789)
client = _c_(562794, _a_(562791, _n_(562790, "bigquery", lambda: bigquery), "Client"), credentials= _n_(562792, "credentials", lambda: credentials), project=_n_(562793, "project_id", lambda: project_id))
_l_(562795)

bqstorageclient = _c_(562799, _a_(562797, _n_(562796, "bigquery_storage_v1beta1", lambda: bigquery_storage_v1beta1), "BigQueryStorageClient"), credentials=_n_(562798, "credentials", lambda: credentials)
)
_l_(562800)


language_query = """
  SELECT repo_name, Language, Bytes,
  CASE 
  when LOWER(Language) NOT IN ('javascript', 'python', 'ruby', 'java'
                        , 'php', 'c++', 'css', 'c#', 'go'
                        , 'c', 'typescript', 'shell', 'swift'
                        , 'scala', 'objective-c') then 'Other'
  else Language END AS language_category
  FROM github_project.langauges

  LIMIT 1000"""
_l_(562801)

language_query_dataframe = _c_(562810, _a_(562808, _c_(562807, _a_(562806, _c_(562805, _a_(562803, _n_(562802, "client", lambda: client), "query"), _n_(562804, "language_query", lambda: language_query)), "result")), "to_dataframe"), bqstorage_client=_n_(562809, "bqstorageclient", lambda: bqstorageclient))
_l_(562811)

commit_query = """
    SELECT Commit, Author, DateSeconds, repo_name
    FROM github_project.commits
    LIMIT 1000
    """
_l_(562812)

commit_query_dataframe = _c_(562821, _a_(562819, _c_(562818, _a_(562817, _c_(562816, _a_(562814, _n_(562813, "client", lambda: client), "query"), _n_(562815, "commit_query", lambda: commit_query)), "result")), "to_dataframe"), bqstorage_client=_n_(562820, "bqstorageclient", lambda: bqstorageclient))
_l_(562822)

merged_data = _c_(562827, _a_(562824, _n_(562823, "pd", lambda: pd), "merge"), _n_(562825, "commit_query_dataframe", lambda: commit_query_dataframe), _n_(562826, "language_query_dataframe", lambda: language_query_dataframe), on='repo_name')
_l_(562828)