# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66919883/python-functions-in-classes-nameerror
#Import library
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(373100)

except ImportError:
    pass
try:
    import math
    _l_(373102)

except ImportError:
    pass
try:
    import numpy as np
    _l_(373104)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(373106)

except ImportError:
    pass

#Automatically creates a dataframe don't need pd.DataFrame
data = _c_(373109, _a_(373108, _n_(373107, "pd", lambda: pd), "read_csv"), "/Users/tianachargin/Desktop/PythonSG/STAT 4490/WidgeOne_CSV.csv")
_l_(373110)
#print out dataset
_c_(373113, _n_(373111, "print", lambda: print), _n_(373112, "data", lambda: data))
_l_(373114)

class Graphs:
    _l_(373394)

#Constructor with parameters
    #Self isn't a pass by value parameter but it allows you to reference
    def __init__(self, quantVar1, quantVar2, qualVar1, qualVar2):
        _l_(373127)

        _n_(373115, "self", lambda: self).A = _n_(373116, "quantVar1", lambda: quantVar1)   #First quantitative variable           
        _l_(373117)   #First quantitative variable           
        _n_(373118, "self", lambda: self).B = _n_(373119, "quantVar2", lambda: quantVar2)   #Second quantitative variable
        _l_(373120)   #Second quantitative variable
        _n_(373121, "self", lambda: self).C = _n_(373122, "qualVar1", lambda: qualVar1)    #First qualitative variable
        _l_(373123)    #First qualitative variable
        _n_(373124, "self", lambda: self).D = _n_(373125, "qualVar2", lambda: qualVar2)    #Second qualitative variable 
        _l_(373126)    #Second qualitative variable 
#Function that calculates bin width for the histogram 
    def bin_width(variable):
        _l_(373173)

        try:
            import math
            _l_(373129)

        except ImportError:
            pass
        
        #Create variable to create array for bins
        #Find min of column
        min = _c_(373133, _a_(373132, _n_(373130, "data", lambda: data)[_n_(373131, "variable", lambda: variable)], "min"))
        _l_(373134)
        #Find max of column
        max = _c_(373138, _a_(373137, _n_(373135, "data", lambda: data)[_n_(373136, "variable", lambda: variable)], "max"))
        _l_(373139)
        #Find the the count of rows (number of data/size/n)
        index = _a_(373141, _n_(373140, "data", lambda: data), "index")
        _l_(373142)
        number_of_rows = _c_(373145, _n_(373143, "len", lambda: len), _n_(373144, "index", lambda: index)) 
        _l_(373146) 
        #Calculate number of bins and round up
        num_of_bins = _c_(373153, _a_(373148, _n_(373147, "math", lambda: math), "ceil"), _c_(373152, _a_(373150, _n_(373149, "math", lambda: math), "sqrt"), _n_(373151, "number_of_rows", lambda: number_of_rows)))
        _l_(373154)
        #Calculate bin width (max - min)/# of bins
        bin_width = ((_n_(373155, "max", lambda: max) - _n_(373156, "min", lambda: min))/_n_(373157, "num_of_bins", lambda: num_of_bins))
        _l_(373158)
        #Round bin width to one decimal place
        increment_bin = _c_(373161, _n_(373159, "round", lambda: round), _n_(373160, "bin_width", lambda: bin_width), 1)
        _l_(373162)
        #Start bin 
        start_bin = (_n_(373163, "min", lambda: min) - _n_(373164, "increment_bin", lambda: increment_bin))
        _l_(373165)
        #End bin
        end_bin = (_n_(373166, "max", lambda: max) + _n_(373167, "increment_bin", lambda: increment_bin))
        _l_(373168)
        aux = _n_(373169, "start_bin", lambda: start_bin), _n_(373170, "end_bin", lambda: end_bin), _n_(373171, "increment_bin", lambda: increment_bin)
        _l_(373172)
        
        return aux
