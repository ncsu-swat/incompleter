# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54223591/how-to-prevent-typeerror-list-indices-must-be-integers-or-slices-not-tuple-in
#Array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
Days = ["Mon1","Tue1","Wed1","Thu1","Fri1","Mon2","Tue2","Wed2","Thu2","Fri2","Mon3","Tue3","Wed3","Thu3","Fri3","Mon4","Tue4","Wed4","Thu4","Fri4"]
_l_(567202)
Buses = ["A","B","C","D","E","F"]
_l_(567203)
BusData = [ [0,0,0,2,2], [4,0,3,4,-2], [-5,0,0,3,4], [-1,8,1,1,-2],  #Bus A
            [0,1,0,0,1], [2,0,0,0,0], [1,0,0,0,2], [0,0,1,0,0],   #Bus B
            [2,0,-1,-1,-2], [-2,-3,-1,0,0], [-2,0,1,1,1], [1,-1,-1,2,-2] #Bus C
            [1,0,0,0,0], [0,0,0,0,0], [2,0,0,0,0], [0,0,0,0,0], #Bus D
            [-1,-1,-1,-2,-4], [-10,-2,0,0,0], [0,1,2,-3,1], [1,3,-1,0,0]  #Bus E
            [0,-5,-5,-5,-4], [-3,-5,0,0,0], [0,-2,-3,1,1], [1,0,0,-2,-5] ] #Bus F
_l_(567204) #Bus F

for i in _n_(567205, "BusData", lambda: BusData):
    _l_(567223)

    count = 0
    _l_(567206)
    for x in _n_(567207, "i", lambda: i):
        _l_(567211)

        if _n_(567208, "x", lambda: x) < 0:
            _l_(567210)

            count +=1
            _l_(567209)
    _c_(567221, _n_(567212, "print", lambda: print), _c_(567220, _a_(567213, "Bus {} was late {} times", "format"), _n_(567214, "Buses", lambda: Buses)[_c_(567218, _a_(567216, _n_(567215, "BusData", lambda: BusData), "index"), _n_(567217, "i", lambda: i))], _n_(567219, "count", lambda: count)))
    _l_(567222)