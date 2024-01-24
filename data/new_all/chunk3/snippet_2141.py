# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61624362/nameerror-name-synset-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(526046, _n_(526045, "print", lambda: print), "Array..............\n\n")
_l_(526047)
tagged=_c_(526051, _a_(526049, _n_(526048, "np", lambda: np), "array"), _n_(526050, "df", lambda: df)['tagged_texts'])
_l_(526052)
temp = []
_l_(526053)
for x in _n_(526054, "tagged", lambda: tagged):
    _l_(526062)

    for y in _n_(526055, "x", lambda: x):
        _l_(526061)

        _c_(526059, _a_(526057, _n_(526056, "temp", lambda: temp), "append"), _n_(526058, "y", lambda: y)) 
        _l_(526060) 
tagged = _n_(526063, "temp", lambda: temp)
_l_(526064)
_c_(526067, _n_(526065, "print", lambda: print), _n_(526066, "tagged", lambda: tagged))
_l_(526068)
pos=neg=obj=count=0
_l_(526069)
for word, tag in _n_(526070, "tagged", lambda: tagged):
    _l_(526142)

    ss_set = []
    _l_(526071)
    if 'NN' in _n_(526072, "tag", lambda: tag) and _c_(526076, _a_(526074, _n_(526073, "swn", lambda: swn), "senti_synsets"), _n_(526075, "word", lambda: word)):
        _l_(526123)

        ss_set = _c_(526082, _n_(526077, "list", lambda: list), _c_(526081, _a_(526079, _n_(526078, "swn", lambda: swn), "senti_synsets"), _n_(526080, "word", lambda: word)))
        _l_(526083)
    elif 'VB' in _n_(526084, "tag", lambda: tag) and _c_(526088, _a_(526086, _n_(526085, "swn", lambda: swn), "senti_synsets"), _n_(526087, "word", lambda: word)):
        _l_(526122)

        ss_set = _c_(526094, _n_(526089, "list", lambda: list), _c_(526093, _a_(526091, _n_(526090, "swn", lambda: swn), "senti_synsets"), _n_(526092, "word", lambda: word)))[0]
        _l_(526095)
    elif 'JJ' in _n_(526096, "tag", lambda: tag) and _c_(526100, _a_(526098, _n_(526097, "swn", lambda: swn), "senti_synsets"), _n_(526099, "word", lambda: word)):
        _l_(526121)

        ss_set = _c_(526106, _n_(526101, "list", lambda: list), _c_(526105, _a_(526103, _n_(526102, "swn", lambda: swn), "senti_synsets"), _n_(526104, "word", lambda: word)))[0]
        _l_(526107)
    elif 'RB' in _n_(526108, "tag", lambda: tag) and _c_(526112, _a_(526110, _n_(526109, "swn", lambda: swn), "senti_synsets"), _n_(526111, "word", lambda: word)):
        _l_(526120)

        ss_set = _c_(526118, _n_(526113, "list", lambda: list), _c_(526117, _a_(526115, _n_(526114, "swn", lambda: swn), "senti_synsets"), _n_(526116, "word", lambda: word)))[0]
        _l_(526119)
    if _n_(526124, "ss_set", lambda: ss_set):
        _l_(526141)

        pos=_n_(526125, "pos", lambda: pos)+_c_(526128, _a_(526127, _n_(526126, "synset", lambda: synset), "pos_score"))
        _l_(526129)
        neg=_n_(526130, "neg", lambda: neg)+_c_(526133, _a_(526132, _n_(526131, "synset", lambda: synset), "neg_score"))
        _l_(526134)
        obj=_n_(526135, "obj", lambda: obj)+_c_(526138, _a_(526137, _n_(526136, "synset", lambda: synset), "obj_score"))
        _l_(526139)
        count+=1
        _l_(526140)
final_score=_n_(526143, "pos", lambda: pos)-_n_(526144, "neg", lambda: neg)
_l_(526145)
_c_(526148, _n_(526146, "print", lambda: print), _n_(526147, "final_score", lambda: final_score))
_l_(526149)
_n_(526150, "df", lambda: df)['final_score']=_n_(526151, "final_score", lambda: final_score)
_l_(526152)