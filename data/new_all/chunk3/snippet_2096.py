# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60129510/nameerror-name-players-data-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
asia = _c_(529195, _n_(529194, "open_exl", lambda: open_exl), 'pubg_as.xls', 0)
_l_(529196)
eu = _c_(529198, _n_(529197, "open_exl", lambda: open_exl), 'pubg_eu.xls', 0)
_l_(529199)
na = _c_(529201, _n_(529200, "open_exl", lambda: open_exl), 'pubg_na.xls', 0)
_l_(529202)
oc = _c_(529204, _n_(529203, "open_exl", lambda: open_exl), 'pubg_oc.xls', 0)
_l_(529205)
sea = _c_(529207, _n_(529206, "open_exl", lambda: open_exl), 'pubg_sea.xls', 0)
_l_(529208)

# Load all data
all_data = _c_(529211, _a_(529210, _n_(529209, "np", lambda: np), "genfromtxt"), 'PUBG_Player_Statistics.csv', delimiter=',')
_l_(529212)
_n_(529213, "all_data", lambda: all_data)[:, 28] = _n_(529214, "all_data", lambda: all_data)[:, 28] * 100
_l_(529215)

# Train data
train_data = _n_(529216, "all_data", lambda: all_data)[1:2000, :][:, [3, 2, 28, 9]]
_l_(529217)
test_data = _n_(529218, "all_data", lambda: all_data)[2000:, :][:, [3, 2, 28, 9]]
_l_(529219)

data = _c_(529228, _a_(529221, _n_(529220, "np", lambda: np), "vstack"), (_n_(529222, "asia", lambda: asia)[1:], _n_(529223, "eu", lambda: eu)[1:], _n_(529224, "na", lambda: na)[1:], _n_(529225, "oc", lambda: oc)[1:], _n_(529226, "sea", lambda: sea)[1:], _n_(529227, "players_data", lambda: players_data)[1:]))
_l_(529229)
df = _c_(529240, _a_(529231, _n_(529230, "pd", lambda: pd), "DataFrame"), {_n_(529232, "data", lambda: data)[0, _n_(529233, "i", lambda: i)]: _n_(529234, "data", lambda: data)[1:, _n_(529235, "i", lambda: i)] for i in _c_(529239, _n_(529236, "range", lambda: range), _a_(529238, _n_(529237, "data", lambda: data), "shape")[1])})
_l_(529241)
m = _c_(529244, _n_(529242, "asfloat", lambda: asfloat), _n_(529243, "data", lambda: data)[1:, :4])
_l_(529245)