# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52726959/i-have-a-problem-with-this-error-message-typeerror-unsupported-operand-types
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
trainingSet=[]
_l_(677352)
testSet=[]
_l_(677353)
_c_(677357, _n_(677354, "loadDataset", lambda: loadDataset), 'iris.csv', 0.66, _n_(677355, "trainingSet", lambda: trainingSet), _n_(677356, "testSet", lambda: testSet))
_l_(677358)
_c_(677365, _n_(677359, "print", lambda: print), 'Train: ' + _c_(677364, _n_(677360, "repr", lambda: repr), _c_(677363, _n_(677361, "len", lambda: len), _n_(677362, "trainingSet", lambda: trainingSet)))) 
_l_(677366) 
_c_(677373, _n_(677367, "print", lambda: print), 'Test: ' + _c_(677372, _n_(677368, "repr", lambda: repr), _c_(677371, _n_(677369, "len", lambda: len), _n_(677370, "testSet", lambda: testSet))))
_l_(677374)