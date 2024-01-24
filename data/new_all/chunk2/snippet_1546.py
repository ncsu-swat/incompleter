# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32972393/python-attributeerror-list-object-has-no-attribute-after-using-queue
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections
    _l_(433168)

except ImportError:
    pass
try:
    import queue
    _l_(433170)

except ImportError:
    pass

class Node:
    _l_(433186)


    def __init__(self, Puzzle, last=None):
        _l_(433177)

        _n_(433171, "self", lambda: self).puzzle = _n_(433172, "Puzzle", lambda: Puzzle)
        _l_(433173)
        _n_(433174, "self", lambda: self).last = _n_(433175, "last", lambda: last)
        _l_(433176)

    def getPuzzle(self):
        _l_(433181)

        aux = _a_(433179, _n_(433178, "self", lambda: self), "puzzle")
        _l_(433180)
        return aux

    def getLast(self):
        _l_(433185)

        aux = _a_(433183, _n_(433182, "self", lambda: self), "last")
        _l_(433184)
        return aux

class Puzzle:
    _l_(433406)


    def __init__(self, startState, goalState):
        _l_(433193)

        _n_(433187, "self", lambda: self).state = _n_(433188, "startState", lambda: startState)
        _l_(433189)
        _n_(433190, "self", lambda: self).goal = _n_(433191, "goalState", lambda: goalState)
        _l_(433192)

    def getState():
        _l_(433197)

        aux = _a_(433195, _n_(433194, "self", lambda: self), "state")
        _l_(433196)
        return aux

    def getMoves(self):
        _l_(433372)


        currentState = _a_(433199, _n_(433198, "self", lambda: self), "state")
        _l_(433200)

        possibleNewStates = []
        _l_(433201)

        zeroPos = _c_(433204, _a_(433203, _n_(433202, "currentState", lambda: currentState), "index"), 0)
        _l_(433205)

        if _n_(433206, "zeroPos", lambda: zeroPos) == 0:
            _l_(433369)

            _c_(433211, _a_(433208, _n_(433207, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433210, _n_(433209, "move", lambda: move), 0,1))
            _l_(433212)
            _c_(433217, _a_(433214, _n_(433213, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433216, _n_(433215, "move", lambda: move), 0,3))
            _l_(433218)
        elif _n_(433219, "zeroPos", lambda: zeroPos) == 1:
            _l_(433368)

            _c_(433224, _a_(433221, _n_(433220, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433223, _n_(433222, "move", lambda: move), 1,0))
            _l_(433225)
            _c_(433230, _a_(433227, _n_(433226, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433229, _n_(433228, "move", lambda: move), 1,2))
            _l_(433231)
            _c_(433236, _a_(433233, _n_(433232, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433235, _n_(433234, "move", lambda: move), 1,4))
            _l_(433237)
        elif _n_(433238, "zeroPos", lambda: zeroPos) == 2:
            _l_(433367)

            _c_(433243, _a_(433240, _n_(433239, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433242, _n_(433241, "move", lambda: move), 2,1))
            _l_(433244)
            _c_(433249, _a_(433246, _n_(433245, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433248, _n_(433247, "move", lambda: move), 2,5))
            _l_(433250)
        elif _n_(433251, "zeroPos", lambda: zeroPos) == 3:
            _l_(433366)

            _c_(433256, _a_(433253, _n_(433252, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433255, _n_(433254, "move", lambda: move), 3,0))
            _l_(433257)
            _c_(433262, _a_(433259, _n_(433258, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433261, _n_(433260, "move", lambda: move), 3,4))
            _l_(433263)
            _c_(433268, _a_(433265, _n_(433264, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433267, _n_(433266, "move", lambda: move), 3,6))
            _l_(433269)
        elif _n_(433270, "zeroPos", lambda: zeroPos) == 4:
            _l_(433365)

            _c_(433276, _a_(433272, _n_(433271, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433275, _a_(433274, _n_(433273, "self", lambda: self), "move"), 4,1))
            _l_(433277)
            _c_(433283, _a_(433279, _n_(433278, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433282, _a_(433281, _n_(433280, "self", lambda: self), "move"), 4,3))
            _l_(433284)
            _c_(433290, _a_(433286, _n_(433285, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433289, _a_(433288, _n_(433287, "self", lambda: self), "move"), 4,5))
            _l_(433291)
            _c_(433297, _a_(433293, _n_(433292, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433296, _a_(433295, _n_(433294, "self", lambda: self), "move"), 4,7))
            _l_(433298)
        elif _n_(433299, "zeroPos", lambda: zeroPos) == 5:
            _l_(433364)

            _c_(433304, _a_(433301, _n_(433300, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433303, _n_(433302, "move", lambda: move), 5,2))
            _l_(433305)
            _c_(433310, _a_(433307, _n_(433306, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433309, _n_(433308, "move", lambda: move), 5,4))
            _l_(433311)
            _c_(433316, _a_(433313, _n_(433312, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433315, _n_(433314, "move", lambda: move), 5,8))
            _l_(433317)
        elif _n_(433318, "zeroPos", lambda: zeroPos) == 6:
            _l_(433363)

            _c_(433323, _a_(433320, _n_(433319, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433322, _n_(433321, "move", lambda: move), 6,3))
            _l_(433324)
            _c_(433329, _a_(433326, _n_(433325, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433328, _n_(433327, "move", lambda: move), 6,7))
            _l_(433330)
        elif _n_(433331, "zeroPos", lambda: zeroPos) == 7:
            _l_(433362)

            _c_(433336, _a_(433333, _n_(433332, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433335, _n_(433334, "move", lambda: move), 7,4))
            _l_(433337)
            _c_(433342, _a_(433339, _n_(433338, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433341, _n_(433340, "move", lambda: move), 7,6))
            _l_(433343)
            _c_(433348, _a_(433345, _n_(433344, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433347, _n_(433346, "move", lambda: move), 7,8))
            _l_(433349)
        else:
            _c_(433354, _a_(433351, _n_(433350, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433353, _n_(433352, "move", lambda: move), 8,5))
            _l_(433355)
            _c_(433360, _a_(433357, _n_(433356, "possibleNewStates", lambda: possibleNewStates), "append"), _c_(433359, _n_(433358, "move", lambda: move), 8,7))
            _l_(433361)
        aux = _n_(433370, "possibleNewStates", lambda: possibleNewStates)
        _l_(433371)

        return aux

    def move(self, current, to):
        _l_(433390)


        changeState = _a_(433374, _n_(433373, "self", lambda: self), "state")
        _l_(433375)

        save = _n_(433376, "changeState", lambda: changeState)[_n_(433377, "to", lambda: to)]
        _l_(433378)
        _n_(433379, "changeState", lambda: changeState)[_n_(433380, "to", lambda: to)] = _n_(433381, "changeState", lambda: changeState)[_n_(433382, "current", lambda: current)]
        _l_(433383)
        _n_(433384, "changeState", lambda: changeState)[_n_(433385, "current", lambda: current)] = _n_(433386, "save", lambda: save)
        _l_(433387)
        aux = _n_(433388, "changeState", lambda: changeState)
        _l_(433389)

        return aux

    def printPuzzle(self):
        _l_(433399)


        copyState = _a_(433392, _n_(433391, "self", lambda: self), "state")
        _l_(433393)
        _c_(433396, _n_(433394, "print", lambda: print), _n_(433395, "copyState", lambda: copyState))
        _l_(433397)
        '''
        for i in range(9):
            if i == 2 or i == 5:
                print((str)(copyState[i]))
            else:
                print((str)(copyState[i])+" ", end="")
            print()
        '''
        _l_(433398)

    def isSolved(self):
        _l_(433405)

        aux = _a_(433401, _n_(433400, "self", lambda: self), "state") == _a_(433403, _n_(433402, "self", lambda: self), "goal")
        _l_(433404)
        return aux

class Solver:
    _l_(433484)


    def __init__(self, Puzzle):
        _l_(433410)

        _n_(433407, "self", lambda: self).puzzle = _n_(433408, "Puzzle", lambda: Puzzle)
        _l_(433409)

    def solveBFS(self):
        _l_(433466)

        puzzle = _a_(433412, _n_(433411, "self", lambda: self), "puzzle")
        _l_(433413)
        startNode = _c_(433416, _n_(433414, "Node", lambda: Node), _n_(433415, "puzzle", lambda: puzzle))
        _l_(433417)
        myQueue = _c_(433420, _a_(433419, _n_(433418, "queue", lambda: queue), "Queue"), 0)
        _l_(433421)
        _c_(433425, _a_(433423, _n_(433422, "myQueue", lambda: myQueue), "put"), _n_(433424, "startNode", lambda: startNode))
        _l_(433426)
        myPuzzle = _c_(433429, _a_(433428, _n_(433427, "startNode", lambda: startNode), "getPuzzle"))
        _l_(433430)
        _c_(433435, _n_(433431, "print", lambda: print), _c_(433434, _a_(433433, _n_(433432, "myPuzzle", lambda: myPuzzle), "isSolved")))
        _l_(433436)
        while _n_(433437, "myQueue", lambda: myQueue):
            _l_(433465)

            currentNode = _c_(433440, _a_(433439, _n_(433438, "myQueue", lambda: myQueue), "get"))
            _l_(433441)
            currentPuzzle = _a_(433443, _n_(433442, "currentNode", lambda: currentNode), "puzzle")
            _l_(433444)

            if _n_(433445, "currentPuzzle", lambda: currentPuzzle) == [0,1,2,3,4,5,6,7,8]:
                _l_(433448)

                aux = _n_(433446, "currentNode", lambda: currentNode)
                _l_(433447)
                return aux

            nextMoves = _c_(433451, _a_(433450, _n_(433449, "currentPuzzle", lambda: currentPuzzle), "getMoves")) # << ERROR HERE
            _l_(433452) # << ERROR HERE
            for state in _n_(433453, "nextMoves", lambda: nextMoves):
                _l_(433464)

                nextNode = _c_(433457, _n_(433454, "Node", lambda: Node), _n_(433455, "state", lambda: state), _n_(433456, "currentNode", lambda: currentNode))
                _l_(433458)
                _c_(433462, _a_(433460, _n_(433459, "myQueue", lambda: myQueue), "put"), _n_(433461, "nextNode", lambda: nextNode))
                _l_(433463)

    startingState = [7,2,4,5,0,6,8,3,1]
    _l_(433467)
    goalState = [0,1,2,3,4,5,6,7,8]
    _l_(433468)
    myPuzzle = _c_(433470, _n_(433469, "Puzzle", lambda: Puzzle), startingState, goalState)
    _l_(433471)
    mySolver = _c_(433473, _n_(433472, "Solver", lambda: Solver), myPuzzle)
    _l_(433474)
    goalNode = _c_(433476, _a_(433475, mySolver, "solveBFS"))
    _l_(433477)
    goalPuzzle = _c_(433479, _a_(433478, goalNode, "getPuzzle"))
    _l_(433480)
    _c_(433482, _a_(433481, goalPuzzle, "printPuzzle"))
    _l_(433483)