#Histogram Function 
    def histogram(self):
        _l_(373228)

        try:
            import math
            _l_(373175)

        except ImportError:
            pass
        try:
            import numpy as np
            _l_(373177)

        except ImportError:
            pass
        try:
            import matplotlib.pyplot as plt
            _l_(373179)

        except ImportError:
            pass
        
        #Create variable that we call the function to calculate the bin width
        bin = _c_(373183, _n_(373180, "bin_width", lambda: bin_width), _a_(373182, _n_(373181, "self", lambda: self), "A")) 
        _l_(373184) 
         
        #Start at value = bin[0], Stop at value = bin[1], Increment by value of bin[2]
        bins = _c_(373193, _a_(373186, _n_(373185, "np", lambda: np), "array"), _c_(373192, _a_(373188, _n_(373187, "np", lambda: np), "arange"), start = _n_(373189, "bin", lambda: bin)[0], stop = _n_(373190, "bin", lambda: bin)[1], step = _n_(373191, "bin", lambda: bin)[2]))
        _l_(373194)
        #Histogram function
        _c_(373203, _a_(373196, _n_(373195, "plt", lambda: plt), "hist"), _n_(373197, "data", lambda: data)[_a_(373199, _n_(373198, "self", lambda: self), "A")], _n_(373200, "bins", lambda: bins), label = _a_(373202, _n_(373201, "self", lambda: self), "A"), color = "red")
        _l_(373204)
        #x-axis label
        _c_(373209, _a_(373206, _n_(373205, "plt", lambda: plt), "xlabel"), _a_(373208, _n_(373207, "self", lambda: self), "A"), fontsize = 16)  
        _l_(373210)  
        #y-axis lable
        _c_(373215, _a_(373212, _n_(373211, "plt", lambda: plt), "ylabel"), "Frequency of " + _a_(373214, _n_(373213, "self", lambda: self), "A"), fontsize = 16)
        _l_(373216)
        #Title of graph
        _c_(373221, _a_(373218, _n_(373217, "plt", lambda: plt), "title"), "Histogram of " + _a_(373220, _n_(373219, "self", lambda: self), "A"), loc = 'center')
        _l_(373222)
        _c_(373225, _a_(373224, _n_(373223, "plt", lambda: plt), "show"))
        _l_(373226)
        aux = ""
        _l_(373227)
        return aux


#Stacked Histogram Function  
    def stacked_histogram(self):
        _l_(373329)

        try:
            import numpy as np
            _l_(373230)

        except ImportError:
            pass
        try:
            from matplotlib import pyplot as plt
            _l_(373232)

        except ImportError:
            pass
        
        #Create combonations of the values for the two options
        _n_(373233, "data", lambda: data)[_a_(373235, _n_(373234, "self", lambda: self), "C") + "-" + _a_(373237, _n_(373236, "self", lambda: self), "D")] = _n_(373238, "data", lambda: data)[_a_(373240, _n_(373239, "self", lambda: self), "C")] + " " + _n_(373241, "data", lambda: data)[_a_(373243, _n_(373242, "self", lambda: self), "D")] 
        _l_(373244) 
        combos = _c_(373252, _a_(373246, _n_(373245, "np", lambda: np), "unique"), _n_(373247, "data", lambda: data)[_a_(373249, _n_(373248, "self", lambda: self), "C") + "-" + _a_(373251, _n_(373250, "self", lambda: self), "D")])
        _l_(373253)
        #Create variable that we call the function to calculate the bin width
        bin = _c_(373257, _n_(373254, "bin_width", lambda: bin_width), _a_(373256, _n_(373255, "self", lambda: self), "A"))
        _l_(373258)
        #Start at value = bin[0], Stop at value = bin[1], Increment by value of bin[2]
        bins = _c_(373267, _a_(373260, _n_(373259, "np", lambda: np), "array"), _c_(373266, _a_(373262, _n_(373261, "np", lambda: np), "arange"), start = _n_(373263, "bin", lambda: bin)[0], stop = _n_(373264, "bin", lambda: bin)[1], step = _n_(373265, "bin", lambda: bin)[2]))
        _l_(373268)
        
        #Create histogram
        for i in _c_(373273, _n_(373269, "range", lambda: range), _c_(373272, _n_(373270, "len", lambda: len), _n_(373271, "combos", lambda: combos))):
            _l_(373299)

            _c_(373297, _a_(373275, _n_(373274, "plt", lambda: plt), "hist"), _n_(373276, "data", lambda: data)[_c_(373288, _a_(373282, _n_(373277, "data", lambda: data)[_a_(373279, _n_(373278, "self", lambda: self), "C") + "-" + _a_(373281, _n_(373280, "self", lambda: self), "D")], "isin"), _n_(373283, "combos", lambda: combos)[_n_(373284, "i", lambda: i):_c_(373287, _n_(373285, "len", lambda: len), _n_(373286, "combos", lambda: combos))])][_a_(373290, _n_(373289, "self", lambda: self), "A")], _n_(373291, "bins", lambda: bins), label = _n_(373292, "combos", lambda: combos)[_n_(373293, "i", lambda: i):_c_(373296, _n_(373294, "len", lambda: len), _n_(373295, "combos", lambda: combos))])
            _l_(373298)
        #x-axis label
        _c_(373304, _a_(373301, _n_(373300, "plt", lambda: plt), "xlabel"), _a_(373303, _n_(373302, "self", lambda: self), "A"), fontsize = 16) 
        _l_(373305) 
        #y-axis lable
        _c_(373308, _a_(373307, _n_(373306, "plt", lambda: plt), "ylabel"), "Frequency of ", fontsize = 16)
        _l_(373309)
        #Legend of graph
        _c_(373312, _a_(373311, _n_(373310, "plt", lambda: plt), "legend"), loc = 'upper left')
        _l_(373313)
        #Title of graph
        _c_(373322, _a_(373315, _n_(373314, "plt", lambda: plt), "title"), "Histogram of " + _a_(373317, _n_(373316, "self", lambda: self), "A") + " with unique combinations of " + _a_(373319, _n_(373318, "self", lambda: self), "D") + " and " + _a_(373321, _n_(373320, "self", lambda: self), "C"), loc = 'center')
        _l_(373323)
        _c_(373326, _a_(373325, _n_(373324, "plt", lambda: plt), "show"))
        _l_(373327)
        aux = ""
        _l_(373328)
        return aux
    

