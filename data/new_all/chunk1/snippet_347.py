# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40582073/trying-to-iterate-and-join-pandas-dfs-attributeerror-series-object-has-no-at
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
'''
Import the modules necessary for analysis
'''
_l_(419966)
try:
    import quandl
    _l_(419968)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(419970)

except ImportError:
    pass
try:
    import numpy as np
    _l_(419972)

except ImportError:
    pass

'''
Set file pathes and API keys
'''
_l_(419973)

ticker_path = ''
_l_(419974)
auth_key = ''
_l_(419975)

'''
Pull a list of tickers in the IGM ETF
'''
_l_(419976)

def ticker_list():
    _l_(419986)

    df = _c_(419982, _a_(419978, _n_(419977, "pd", lambda: pd), "read_csv"), _c_(419981, _a_(419979, '{}IGM Tickers.csv', "format"), _n_(419980, "ticker_path", lambda: ticker_path)))
    _l_(419983)
    aux = _n_(419984, "df", lambda: df)['Ticker']
    _l_(419985)
    # print(df['Ticker'])
    return aux

'''
Pull the historical prices for the securities within Ticker List
'''
_l_(419987)

def grab_constituent_data():
    _l_(420056)

    tickers = _c_(419989, _n_(419988, "ticker_list", lambda: ticker_list))
    _l_(419990)
    main_df = _c_(419993, _a_(419992, _n_(419991, "pd", lambda: pd), "DataFrame"))
    _l_(419994)

    for abbv in _n_(419995, "tickers", lambda: tickers):
        _l_(420049)

        query = _c_(420000, _a_(419996, 'EOD/{}', "format"), _c_(419999, _n_(419997, "str", lambda: str), _n_(419998, "abbv", lambda: abbv)))
        _l_(420001)
        df = _c_(420006, _a_(420003, _n_(420002, "quandl", lambda: quandl), "get"), _n_(420004, "query", lambda: query), authtoken=_n_(420005, "auth_key", lambda: auth_key))
        _l_(420007)
        _c_(420012, _n_(420008, "print", lambda: print), _c_(420011, _a_(420009, 'Competed the query for {}', "format"), _n_(420010, "query", lambda: query)))
        _l_(420013)

        _n_(420014, "df", lambda: df)[_c_(420019, _a_(420015, '{} Adj_Close', "format"), _c_(420018, _n_(420016, "str", lambda: str), _n_(420017, "abbv", lambda: abbv)))] = _c_(420022, _a_(420021, _n_(420020, "df", lambda: df)['Adj_Close'], "copy"))
        _l_(420023)
        df = _n_(420024, "df", lambda: df)[_c_(420029, _a_(420025, '{} Adj_Close', "format"), _c_(420028, _n_(420026, "str", lambda: str), _n_(420027, "abbv", lambda: abbv)))]
        _l_(420030)
        _c_(420037, _n_(420031, "print", lambda: print), _c_(420036, _a_(420032, 'Completed the column adjustment for {}', "format"), _c_(420035, _n_(420033, "str", lambda: str), _n_(420034, "abbv", lambda: abbv))))
        _l_(420038)

        if _a_(420040, _n_(420039, "main_df", lambda: main_df), "empty"):
            _l_(420048)

            main_df = _n_(420041, "df", lambda: df)
            _l_(420042)
        else:
            main_df = _c_(420046, _a_(420044, _n_(420043, "main_df", lambda: main_df), "join"), _n_(420045, "df", lambda: df))
            _l_(420047)

    _c_(420054, _n_(420050, "print", lambda: print), _c_(420053, _a_(420052, _n_(420051, "main_df", lambda: main_df), "head")))
    _l_(420055)