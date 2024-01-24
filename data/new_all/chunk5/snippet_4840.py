# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46173323/getting-error-on-frequency-distribution-typeerror-unhashable-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
doc_clean = []
_l_(693253)
stopwords_corpus = _c_(693255, _n_(693254, "UrduCorpusReader", lambda: UrduCorpusReader), './data', ['stopwords-ur.txt'])    
_l_(693256)    
stopwords = _c_(693259, _a_(693258, _n_(693257, "stopwords_corpus", lambda: stopwords_corpus), "words"))
_l_(693260)
# print(stopwords)
for infile in _c_(693263, _a_(693262, _n_(693261, "wordlists", lambda: wordlists), "fileids")):
    _l_(693290)

    words = _c_(693267, _a_(693265, _n_(693264, "wordlists", lambda: wordlists), "words"), _n_(693266, "infile", lambda: infile))
    _l_(693268)
    _c_(693271, _n_(693269, "print", lambda: print), _n_(693270, "infile", lambda: infile))
    _l_(693272)
    #print(words)
    finalized_words = _c_(693276, _n_(693273, "remove_urdu_stopwords", lambda: remove_urdu_stopwords), _n_(693274, "stopwords", lambda: stopwords), _n_(693275, "words", lambda: words))
    _l_(693277)
    _c_(693279, _n_(693278, "print", lambda: print), "\n==== WITHOUT STOPWORDS ===========\n")
    _l_(693280)
    _c_(693283, _n_(693281, "print", lambda: print), _n_(693282, "finalized_words", lambda: finalized_words))
    _l_(693284)
    _c_(693288, _a_(693286, _n_(693285, "doc_clean", lambda: doc_clean), "append"), _n_(693287, "finalized_words", lambda: finalized_words))
    _l_(693289)
fdist1 = _c_(693293, _n_(693291, "FreqDist", lambda: FreqDist), _n_(693292, "doc_clean", lambda: doc_clean)) 
_l_(693294) 
_c_(693297, _n_(693295, "print", lambda: print), _n_(693296, "fdist1", lambda: fdist1)) 
_l_(693298) 