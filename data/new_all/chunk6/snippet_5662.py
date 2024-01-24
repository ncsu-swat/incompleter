# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/24091859/name-error-in-random-generator-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(373832)

except ImportError:
    pass

class DNA_mutant_generator:
    _l_(373887)

    def __init__ (self, dna):
        _l_(373837)

        _n_(373833, "self", lambda: self).dna = _n_(373834, "dna", lambda: dna)
        _l_(373835)
        dna = "GGCTCTCCAACAGgtaagcactgaagggtagaaggcatcgtctgtctcagacatgtctggcaccatccgctaagacattaccacgtgggtctcgagtatagctaacacccttctgtttggcagCTTACAGGAGCGAACGTTGG"
        _l_(373836)

    def mutate(mutation_rate=0.0066):
        _l_(373886)

        result = []
        _l_(373838)
        mutations = []
        _l_(373839)
        for base in _n_(373840, "dna", lambda: dna):
            _l_(373871)

            if _c_(373843, _a_(373842, _n_(373841, "random", lambda: random), "random")) < _n_(373844, "mutation_rate", lambda: mutation_rate):
                _l_(373870)

                new_base = _n_(373845, "bases", lambda: bases)[_c_(373849, _a_(373847, _n_(373846, "bases", lambda: bases), "index"), _n_(373848, "base", lambda: base)) - _c_(373852, _a_(373851, _n_(373850, "random", lambda: random), "randint"), 1, 3)] # negatives are OK
                _l_(373853) # negatives are OK
                _c_(373857, _a_(373855, _n_(373854, "result", lambda: result), "append"), _n_(373856, "new_base", lambda: new_base))
                _l_(373858)
                _c_(373863, _a_(373860, _n_(373859, "mutations", lambda: mutations), "append"), (_n_(373861, "base", lambda: base), _n_(373862, "new_base", lambda: new_base)))#appends the original base, as well as the new mutated base to a list of tuples
                _l_(373864)#appends the original base, as well as the new mutated base to a list of tuples
            else:
                _c_(373868, _a_(373866, _n_(373865, "result", lambda: result), "append"), _n_(373867, "base", lambda: base))
                _l_(373869)
        aux = _c_(373874, _a_(373872, "", "join"), _n_(373873, "result", lambda: result)), _n_(373875, "mutations", lambda: mutations)
        _l_(373876)
        return aux

        for result_string, mutations in _n_(373877, "results", lambda: results):
            _l_(373885)

            if _n_(373878, "mutations", lambda: mutations):
                _l_(373884)

                _c_(373882, _n_(373879, "print", lambda: print), _n_(373880, "result_string", lambda: result_string), _n_(373881, "mutations", lambda: mutations))    
                _l_(373883)    

results = [_c_(373891, _a_(373889, _n_(373888, "DNA_mutant_generator", lambda: DNA_mutant_generator), "mutate"), _n_(373890, "dna", lambda: dna)) for _ in _c_(373893, _n_(373892, "range", lambda: range), 100)]
_l_(373894)


dna_mutants = _c_(373896, _n_(373895, "DNA_mutant_generator", lambda: DNA_mutant_generator))
_l_(373897)
_c_(373900, _a_(373899, _n_(373898, "dna_mutants", lambda: dna_mutants), "mutate"))
_l_(373901)