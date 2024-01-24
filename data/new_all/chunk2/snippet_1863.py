# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47715289/typeerror-not-supported-between-instances-of-float-and-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(429292)

except ImportError:
    pass

def generateVirus(length):
    _l_(429302)

    aux = _c_(429300, _a_(429293, '', "join"), [_c_(429296, _a_(429295, _n_(429294, "random", lambda: random), "choice"), ['A', 'G', 'T', 'C']) for i in _c_(429299, _n_(429297, "range", lambda: range), _n_(429298, "length", lambda: length))])
    _l_(429301)
    return aux

def mutate(virus):
    _l_(429322)

    rand = _c_(429308, _a_(429304, _n_(429303, "random", lambda: random), "randint"), 0, _c_(429307, _n_(429305, "len", lambda: len), _n_(429306, "virus", lambda: virus))-1)
    _l_(429309)
    aux = _n_(429310, "virus", lambda: virus)[:_n_(429311, "rand", lambda: rand)] + _c_(429318, _a_(429313, _n_(429312, "random", lambda: random), "choice"), [_n_(429314, "i", lambda: i) for i in 'AGTC' if _n_(429315, "i", lambda: i) != _n_(429316, "virus", lambda: virus)[_n_(429317, "rand", lambda: rand)]]) + _n_(429319, "virus", lambda: virus)[_n_(429320, "rand", lambda: rand)+1:]
    _l_(429321)
    return aux

def kill(viruses, mortalityProb):
    _l_(429330)

    aux = [_n_(429323, "survivors", lambda: survivors) for survivors in _n_(429324, "viruses", lambda: viruses) if _c_(429327, _a_(429326, _n_(429325, "random", lambda: random), "random")) > _n_(429328, "mortalityProb", lambda: mortalityProb)]
    _l_(429329)
    return aux

def reproduce(viruses, mutationProb, reproductionProb):
    _l_(429363)

    nextgen = []
    _l_(429331)
    for i in _n_(429332, "viruses", lambda: viruses):
        _l_(429360)

        _c_(429336, _a_(429334, _n_(429333, "nextgen", lambda: nextgen), "append"), _n_(429335, "i", lambda: i))
        _l_(429337)
        if _c_(429340, _a_(429339, _n_(429338, "random", lambda: random), "random")) < _n_(429341, "reproductionProb", lambda: reproductionProb):
            _l_(429359)

            if _c_(429344, _a_(429343, _n_(429342, "random", lambda: random), "random")) < _n_(429345, "mutationProb", lambda: mutationProb):
                _l_(429358)

                _c_(429351, _a_(429347, _n_(429346, "nextgen", lambda: nextgen), "append"), _c_(429350, _n_(429348, "mutate", lambda: mutate), _n_(429349, "i", lambda: i)))
                _l_(429352)
            else:
                _c_(429356, _a_(429354, _n_(429353, "nextgen", lambda: nextgen), "append"), _n_(429355, "i", lambda: i))
                _l_(429357)
    aux = _n_(429361, "nextgen", lambda: nextgen)
    _l_(429362)
    return aux

def reproductionProbability(viruses, maxReproductionProb, maxPopulation):
    _l_(429370)

    aux = (1 - (_c_(429366, _n_(429364, "len", lambda: len), _n_(429365, "viruses", lambda: viruses)) / _n_(429367, "maxPopulation", lambda: maxPopulation))) * _n_(429368, "maxReproductionProb", lambda: maxReproductionProb)
    _l_(429369)
    return aux

def simulate(viruses, mortalityProb, mutationProb, maxReproductionProb, 
    maxPopulation, timesteps = 500):
    _l_(429401)

    pop_size = []
    _l_(429371)
    while _n_(429372, "timesteps", lambda: timesteps) > -1:
        _l_(429398)

        survivors = _c_(429376, _n_(429373, "kill", lambda: kill), _n_(429374, "viruses", lambda: viruses), _n_(429375, "mortalityProb", lambda: mortalityProb))
        _l_(429377)
        reproductionProb = _c_(429382, _n_(429378, "reproductionProbability", lambda: reproductionProbability), _n_(429379, "survivors", lambda: survivors), _n_(429380, "maxReproductionProb", lambda: maxReproductionProb), _n_(429381, "maxPopulation", lambda: maxPopulation))
        _l_(429383)
        viruses = _c_(429388, _n_(429384, "reproduce", lambda: reproduce), _n_(429385, "survivors", lambda: survivors), _n_(429386, "mutationProb", lambda: mutationProb), _n_(429387, "reproductionProb", lambda: reproductionProb))
        _l_(429389)
        _c_(429395, _a_(429391, _n_(429390, "pop_size", lambda: pop_size), "append"), _c_(429394, _n_(429392, "len", lambda: len), _n_(429393, "viruses", lambda: viruses)))
        _l_(429396)
        timesteps -= 1
        _l_(429397)
    aux = _n_(429399, "pop_size", lambda: pop_size)
    _l_(429400)
    return aux

_c_(429405, _n_(429402, "print", lambda: print), _c_(429404, _n_(429403, "simulate", lambda: simulate), ['GCTCC', 'CCGG', 'AACCGG', 'CCCTATAGG'], 0.05, 0.1, 0.07, 1000))
_l_(429406)