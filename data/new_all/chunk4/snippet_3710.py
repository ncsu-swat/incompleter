# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66610488/correlation-in-pandas-attributeerror-float-object-has-no-attribute-shape
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dfCorrelation=_c_(584393, _a_(584391, _n_(584390, "pd", lambda: pd), "read_csv"), _n_(584392, "filename", lambda: filename))
_l_(584394)
df1 = _a_(584396, _n_(584395, "dfCorrelation", lambda: dfCorrelation), "loc")[1] #to subset the first row
_l_(584397) #to subset the first row
df2 = _a_(584399, _n_(584398, "dfCorrelation", lambda: dfCorrelation), "loc")[2] #to subset the second row
_l_(584400) #to subset the second row
_c_(584406, _n_(584401, "print", lambda: print), _c_(584405, _a_(584403, _n_(584402, "df1", lambda: df1), "corr"), _n_(584404, "df2", lambda: df2)))
_l_(584407)