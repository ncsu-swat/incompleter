# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50608941/typeerror-column-object-is-not-callable-when-use-case-when
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(342222)

except ImportError:
    pass
try:
    from pyspark.sql.window import Window
    _l_(342224)

except ImportError:
    pass
try:
    from pyspark.sql import Row
    _l_(342226)

except ImportError:
    pass
try:
    import pyspark.sql.functions as func
    _l_(342228)

except ImportError:
    pass
try:
    from pyspark.sql import DataFrameStatFunctions as statFunc
    _l_(342230)

except ImportError:
    pass
try:
    from pyspark.sql.functions import coalesce, current_date, current_timestamp, lit, unix_timestamp, from_unixtime, \
    row_number, mean
    _l_(342232)

except ImportError:
    pass

a_df = _c_(342235, _a_(342234, _n_(342233, "sqlContext", lambda: sqlContext), "table"), 'opssup_dev_wrk_ct.wrk_ct_ods_batch_derived_extnd_stg2')
_l_(342236)
b_df = _c_(342239, _a_(342238, _n_(342237, "sqlContext", lambda: sqlContext), "table"), 'opssup_dev_wrk_ct.wrk_ct_sap_batch_specific_dates')
_l_(342240)
fdsi_df = _c_(342243, _a_(342242, _n_(342241, "sqlContext", lambda: sqlContext), "table"), 'opssup_dev_wrk_ct.wrk_ct_sap_batch_specific_dates')
_l_(342244)
ldsi_df = _c_(342247, _a_(342246, _n_(342245, "sqlContext", lambda: sqlContext), "table"), 'opssup_dev_wrk_ct.wrk_ct_sap_batch_specific_dates')
_l_(342248)
fds_df = _c_(342251, _a_(342250, _n_(342249, "sqlContext", lambda: sqlContext), "table"), 'opssup_dev_wrk_ct.wrk_ct_sap_batch_specific_dates')
_l_(342252)
temp22_df = _c_(342306, _a_(342282, _c_(342281, _a_(342275, _c_(342274, _a_(342268, _c_(342267, _a_(342261, _c_(342260, _a_(342254, _n_(342253, "a_df", lambda: a_df), "join"), _n_(342255, "b_df", lambda: b_df),(_a_(342257, _n_(342256, "a_df", lambda: a_df), "batch_number")==_a_(342259, _n_(342258, "b_df", lambda: b_df), "Batch_Number"))), "join"), _n_(342262, "fdsi_df", lambda: fdsi_df),(_a_(342264, _n_(342263, "a_df", lambda: a_df), "First_DSI_BATCH_NUMBER")==_a_(342266, _n_(342265, "fdsi_df", lambda: fdsi_df), "Batch_Number")),"left_outer"), "join"), _n_(342269, "ldsi_df", lambda: ldsi_df),(_a_(342271, _n_(342270, "a_df", lambda: a_df), "Last_DSI_BATCH_NUMBER")==_a_(342273, _n_(342272, "ldsi_df", lambda: ldsi_df), "Batch_Number")),"left_outer"), "join"), _n_(342276, "fds_df", lambda: fds_df),(_a_(342278, _n_(342277, "a_df", lambda: a_df), "First_DS_BATCH_NUMBER")==_a_(342280, _n_(342279, "fds_df", lambda: fds_df), "Batch_Number")),"left_outer"), "select"), _a_(342284, _n_(342283, "a_df", lambda: a_df), "driving_batch_number"), \
        _a_(342286, _n_(342285, "a_df", lambda: a_df), "batch_number"), \
        _a_(342288, _n_(342287, "b_df", lambda: b_df), "Material_Group"), \
        _a_(342290, _n_(342289, "a_df", lambda: a_df), "mfg_stage_code"), \
        _c_(342305, _a_(342304, _c_(342303, _a_(342300, _c_(342299, _a_(342292, _n_(342291, "func", lambda: func), "when"), _a_(342294, _n_(342293, "a_df", lambda: a_df), "batch_number")==_a_(342296, _n_(342295, "a_df", lambda: a_df), "First_DSI_BATCH_NUMBER"),_c_(342298, _n_(342297, "lit", lambda: lit), '0')), "otherwisw"), _c_(342302, _n_(342301, "lit", lambda: lit), '')), "alias"), 'mfg_start_date') \
           )
_l_(342307)