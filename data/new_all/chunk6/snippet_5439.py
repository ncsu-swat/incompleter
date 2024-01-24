# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50608941/typeerror-column-object-is-not-callable-when-use-case-when
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(356453)

except ImportError:
    pass
try:
    from pyspark.sql.window import Window
    _l_(356455)

except ImportError:
    pass
try:
    from pyspark.sql import Row
    _l_(356457)

except ImportError:
    pass
try:
    import pyspark.sql.functions as func
    _l_(356459)

except ImportError:
    pass
try:
    from pyspark.sql import DataFrameStatFunctions as statFunc
    _l_(356461)

except ImportError:
    pass
try:
    from pyspark.sql.functions import coalesce, current_date, current_timestamp, lit, unix_timestamp, from_unixtime, \
    row_number, mean
    _l_(356463)

except ImportError:
    pass

a_df = _c_(356466, _a_(356465, _n_(356464, "sqlContext", lambda: sqlContext), "table"), 'opssup_dev_wrk_ct.wrk_ct_ods_batch_derived_extnd_stg2')
_l_(356467)
b_df = _c_(356470, _a_(356469, _n_(356468, "sqlContext", lambda: sqlContext), "table"), 'opssup_dev_wrk_ct.wrk_ct_sap_batch_specific_dates')
_l_(356471)
fdsi_df = _c_(356474, _a_(356473, _n_(356472, "sqlContext", lambda: sqlContext), "table"), 'opssup_dev_wrk_ct.wrk_ct_sap_batch_specific_dates')
_l_(356475)
ldsi_df = _c_(356478, _a_(356477, _n_(356476, "sqlContext", lambda: sqlContext), "table"), 'opssup_dev_wrk_ct.wrk_ct_sap_batch_specific_dates')
_l_(356479)
fds_df = _c_(356482, _a_(356481, _n_(356480, "sqlContext", lambda: sqlContext), "table"), 'opssup_dev_wrk_ct.wrk_ct_sap_batch_specific_dates')
_l_(356483)
temp22_df = _c_(356537, _a_(356513, _c_(356512, _a_(356506, _c_(356505, _a_(356499, _c_(356498, _a_(356492, _c_(356491, _a_(356485, _n_(356484, "a_df", lambda: a_df), "join"), _n_(356486, "b_df", lambda: b_df),(_a_(356488, _n_(356487, "a_df", lambda: a_df), "batch_number")==_a_(356490, _n_(356489, "b_df", lambda: b_df), "Batch_Number"))), "join"), _n_(356493, "fdsi_df", lambda: fdsi_df),(_a_(356495, _n_(356494, "a_df", lambda: a_df), "First_DSI_BATCH_NUMBER")==_a_(356497, _n_(356496, "fdsi_df", lambda: fdsi_df), "Batch_Number")),"left_outer"), "join"), _n_(356500, "ldsi_df", lambda: ldsi_df),(_a_(356502, _n_(356501, "a_df", lambda: a_df), "Last_DSI_BATCH_NUMBER")==_a_(356504, _n_(356503, "ldsi_df", lambda: ldsi_df), "Batch_Number")),"left_outer"), "join"), _n_(356507, "fds_df", lambda: fds_df),(_a_(356509, _n_(356508, "a_df", lambda: a_df), "First_DS_BATCH_NUMBER")==_a_(356511, _n_(356510, "fds_df", lambda: fds_df), "Batch_Number")),"left_outer"), "select"), _a_(356515, _n_(356514, "a_df", lambda: a_df), "driving_batch_number"), \
        _a_(356517, _n_(356516, "a_df", lambda: a_df), "batch_number"), \
        _a_(356519, _n_(356518, "b_df", lambda: b_df), "Material_Group"), \
        _a_(356521, _n_(356520, "a_df", lambda: a_df), "mfg_stage_code"), \
        _c_(356536, _a_(356535, _c_(356534, _a_(356531, _c_(356530, _a_(356523, _n_(356522, "func", lambda: func), "when"), _a_(356525, _n_(356524, "a_df", lambda: a_df), "batch_number")==_a_(356527, _n_(356526, "a_df", lambda: a_df), "First_DSI_BATCH_NUMBER"),_c_(356529, _n_(356528, "lit", lambda: lit), '0')), "otherwisw"), _c_(356533, _n_(356532, "lit", lambda: lit), '')), "alias"), 'mfg_start_date') \
           )
_l_(356538)