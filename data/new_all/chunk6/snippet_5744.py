# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37583561/typeerror-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(338422)

except ImportError:
    pass

noun = ["fossil" , "horse" , "aardvark" , "chef" , "judge"]
_l_(338423)
verb= [ "kicks", "jingles", "bounces", "slurps", "meows"]
_l_(338424)
adjs= ["fury" , "balding" , "incredulous" , "fragant"]
_l_(338425)
prep= ["against" , "after" , "into" , "beneath" , "for", "in"]
_l_(338426)
ads= ["curiously" , "extravagantly" , "furiously" , "sensuously"]
_l_(338427)
 
def selectn(list, n) :
    _l_(338451)

    selection = []
    _l_(338428)
    while (_c_(338431, _n_(338429, "len", lambda: len), _n_(338430, "selection", lambda: selection)) != _n_(338432, "n", lambda: n)) :
        _l_(338446)

        w = _c_(338436, _a_(338434, _n_(338433, "random", lambda: random), "choice"), _n_(338435, "list", lambda: list))
        _l_(338437)
        if _n_(338438, "w", lambda: w) not in _n_(338439, "selection", lambda: selection) :
            _l_(338445)

            _c_(338443, _a_(338441, _n_(338440, "selection", lambda: selection), "append"), _n_(338442, "w", lambda: w))
            _l_(338444)
    _c_(338449, _n_(338447, "print", lambda: print), _n_(338448, "selection", lambda: selection))
    _l_(338450)

def makePoem() :
    _l_(338511)

    my_nouns = _c_(338454, _n_(338452, "selectn", lambda: selectn), _n_(338453, "noun", lambda: noun),3)
    _l_(338455)
    my_verbs = _c_(338458, _n_(338456, "selectn", lambda: selectn), _n_(338457, "verb", lambda: verb),3)
    _l_(338459)
    my_adj = _c_(338462, _n_(338460, "selectn", lambda: selectn), _n_(338461, "adjs", lambda: adjs),3)
    _l_(338463)
    my_adverb = _c_(338466, _n_(338464, "selectn", lambda: selectn), _n_(338465, "ads", lambda: ads),1)
    _l_(338467)
    my_prepo = _c_(338470, _n_(338468, "selectn", lambda: selectn), _n_(338469, "prep", lambda: prep),2)
    _l_(338471)
    
    _c_(338477, _n_(338472, "print", lambda: print), _c_(338476, _a_(338473, "A {} {}", "format"), _n_(338474, "my_adj", lambda: my_adj)[0], _n_(338475, "my_nouns", lambda: my_nouns)[0]))
    _l_(338478)
    _c_(338480, _n_(338479, "print", lambda: print), "")
    _l_(338481)
    _c_(338491, _n_(338482, "print", lambda: print), _c_(338490, _a_(338483, "A {} {} {} {} the {} {}", "format"), _n_(338484, "my_adj", lambda: my_adj)[0], _n_(338485, "my_nouns", lambda: my_nouns)[0], _n_(338486, "my_verbs", lambda: my_verbs)[0], _n_(338487, "my_prepo", lambda: my_prepo)[0], _n_(338488, "my_adj", lambda: my_adj)[1], _n_(338489, "my_nouns", lambda: my_nouns)[1]))
    _l_(338492)
    _c_(338499, _n_(338493, "print", lambda: print), _c_(338498, _a_(338494, "{}, the {} {}", "format"), _n_(338495, "my_adverb", lambda: my_adverb)[0], _n_(338496, "my_nouns", lambda: my_nouns)[0], _n_(338497, "my_verbs", lambda: my_verbs)[1]))
    _l_(338500)
    _c_(338509, _n_(338501, "print", lambda: print), _c_(338508, _a_(338502, "the {} {} {} a {} {}", "format"), _n_(338503, "my_nouns", lambda: my_nouns)[1], _n_(338504, "my_verbs", lambda: my_verbs)[2], _n_(338505, "my_prepo", lambda: my_prepo)[1], _n_(338506, "my_adj", lambda: my_adj)[2], _n_(338507, "my_nouns", lambda: my_nouns)[2]))
    _l_(338510)

_c_(338513, _n_(338512, "makePoem", lambda: makePoem))
_l_(338514)