# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53760038/python-typeerror-unsupported-operand-types-for-io-textiowrapper-and-s
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
today=_c_(414169, _a_(414168, _c_(414167, _a_(414166, _a_(414165, _n_(414164, "datetime", lambda: datetime), "datetime"), "today")), "strftime"), "%Y%m%d-%H%M%S")
_l_(414170)
string_file="string_"+_n_(414171, "today", lambda: today)+".csv"
_l_(414172)
outputFile = _c_(414175, _n_(414173, "open", lambda: open), _n_(414174, "string_file_rdkb", lambda: string_file_rdkb), "w")
_l_(414176)
#....some code here...
my_df=_c_(414180, _a_(414178, _n_(414177, "pd", lambda: pd), "DataFrame"), _n_(414179, "datalist2", lambda: datalist2))
_l_(414181)
_c_(414185, _a_(414183, _n_(414182, "my_df", lambda: my_df), "to_csv"), _n_(414184, "outputFile", lambda: outputFile), index=False, header=False)
_l_(414186)
_c_(414189, _n_(414187, "print", lambda: print), _n_(414188, "outputFile", lambda: outputFile) + " is generated") #Here is the issue
_l_(414190) #Here is the issue