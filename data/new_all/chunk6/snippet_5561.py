# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49112402/typeerror-unsupported-operand-types-for-float-and-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ratio_Production_Budget = _c_(371737, _n_(371727, "abs", lambda: abs), (_c_(371730, _a_(371729, _n_(371728, "df_data", lambda: df_data)['Production Budget'], "mean")) - _c_(371733, _a_(371732, _n_(371731, "df_data", lambda: df_data)['Production Budget'], "median"))) / _c_(371736, _a_(371735, _n_(371734, "df_data", lambda: df_data)['Production Budget'], "median")))
_l_(371738)
ratio_Worldwide_Gross = _c_(371749, _n_(371739, "abs", lambda: abs), (_c_(371742, _a_(371741, _n_(371740, "df_data", lambda: df_data)['Worldwide Gross'], "mean")) - _c_(371745, _a_(371744, _n_(371743, "df_data", lambda: df_data)['Worldwide Gross'], "median"))) / _c_(371748, _a_(371747, _n_(371746, "df_data", lambda: df_data)['Worldwide Gross'], "median")))
_l_(371750)
ratio_quarter = _c_(371761, _n_(371751, "abs", lambda: abs), (_c_(371754, _a_(371753, _n_(371752, "df_data", lambda: df_data)['quarter'], "mean")) - _c_(371757, _a_(371756, _n_(371755, "df_data", lambda: df_data)['quarter'], "median"))) / _c_(371760, _a_(371759, _n_(371758, "df_data", lambda: df_data)['quarter'], "median")))
_l_(371762)
ratio_duration = _c_(371773, _n_(371763, "abs", lambda: abs), (_c_(371766, _a_(371765, _n_(371764, "df_data", lambda: df_data)['duration'], "mean")) - _c_(371769, _a_(371768, _n_(371767, "df_data", lambda: df_data)['duration'], "median"))) / _c_(371772, _a_(371771, _n_(371770, "df_data", lambda: df_data)['duration'], "median")))
_l_(371774)
ratio_actor_1_facebook_likes = _c_(371785, _n_(371775, "abs", lambda: abs), (_c_(371778, _a_(371777, _n_(371776, "df_data", lambda: df_data)['actor_1_facebook_likes'], "mean")) - _c_(371781, _a_(371780, _n_(371779, "df_data", lambda: df_data)['actor_1_facebook_likes'], "median"))) / _c_(371784, _a_(371783, _n_(371782, "df_data", lambda: df_data)['actor_1_facebook_likes'], "median")))
_l_(371786)
ratio_imdb_score = _c_(371797, _n_(371787, "abs", lambda: abs), (_c_(371790, _a_(371789, _n_(371788, "df_data", lambda: df_data)['imdb_score'], "mean")) - _c_(371793, _a_(371792, _n_(371791, "df_data", lambda: df_data)['imdb_score'], "median"))) / _c_(371796, _a_(371795, _n_(371794, "df_data", lambda: df_data)['imdb_score'], "median")))
_l_(371798)
ratio_weekendTotal = _c_(371808, _n_(371799, "abs", lambda: abs), (_c_(371802, _a_(371801, _n_(371800, "df_data", lambda: df_data)['weekendTotal'], "mean")) - _c_(371805, _a_(371804, _n_(371803, "df_data", lambda: df_data)['weekendTotal'], "median"))) / _a_(371807, _n_(371806, "df_data", lambda: df_data)['weekendTotal'], "median"))
_l_(371809)
ratio_midweekTotal = _c_(371819, _n_(371810, "abs", lambda: abs), (_c_(371813, _a_(371812, _n_(371811, "df_data", lambda: df_data)['midweekTotal'], "mean")) - _c_(371816, _a_(371815, _n_(371814, "df_data", lambda: df_data)['midweekTotal'], "median"))) / _a_(371818, _n_(371817, "df_data", lambda: df_data)['midweekTotal'], "median"))
_l_(371820)

w1_mm = _c_(371831, _a_(371822, _n_(371821, "pd", lambda: pd), "Series"), data= [_n_(371823, "ratio_Production_Budget", lambda: ratio_Production_Budget), _n_(371824, "ration_Worldwide_Gross", lambda: ration_Worldwide_Gross), _n_(371825, "ratio_quarter", lambda: ratio_quarter), _n_(371826, "ratio_duration", lambda: ratio_duration), _n_(371827, "ratio_actor_1_facebook_likes", lambda: ratio_actor_1_facebook_likes), _n_(371828, "ratio_imdb_score", lambda: ratio_imdb_score), _n_(371829, "ratio_weekendTotal", lambda: ratio_weekendTotal), _n_(371830, "ratio_midweekTotal", lambda: ratio_midweekTotal)],
                          index = ['Production Budget', 'Worldwide Gross', 'quarter', 'duration', 'actor_1_facebook_likes', 'imdb_score', 'weekendTotal', 'midweekTotal'])
_l_(371832)