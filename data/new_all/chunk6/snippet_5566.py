# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49112402/typeerror-unsupported-operand-types-for-float-and-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ratio_Production_Budget = _c_(338070, _n_(338060, "abs", lambda: abs), (_c_(338063, _a_(338062, _n_(338061, "df_data", lambda: df_data)['Production Budget'], "mean")) - _c_(338066, _a_(338065, _n_(338064, "df_data", lambda: df_data)['Production Budget'], "median"))) / _c_(338069, _a_(338068, _n_(338067, "df_data", lambda: df_data)['Production Budget'], "median")))
_l_(338071)
ratio_Worldwide_Gross = _c_(338082, _n_(338072, "abs", lambda: abs), (_c_(338075, _a_(338074, _n_(338073, "df_data", lambda: df_data)['Worldwide Gross'], "mean")) - _c_(338078, _a_(338077, _n_(338076, "df_data", lambda: df_data)['Worldwide Gross'], "median"))) / _c_(338081, _a_(338080, _n_(338079, "df_data", lambda: df_data)['Worldwide Gross'], "median")))
_l_(338083)
ratio_quarter = _c_(338094, _n_(338084, "abs", lambda: abs), (_c_(338087, _a_(338086, _n_(338085, "df_data", lambda: df_data)['quarter'], "mean")) - _c_(338090, _a_(338089, _n_(338088, "df_data", lambda: df_data)['quarter'], "median"))) / _c_(338093, _a_(338092, _n_(338091, "df_data", lambda: df_data)['quarter'], "median")))
_l_(338095)
ratio_duration = _c_(338106, _n_(338096, "abs", lambda: abs), (_c_(338099, _a_(338098, _n_(338097, "df_data", lambda: df_data)['duration'], "mean")) - _c_(338102, _a_(338101, _n_(338100, "df_data", lambda: df_data)['duration'], "median"))) / _c_(338105, _a_(338104, _n_(338103, "df_data", lambda: df_data)['duration'], "median")))
_l_(338107)
ratio_actor_1_facebook_likes = _c_(338118, _n_(338108, "abs", lambda: abs), (_c_(338111, _a_(338110, _n_(338109, "df_data", lambda: df_data)['actor_1_facebook_likes'], "mean")) - _c_(338114, _a_(338113, _n_(338112, "df_data", lambda: df_data)['actor_1_facebook_likes'], "median"))) / _c_(338117, _a_(338116, _n_(338115, "df_data", lambda: df_data)['actor_1_facebook_likes'], "median")))
_l_(338119)
ratio_imdb_score = _c_(338130, _n_(338120, "abs", lambda: abs), (_c_(338123, _a_(338122, _n_(338121, "df_data", lambda: df_data)['imdb_score'], "mean")) - _c_(338126, _a_(338125, _n_(338124, "df_data", lambda: df_data)['imdb_score'], "median"))) / _c_(338129, _a_(338128, _n_(338127, "df_data", lambda: df_data)['imdb_score'], "median")))
_l_(338131)
ratio_weekendTotal = _c_(338141, _n_(338132, "abs", lambda: abs), (_c_(338135, _a_(338134, _n_(338133, "df_data", lambda: df_data)['weekendTotal'], "mean")) - _c_(338138, _a_(338137, _n_(338136, "df_data", lambda: df_data)['weekendTotal'], "median"))) / _a_(338140, _n_(338139, "df_data", lambda: df_data)['weekendTotal'], "median"))
_l_(338142)
ratio_midweekTotal = _c_(338152, _n_(338143, "abs", lambda: abs), (_c_(338146, _a_(338145, _n_(338144, "df_data", lambda: df_data)['midweekTotal'], "mean")) - _c_(338149, _a_(338148, _n_(338147, "df_data", lambda: df_data)['midweekTotal'], "median"))) / _a_(338151, _n_(338150, "df_data", lambda: df_data)['midweekTotal'], "median"))
_l_(338153)

w1_mm = _c_(338164, _a_(338155, _n_(338154, "pd", lambda: pd), "Series"), data= [_n_(338156, "ratio_Production_Budget", lambda: ratio_Production_Budget), _n_(338157, "ration_Worldwide_Gross", lambda: ration_Worldwide_Gross), _n_(338158, "ratio_quarter", lambda: ratio_quarter), _n_(338159, "ratio_duration", lambda: ratio_duration), _n_(338160, "ratio_actor_1_facebook_likes", lambda: ratio_actor_1_facebook_likes), _n_(338161, "ratio_imdb_score", lambda: ratio_imdb_score), _n_(338162, "ratio_weekendTotal", lambda: ratio_weekendTotal), _n_(338163, "ratio_midweekTotal", lambda: ratio_midweekTotal)],
                          index = ['Production Budget', 'Worldwide Gross', 'quarter', 'duration', 'actor_1_facebook_likes', 'imdb_score', 'weekendTotal', 'midweekTotal'])
_l_(338165)