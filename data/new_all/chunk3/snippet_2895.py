# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59214111/how-to-resolve-attributeerror-when-trying-to-set-none-as-default-method-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sa_reporting
    _l_(538503)

except ImportError:
    pass
try:
    from sa_body import *
    _l_(538505)

except ImportError:
    pass

dim_campaign_test = _c_(538509, _a_(538507, _n_(538506, "sa_reporting", lambda: sa_reporting), "saReport"), body=_n_(538508, "dim_campaign_body", lambda: dim_campaign_body),
    to_table='dimsa360CampaignTest',
    normalise=True,
    date_col=[4,5]
)
_l_(538510)
dim_campaign_test_download = _c_(538513, _a_(538512, _n_(538511, "dim_campaign_test", lambda: dim_campaign_test), "download_reports"))
_l_(538514)
_c_(538517, _a_(538516, _n_(538515, "dim_campaign_test_download", lambda: dim_campaign_test_download), "load_to_db"), sort_by=0) # THIS IS WHERE THE ERROR OCCURS
_l_(538518) # THIS IS WHERE THE ERROR OCCURS