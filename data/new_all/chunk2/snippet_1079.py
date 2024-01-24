# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41320337/attributeerror-type-object-minimalfeatureextractionsettings-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(468151)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(468153)

except ImportError:
    pass

column_names = ['time_series1', 'time_series2','time_series3']
_l_(468154)
ts = _c_(468158, _a_(468157, _a_(468156, _n_(468155, "np", lambda: np), "random"), "rand"), 6,3)
_l_(468159)


df_to_extract = _c_(468164, _a_(468161, _n_(468160, "pd", lambda: pd), "DataFrame"), data=_n_(468162, "ts", lambda: ts), columns = _n_(468163, "column_names", lambda: column_names))
_l_(468165)

_n_(468166, "df_to_extract", lambda: df_to_extract)['id'] = 1
_l_(468167)
_n_(468168, "df_to_extract", lambda: df_to_extract)['time'] = _c_(468171, _a_(468170, _n_(468169, "np", lambda: np), "arange"), 1,7)
_l_(468172)
try:
    import tsfresh
    _l_(468174)

except ImportError:
    pass
try:
    from tsfresh import extract_features
    _l_(468176)

except ImportError:
    pass
try:
    from tsfresh import select_features
    _l_(468178)

except ImportError:
    pass
try:
    from tsfresh.utilities.dataframe_functions import impute
    _l_(468180)

except ImportError:
    pass
try:
    from tsfresh import extract_relevant_features
    _l_(468182)

except ImportError:
    pass
try:
    from tsfresh.feature_extraction import extract_features, MinimalFeatureExtractionSettings
    _l_(468184)

except ImportError:
    pass
try:
    from tsfresh.feature_extraction.settings import *
    _l_(468186)

except ImportError:
    pass
try:
    from tsfresh.feature_extraction.settings import FeatureExtractionSettings
    _l_(468188)

except ImportError:
    pass
try:
    import tsfresh.feature_extraction.settings
    _l_(468190)

except ImportError:
    pass
try:
    from tsfresh import utilities
    _l_(468192)

except ImportError:
    pass
try:
    from tsfresh import feature_extraction
    _l_(468194)

except ImportError:
    pass


extracted_features = _c_(468198, _n_(468195, "extract_features", lambda: extract_features), _n_(468196, "df_to_extract", lambda: df_to_extract), 
                                      column_id="id", 
                                      column_sort="time", 
                                      parallelization= 'per_kind', 
                                      feature_extraction_settings= _n_(468197, "MinimalFeatureExtractionSettings", lambda: MinimalFeatureExtractionSettings))
_l_(468199)