# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47939513/name-error-when-calling-defined-function-in-jupyter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def merge_dfs_on_column(dataframes, labels, col):
    _l_(416277)

    '''merge a single column of each dataframe on to a new combined dataframe'''
    _l_(416257)
    series_dict={}
    _l_(416258)
    for index in _c_(416263, _n_(416259, "range", lambda: range), _c_(416262, _n_(416260, "len", lambda: len), _n_(416261, "dataframes", lambda: dataframes))):
        _l_(416271)

        _n_(416264, "series_dict", lambda: series_dict)[_n_(416265, "labels", lambda: labels)[_n_(416266, "index", lambda: index)]]=_n_(416267, "dataframes", lambda: dataframes)[_n_(416268, "index", lambda: index)][_n_(416269, "col", lambda: col)]
        _l_(416270)
    aux = _c_(416275, _a_(416273, _n_(416272, "pd", lambda: pd), "DataFrame"), _n_(416274, "series_dict", lambda: series_dict))
    _l_(416276)
    return aux
# Merge the BTC price dataseries into a single dataframe
btc_usd_datasets= _c_(416289, _n_(416278, "merge_dfs_on_column", lambda: merge_dfs_on_column), _c_(416283, _n_(416279, "list", lambda: list), _c_(416282, _a_(416281, _n_(416280, "exchange_data", lambda: exchange_data), "values"))),_c_(416288, _n_(416284, "list", lambda: list), _c_(416287, _a_(416286, _n_(416285, "exchange_data", lambda: exchange_data), "keys"))),'Weighted Price')
_l_(416290)