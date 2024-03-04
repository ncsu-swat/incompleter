# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16327055/how-to-add-an-empty-column-to-a-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(64093, "df", lambda: df)['column'] = None #This works. This will create a new column with None type
_l_(64094) #This works. This will create a new column with None type
_n_(64095, "df", lambda: df).column = None #This will work only when the column is already present in the dataframe 
_l_(64096) #This will work only when the column is already present in the dataframe 

