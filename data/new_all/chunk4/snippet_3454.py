# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74009860/how-do-i-fix-nameerror-in-python-i-defined-a-variable-in-a-for-loop-and-when-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
Carpeta = "C:/Users/Aguilar/datos de prueba" #directory
_l_(629395) #directory

for subdirectorio in _c_(629399, _a_(629397, _n_(629396, "os", lambda: os), "listdir"), _n_(629398, "Carpeta", lambda: Carpeta)):
    _l_(629442)

    _c_(629402, _n_(629400, "print", lambda: print), _n_(629401, "subdirectorio", lambda: subdirectorio))
    _l_(629403)


    for archivo in _c_(629408, _a_(629405, _n_(629404, "os", lambda: os), "listdir"), _n_(629406, "Carpeta", lambda: Carpeta)+'/'+_n_(629407, "subdirectorio", lambda: subdirectorio)):
        _l_(629441)

        if _c_(629411, _a_(629410, _n_(629409, "archivo", lambda: archivo), "endswith"), ".lc"):
            _l_(629440)

            _c_(629414, _n_(629412, "print", lambda: print), _n_(629413, "archivo", lambda: archivo))
            _l_(629415)
        
        
            # making data frame from csv file 
       
            data = _c_(629421, _a_(629417, _n_(629416, "pd", lambda: pd), "read_csv"), _n_(629418, "Carpeta", lambda: Carpeta)+'/'+_n_(629419, "subdirectorio", lambda: subdirectorio)+'/'+_n_(629420, "archivo", lambda: archivo), delimiter=' ', na_values='*********', usecols=[0,2,3], names = ['time', 'magnitude', 'error']) 
            _l_(629422) 

            # sorting by first name 
            _c_(629425, _a_(629424, _n_(629423, "data", lambda: data), "sort_values"), 'time', inplace = True) 
            _l_(629426) 

            # dropping ALL duplicate values 
            _c_(629429, _a_(629428, _n_(629427, "data", lambda: data), "drop_duplicates"), subset ="time", keep = False, inplace = True) 
            _l_(629430) 

            data = _n_(629431, "data", lambda: data)[_c_(629434, _a_(629433, _n_(629432, "data", lambda: data)['magnitude'], "notna"))]
            _l_(629435)

            tess_lc_raw = _c_(629438, _a_(629437, _n_(629436, "data", lambda: data), "to_records"), index=False)
            _l_(629439)