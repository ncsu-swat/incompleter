# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61930815/typeerror-module-object-is-not-callable-apriori
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import argparse
    _l_(345224)

except ImportError:
    pass
try:
    import time
    _l_(345226)

except ImportError:
    pass
try:
    import sys
    _l_(345228)

except ImportError:
    pass
try:
    import random
    _l_(345230)

except ImportError:
    pass
try:
    from efficient_apriori import apriori
    _l_(345232)

except ImportError:
    pass
parser = _c_(345235, _a_(345234, _n_(345233, "argparse", lambda: argparse), "ArgumentParser"), description="datasets")
_l_(345236)
_c_(345239, _a_(345238, _n_(345237, "parser", lambda: parser), "add_argument"), '-f', '--file', 
default="sample.txt",help="http://fimi.uantwerpen.be/data/")
_l_(345240)
_c_(345243, _a_(345242, _n_(345241, "parser", lambda: parser), "add_argument"), '-s', '--min_support', default = 0.5,
                help="minimum support, set to 0.5 by default")
_l_(345244)
_c_(345247, _a_(345246, _n_(345245, "parser", lambda: parser), "add_argument"), '-c', '--min_confidence', default = 0.5,
                help="minimum confidence, set to 1 by default")
_l_(345248)
_c_(345251, _a_(345250, _n_(345249, "parser", lambda: parser), "add_argument"), '-p', '--probability', default = 1,
                help="Probability for randomlized slice")               
_l_(345252)               
args = _c_(345255, _a_(345254, _n_(345253, "parser", lambda: parser), "parse_args"))
_l_(345256)
#memory_data [Brisket_Number][Item_Number]
memory_data = []
_l_(345257)
data_list = []
_l_(345258)
def decision(probability):
    _l_(345266)

    aux = _c_(345261, _a_(345260, _n_(345259, "random", lambda: random), "random")) < _c_(345264, _n_(345262, "float", lambda: float), _n_(345263, "probability", lambda: probability))
    _l_(345265)
    return aux
#------------------------------------------File Handling------------------------------------------
def file_to_array():
    _l_(345312)

    i = 1
    _l_(345267)
    data_file = _c_(345271, _n_(345268, "open", lambda: open), _a_(345270, _n_(345269, "args", lambda: args), "file"), "r")
    _l_(345272)
    _c_(345274, _n_(345273, "print", lambda: print), "Reading File into Array...\n")
    _l_(345275)
    #if its comment line
    for line in _n_(345276, "data_file", lambda: data_file):
        _l_(345303)


        line = _c_(345279, _a_(345278, _n_(345277, "line", lambda: line), "rstrip"))
        _l_(345280)
        line_row = _c_(345283, _a_(345282, _n_(345281, "line", lambda: line), "split"))
        _l_(345284)

        _c_(345288, _a_(345286, _n_(345285, "memory_data", lambda: memory_data), "append"), _n_(345287, "line_row", lambda: line_row))
        _l_(345289)
        if _c_(345293, _n_(345290, "decision", lambda: decision), _a_(345292, _n_(345291, "args", lambda: args), "probability")):
            _l_(345301)

            _c_(345299, _a_(345295, _n_(345294, "data_list", lambda: data_list), "append"), _c_(345298, _n_(345296, "tuple", lambda: tuple), _n_(345297, "line_row", lambda: line_row)))
            _l_(345300)
        i += 1
        _l_(345302)
    _c_(345306, _a_(345305, _n_(345304, "data_file", lambda: data_file), "close"))
    _l_(345307)
    #print("Array:",memory_data,"\n")
    #print("Data_list:",data_list)
    _c_(345310, _n_(345308, "print", lambda: print), "Reading complete ",_n_(345309, "i", lambda: i), " lines in total.")
    _l_(345311)
def main():
    _l_(345343)

    start_time = _c_(345315, _a_(345314, _n_(345313, "time", lambda: time), "time"))
    _l_(345316)
    _c_(345318, _n_(345317, "file_to_array", lambda: file_to_array))
    _l_(345319)
    #Apriori()
    itemsets, rules = _c_(345330, _n_(345320, "apriori", lambda: apriori), _n_(345321, "data_list", lambda: data_list), min_support= _c_(345325, _n_(345322, "float", lambda: float), _a_(345324, _n_(345323, "args", lambda: args), "min_support")),  
min_confidence=_c_(345329, _n_(345326, "float", lambda: float), _a_(345328, _n_(345327, "args", lambda: args), "min_confidence")))
    _l_(345331)
    #print(itemsets)
    _c_(345334, _n_(345332, "print", lambda: print), _n_(345333, "rules", lambda: rules)) 
    _l_(345335) 
    _c_(345341, _n_(345336, "print", lambda: print), "--- Total run time: %s seconds ---" % (_c_(345339, _a_(345338, _n_(345337, "time", lambda: time), "time")) - _n_(345340, "start_time", lambda: start_time)))
    _l_(345342)
if _n_(345344, "__name__", lambda: __name__) == "__main__":
    _l_(345348)

    _c_(345346, _n_(345345, "main", lambda: main))
    _l_(345347)