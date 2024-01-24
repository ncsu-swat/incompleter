# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62526457/attributeerror-series-object-has-no-attribute-df-hotel
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
perc_country_df_hotel = _a_(648667, _c_(648666, _a_(648657, _n_(648656, "pd", lambda: pd), "DataFrame"), [_c_(648663, _a_(648662, _a_(648661, _c_(648660, _a_(648659, _n_(648658, "df_hotel", lambda: df_hotel)['country'], "value_counts")), "df_hotel")['country'], "value_counts"))*100/_a_(648665, _n_(648664, "df_hotel", lambda: df_hotel), "shape")[0]]), "T")
_l_(648668)
_n_(648669, "perc_country_df_Hotel", lambda: perc_country_df_Hotel).columns = ['Count', '% Distribution']
_l_(648670)
_n_(648671, "perc_country_df_hotel", lambda: perc_country_df_hotel)
_l_(648672)

#then, 
_c_(648675, _a_(648674, _n_(648673, "df_hotel", lambda: df_hotel)['country'], "fillna"), 'CountryWithBigPercentage', inplace= True)
_l_(648676)