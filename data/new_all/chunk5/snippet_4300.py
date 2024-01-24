# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60084673/typeerror-unhashable-type-list-when-using-nltk-freqdist-on-pandas-series
#divide to words
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
tokenizer = _c_(705715, _n_(705714, "RegexpTokenizer", lambda: RegexpTokenizer), r'\w+')
_l_(705716)
_n_(705717, "df", lambda: df)['tokenized_sents'] = _c_(705722, _a_(705719, _n_(705718, "df", lambda: df)['Responses'], "apply"), _a_(705721, _n_(705720, "nltk", lambda: nltk), "word_tokenize"))
_l_(705723)