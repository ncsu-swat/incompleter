# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76192885/attributeerror-module-nltk-has-no-attribute-suggest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import nltk
  _l_(606909)

except ImportError:
  pass
_c_(606912, _a_(606911, _n_(606910, "nltk", lambda: nltk), "download"), 'udhr')
_l_(606913)
try:
  from nltk.corpus import udhr
  _l_(606915)

except ImportError:
  pass
_c_(606920, _a_(606919, _a_(606918, _a_(606917, _n_(606916, "nltk", lambda: nltk), "corpus"), "udhr"), "fileids"))
_l_(606921)
somali_text = _c_(606926, _a_(606925, _a_(606924, _a_(606923, _n_(606922, "nltk", lambda: nltk), "corpus"), "udhr"), "raw"), 'Somali-Latin1')
_l_(606927)
_c_(606930, _n_(606928, "len", lambda: len), _n_(606929, "somali_text", lambda: somali_text))
_l_(606931)
words = _c_(606934, _n_(606932, "list", lambda: list), _n_(606933, "somali_text", lambda: somali_text))
_l_(606935)
_c_(606938, _n_(606936, "print", lambda: print), _n_(606937, "words", lambda: words))
_l_(606939)
#dictionary that maps each word to its frequency

frequence_dict = {}
_l_(606940)
for word in _n_(606941, "words", lambda: words):
  _l_(606951)

  if _n_(606942, "word", lambda: word) not in _n_(606943, "frequence_dict", lambda: frequence_dict):
    _l_(606950)

    _n_(606944, "frequence_dict", lambda: frequence_dict)[_n_(606945, "word", lambda: word)] = 1
    _l_(606946)
  else:
    _n_(606947, "frequence_dict", lambda: frequence_dict)[_n_(606948, "word", lambda: word)] += 1
    _l_(606949)

#sorting the dictionary by frequency

sorted_frequency_dict = _c_(606957, _n_(606952, "sorted", lambda: sorted), _c_(606955, _a_(606954, _n_(606953, "frequence_dict", lambda: frequence_dict), "items")), key = lambda x: _n_(606956, "x", lambda: x)[1], reverse = True)
_l_(606958)

#misspelled words
misspelled_words = []
_l_(606959)
for word, frequency in _n_(606960, "sorted_frequency_dict", lambda: sorted_frequency_dict):
  _l_(606968)

  if _n_(606961, "frequency", lambda: frequency) < 3:
    _l_(606967)

    _c_(606965, _a_(606963, _n_(606962, "misspelled_words", lambda: misspelled_words), "append"), _n_(606964, "word", lambda: word))
    _l_(606966)
#corrections for misspelled words

corrections = {}
_l_(606969)
for misspelled_word in _n_(606970, "misspelled_words", lambda: misspelled_words):
  _l_(606978)

  _n_(606971, "corrections", lambda: corrections)[_n_(606972, "misspelled_word", lambda: misspelled_word)] = _c_(606976, _a_(606974, _n_(606973, "nltk", lambda: nltk), "suggest"), _n_(606975, "misspelled_word", lambda: misspelled_word))
  _l_(606977)