# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52262519/typeerror-cannot-do-slice-indexing-on-class-pandas-core-indexes-base-index
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(442489)

except ImportError:
    pass

#Reading Input File and converting into dataframe

input_data=_c_(442492, _a_(442491, _n_(442490, "pd", lambda: pd), "read_csv"), "C:\\Users\\hp\\Desktop\\py\\Input_Data.txt",delimiter =',') 
_l_(442493) 
input_data_df=_c_(442497, _a_(442495, _n_(442494, "pd", lambda: pd), "DataFrame"), _n_(442496, "input_data", lambda: input_data))
_l_(442498)


#Reading Reference File and converting into dataframe

reference_data=_c_(442501, _a_(442500, _n_(442499, "pd", lambda: pd), "read_csv"), "C:\\Users\\hp\\Desktop\\py\\Reference_Data.txt",delimiter =',') 
_l_(442502) 
reference_data_df=_c_(442506, _a_(442504, _n_(442503, "pd", lambda: pd), "DataFrame"), _n_(442505, "reference_data", lambda: reference_data))
_l_(442507)



#Merging files based on unique Columns

Input_Reference_merge= _c_(442512, _a_(442509, _n_(442508, "pd", lambda: pd), "merge"), _n_(442510, "input_data_df", lambda: input_data_df), _n_(442511, "reference_data_df", lambda: reference_data_df), on=['emp_id', 'emp_name'])
_l_(442513)
_c_(442516, _n_(442514, "print", lambda: print), _n_(442515, "Input_Reference_merge", lambda: Input_Reference_merge))
_l_(442517)


# Get the index where jan starts
months_index_start = _c_(442521, _a_(442520, _a_(442519, _n_(442518, "input_data_df", lambda: input_data_df), "columns"), "get_loc"), "jan")
_l_(442522)

# Calculate the total salary for each row according to the months_worked column

_n_(442523, "Input_Reference_merge", lambda: Input_Reference_merge)["total_sal"] = _c_(442532, _a_(442525, _n_(442524, "Input_Reference_merge", lambda: Input_Reference_merge), "apply"), lambda x : _c_(442531, _a_(442530, _n_(442526, "x", lambda: x)[_n_(442527, "months_index_start", lambda: months_index_start) : _n_(442528, "months_index_start", lambda: months_index_start) + _n_(442529, "x", lambda: x)["months_worked"]], "sum")), axis = 1)
_l_(442533)
_c_(442536, _n_(442534, "print", lambda: print), _n_(442535, "Input_Reference_merge", lambda: Input_Reference_merge))
_l_(442537)