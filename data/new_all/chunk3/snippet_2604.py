# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69658815/typeerror-to-csv-got-an-unexpected-keyword-argument-startrow
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mokacsv(file_name):
    _l_(543301)

    importing = _c_(543291, _a_(543289, _n_(543288, "pd", lambda: pd), "read_csv"), _n_(543290, "file_name", lambda: file_name))
    _l_(543292)
    column_netsales = _n_(543293, "importing", lambda: importing)['Net Sales']
    _l_(543294)
    sum_of_netsales = _n_(543295, "column_netsales", lambda: (column_netsales))
    _l_(543296)
    _c_(543299, _a_(543298, _n_(543297, "sum_of_netsales", lambda: sum_of_netsales), "to_csv"), 'example1.csv', index=False, header=True, startrow=30)
    _l_(543300)



_c_(543305, _n_(543302, "print", lambda: print), _c_(543304, _n_(543303, "mokacsv", lambda: mokacsv), r"example2.csv"))
_l_(543306)