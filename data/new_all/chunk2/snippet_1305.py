# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48768084/nltk-unigramtagger-typeerror-unhashable-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
brown_tagged_sents = _c_(458249, _a_(458248, _n_(458247, "brown", lambda: brown), "tagged_sents"))
_l_(458250)
brown_sents = _c_(458253, _a_(458252, _n_(458251, "brown", lambda: brown), "sents"))
_l_(458254)

unigram_tagger = _c_(458258, _a_(458256, _n_(458255, "nltk", lambda: nltk), "UnigramTagger"), _n_(458257, "brown_tagged_sents", lambda: brown_tagged_sents))
_l_(458259)
_c_(458263, _a_(458261, _n_(458260, "unigram_tagger", lambda: unigram_tagger), "tag"), _n_(458262, "brown_sents", lambda: brown_sents))
_l_(458264)
_c_(458268, _a_(458266, _n_(458265, "unigram_tagger", lambda: unigram_tagger), "evaluate"), _n_(458267, "brown_tagged_sents", lambda: brown_tagged_sents))
_l_(458269)