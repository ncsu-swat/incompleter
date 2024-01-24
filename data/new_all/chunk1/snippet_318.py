# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51690241/python-attributeerror-module-pandas-has-no-attribute-ewm
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from binance.client import Client
    _l_(405735)

except ImportError:
    pass
try:
    import numpy as np
    _l_(405737)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(405739)

except ImportError:
    pass
try:
    import smtplib
    _l_(405741)

except ImportError:
    pass
try:
    import time
    _l_(405743)

except ImportError:
    pass
try:
    import yaml
    _l_(405745)

except ImportError:
    pass

CONFIG = _c_(405750, _a_(405747, _n_(405746, "yaml", lambda: yaml), "load"), _c_(405749, _n_(405748, "open", lambda: open), './CONFIG.yml'))    
_l_(405751)    
API_KEY = _n_(405752, "CONFIG", lambda: CONFIG)['binance_api']['key']    
_l_(405753)    
API_SECRET = _n_(405754, "CONFIG", lambda: CONFIG)['binance_api']['secret']    
_l_(405755)    
user = _n_(405756, "CONFIG", lambda: CONFIG)['gmail']['user']    
_l_(405757)    
passwd = _n_(405758, "CONFIG", lambda: CONFIG)['gmail']['password']    
_l_(405759)    

client = _c_(405763, _n_(405760, "Client", lambda: Client), _n_(405761, "API_KEY", lambda: API_KEY), _n_(405762, "API_SECRET", lambda: API_SECRET))
_l_(405764)

# against ETH    
SYMBOLS = ('ADA', 'ADX', 'BAT', 'BCC', 'DASH', 'EOS', 'IOTA',

        'LTC', 'NEO', 'OMG', 'STORJ', 'XLM', 'NANO', 'XRP', 'XVG', 'ZEC')    
_l_(405765)    
RSI_N = 14    
_l_(405766)    
RSI_THRESHOLD = 8    
_l_(405767)    
RUN_INTERVAL_MINS = 30
_l_(405768)

def send_email(rsi_values):
    _l_(405815)

    if _c_(405771, _n_(405769, "len", lambda: len), _n_(405770, "rsi_values", lambda: rsi_values)) > 0:
        _l_(405814)

        message = _c_(405778, _a_(405772, '\n', "join"), (_c_(405776, _a_(405773, '{0:>8} {1:.2f}', "format"), _n_(405774, "symbol", lambda: symbol), _n_(405775, "rsi", lambda: rsi)) for (symbol, rsi) in _n_(405777, "rsi_values", lambda: rsi_values)))    
        _l_(405779)    
        email_text = _c_(405784, _a_(405780, 'From: {0}\nTo: {1}\nSubject: Stock Recommendations\n\n{2}', "format"), _n_(405781, "user", lambda: user), _n_(405782, "user", lambda: user), _n_(405783, "message", lambda: message))
        _l_(405785)

        try:
            _l_(405813)

            server = _c_(405788, _a_(405787, _n_(405786, "smtplib", lambda: smtplib), "SMTP_SSL"), 'smtp.gmail.com', 465)    
            _l_(405789)    
            _c_(405792, _a_(405791, _n_(405790, "server", lambda: server), "ehlo"))    
            _l_(405793)    
            _c_(405798, _a_(405795, _n_(405794, "server", lambda: server), "login"), _n_(405796, "user", lambda: user), _n_(405797, "passwd", lambda: passwd))    
            _l_(405799)    
            _c_(405805, _a_(405801, _n_(405800, "server", lambda: server), "sendmail"), _n_(405802, "user", lambda: user), _n_(405803, "user", lambda: user), _n_(405804, "email_text", lambda: email_text))    
            _l_(405806)    
            _c_(405809, _a_(405808, _n_(405807, "server", lambda: server), "close"))    
            _l_(405810)    
        except:
            _l_(405812)

            pass
            _l_(405811)

while True:
    _l_(405900)

    rsi_values = []    
    _l_(405816)    
    for SYMBOL in _n_(405817, "SYMBOLS", lambda: SYMBOLS):
        _l_(405872)

        klines = _c_(405826, _a_(405819, _n_(405818, "client", lambda: client), "get_historical_klines"), _n_(405820, "SYMBOL", lambda: SYMBOL) + 'ETH', _a_(405822, _n_(405821, "Client", lambda: Client), "KLINE_INTERVAL_30MINUTE"), _c_(405825, _a_(405823, '{} hours ago UTC', "format"), (_n_(405824, "RSI_N", lambda: RSI_N) + 3) // 2))    
        _l_(405827)    
        closings = _c_(405833, _a_(405829, _n_(405828, "np", lambda: np), "asarray"), _n_(405830, "klines", lambda: klines), dtype=_a_(405832, _n_(405831, "np", lambda: np), "float"))[-_n_(405834, "RSI_N", lambda: RSI_N) - 1:, 4]        
        _l_(405835)        
        diffs = _c_(405839, _a_(405837, _n_(405836, "np", lambda: np), "diff"), _n_(405838, "closings", lambda: closings))    
        _l_(405840)    
        ups = _c_(405843, _a_(405842, _n_(405841, "diffs", lambda: diffs), "clip"), min=0)    
        _l_(405844)    
        downs = _c_(405847, _a_(405846, _n_(405845, "diffs", lambda: diffs), "clip"), max=0)    
        _l_(405848)    
        ups_avg = _c_(405853, _a_(405850, _n_(405849, "pd", lambda: pd), "ewma"), _n_(405851, "ups", lambda: ups), span=_n_(405852, "RSI_N", lambda: RSI_N))[-1]    
        _l_(405854)    
        downs_avg = -_c_(405859, _a_(405856, _n_(405855, "pd", lambda: pd), "ewma"), _n_(405857, "downs", lambda: downs), span=_n_(405858, "RSI_N", lambda: RSI_N))[-1]    
        _l_(405860)    
        rs = _n_(405861, "ups_avg", lambda: ups_avg) / _n_(405862, "downs_avg", lambda: downs_avg)    
        _l_(405863)    
        rsi = 100 - 100 / (1 + _n_(405864, "rs", lambda: rs))    
        _l_(405865)    
        _c_(405870, _a_(405867, _n_(405866, "rsi_values", lambda: rsi_values), "append"), (_n_(405868, "SYMBOL", lambda: SYMBOL), _n_(405869, "rsi", lambda: rsi)))
        _l_(405871)

    _c_(405881, _n_(405873, "print", lambda: print), _c_(405880, _a_(405874, '\n', "join"), (_c_(405878, _a_(405875, '{0:>8} {1:.2f}', "format"), _n_(405876, "symbol", lambda: symbol), _n_(405877, "rsi", lambda: rsi)) for (symbol, rsi) in _n_(405879, "rsi_values", lambda: rsi_values))))    
    _l_(405882)    
    rsi_values = _c_(405889, _n_(405883, "list", lambda: list), _c_(405888, _n_(405884, "filter", lambda: filter), lambda x: _n_(405885, "x", lambda: x)[1] < _n_(405886, "RSI_THRESHOLD", lambda: RSI_THRESHOLD), _n_(405887, "rsi_values", lambda: rsi_values)))        
    _l_(405890)        
    _c_(405893, _n_(405891, "send_email", lambda: send_email), _n_(405892, "rsi_values", lambda: rsi_values))        
    _l_(405894)        
    _c_(405898, _a_(405896, _n_(405895, "time", lambda: time), "sleep"), 60 * _n_(405897, "RUN_INTERVAL_MINS", lambda: RUN_INTERVAL_MINS))
    _l_(405899)