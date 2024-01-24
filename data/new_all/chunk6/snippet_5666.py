# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/24091859/name-error-in-random-generator-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(370945)

except ImportError:
    pass

class DNA_mutant_generator:
    _l_(371003)

    def __init__ (self, dna):
        _l_(370952)

        _n_(370946, "self", lambda: self).dna = _n_(370947, "dna", lambda: dna)
        _l_(370948)
        _n_(370949, "self", lambda: self).bases = _n_(370950, "bases", lambda: bases)
        _l_(370951)

    def mutate(mutation_rate=0.0066):
        _l_(371002)

        result = []
        _l_(370953)
        mutations = []
        _l_(370954)
        for base in _a_(370956, _n_(370955, "self", lambda: self), "dna"):
            _l_(370987)

            if _c_(370959, _a_(370958, _n_(370957, "random", lambda: random), "random")) < _n_(370960, "mutation_rate", lambda: mutation_rate):
                _l_(370986)

                new_base = _n_(370961, "bases", lambda: bases)[_c_(370965, _a_(370963, _n_(370962, "bases", lambda: bases), "index"), _n_(370964, "base", lambda: base)) - _c_(370968, _a_(370967, _n_(370966, "random", lambda: random), "randint"), 1, 3)] # negatives are OK
                _l_(370969) # negatives are OK
                _c_(370973, _a_(370971, _n_(370970, "result", lambda: result), "append"), _n_(370972, "new_base", lambda: new_base))
                _l_(370974)
                _c_(370979, _a_(370976, _n_(370975, "mutations", lambda: mutations), "append"), (_n_(370977, "base", lambda: base), _n_(370978, "new_base", lambda: new_base)))#appends the original base, as well as the new mutated base to a list of tuples
                _l_(370980)#appends the original base, as well as the new mutated base to a list of tuples
            else:
                _c_(370984, _a_(370982, _n_(370981, "result", lambda: result), "append"), _n_(370983, "base", lambda: base))
                _l_(370985)
        aux = _c_(370990, _a_(370988, "", "join"), _n_(370989, "result", lambda: result)), _n_(370991, "mutations", lambda: mutations)
        _l_(370992)
        return aux

        for result_string, mutations in _n_(370993, "results", lambda: results):
            _l_(371001)

            if _n_(370994, "mutations", lambda: mutations):
                _l_(371000)

                _c_(370998, _n_(370995, "print", lambda: print), _n_(370996, "result_string", lambda: result_string), _n_(370997, "mutations", lambda: mutations))    
                _l_(370999)    
bases = "ACTG"
_l_(371004)
dna = "GGCTCTCCAACAGgtaagcactgaagggtagaaggcatcgtctgtctcagacatgtctggcaccatccgctaagacattaccacgtgggtctcgagtatagctaacacccttctgtttggcagCTTACAGGAGCGAACGTTGG"
_l_(371005)
dna_mutants = _c_(371008, _n_(371006, "DNA_mutant_generator", lambda: DNA_mutant_generator), _n_(371007, "dna", lambda: dna))
_l_(371009)
_c_(371012, _a_(371011, _n_(371010, "dna_mutants", lambda: dna_mutants), "mutate"))
_l_(371013)
results = [_c_(371016, _a_(371015, _n_(371014, "DNA_mutants", lambda: DNA_mutants), "mutate")) for _ in _c_(371018, _n_(371017, "range", lambda: range), 100)]
_l_(371019)