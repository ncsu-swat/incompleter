# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58256867/attributeerror-dataframe-object-has-no-attribute-net-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(532492)

except ImportError:
    pass
try:
    import os
    _l_(532494)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(532496)

except ImportError:
    pass
try:
    import datetime
    _l_(532498)

except ImportError:
    pass
try:
    import numpy as np
    _l_(532500)

except ImportError:
    pass
try:
    from time import gmtime, strftime
    _l_(532502)

except ImportError:
    pass
WCOUNT=_c_(532506, _n_(532503, "strftime", lambda: strftime), "%V", _c_(532505, _n_(532504, "gmtime", lambda: gmtime)))
_l_(532507)
WCOUNT = _c_(532510, _n_(532508, "int", lambda: int), _n_(532509, "WCOUNT", lambda: WCOUNT))
_l_(532511)
WCOUNT_last = _c_(532514, _n_(532512, "int", lambda: int), _n_(532513, "WCOUNT", lambda: WCOUNT))-1
_l_(532515)
_a_(532517, _n_(532516, "os", lambda: os), "environ")['NLS_LANG'] = 'Russian.AL32UTF8'
_l_(532518)

cell_file_list=_c_(532521, _a_(532520, _n_(532519, "pd", lambda: pd), "read_excel"), 'cdt_config.xlsx',sheet_name ='cdt_config',index_col='para_name')
_l_(532522)
filial_name_list=_c_(532525, _a_(532524, _n_(532523, "pd", lambda: pd), "read_excel"), 'FILIAL_NAME.xlsx')
_l_(532526)
gcell_file_name1=_a_(532529, _a_(532528, _n_(532527, "cell_file_list", lambda: cell_file_list), "para_value"), "loc")['ucell_file_name']
_l_(532530)
ecell_file_name=_a_(532533, _a_(532532, _n_(532531, "cell_file_list", lambda: cell_file_list), "para_value"), "loc")['ecell_file_name']
_l_(532534)
cols_simple=['RECDATE','REGION_PHOENIX_NAME','NET_NAME','CELL_NAME_IN_BSC','ENODEB_NAME','ECELL_TYPE','NRI_ADDRESS', 'NRI_BS_NUMBER','NRI_SITEID','STOPTIME',  ]
_l_(532535)
cols_export=['GSM', 'UMTS', 'LTE', 'TOTAL', 'NWEEK', 'SHARING' ]
_l_(532536)
ecell_df=df = _c_(532541, _a_(532538, _n_(532537, "pd", lambda: pd), "read_csv"), _n_(532539, "ecell_file_name", lambda: ecell_file_name), sep=",",encoding='cp1251',
                dtype={'NRI_SITEID': _n_(532540, "str", lambda: str)})
_l_(532542)

ecell_df=_c_(532545, _a_(532544, _n_(532543, "ecell_df", lambda: ecell_df), "rename"), columns={"RECDATE.DATE": "RECDATE"})
_l_(532546)
ecell_df=_c_(532549, _a_(532548, _n_(532547, "ecell_df", lambda: ecell_df), "rename"), columns={"ECELL_MNEMONIC": "CELL_NAME_IN_BSC"})
_l_(532550)

#replace ","
_n_(532551, "ecell_df", lambda: ecell_df).STOPTIME=_c_(532558, _a_(532553, _n_(532552, "pd", lambda: pd), "to_numeric"), _c_(532557, _a_(532556, _a_(532555, _n_(532554, "ecell_df", lambda: ecell_df), "STOPTIME"), "replace"), ',', '', regex=True), errors='coerce')/3600
_l_(532559)
ecell_df=_n_(532560, "ecell_df", lambda: ecell_df)[_n_(532561, "cols_simple", lambda: cols_simple)]
_l_(532562)
#pivot ecell table
ecell_sum_df=_c_(532566, _a_(532564, _n_(532563, "pd", lambda: pd), "pivot_table"), _n_(532565, "ecell_df", lambda: ecell_df),values='STOPTIME',index=['RECDATE','NRI_SITEID','REGION_PHOENIX_NAME','NET_NAME','ENODEB_NAME','ECELL_TYPE'],aggfunc='sum')
_l_(532567)
ecell_sum_df=_c_(532570, _a_(532569, _n_(532568, "ecell_sum_df", lambda: ecell_sum_df), "fillna"), 0)
_l_(532571)
#create a empty column with the same index as the pivot table.
ecell_export_df= _c_(532578, _a_(532573, _n_(532572, "pd", lambda: pd), "DataFrame"), index=_c_(532577, _a_(532576, _a_(532575, _n_(532574, "ecell_sum_df", lambda: ecell_sum_df), "index"), "copy")))
_l_(532579)
ecell_export_df=_c_(532582, _a_(532581, _n_(532580, "ecell_export_df", lambda: ecell_export_df), "assign"), LTE=0)
_l_(532583)
_n_(532584, "ecell_export_df", lambda: ecell_export_df).LTE=_a_(532586, _n_(532585, "ecell_sum_df", lambda: ecell_sum_df), "STOPTIME")
_l_(532587)
_n_(532588, "ecell_export_df", lambda: ecell_export_df)['SHARING'] = 0
_l_(532589)
_c_(532597, _a_(532592, _a_(532591, _n_(532590, "ecell_export_df", lambda: ecell_export_df), "SHARING"), "replace"), _a_(532594, _n_(532593, "ecell_export_df", lambda: ecell_export_df), "NET_NAME") in _n_(532595, "filial_name_list", lambda: filial_name_list), _n_(532596, "ENODEB_NAME", lambda: ENODEB_NAME),inplace=True)
_l_(532598)
_c_(532601, _n_(532599, "print", lambda: print), _n_(532600, "ecell_export_df", lambda: ecell_export_df))
_l_(532602)
#print (ecell_export_df)
del ecell_df
_l_(532603)
del ecell_sum_df
_l_(532604)

export_df=_c_(532608, _a_(532606, _n_(532605, "pd", lambda: pd), "concat"), [_n_(532607, "ecell_export_df", lambda: ecell_export_df)],join='outer',axis=1)
_l_(532609)
export_df=_c_(532612, _a_(532611, _n_(532610, "export_df", lambda: export_df), "fillna"), 0)
_l_(532613)
_n_(532614, "export_df", lambda: export_df)['TOTAL'] = _c_(532617, _a_(532616, _n_(532615, "export_df", lambda: export_df), "sum"), axis=1)
_l_(532618)
_n_(532619, "export_df", lambda: export_df)['NWEEK'] = _n_(532620, "WCOUNT_last", lambda: WCOUNT_last)
_l_(532621)

del ecell_export_df
_l_(532622)
#################################################