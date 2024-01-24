# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54593676/how-to-fix-featurtools-type-error-on-colab
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(459410)

except ImportError:
    pass
try:
    import featuretools as ft
    _l_(459412)

except ImportError:
    pass

df1 = _c_(459415, _a_(459414, _n_(459413, "pd", lambda: pd), "DataFrame"), {'df_index' : [1,2,3,4,5],
                 'location':['aust','aust','aust','canada','canada'],
                  'prices':[34,52,46,25,67],
                   'values':[786,345,123,654,841]
                  })
_l_(459416)

es = _c_(459419, _a_(459418, _n_(459417, "ft", lambda: ft), "EntitySet"), id='Transactions')
_l_(459420)

_c_(459424, _a_(459422, _n_(459421, "es", lambda: es), "entity_from_dataframe"), entity_id='log', 
                         dataframe=_n_(459423, "df1", lambda: df1), 
                         index='df_index',
                         time_index='date'
                        )
_l_(459425)

_c_(459428, _a_(459427, _n_(459426, "es", lambda: es), "normalize_entity"), base_entity_id='log', new_entity_id='loc', index= 'location' )
_l_(459429)


fm, features = _c_(459433, _a_(459431, _n_(459430, "ft", lambda: ft), "dfs"), entityset=_n_(459432, "es", lambda: es), target_entity='log',
                      trans_primitives = ['add', 'multiply'],
                      agg_primitives = ['sum', 'mean'],
                      max_depth = 2,
                      verbose = 2
                     )
_l_(459434)