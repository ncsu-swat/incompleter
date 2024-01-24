# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54013527/typeerror-unsupported-operand-types-for-slice-and-int-with-bt-backtest
#Format price data
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
csv_f = _c_(399436, _a_(399435, _n_(399434, "pd", lambda: pd), "read_csv"), 'cryptodata.csv')
_l_(399437)
data = _c_(399441, _a_(399439, _n_(399438, "pd", lambda: pd), "DataFrame"), _n_(399440, "csv_f", lambda: csv_f))
_l_(399442)
_n_(399443, "data", lambda: data)['date'] = _c_(399447, _a_(399445, _n_(399444, "pd", lambda: pd), "to_datetime"), _n_(399446, "data", lambda: data)['date'])
_l_(399448)
_c_(399451, _a_(399450, _n_(399449, "data", lambda: data), "set_index"), 'date', inplace = True)
_l_(399452)
df1 = _n_(399453, "data", lambda: data)[:-1]
_l_(399454)
df1 = _c_(399457, _a_(399456, _n_(399455, "df1", lambda: df1), "dropna"))
_l_(399458)

def momentum_strategy(data, mom1 = 15, mom2 = 30, mom3 = 60, selection = 5 , cost = 0.025):
    _l_(399526)


    #Momentum calc 
    mom_1 = _c_(399462, _a_(399460, _n_(399459, "data", lambda: data), "pct_change"), _n_(399461, "mom1", lambda: mom1))
    _l_(399463)
    mom_2 = _c_(399467, _a_(399465, _n_(399464, "data", lambda: data), "pct_change"), _n_(399466, "mom2", lambda: mom2))
    _l_(399468)
    mom_3 = _c_(399472, _a_(399470, _n_(399469, "data", lambda: data), "pct_change"), _n_(399471, "mom3", lambda: mom3))
    _l_(399473)

    mom_average = (_n_(399474, "mom_1", lambda: mom_1) + _n_(399475, "mom_2", lambda: mom_2) + _n_(399476, "mom_3", lambda: mom_3)) / 3
    _l_(399477)
    mom_average = _c_(399480, _a_(399479, _n_(399478, "mom_average", lambda: mom_average), "dropna"))
    _l_(399481)

    #Weight
    mom_average_rank = _c_(399484, _a_(399483, _n_(399482, "mom_average", lambda: mom_average), "rank"), 1, ascending = True)
    _l_(399485)
    mom_selection = _n_(399486, "selection", lambda: selection) > _n_(399487, "mom_average_rank", lambda: mom_average_rank)
    _l_(399488)

    #create strategy

    s = _c_(399512, _a_(399490, _n_(399489, "bt", lambda: bt), "Strategy"), 'mom_s',[_c_(399495, _a_(399493, _a_(399492, _n_(399491, "bt", lambda: bt), "algos"), "SelectWhere"), _n_(399494, "mom_selection", lambda: mom_selection)),
                        _c_(399499, _a_(399498, _a_(399497, _n_(399496, "bt", lambda: bt), "algos"), "RunWeekly")),
                        _c_(399503, _a_(399502, _a_(399501, _n_(399500, "bt", lambda: bt), "algos"), "SelectAll")),
                        _c_(399507, _a_(399506, _a_(399505, _n_(399504, "bt", lambda: bt), "algos"), "WeighEqually")),
                        _c_(399511, _a_(399510, _a_(399509, _n_(399508, "bt", lambda: bt), "algos"), "Rebalance"))])
    _l_(399513)
    aux = _c_(399524, _a_(399515, _n_(399514, "bt", lambda: bt), "Backtest"), _n_(399516, "s", lambda: s), _n_(399517, "data", lambda: data), commissions = lambda q, p: _c_(399523, _n_(399518, "max", lambda: max), 100, _c_(399521, _n_(399519, "abs", lambda: abs), _n_(399520, "q", lambda: q)) * _n_(399522, "cost", lambda: cost) ))
    _l_(399525)

    return aux

#create the backtests
mom_1 = _c_(399529, _n_(399527, "momentum_strategy", lambda: momentum_strategy), _n_(399528, "df1", lambda: df1), 15, 30, 60, 5, 0.025)
_l_(399530)

#run backtests
res = _c_(399534, _a_(399532, _n_(399531, "bt", lambda: bt), "run"), _n_(399533, "mom_1", lambda: mom_1))
_l_(399535)