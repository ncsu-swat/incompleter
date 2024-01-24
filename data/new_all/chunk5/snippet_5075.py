# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52726959/i-have-a-problem-with-this-error-message-typeerror-unsupported-operand-types
#main
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main():
    _l_(668022)

    # prepare data
    trainingSet=[]
    _l_(667952)
    testSet=[]
    _l_(667953)
    split = 0.67
    _l_(667954)
    _c_(667959, _n_(667955, "loadDataset", lambda: loadDataset), 'iris.csv', _n_(667956, "split", lambda: split), _n_(667957, "trainingSet", lambda: trainingSet), _n_(667958, "testSet", lambda: testSet))
    _l_(667960)
    _c_(667967, _n_(667961, "print", lambda: print), 'Train set: ' + _c_(667966, _n_(667962, "repr", lambda: repr), _c_(667965, _n_(667963, "len", lambda: len), _n_(667964, "trainingSet", lambda: trainingSet))))
    _l_(667968)
    _c_(667975, _n_(667969, "print", lambda: print), 'Test set: ' + _c_(667974, _n_(667970, "repr", lambda: repr), _c_(667973, _n_(667971, "len", lambda: len), _n_(667972, "testSet", lambda: testSet))))
    _l_(667976)
    # generate predictions
    predictions=[]
    _l_(667977)
    k = 3
    _l_(667978)
    for x in _c_(667983, _n_(667979, "range", lambda: range), _c_(667982, _n_(667980, "len", lambda: len), _n_(667981, "testSet", lambda: testSet))):
        _l_(668010)

        neighbors = _c_(667989, _n_(667984, "getNeighbors", lambda: getNeighbors), _n_(667985, "trainingSet", lambda: trainingSet), _n_(667986, "testSet", lambda: testSet)[_n_(667987, "x", lambda: x)], _n_(667988, "k", lambda: k))
        _l_(667990)
        result = _c_(667993, _n_(667991, "getResponse", lambda: getResponse), _n_(667992, "neighbors", lambda: neighbors))
        _l_(667994)
        _c_(667998, _a_(667996, _n_(667995, "predictions", lambda: predictions), "append"), _n_(667997, "result", lambda: result))
        _l_(667999)
        _c_(668008, _n_(668000, "print", lambda: print), '> predicted=' + _c_(668003, _n_(668001, "repr", lambda: repr), _n_(668002, "result", lambda: result)) + ', actual=' + _c_(668007, _n_(668004, "repr", lambda: repr), _n_(668005, "testSet", lambda: testSet)[_n_(668006, "x", lambda: x)][-1]))
        _l_(668009)
    accuracy = _c_(668014, _n_(668011, "getAccuracy", lambda: getAccuracy), _n_(668012, "testSet", lambda: testSet), _n_(668013, "predictions", lambda: predictions))
    _l_(668015)
    _c_(668020, _n_(668016, "print", lambda: print), 'Accuracy: ' + _c_(668019, _n_(668017, "repr", lambda: repr), _n_(668018, "accuracy", lambda: accuracy)) + '%')
    _l_(668021)

_c_(668024, _n_(668023, "main", lambda: main))
_l_(668025)