# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62772575/typeerror-argument-must-be-a-string-or-number-on-column-with-strings-that-are-n
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(358636)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(358638)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(358640)

except ImportError:
    pass

# Making a list of missing value types
missing_values = ["?"]
_l_(358641)
df= _c_(358645, _a_(358643, _n_(358642, "pd", lambda: pd), "read_csv"), 'D:\\data.csv',na_values = _n_(358644, "missing_values", lambda: missing_values))
_l_(358646)

#print the new table with the missing values 
# print (df)
# print (df.isnull())


X = _a_(358649, _a_(358648, _n_(358647, "df", lambda: df), "iloc")[:, :-1], "values") #Matrix - independent variables (features)
_l_(358650) #Matrix - independent variables (features)
y = _a_(358653, _a_(358652, _n_(358651, "df", lambda: df), "iloc")[:, 24], "values") #dependent variables vectors
_l_(358654) #dependent variables vectors
try:
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    _l_(358656)

except ImportError:
    pass
labelencoder_X2 = _c_(358658, _n_(358657, "LabelEncoder", lambda: LabelEncoder))
_l_(358659)
_n_(358660, "X", lambda: X)[:, 2] = _c_(358664, _a_(358662, _n_(358661, "labelencoder_X2", lambda: labelencoder_X2), "fit_transform"), _n_(358663, "X", lambda: X)[:, 2]) #gas=0, fuel=1 
_l_(358665) #gas=0, fuel=1 

labelencoder_X3 = _c_(358667, _n_(358666, "LabelEncoder", lambda: LabelEncoder))
_l_(358668)
_n_(358669, "X", lambda: X)[:, 3] = _c_(358673, _a_(358671, _n_(358670, "labelencoder_X3", lambda: labelencoder_X3), "fit_transform"), _n_(358672, "X", lambda: X)[:, 3])
_l_(358674)

#I get an error her
labelencoder_X4 = _c_(358676, _n_(358675, "LabelEncoder", lambda: LabelEncoder))
_l_(358677)
_n_(358678, "X", lambda: X)[:, 4] = _c_(358682, _a_(358680, _n_(358679, "labelencoder_X4", lambda: labelencoder_X4), "fit_transform"), _n_(358681, "X", lambda: X)[:, 4])
_l_(358683)

labelencoder_X5 = _c_(358685, _n_(358684, "LabelEncoder", lambda: LabelEncoder))
_l_(358686)
_n_(358687, "X", lambda: X)[:, 5] = _c_(358691, _a_(358689, _n_(358688, "labelencoder_X5", lambda: labelencoder_X5), "fit_transform"), _n_(358690, "X", lambda: X)[:,5])
_l_(358692)

labelencoder_X6 = _c_(358694, _n_(358693, "LabelEncoder", lambda: LabelEncoder))
_l_(358695)
_n_(358696, "X", lambda: X)[:, 6] = _c_(358700, _a_(358698, _n_(358697, "labelencoder_X6", lambda: labelencoder_X6), "fit_transform"), _n_(358699, "X", lambda: X)[:, 6])
_l_(358701)

labelencoder_X7 = _c_(358703, _n_(358702, "LabelEncoder", lambda: LabelEncoder))
_l_(358704)
_n_(358705, "X", lambda: X)[:, 7] = _c_(358709, _a_(358707, _n_(358706, "labelencoder_X7", lambda: labelencoder_X7), "fit_transform"), _n_(358708, "X", lambda: X)[:, 7])
_l_(358710)

labelencoder_X13 = _c_(358712, _n_(358711, "LabelEncoder", lambda: LabelEncoder))
_l_(358713)
_n_(358714, "X", lambda: X)[:, 13] = _c_(358718, _a_(358716, _n_(358715, "labelencoder_X13", lambda: labelencoder_X13), "fit_transform"), _n_(358717, "X", lambda: X)[:, 13])
_l_(358719)

labelencoder_X14 = _c_(358721, _n_(358720, "LabelEncoder", lambda: LabelEncoder))
_l_(358722)
_n_(358723, "X", lambda: X)[:, 14] = _c_(358727, _a_(358725, _n_(358724, "labelencoder_X14", lambda: labelencoder_X14), "fit_transform"), _n_(358726, "X", lambda: X)[:, 14])
_l_(358728)

labelencoder_X15 = _c_(358730, _n_(358729, "LabelEncoder", lambda: LabelEncoder))
_l_(358731)
_n_(358732, "X", lambda: X)[:, 16] = _c_(358736, _a_(358734, _n_(358733, "labelencoder_X14", lambda: labelencoder_X14), "fit_transform"), _n_(358735, "X", lambda: X)[:, 16])
_l_(358737)
try:
    from sklearn.impute import SimpleImputer
    _l_(358739)

except ImportError:
    pass
imputer=_c_(358741, _n_(358740, "SimpleImputer", lambda: SimpleImputer), missing_values="NaN", strategy='mean')
_l_(358742)
_c_(358746, _a_(358744, _n_(358743, "imputer", lambda: imputer), "fit"), _n_(358745, "X", lambda: X)[:, 1:24])  
_l_(358747)  
_n_(358748, "X", lambda: X)[:, 1:24]=_c_(358752, _a_(358750, _n_(358749, "imputer", lambda: imputer), "transform"), _n_(358751, "X", lambda: X)[:, 1:24])
_l_(358753)