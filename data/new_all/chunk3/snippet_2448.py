# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32611322/receiving-type-error-0-while-updating-pandas-df-using-data-nitro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for m in _c_(526465, _n_(526461, "range", lambda: range), 0,_c_(526464, _n_(526462, "len", lambda: len), _n_(526463, "product_sales_price", lambda: product_sales_price))):
                _l_(526561)

                if _c_(526475, _n_(526466, "exact_match", lambda: exact_match), _c_(526470, _n_(526467, "str", lambda: str), _n_(526468, "sales_record", lambda: sales_record)[_n_(526469, "n", lambda: n)-1]),_c_(526474, _n_(526471, "str", lambda: str), _n_(526472, "product_sales_price", lambda: product_sales_price)[_n_(526473, "m", lambda: m)]))==True:
                                _l_(526509)


                                total_product_daily_sales = _n_(526476, "counter", lambda: counter) * _n_(526477, "product_sales_price", lambda: product_sales_price)[_n_(526478, "m", lambda: m)+1]
                                _l_(526479)
                                '''
                    print(total_product_daily_sales)
                    '''
                                _l_(526480)

                                total_product_daily_net_profit = _n_(526481, "total_product_daily_sales", lambda: total_product_daily_sales) *.1
                                _l_(526482)


                                _c_(526485, _n_(526483, "print", lambda: print), _n_(526484, "counter", lambda: counter))
                                _l_(526486)
                                _c_(526490, _n_(526487, "print", lambda: print), _n_(526488, "product_sales_price", lambda: product_sales_price)[_n_(526489, "m", lambda: m)+1])
                                _l_(526491)
                                _c_(526494, _n_(526492, "print", lambda: print), _n_(526493, "total_product_daily_sales", lambda: total_product_daily_sales))
                                _l_(526495)
                                _c_(526498, _n_(526496, "print", lambda: print), _n_(526497, "total_product_daily_net_profit", lambda: total_product_daily_net_profit))
                                _l_(526499)
                                _c_(526502, _n_(526500, "print", lambda: print), _n_(526501, "m", lambda: m))
                                _l_(526503)
                                _c_(526507, _n_(526504, "print", lambda: print), _n_(526505, "product_sales_price", lambda: product_sales_price)[_n_(526506, "m", lambda: m)])
                                _l_(526508)


                if _c_(526515, _a_(526514, (_a_(526511, _n_(526510, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "ix")[:,0] ==  _n_(526512, "product_sales_price", lambda: product_sales_price)[_n_(526513, "m", lambda: m)]), "any")) == True :
                                _l_(526560)


                                _a_(526517, _n_(526516, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "ix")[:,:][(_a_(526519, _n_(526518, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "ix")[:,
                                                                           0] ==  _n_(526520, "product_sales_price", lambda: product_sales_price)[_n_(526521, "m", lambda: m)])] = [
                                    _a_(526523, _n_(526522, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "ix")[:,0][(_a_(526525, _n_(526524, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "ix")[:,
                                                                           0] ==  _n_(526526, "product_sales_price", lambda: product_sales_price)[_n_(526527, "m", lambda: m)])],
                                    _a_(526529, _n_(526528, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "ix")[:,1][(_a_(526531, _n_(526530, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "ix")[:,
                                                                           0] ==  _n_(526532, "product_sales_price", lambda: product_sales_price)[_n_(526533, "m", lambda: m)])]+_n_(526534, "counter", lambda: counter),
                                    _a_(526536, _n_(526535, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "ix")[:,2][(_a_(526538, _n_(526537, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "ix")[:,
                                                                           0] ==  _n_(526539, "product_sales_price", lambda: product_sales_price)[
                                        _n_(526540, "m", lambda: m)])]+_n_(526541, "total_product_daily_sales", lambda: total_product_daily_sales),_a_(526543, _n_(526542, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "ix")[:,
                                                                       3][(_a_(526545, _n_(526544, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "ix")[:,0] ==  _n_(526546, "product_sales_price", lambda: product_sales_price)[
                                        _n_(526547, "m", lambda: m)])]+_n_(526548, "total_product_daily_net_profit", lambda: total_product_daily_net_profit)]
                                _l_(526549)
                else:

                    _a_(526551, _n_(526550, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "ix")[(_a_(526553, _n_(526552, "product_revenue_and_net_profit_df", lambda: product_revenue_and_net_profit_df), "shape")[0]+1),:] = (
                        [_n_(526554, "product_sales_price", lambda: product_sales_price)[_n_(526555, "m", lambda: m)],_n_(526556, "counter", lambda: counter),_n_(526557, "total_product_daily_sales", lambda: total_product_daily_sales),
                         _n_(526558, "total_product_daily_net_profit", lambda: total_product_daily_net_profit)]
                        )             
                    _l_(526559)             