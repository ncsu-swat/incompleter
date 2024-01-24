# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60990112/typeerror-fit-takes-1-positional-argument-but-3-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyClass (_n_(357205, "BaseEstimator", lambda: BaseEstimator), _n_(357206, "ClassifierMixin", lambda: ClassifierMixin)):
    _l_(357220)


    def __init__(self, FilePath1, FilePath2):
        _l_(357213)

        _n_(357207, "self", lambda: self).fp1 = _n_(357208, "FilePath1", lambda: FilePath1)
        _l_(357209)
        _n_(357210, "self", lambda: self).fp2 = _n_(357211, "FilePath2", lambda: FilePath2)
        _l_(357212)

    #Return self nothing else to do here    
    def fit( self, X = None, y = None ):
        _l_(357216)

        aux = _n_(357214, "self", lambda: self) 
        _l_(357215) 
        return aux 

    def transform( self, X, y = None ):
        _l_(357219)

        aux = _n_(357217, "X", lambda: X)
        _l_(357218)
        return aux