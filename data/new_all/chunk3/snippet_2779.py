# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63338052/attributeerror-nonetype-object-has-no-attribute-find-in-bs4
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime as dt
    _l_(569265)

except ImportError:
    pass
try:
    import requests
    _l_(569267)

except ImportError:
    pass
try:
    import bs4
    _l_(569269)

except ImportError:
    pass
try:
    import lxml
    _l_(569271)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(569273)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(569275)

except ImportError:
    pass
try:
    import numpy as np
    _l_(569277)

except ImportError:
    pass
try:
    import math
    _l_(569279)

except ImportError:
    pass
try:
    from alpha_vantage.timeseries import TimeSeries
    _l_(569281)

except ImportError:
    pass
try:
    from alpha_vantage.techindicators import TechIndicators
    _l_(569283)

except ImportError:
    pass

url=r'https://www.marketwatch.com/tools/stockresearch/screener/results.asp?submit=Screen&Symbol=true&Symbol=false&ChangePct=true&ChangePct=false&FiftyTwoWeekLow=false&CompanyName=true&CompanyName=false&Volume=true&Volume=false&PERatio=false&Price=true&Price=false&LastTradeTime=false&MarketCap=false&Change=true&Change=false&FiftyTwoWeekHigh=false&MoreInfo=true&MoreInfo=false&SortyBy=Symbol&SortDirection=Descending&ResultsPerPage=OneHundred&TradesShareEnable=false&TradesShareMin=&TradesShareMax=&PriceDirEnable=true&PriceDir=Up&PriceDirPct=100&LastYearEnable=false&LastYearAboveHigh=&TradeVolEnable=false&TradeVolMin=&TradeVolMax=&BlockEnable=false&BlockAmt=&BlockTime=&PERatioEnable=false&PERatioMin=&PERatioMax=&MktCapEnable=false&MktCapMin=&MktCapMax=&MovAvgEnable=false&MovAvgType=Outperform&MovAvgTime=FiftyDay&MktIdxEnable=false&MktIdxType=Outperform&MktIdxPct=&MktIdxExchange=&Exchange=All&IndustryEnable=false&Industry='
_l_(569284)

res=_c_(569288, _a_(569286, _n_(569285, "requests", lambda: requests), "get"), _n_(569287, "url", lambda: url))
_l_(569289)
soup=_c_(569294, _a_(569291, _n_(569290, "bs4", lambda: bs4), "BeautifulSoup"), _a_(569293, _n_(569292, "res", lambda: res), "text"), 'lxml')
_l_(569295)
tick=_a_(569301, _c_(569300, _a_(569299, _c_(569298, _a_(569297, _n_(569296, "soup", lambda: soup), "find"), 'td', {'class' :'aleft'}), "find"), 'a'), "text")
_l_(569302)
_c_(569305, _n_(569303, "print", lambda: print), _n_(569304, "tick", lambda: tick))
_l_(569306)