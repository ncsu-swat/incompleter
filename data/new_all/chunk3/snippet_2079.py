# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65454097/exception-has-occurred-attributeerror-list-object-has-no-attribute-get-wh
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
STOCK_DIM = 422 # INITIAL_BALANCE, Amount_of_shares,  60 days * (Norm_close, 1m/2m/3m/1y ret, macd,rsi) 
_l_(561836) # INITIAL_BALANCE, Amount_of_shares,  60 days * (Norm_close, 1m/2m/3m/1y ret, macd,rsi) 
INITIAL_ACCOUNT_BALANCE = 1000000
_l_(561837)
TRANSACTION_FEE_PERCENT = 0.01
_l_(561838)
REWARD_SCALING = 1e-5
_l_(561839)
HMAX_NORMALIZE = 100
_l_(561840)
N = _a_(561842, _n_(561841, "config", lambda: config), "PREV_DATA_POINTS")
_l_(561843)


class StockEnv_Train(_a_(561845, _n_(561844, "gym", lambda: gym), "Env")):
    _l_(562372)

    def __init__(self,df,day = 374):
        _l_(561955)

        # day set to 260 since we need to account for the annual returns that only start around 252 days,
        # macd only starts from 254
        # we add 63 days to this to account for the historical data
        _n_(561846, "self", lambda: self).day = _n_(561847, "day", lambda: day)
        _l_(561848)
        _n_(561849, "self", lambda: self).df = _n_(561850, "df", lambda: df)
        _l_(561851)
        _n_(561852, "self", lambda: self).action_space = _c_(561855, _a_(561854, _n_(561853, "spaces", lambda: spaces), "Box"), low = -1,high = 1,shape =(1,) )
        _l_(561856)
        _n_(561857, "self", lambda: self).observation_space = _c_(561863, _a_(561859, _n_(561858, "spaces", lambda: spaces), "Box"), low = 0, high = _a_(561861, _n_(561860, "np", lambda: np), "inf"), shape = (_n_(561862, "STOCK_DIM", lambda: STOCK_DIM),))
        _l_(561864)
        _n_(561865, "self", lambda: self).terminal = False
        _l_(561866)

        _n_(561867, "self", lambda: self).state = [_n_(561868, "INITIAL_ACCOUNT_BALANCE", lambda: INITIAL_ACCOUNT_BALANCE)] + [0] + _c_(561878, _a_(561877, _a_(561871, _a_(561870, _n_(561869, "self", lambda: self), "df"), "iloc")[_a_(561873, _n_(561872, "self", lambda: self), "day")-_n_(561874, "N", lambda: N):_a_(561876, _n_(561875, "self", lambda: self), "day"),1], "tolist")) + \
                        _c_(561888, _a_(561887, _a_(561881, _a_(561880, _n_(561879, "self", lambda: self), "df"), "iloc")[_a_(561883, _n_(561882, "self", lambda: self), "day")-_n_(561884, "N", lambda: N):_a_(561886, _n_(561885, "self", lambda: self), "day"),2], "tolist")) + _c_(561898, _a_(561897, _a_(561891, _a_(561890, _n_(561889, "self", lambda: self), "df"), "iloc")[_a_(561893, _n_(561892, "self", lambda: self), "day")-_n_(561894, "N", lambda: N):_a_(561896, _n_(561895, "self", lambda: self), "day"),3], "tolist")) + \
                        _c_(561908, _a_(561907, _a_(561901, _a_(561900, _n_(561899, "self", lambda: self), "df"), "iloc")[_a_(561903, _n_(561902, "self", lambda: self), "day")-_n_(561904, "N", lambda: N):_a_(561906, _n_(561905, "self", lambda: self), "day"),4], "tolist")) + _c_(561918, _a_(561917, _a_(561911, _a_(561910, _n_(561909, "self", lambda: self), "df"), "iloc")[_a_(561913, _n_(561912, "self", lambda: self), "day")-_n_(561914, "N", lambda: N):_a_(561916, _n_(561915, "self", lambda: self), "day"),5], "tolist")) + \
                        _c_(561928, _a_(561927, _a_(561921, _a_(561920, _n_(561919, "self", lambda: self), "df"), "iloc")[_a_(561923, _n_(561922, "self", lambda: self), "day")-_n_(561924, "N", lambda: N):_a_(561926, _n_(561925, "self", lambda: self), "day"),6], "tolist")) + _c_(561938, _a_(561937, _a_(561931, _a_(561930, _n_(561929, "self", lambda: self), "df"), "iloc")[_a_(561933, _n_(561932, "self", lambda: self), "day")-_n_(561934, "N", lambda: N):_a_(561936, _n_(561935, "self", lambda: self), "day"),7], "tolist"))
        _l_(561939)

        _n_(561940, "self", lambda: self).reward = 0
        _l_(561941)
        _n_(561942, "self", lambda: self).asset_memory = [_n_(561943, "INITIAL_ACCOUNT_BALANCE", lambda: INITIAL_ACCOUNT_BALANCE)]
        _l_(561944)
        _n_(561945, "self", lambda: self).cost = 0
        _l_(561946)
        _n_(561947, "self", lambda: self).rewards_memory = []
        _l_(561948)
        _n_(561949, "self", lambda: self).trades = 0
        _l_(561950)

        _c_(561953, _a_(561952, _n_(561951, "self", lambda: self), "_seed"))
        _l_(561954)

    
    def _sell_stock(self,action):
        _l_(562005)

        if _a_(561957, _n_(561956, "self", lambda: self), "state")[1] > 0:
            _l_(562004)

            _a_(561959, _n_(561958, "self", lambda: self), "state")[0] += _c_(561974, _a_(561973, (_a_(561962, _a_(561961, _n_(561960, "self", lambda: self), "df"), "iloc")[_a_(561964, _n_(561963, "self", lambda: self), "day"),-1]*_c_(561971, _n_(561965, "min", lambda: min), _c_(561968, _n_(561966, "abs", lambda: abs), _n_(561967, "action", lambda: action)),_a_(561970, _n_(561969, "self", lambda: self), "state")[1]) * \
                            (1- _n_(561972, "TRANSACTION_FEE_PERCENT", lambda: TRANSACTION_FEE_PERCENT))), "item"))
            _l_(561975)
            _n_(561976, "self", lambda: self).cost +=_a_(561979, _a_(561978, _n_(561977, "self", lambda: self), "df"), "iloc")[_a_(561981, _n_(561980, "self", lambda: self), "day"),-1]*_c_(561988, _n_(561982, "min", lambda: min), _c_(561985, _n_(561983, "abs", lambda: abs), _n_(561984, "action", lambda: action)),_a_(561987, _n_(561986, "self", lambda: self), "state")[1]) * \
                            _n_(561989, "TRANSACTION_FEE_PERCENT", lambda: TRANSACTION_FEE_PERCENT)
            _l_(561990)
            _a_(561992, _n_(561991, "self", lambda: self), "state")[1] -= _c_(561999, _n_(561993, "min", lambda: min), _c_(561996, _n_(561994, "abs", lambda: abs), _n_(561995, "action", lambda: action)), _a_(561998, _n_(561997, "self", lambda: self), "state")[1])
            _l_(562000)
            _n_(562001, "self", lambda: self).trades+=1
            _l_(562002)
        else:
            pass
            _l_(562003)

    def _buy_stock(self,action):
        _l_(562050)

        # perform buy action based on the sign of the action
        available_amount = _a_(562007, _n_(562006, "self", lambda: self), "state")[0] // _a_(562010, _a_(562009, _n_(562008, "self", lambda: self), "df"), "iloc")[_a_(562012, _n_(562011, "self", lambda: self), "day"),-1]
        _l_(562013)
        # print('available_amount:{}'.format(available_amount))

        #update balance
        _a_(562015, _n_(562014, "self", lambda: self), "state")[0] -= _c_(562027, _a_(562026, (_a_(562018, _a_(562017, _n_(562016, "self", lambda: self), "df"), "iloc")[_a_(562020, _n_(562019, "self", lambda: self), "day"),-1]*_c_(562024, _n_(562021, "min", lambda: min), _n_(562022, "available_amount", lambda: available_amount), _n_(562023, "action", lambda: action))* \
                          (1+ _n_(562025, "TRANSACTION_FEE_PERCENT", lambda: TRANSACTION_FEE_PERCENT))), "item"))
        _l_(562028)

        _a_(562030, _n_(562029, "self", lambda: self), "state")[1] += _c_(562034, _n_(562031, "min", lambda: min), _n_(562032, "available_amount", lambda: available_amount), _n_(562033, "action", lambda: action))
        _l_(562035)

        _n_(562036, "self", lambda: self).cost+=_a_(562039, _a_(562038, _n_(562037, "self", lambda: self), "df"), "iloc")[_a_(562041, _n_(562040, "self", lambda: self), "day"),-1]*_c_(562045, _n_(562042, "min", lambda: min), _n_(562043, "available_amount", lambda: available_amount), _n_(562044, "action", lambda: action))* \
                          _n_(562046, "TRANSACTION_FEE_PERCENT", lambda: TRANSACTION_FEE_PERCENT)
        _l_(562047)
        _n_(562048, "self", lambda: self).trades+=1
        _l_(562049)

    def step(self,action):
        _l_(562268)

        _n_(562051, "self", lambda: self).terminal = _a_(562053, _n_(562052, "self", lambda: self), "day") >= _c_(562060, _n_(562054, "len", lambda: len), _c_(562059, _a_(562058, _a_(562057, _a_(562056, _n_(562055, "self", lambda: self), "df"), "Date"), "unique"))) - 1
        _l_(562061)

        if _a_(562063, _n_(562062, "self", lambda: self), "terminal"):
            _l_(562254)

            _c_(562068, _a_(562065, _n_(562064, "plt", lambda: plt), "plot"), _a_(562067, _n_(562066, "self", lambda: self), "asset_memory"),'r')
            _l_(562069)
            _c_(562072, _a_(562071, _n_(562070, "plt", lambda: plt), "savefig"), 'results/account_value_train.png')
            _l_(562073)
            _c_(562076, _a_(562075, _n_(562074, "plt", lambda: plt), "close"))
            _l_(562077)

            df_total_value = _c_(562082, _a_(562079, _n_(562078, "pd", lambda: pd), "DataFrame"), _a_(562081, _n_(562080, "self", lambda: self), "asset_memory"))
            _l_(562083)
            _c_(562086, _a_(562085, _n_(562084, "df_total_value", lambda: df_total_value), "to_csv"), 'results/account_value_train.csv')
            _l_(562087)

            _n_(562088, "df_total_value", lambda: df_total_value).columns = ['account_value']
            _l_(562089)
            _n_(562090, "df_total_value", lambda: df_total_value)['daily_return'] = _c_(562093, _a_(562092, _n_(562091, "df_total_value", lambda: df_total_value), "pct_change"), 1)
            _l_(562094)
            
            df_rewards = _c_(562099, _a_(562096, _n_(562095, "pd", lambda: pd), "DataFrame"), _a_(562098, _n_(562097, "self", lambda: self), "rewards_memory"))
            _l_(562100)
            aux = _a_(562102, _n_(562101, "self", lambda: self), "state"), _a_(562104, _n_(562103, "self", lambda: self), "reward")*_n_(562105, "REWARD_SCALING", lambda: REWARD_SCALING),_a_(562107, _n_(562106, "self", lambda: self), "terminal"), {}
            _l_(562108)
            
            return aux

        else:
            # print(np.array(self.state[1:29]))

            action = _n_(562109, "action", lambda: action) * _n_(562110, "HMAX_NORMALIZE", lambda: HMAX_NORMALIZE)
            _l_(562111)
            #actions = (actions.astype(int))
            
            begin_total_asset = _a_(562113, _n_(562112, "self", lambda: self), "state")[0]+ _a_(562115, _n_(562114, "self", lambda: self), "state")[1]*_a_(562118, _a_(562117, _n_(562116, "self", lambda: self), "df"), "iloc")[_a_(562120, _n_(562119, "self", lambda: self), "day"),-1]
            _l_(562121)
            
            if _n_(562122, "action", lambda: action)<0:
                _l_(562133)

                _c_(562126, _a_(562124, _n_(562123, "self", lambda: self), "_sell_stock"), _n_(562125, "action", lambda: action))
                _l_(562127)
            else:
                _c_(562131, _a_(562129, _n_(562128, "self", lambda: self), "_buy_stock"), _n_(562130, "action", lambda: action))
                _l_(562132)

            _n_(562134, "self", lambda: self).day += 1        
            _l_(562135)        
            #load next state
            # print("stock_shares:{}".format(self.state[29:]))

            _n_(562136, "self", lambda: self).state = [_a_(562138, _n_(562137, "self", lambda: self), "state")[0]] + [_a_(562140, _n_(562139, "self", lambda: self), "state")[1]] + _c_(562150, _a_(562149, _a_(562143, _a_(562142, _n_(562141, "self", lambda: self), "df"), "iloc")[_a_(562145, _n_(562144, "self", lambda: self), "day")-_n_(562146, "N", lambda: N):_a_(562148, _n_(562147, "self", lambda: self), "day"),1], "tolist")) + \
                        _c_(562160, _a_(562159, _a_(562153, _a_(562152, _n_(562151, "self", lambda: self), "df"), "iloc")[_a_(562155, _n_(562154, "self", lambda: self), "day")-_n_(562156, "N", lambda: N):_a_(562158, _n_(562157, "self", lambda: self), "day"),2], "tolist")) + _c_(562170, _a_(562169, _a_(562163, _a_(562162, _n_(562161, "self", lambda: self), "df"), "iloc")[_a_(562165, _n_(562164, "self", lambda: self), "day")-_n_(562166, "N", lambda: N):_a_(562168, _n_(562167, "self", lambda: self), "day"),3], "tolist")) + \
                        _c_(562180, _a_(562179, _a_(562173, _a_(562172, _n_(562171, "self", lambda: self), "df"), "iloc")[_a_(562175, _n_(562174, "self", lambda: self), "day")-_n_(562176, "N", lambda: N):_a_(562178, _n_(562177, "self", lambda: self), "day"),4], "tolist")) + _c_(562190, _a_(562189, _a_(562183, _a_(562182, _n_(562181, "self", lambda: self), "df"), "iloc")[_a_(562185, _n_(562184, "self", lambda: self), "day")-_n_(562186, "N", lambda: N):_a_(562188, _n_(562187, "self", lambda: self), "day"),5], "tolist")) + \
                        _c_(562200, _a_(562199, _a_(562193, _a_(562192, _n_(562191, "self", lambda: self), "df"), "iloc")[_a_(562195, _n_(562194, "self", lambda: self), "day")-_n_(562196, "N", lambda: N):_a_(562198, _n_(562197, "self", lambda: self), "day"),6], "tolist")) + _c_(562210, _a_(562209, _a_(562203, _a_(562202, _n_(562201, "self", lambda: self), "df"), "iloc")[_a_(562205, _n_(562204, "self", lambda: self), "day")-_n_(562206, "N", lambda: N):_a_(562208, _n_(562207, "self", lambda: self), "day"),7], "tolist"))
            _l_(562211)
            
            end_total_asset = _a_(562213, _n_(562212, "self", lambda: self), "state")[0]+ _a_(562215, _n_(562214, "self", lambda: self), "state")[1]*_a_(562218, _a_(562217, _n_(562216, "self", lambda: self), "df"), "iloc")[_a_(562220, _n_(562219, "self", lambda: self), "day"),-1]
            _l_(562221)

            try:
                _l_(562237)

                _c_(562228, _a_(562224, _a_(562223, _n_(562222, "self", lambda: self), "asset_memory"), "append"), _c_(562227, _a_(562226, _n_(562225, "end_total_asset", lambda: end_total_asset), "item")))
                _l_(562229)
            except:
                _l_(562236)

                _c_(562234, _a_(562232, _a_(562231, _n_(562230, "self", lambda: self), "asset_memory"), "append"), _n_(562233, "end_total_asset", lambda: end_total_asset))
                _l_(562235)

            #print("end_total_asset:{}".format(end_total_asset))
            
            _n_(562238, "self", lambda: self).reward = _n_(562239, "end_total_asset", lambda: end_total_asset) - _n_(562240, "begin_total_asset", lambda: begin_total_asset)            
            _l_(562241)            
            _c_(562247, _a_(562244, _a_(562243, _n_(562242, "self", lambda: self), "rewards_memory"), "append"), _a_(562246, _n_(562245, "self", lambda: self), "reward"))
            _l_(562248)
            _n_(562249, "self", lambda: self).reward = _a_(562251, _n_(562250, "self", lambda: self), "reward")*_n_(562252, "REWARD_SCALING", lambda: REWARD_SCALING)
            _l_(562253)
            
        aux = _c_(562259, _a_(562256, _n_(562255, "np", lambda: np), "array"), [_a_(562258, _n_(562257, "self", lambda: self), "state")]),_c_(562264, _a_(562261, _n_(562260, "np", lambda: np), "array"), [_a_(562263, _n_(562262, "self", lambda: self), "reward")]),_a_(562266, _n_(562265, "self", lambda: self), "terminal"),{}
        _l_(562267)
        return aux

    
    def reset(self):
        _l_(562358)

        _n_(562269, "self", lambda: self).asset_memory = [_n_(562270, "INITIAL_ACCOUNT_BALANCE", lambda: INITIAL_ACCOUNT_BALANCE)]
        _l_(562271)
        _n_(562272, "self", lambda: self).day = 374
        _l_(562273)
        _n_(562274, "self", lambda: self).cost = 0
        _l_(562275)
        _n_(562276, "self", lambda: self).trades = 0
        _l_(562277)
        _n_(562278, "self", lambda: self).terminal = False
        _l_(562279)
        _n_(562280, "self", lambda: self).rewards_memory = []
        _l_(562281)

        _n_(562282, "self", lambda: self).state = [_n_(562283, "INITIAL_ACCOUNT_BALANCE", lambda: INITIAL_ACCOUNT_BALANCE)] + [0] + _c_(562293, _a_(562292, _a_(562286, _a_(562285, _n_(562284, "self", lambda: self), "df"), "iloc")[_a_(562288, _n_(562287, "self", lambda: self), "day")-_n_(562289, "N", lambda: N):_a_(562291, _n_(562290, "self", lambda: self), "day"),1], "tolist")) + \
                        _c_(562303, _a_(562302, _a_(562296, _a_(562295, _n_(562294, "self", lambda: self), "df"), "iloc")[_a_(562298, _n_(562297, "self", lambda: self), "day")-_n_(562299, "N", lambda: N):_a_(562301, _n_(562300, "self", lambda: self), "day"),2], "tolist")) + _c_(562313, _a_(562312, _a_(562306, _a_(562305, _n_(562304, "self", lambda: self), "df"), "iloc")[_a_(562308, _n_(562307, "self", lambda: self), "day")-_n_(562309, "N", lambda: N):_a_(562311, _n_(562310, "self", lambda: self), "day"),3], "tolist")) + \
                        _c_(562323, _a_(562322, _a_(562316, _a_(562315, _n_(562314, "self", lambda: self), "df"), "iloc")[_a_(562318, _n_(562317, "self", lambda: self), "day")-_n_(562319, "N", lambda: N):_a_(562321, _n_(562320, "self", lambda: self), "day"),4], "tolist")) + _c_(562333, _a_(562332, _a_(562326, _a_(562325, _n_(562324, "self", lambda: self), "df"), "iloc")[_a_(562328, _n_(562327, "self", lambda: self), "day")-_n_(562329, "N", lambda: N):_a_(562331, _n_(562330, "self", lambda: self), "day"),5], "tolist")) + \
                        _c_(562343, _a_(562342, _a_(562336, _a_(562335, _n_(562334, "self", lambda: self), "df"), "iloc")[_a_(562338, _n_(562337, "self", lambda: self), "day")-_n_(562339, "N", lambda: N):_a_(562341, _n_(562340, "self", lambda: self), "day"),6], "tolist")) + _c_(562353, _a_(562352, _a_(562346, _a_(562345, _n_(562344, "self", lambda: self), "df"), "iloc")[_a_(562348, _n_(562347, "self", lambda: self), "day")-_n_(562349, "N", lambda: N):_a_(562351, _n_(562350, "self", lambda: self), "day"),7], "tolist"))
        _l_(562354)
        aux = _a_(562356, _n_(562355, "self", lambda: self), "state")
        _l_(562357)
        return aux

    def render(self,mode='human'):
        _l_(562362)

        aux = _a_(562360, _n_(562359, "self", lambda: self), "state")
        _l_(562361)
        return aux

    def _seed(self,seed=None):
        _l_(562371)

        _n_(562363, "self", lambda: self).np_random, seed = _c_(562367, _a_(562365, _n_(562364, "seeding", lambda: seeding), "np_random"), _n_(562366, "seed", lambda: seed))
        _l_(562368)
        aux = [_n_(562369, "seed", lambda: seed)]
        _l_(562370)
        return aux