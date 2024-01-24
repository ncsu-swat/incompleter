# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/24091859/name-error-in-random-generator-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(366644)

except ImportError:
    pass

class DNA_mutant_generator:
    _l_(366702)

    def __init__ (self, dna):
        _l_(366651)

        _n_(366645, "self", lambda: self).dna = _n_(366646, "dna", lambda: dna)
        _l_(366647)
        _n_(366648, "self", lambda: self).bases = _n_(366649, "bases", lambda: bases)
        _l_(366650)

    def mutate(mutation_rate=0.0066):
        _l_(366701)

        result = []
        _l_(366652)
        mutations = []
        _l_(366653)
        for base in _a_(366655, _n_(366654, "self", lambda: self), "dna"):
            _l_(366686)

            if _c_(366658, _a_(366657, _n_(366656, "random", lambda: random), "random")) < _n_(366659, "mutation_rate", lambda: mutation_rate):
                _l_(366685)

                new_base = _n_(366660, "bases", lambda: bases)[_c_(366664, _a_(366662, _n_(366661, "bases", lambda: bases), "index"), _n_(366663, "base", lambda: base)) - _c_(366667, _a_(366666, _n_(366665, "random", lambda: random), "randint"), 1, 3)] # negatives are OK
                _l_(366668) # negatives are OK
                _c_(366672, _a_(366670, _n_(366669, "result", lambda: result), "append"), _n_(366671, "new_base", lambda: new_base))
                _l_(366673)
                _c_(366678, _a_(366675, _n_(366674, "mutations", lambda: mutations), "append"), (_n_(366676, "base", lambda: base), _n_(366677, "new_base", lambda: new_base)))#appends the original base, as well as the new mutated base to a list of tuples
                _l_(366679)#appends the original base, as well as the new mutated base to a list of tuples
            else:
                _c_(366683, _a_(366681, _n_(366680, "result", lambda: result), "append"), _n_(366682, "base", lambda: base))
                _l_(366684)
        aux = _c_(366689, _a_(366687, "", "join"), _n_(366688, "result", lambda: result)), _n_(366690, "mutations", lambda: mutations)
        _l_(366691)
        return aux

        for result_string, mutations in _n_(366692, "results", lambda: results):
            _l_(366700)

            if _n_(366693, "mutations", lambda: mutations):
                _l_(366699)

                _c_(366697, _n_(366694, "print", lambda: print), _n_(366695, "result_string", lambda: result_string), _n_(366696, "mutations", lambda: mutations))    
                _l_(366698)    
bases = "ACTG"
_l_(366703)
dna = "GGCTCTCCAACAGgtaagcactgaagggtagaaggcatcgtctgtctcagacatgtctggcaccatccgctaagacattaccacgtgggtctcgagtatagctaacacccttctgtttggcagCTTACAGGAGCGAACGTTGG"
_l_(366704)
dna_mutants = _c_(366707, _n_(366705, "DNA_mutant_generator", lambda: DNA_mutant_generator), _n_(366706, "dna", lambda: dna))
_l_(366708)
_c_(366711, _a_(366710, _n_(366709, "dna_mutants", lambda: dna_mutants), "mutate"))
_l_(366712)
results = [_c_(366715, _a_(366714, _n_(366713, "DNA_mutants", lambda: DNA_mutants), "mutate")) for _ in _c_(366717, _n_(366716, "range", lambda: range), 100)]
_l_(366718)