#Overlapping Histogram Function 
    def overlap_histogram(self):
        _l_(373393)

        try:
            import numpy as np
            _l_(373331)

        except ImportError:
            pass
        try:
            from matplotlib import pyplot as plt
            _l_(373333)

        except ImportError:
            pass
        
        #Create variable that we call the function to calculate the bin width
        bin = _c_(373337, _n_(373334, "bin_width", lambda: bin_width), _a_(373336, _n_(373335, "self", lambda: self), "A"))
        _l_(373338)
        
        #Start at value = bin[0], Stop at value = bin[1], Increment by value of bin[2]
        bins = _c_(373347, _a_(373340, _n_(373339, "np", lambda: np), "array"), _c_(373346, _a_(373342, _n_(373341, "np", lambda: np), "arange"), start = _n_(373343, "bin", lambda: bin)[0], stop = _n_(373344, "bin", lambda: bin)[1], step = _n_(373345, "bin", lambda: bin)[2]))
        _l_(373348)
        #Create histogram
        _c_(373357, _a_(373350, _n_(373349, "plt", lambda: plt), "hist"), _n_(373351, "data", lambda: data)[_a_(373353, _n_(373352, "self", lambda: self), "A")], _n_(373354, "bins", lambda: bins), alpha = 0.5, label = _a_(373356, _n_(373355, "self", lambda: self), "A"), color = "red")
        _l_(373358)
        _c_(373367, _a_(373360, _n_(373359, "plt", lambda: plt), "hist"), _n_(373361, "data", lambda: data)[_a_(373363, _n_(373362, "self", lambda: self), "B")], _n_(373364, "bins", lambda: bins), alpha = 0.5, label = _a_(373366, _n_(373365, "self", lambda: self), "B"), color = "blue")
        _l_(373368)
        #x-axis label
        _c_(373371, _a_(373370, _n_(373369, "plt", lambda: plt), "xlabel"), "Variables", fontsize = 16)  
        _l_(373372)  
        #y-axis lable
        _c_(373375, _a_(373374, _n_(373373, "plt", lambda: plt), "ylabel"), "Frequency", fontsize = 16)
        _l_(373376)
        #Legend of graph
        _c_(373379, _a_(373378, _n_(373377, "plt", lambda: plt), "legend"), loc = 'upper left')
        _l_(373380)
        #Title of graph
        _c_(373387, _a_(373382, _n_(373381, "plt", lambda: plt), "title"), "Overlapping Histogram of Variables " + _a_(373384, _n_(373383, "self", lambda: self), "A") + " and " + _a_(373386, _n_(373385, "self", lambda: self), "B"), loc = 'center')
        _l_(373388)
        _c_(373391, _a_(373390, _n_(373389, "plt", lambda: plt), "show"))
        _l_(373392)

#Create an object from class Graphs that will have one parameter
histo = _c_(373396, _n_(373395, "Graphs", lambda: Graphs), 'YRONJOB', None, None, None)
_l_(373397)
#Call histogram() function to apply to object
_c_(373400, _a_(373399, _n_(373398, "histo", lambda: histo), "histogram"))
_l_(373401)