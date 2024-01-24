# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71607384/python-function-error-typeerror-tuple-indices-must-be-integers-or-slices-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
clusters = _c_(581388, _a_(581384, _n_(581383, "np", lambda: np), "zeros"), (_c_(581387, _n_(581385, "len", lambda: len), _n_(581386, "dataset", lambda: dataset)),1))
_l_(581389)

def assign(centroids,dataset,clusters,k):
    _l_(581430)

    numOfObject=_c_(581392, _n_(581390, "len", lambda: len), _n_(581391, "dataset", lambda: dataset))
    _l_(581393)
    #for every object in the dataset
    for i in _c_(581396, _n_(581394, "range", lambda: range), _n_(581395, "numOfObject", lambda: numOfObject)):
        _l_(581429)

        X=_n_(581397, "dataset", lambda: dataset)[_n_(581398, "i", lambda: i),1:-1]
        _l_(581399)
        #find the closest centroid
        centroidOfX= -1
        _l_(581400)
        distanceToClosestcentroids = _a_(581402, _n_(581401, "np", lambda: np), "Inf")
        _l_(581403)
        for y in _c_(581406, _n_(581404, "range", lambda: range), _n_(581405, "k", lambda: k)):
            _l_(581422)

            
            currentcentroids=_n_(581407, "centroids", lambda: centroids)[_n_(581408, "y", lambda: y),:]
            _l_(581409)
            dist=_c_(581413, _n_(581410, "distance", lambda: distance), _n_(581411, "X", lambda: X),_n_(581412, "currentcentroids", lambda: currentcentroids))
            _l_(581414)
            if _n_(581415, "dist", lambda: dist)<_n_(581416, "distanceToClosestcentroids", lambda: distanceToClosestcentroids):
                _l_(581421)

                #Found closer Centroid
                distanceToClosestcentroids= _n_(581417, "dist", lambda: dist)
                _l_(581418)
                centroidOfX=_n_(581419, "y", lambda: y)
                _l_(581420)
        #assign to X its closest centroid
        _n_(581423, "clusters", lambda: clusters)[_n_(581424, "i", lambda: i)]=_c_(581427, _n_(581425, "int", lambda: int), _n_(581426, "centroidOfX", lambda: centroidOfX))
        _l_(581428)


#assign((2.5),dataset,clusters,20)
_c_(581434, _n_(581431, "assign", lambda: assign), (2,1),_n_(581432, "dataset", lambda: dataset),_n_(581433, "clusters", lambda: clusters),20)
_l_(581435)