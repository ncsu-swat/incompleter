# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61930815/typeerror-module-object-is-not-callable-apriori
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import argparse
    _l_(360589)

except ImportError:
    pass
try:
    import time
    _l_(360591)

except ImportError:
    pass
try:
    import sys
    _l_(360593)

except ImportError:
    pass
try:
    import random
    _l_(360595)

except ImportError:
    pass
try:
    from efficient_apriori import apriori
    _l_(360597)

except ImportError:
    pass
parser = _c_(360600, _a_(360599, _n_(360598, "argparse", lambda: argparse), "ArgumentParser"), description="datasets")
_l_(360601)
_c_(360604, _a_(360603, _n_(360602, "parser", lambda: parser), "add_argument"), '-f', '--file', 
default="sample.txt",help="http://fimi.uantwerpen.be/data/")
_l_(360605)
_c_(360608, _a_(360607, _n_(360606, "parser", lambda: parser), "add_argument"), '-s', '--min_support', default = 0.5,
                help="minimum support, set to 0.5 by default")
_l_(360609)
_c_(360612, _a_(360611, _n_(360610, "parser", lambda: parser), "add_argument"), '-c', '--min_confidence', default = 0.5,
                help="minimum confidence, set to 1 by default")
_l_(360613)
_c_(360616, _a_(360615, _n_(360614, "parser", lambda: parser), "add_argument"), '-p', '--probability', default = 1,
                help="Probability for randomlized slice")               
_l_(360617)               
args = _c_(360620, _a_(360619, _n_(360618, "parser", lambda: parser), "parse_args"))
_l_(360621)
#memory_data [Brisket_Number][Item_Number]
memory_data = []
_l_(360622)
data_list = []
_l_(360623)
def decision(probability):
    _l_(360631)

    aux = _c_(360626, _a_(360625, _n_(360624, "random", lambda: random), "random")) < _c_(360629, _n_(360627, "float", lambda: float), _n_(360628, "probability", lambda: probability))
    _l_(360630)
    return aux
#------------------------------------------File Handling------------------------------------------
def file_to_array():
    _l_(360677)

    i = 1
    _l_(360632)
    data_file = _c_(360636, _n_(360633, "open", lambda: open), _a_(360635, _n_(360634, "args", lambda: args), "file"), "r")
    _l_(360637)
    _c_(360639, _n_(360638, "print", lambda: print), "Reading File into Array...\n")
    _l_(360640)
    #if its comment line
    for line in _n_(360641, "data_file", lambda: data_file):
        _l_(360668)


        line = _c_(360644, _a_(360643, _n_(360642, "line", lambda: line), "rstrip"))
        _l_(360645)
        line_row = _c_(360648, _a_(360647, _n_(360646, "line", lambda: line), "split"))
        _l_(360649)

        _c_(360653, _a_(360651, _n_(360650, "memory_data", lambda: memory_data), "append"), _n_(360652, "line_row", lambda: line_row))
        _l_(360654)
        if _c_(360658, _n_(360655, "decision", lambda: decision), _a_(360657, _n_(360656, "args", lambda: args), "probability")):
            _l_(360666)

            _c_(360664, _a_(360660, _n_(360659, "data_list", lambda: data_list), "append"), _c_(360663, _n_(360661, "tuple", lambda: tuple), _n_(360662, "line_row", lambda: line_row)))
            _l_(360665)
        i += 1
        _l_(360667)
    _c_(360671, _a_(360670, _n_(360669, "data_file", lambda: data_file), "close"))
    _l_(360672)
    #print("Array:",memory_data,"\n")
    #print("Data_list:",data_list)
    _c_(360675, _n_(360673, "print", lambda: print), "Reading complete ",_n_(360674, "i", lambda: i), " lines in total.")
    _l_(360676)
def main():
    _l_(360708)

    start_time = _c_(360680, _a_(360679, _n_(360678, "time", lambda: time), "time"))
    _l_(360681)
    _c_(360683, _n_(360682, "file_to_array", lambda: file_to_array))
    _l_(360684)
    #Apriori()
    itemsets, rules = _c_(360695, _n_(360685, "apriori", lambda: apriori), _n_(360686, "data_list", lambda: data_list), min_support= _c_(360690, _n_(360687, "float", lambda: float), _a_(360689, _n_(360688, "args", lambda: args), "min_support")),  
min_confidence=_c_(360694, _n_(360691, "float", lambda: float), _a_(360693, _n_(360692, "args", lambda: args), "min_confidence")))
    _l_(360696)
    #print(itemsets)
    _c_(360699, _n_(360697, "print", lambda: print), _n_(360698, "rules", lambda: rules)) 
    _l_(360700) 
    _c_(360706, _n_(360701, "print", lambda: print), "--- Total run time: %s seconds ---" % (_c_(360704, _a_(360703, _n_(360702, "time", lambda: time), "time")) - _n_(360705, "start_time", lambda: start_time)))
    _l_(360707)
if _n_(360709, "__name__", lambda: __name__) == "__main__":
    _l_(360713)

    _c_(360711, _n_(360710, "main", lambda: main))
    _l_(360712)