# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61262052/receiving-following-error-when-trying-to-write-python3-program-nameerror-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        import itertools
        _l_(654006)

except ImportError:
        pass
try:
        import random
        _l_(654008)

except ImportError:
        pass
try:
        import busters
        _l_(654010)

except ImportError:
        pass
try:
        import game
        _l_(654012)

except ImportError:
        pass
try:
        from util import manhattanDistance, raiseNotDefined
        _l_(654014)

except ImportError:
        pass

def getBeliefDistribution(self):
        _l_(654032)

        """
        Return the agent's current belief state, a distribution over ghost
        locations conditioned on all evidence and time passage. This method
        essentially converts a list of particles into a belief distribution.

        This function should return a normalized distribution.
        """
        "*** YOUR CODE HERE ***"
        _l_(654015)
        beliefDistribution = _c_(654018, _a_(654017, _n_(654016, "util", lambda: util), "Counter"))
        _l_(654019)

        for particle in _a_(654021, _n_(654020, "self", lambda: self), "particles"):
                _l_(654025)

                _n_(654022, "beliefDistribution", lambda: beliefDistribution)[_n_(654023, "particle", lambda: particle)] += 1 #weighing all the particles
                _l_(654024) #weighing all the particles
        _c_(654028, _a_(654027, _n_(654026, "beliefDistribution", lambda: beliefDistribution), "normalize")) #normalizing
        _l_(654029) #normalizing
        aux = _n_(654030, "beliefDistribution", lambda: beliefDistribution) #returns distribution
        _l_(654031) #returns distribution

        return aux #returns distribution