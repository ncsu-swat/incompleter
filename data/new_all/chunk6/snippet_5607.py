# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61930815/typeerror-module-object-is-not-callable-apriori
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import argparse
    _l_(372974)

except ImportError:
    pass
try:
    import time
    _l_(372976)

except ImportError:
    pass
try:
    import sys
    _l_(372978)

except ImportError:
    pass
try:
    import random
    _l_(372980)

except ImportError:
    pass
try:
    from efficient_apriori import apriori
    _l_(372982)

except ImportError:
    pass
parser = _c_(372985, _a_(372984, _n_(372983, "argparse", lambda: argparse), "ArgumentParser"), description="datasets")
_l_(372986)
_c_(372989, _a_(372988, _n_(372987, "parser", lambda: parser), "add_argument"), '-f', '--file', 
default="sample.txt",help="http://fimi.uantwerpen.be/data/")
_l_(372990)
_c_(372993, _a_(372992, _n_(372991, "parser", lambda: parser), "add_argument"), '-s', '--min_support', default = 0.5,
                help="minimum support, set to 0.5 by default")
_l_(372994)
_c_(372997, _a_(372996, _n_(372995, "parser", lambda: parser), "add_argument"), '-c', '--min_confidence', default = 0.5,
                help="minimum confidence, set to 1 by default")
_l_(372998)
_c_(373001, _a_(373000, _n_(372999, "parser", lambda: parser), "add_argument"), '-p', '--probability', default = 1,
                help="Probability for randomlized slice")               
_l_(373002)               
args = _c_(373005, _a_(373004, _n_(373003, "parser", lambda: parser), "parse_args"))
_l_(373006)
#memory_data [Brisket_Number][Item_Number]
memory_data = []
_l_(373007)
data_list = []
_l_(373008)
def decision(probability):
    _l_(373016)

    aux = _c_(373011, _a_(373010, _n_(373009, "random", lambda: random), "random")) < _c_(373014, _n_(373012, "float", lambda: float), _n_(373013, "probability", lambda: probability))
    _l_(373015)
    return aux
#------------------------------------------File Handling------------------------------------------
def file_to_array():
    _l_(373062)

    i = 1
    _l_(373017)
    data_file = _c_(373021, _n_(373018, "open", lambda: open), _a_(373020, _n_(373019, "args", lambda: args), "file"), "r")
    _l_(373022)
    _c_(373024, _n_(373023, "print", lambda: print), "Reading File into Array...\n")
    _l_(373025)
    #if its comment line
    for line in _n_(373026, "data_file", lambda: data_file):
        _l_(373053)


        line = _c_(373029, _a_(373028, _n_(373027, "line", lambda: line), "rstrip"))
        _l_(373030)
        line_row = _c_(373033, _a_(373032, _n_(373031, "line", lambda: line), "split"))
        _l_(373034)

        _c_(373038, _a_(373036, _n_(373035, "memory_data", lambda: memory_data), "append"), _n_(373037, "line_row", lambda: line_row))
        _l_(373039)
        if _c_(373043, _n_(373040, "decision", lambda: decision), _a_(373042, _n_(373041, "args", lambda: args), "probability")):
            _l_(373051)

            _c_(373049, _a_(373045, _n_(373044, "data_list", lambda: data_list), "append"), _c_(373048, _n_(373046, "tuple", lambda: tuple), _n_(373047, "line_row", lambda: line_row)))
            _l_(373050)
        i += 1
        _l_(373052)
    _c_(373056, _a_(373055, _n_(373054, "data_file", lambda: data_file), "close"))
    _l_(373057)
    #print("Array:",memory_data,"\n")
    #print("Data_list:",data_list)
    _c_(373060, _n_(373058, "print", lambda: print), "Reading complete ",_n_(373059, "i", lambda: i), " lines in total.")
    _l_(373061)
def main():
    _l_(373093)

    start_time = _c_(373065, _a_(373064, _n_(373063, "time", lambda: time), "time"))
    _l_(373066)
    _c_(373068, _n_(373067, "file_to_array", lambda: file_to_array))
    _l_(373069)
    #Apriori()
    itemsets, rules = _c_(373080, _n_(373070, "apriori", lambda: apriori), _n_(373071, "data_list", lambda: data_list), min_support= _c_(373075, _n_(373072, "float", lambda: float), _a_(373074, _n_(373073, "args", lambda: args), "min_support")),  
min_confidence=_c_(373079, _n_(373076, "float", lambda: float), _a_(373078, _n_(373077, "args", lambda: args), "min_confidence")))
    _l_(373081)
    #print(itemsets)
    _c_(373084, _n_(373082, "print", lambda: print), _n_(373083, "rules", lambda: rules)) 
    _l_(373085) 
    _c_(373091, _n_(373086, "print", lambda: print), "--- Total run time: %s seconds ---" % (_c_(373089, _a_(373088, _n_(373087, "time", lambda: time), "time")) - _n_(373090, "start_time", lambda: start_time)))
    _l_(373092)
if _n_(373094, "__name__", lambda: __name__) == "__main__":
    _l_(373098)

    _c_(373096, _n_(373095, "main", lambda: main))
    _l_(373097)