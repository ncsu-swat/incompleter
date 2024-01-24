# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65552218/how-to-fix-attributeerror-nonetype-object-has-no-attribute-locpandas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
     import pandas as pd
     _l_(442174)

except ImportError:
     pass

data = _c_(442177, _a_(442176, _n_(442175, "pd", lambda: pd), "read_csv"), 'sample.csv',delimiter=',')
_l_(442178)

def mapping(df):
     _l_(442197)

     #work of data mapping
     for column_name, column in _c_(442183, _a_(442182, _c_(442181, _a_(442180, _n_(442179, "df", lambda: df), "transpose")), "iterrows")):
          _l_(442196)

          _c_(442186, _a_(442185, _n_(442184, "df", lambda: df), "rename"), columns ={'first name' : 'FNAME', 'secret': 'CODE'}, inplace = True)
          _l_(442187)
          _c_(442190, _a_(442189, _n_(442188, "df", lambda: df), "rename"), columns ={'alias' : 'FNAME', 'code': 'CODE'}, inplace = True)
          _l_(442191)
          _c_(442194, _a_(442193, _n_(442192, "df", lambda: df), "rename"), columns ={'initial name' : 'FNAME', 'id': 'CODE'}, inplace = True)
          _l_(442195)

final_df = _c_(442200, _n_(442198, "mapping", lambda: mapping), _n_(442199, "data", lambda: data))
_l_(442201)

#If the code is greater than 12 digits, leave it blank
_a_(442203, _n_(442202, "final_df", lambda: final_df), "loc")[_c_(442210, _a_(442209, _a_(442208, _c_(442207, _a_(442205, _n_(442204, "final_df", lambda: final_df)['CODE'], "astype"), _n_(442206, "str", lambda: str)), "str"), "len")) >12, 'CODE']= ''
_l_(442211)