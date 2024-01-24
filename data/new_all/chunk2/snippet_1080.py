# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41320337/attributeerror-type-object-minimalfeatureextractionsettings-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
settings= _c_(454095, _n_(454094, "MinimalFeatureExtractionSettings", lambda: MinimalFeatureExtractionSettings))
_l_(454096)

extracted_features = _c_(454100, _n_(454097, "extract_features", lambda: extract_features), _n_(454098, "df_to_extract", lambda: df_to_extract), 
                                      column_id="id", 
                                      column_sort="time", 
                                      parallelization= 'per_kind', 
                                      feature_extraction_settings= _n_(454099, "settings", lambda: settings))
_l_(454101)