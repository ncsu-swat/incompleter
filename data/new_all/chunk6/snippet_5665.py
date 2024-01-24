# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/24091859/name-error-in-random-generator-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(334974)

except ImportError:
    pass

class DNA_mutant_generator:
    _l_(335029)

    def __init__ (self, dna):
        _l_(334979)

        _n_(334975, "self", lambda: self).dna = _n_(334976, "dna", lambda: dna)
        _l_(334977)
        dna = "GGCTCTCCAACAGgtaagcactgaagggtagaaggcatcgtctgtctcagacatgtctggcaccatccgctaagacattaccacgtgggtctcgagtatagctaacacccttctgtttggcagCTTACAGGAGCGAACGTTGG"
        _l_(334978)

    def mutate(mutation_rate=0.0066):
        _l_(335028)

        result = []
        _l_(334980)
        mutations = []
        _l_(334981)
        for base in _n_(334982, "dna", lambda: dna):
            _l_(335013)

            if _c_(334985, _a_(334984, _n_(334983, "random", lambda: random), "random")) < _n_(334986, "mutation_rate", lambda: mutation_rate):
                _l_(335012)

                new_base = _n_(334987, "bases", lambda: bases)[_c_(334991, _a_(334989, _n_(334988, "bases", lambda: bases), "index"), _n_(334990, "base", lambda: base)) - _c_(334994, _a_(334993, _n_(334992, "random", lambda: random), "randint"), 1, 3)] # negatives are OK
                _l_(334995) # negatives are OK
                _c_(334999, _a_(334997, _n_(334996, "result", lambda: result), "append"), _n_(334998, "new_base", lambda: new_base))
                _l_(335000)
                _c_(335005, _a_(335002, _n_(335001, "mutations", lambda: mutations), "append"), (_n_(335003, "base", lambda: base), _n_(335004, "new_base", lambda: new_base)))#appends the original base, as well as the new mutated base to a list of tuples
                _l_(335006)#appends the original base, as well as the new mutated base to a list of tuples
            else:
                _c_(335010, _a_(335008, _n_(335007, "result", lambda: result), "append"), _n_(335009, "base", lambda: base))
                _l_(335011)
        aux = _c_(335016, _a_(335014, "", "join"), _n_(335015, "result", lambda: result)), _n_(335017, "mutations", lambda: mutations)
        _l_(335018)
        return aux

        for result_string, mutations in _n_(335019, "results", lambda: results):
            _l_(335027)

            if _n_(335020, "mutations", lambda: mutations):
                _l_(335026)

                _c_(335024, _n_(335021, "print", lambda: print), _n_(335022, "result_string", lambda: result_string), _n_(335023, "mutations", lambda: mutations))    
                _l_(335025)    

results = [_c_(335033, _a_(335031, _n_(335030, "DNA_mutant_generator", lambda: DNA_mutant_generator), "mutate"), _n_(335032, "dna", lambda: dna)) for _ in _c_(335035, _n_(335034, "range", lambda: range), 100)]
_l_(335036)


dna_mutants = _c_(335038, _n_(335037, "DNA_mutant_generator", lambda: DNA_mutant_generator))
_l_(335039)
_c_(335042, _a_(335041, _n_(335040, "dna_mutants", lambda: dna_mutants), "mutate"))
_l_(335043)