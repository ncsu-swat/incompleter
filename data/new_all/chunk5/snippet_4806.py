# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47741315/showing-typeerror-unhashable-type-list-while-using-it-in-nltk-freqdist-f
from __future__ import division
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(660861)
try:
  import operator
  _l_(660863)

except ImportError:
  pass
try:
  import nltk
  _l_(660865)

except ImportError:
  pass
try:
  import string
  _l_(660867)

except ImportError:
  pass

def isPunct(word):
  _l_(660875)

  aux = _c_(660870, _n_(660868, "len", lambda: len), _n_(660869, "word", lambda: word)) == 1 and _n_(660871, "word", lambda: word) in _a_(660873, _n_(660872, "string", lambda: string), "punctuation")
  _l_(660874)
  return aux

def isNumeric(word):
  _l_(660889)

  try:
    _l_(660888)

    _c_(660878, _n_(660876, "float", lambda: float), _n_(660877, "word", lambda: word)) if '.' in _n_(660879, "word", lambda: word) else _c_(660882, _n_(660880, "int", lambda: int), _n_(660881, "word", lambda: word))
    _l_(660883)
    aux = True
    _l_(660884)
    return aux
  except _n_(660885, "ValueError", lambda: ValueError):
    _l_(660887)

    aux = False
    _l_(660886)
    return aux

class KeyExt:
  _l_(661072)


  def __init__(self):
    _l_(660901)

    _n_(660890, "self", lambda: self).stopwords = _c_(660897, _n_(660891, "set", lambda: set), _c_(660896, _a_(660895, _a_(660894, _a_(660893, _n_(660892, "nltk", lambda: nltk), "corpus"), "stopwords"), "words")))
    _l_(660898)
    _n_(660899, "self", lambda: self).top_fraction = 1
    _l_(660900)

  def _generate_candidate_keywords(self, sentences):
    _l_(660943)

    phrase_list = []
    _l_(660902)
    for sentence in _n_(660903, "sentences", lambda: sentences):
      _l_(660940)

      words = _c_(660915, _n_(660904, "map", lambda: map), lambda x: "|" if _n_(660905, "x", lambda: x) in _a_(660907, _n_(660906, "self", lambda: self), "stopwords") else _n_(660908, "x", lambda: x), _c_(660914, _a_(660910, _n_(660909, "nltk", lambda: nltk), "word_tokenize"), _c_(660913, _a_(660912, _n_(660911, "sentence", lambda: sentence), "lower"))))
      _l_(660916)
      phrase = []
      _l_(660917)
      for word in _n_(660918, "words", lambda: words):
        _l_(660939)

        if _n_(660919, "word", lambda: word) == "|" or _c_(660922, _n_(660920, "isPunct", lambda: isPunct), _n_(660921, "word", lambda: word)):
          _l_(660938)

          if _c_(660925, _n_(660923, "len", lambda: len), _n_(660924, "phrase", lambda: phrase)) > 0:
            _l_(660932)

            _c_(660929, _a_(660927, _n_(660926, "phrase_list", lambda: phrase_list), "append"), _n_(660928, "phrase", lambda: phrase))
            _l_(660930)
            phrase = []
            _l_(660931)
        else:
          _c_(660936, _a_(660934, _n_(660933, "phrase", lambda: phrase), "append"), _n_(660935, "word", lambda: word))
          _l_(660937)
    aux = _n_(660941, "phrase_list", lambda: phrase_list)
    _l_(660942)
    return aux

  def _calculate_word_scores(self, phrase_list):
    _l_(660999)

    word_freq = _c_(660946, _a_(660945, _n_(660944, "nltk", lambda: nltk), "FreqDist"))
    _l_(660947)
    word_degree = _c_(660950, _a_(660949, _n_(660948, "nltk", lambda: nltk), "FreqDist"))
    _l_(660951)
    for phrase in _n_(660952, "phrase_list", lambda: phrase_list):
      _l_(660973)

      degree = [_n_(660953, "x", lambda: x) for x in _n_(660954, "phrase", lambda: phrase) if not _c_(660957, _n_(660955, "isNumeric", lambda: isNumeric), _n_(660956, "x", lambda: x))] 
      _l_(660958) 
      for word in _n_(660959, "phrase", lambda: phrase):
        _l_(660972)

        _n_(660960, "word_freq", lambda: word_freq)[_n_(660961, "word", lambda: word)]=_n_(660962, "word_freq", lambda: word_freq)[_n_(660963, "word", lambda: word)]+1
        _l_(660964)
        _n_(660965, "word_degree", lambda: word_degree)[_n_(660966, "word", lambda: word), _n_(660967, "degree", lambda: degree)]=_n_(660968, "word_degree", lambda: word_degree)[_n_(660969, "word", lambda: word), _n_(660970, "degree", lambda: degree)]+1 
        _l_(660971) 
    for word in _c_(660976, _a_(660975, _n_(660974, "word_freq", lambda: word_freq), "keys")):
      _l_(660984)

      _n_(660977, "word_degree", lambda: word_degree)[_n_(660978, "word", lambda: word)] = _n_(660979, "word_degree", lambda: word_degree)[_n_(660980, "word", lambda: word)] + _n_(660981, "word_freq", lambda: word_freq)[_n_(660982, "word", lambda: word)] 
      _l_(660983) 
    word_scores = {}
    _l_(660985)
    for word in _c_(660988, _a_(660987, _n_(660986, "word_freq", lambda: word_freq), "keys")):
      _l_(660996)

      _n_(660989, "word_scores", lambda: word_scores)[_n_(660990, "word", lambda: word)] = _n_(660991, "word_degree", lambda: word_degree)[_n_(660992, "word", lambda: word)] / _n_(660993, "word_freq", lambda: word_freq)[_n_(660994, "word", lambda: word)]
      _l_(660995)
    aux = _n_(660997, "word_scores", lambda: word_scores)
    _l_(660998)
    return aux

  def _calculate_phrase_scores(self, phrase_list, word_scores):
    _l_(661017)

    phrase_scores = {}
    _l_(661000)
    for phrase in _n_(661001, "phrase_list", lambda: phrase_list):
      _l_(661014)

      phrase_score = 0
      _l_(661002)
      for word in _n_(661003, "phrase", lambda: phrase):
        _l_(661007)

        phrase_score += _n_(661004, "word_scores", lambda: word_scores)[_n_(661005, "word", lambda: word)]
        _l_(661006)
      _n_(661008, "phrase_scores", lambda: phrase_scores)[_c_(661011, _a_(661009, " ", "join"), _n_(661010, "phrase", lambda: phrase))] = _n_(661012, "phrase_score", lambda: phrase_score)
      _l_(661013)
    aux = _n_(661015, "phrase_scores", lambda: phrase_scores)
    _l_(661016)
    return aux

  def extract(self, text, incl_scores=False):
    _l_(661071)

    sentences = _c_(661021, _a_(661019, _n_(661018, "nltk", lambda: nltk), "sent_tokenize"), _n_(661020, "text", lambda: text))
    _l_(661022)
    phrase_list = _c_(661026, _a_(661024, _n_(661023, "self", lambda: self), "_generate_candidate_keywords"), _n_(661025, "sentences", lambda: sentences))
    _l_(661027)
    word_scores = _c_(661031, _a_(661029, _n_(661028, "self", lambda: self), "_calculate_word_scores"), _n_(661030, "phrase_list", lambda: phrase_list))
    _l_(661032)
    phrase_scores = _c_(661037, _a_(661034, _n_(661033, "self", lambda: self), "_calculate_phrase_scores"), _n_(661035, "phrase_list", lambda: phrase_list), _n_(661036, "word_scores", lambda: word_scores))
    _l_(661038)
    sorted_phrase_scores = _c_(661046, _n_(661039, "sorted", lambda: sorted), _c_(661042, _a_(661041, _n_(661040, "phrase_scores", lambda: phrase_scores), "items")), key=_c_(661045, _a_(661044, _n_(661043, "operator", lambda: operator), "itemgetter"), 1), reverse=True)
    _l_(661047)
    n_phrases = _c_(661050, _n_(661048, "len", lambda: len), _n_(661049, "sorted_phrase_scores", lambda: sorted_phrase_scores))
    _l_(661051)
    if _n_(661052, "incl_scores", lambda: incl_scores):
      _l_(661070)

      aux = _n_(661053, "sorted_phrase_scores", lambda: sorted_phrase_scores)[0:_c_(661058, _n_(661054, "int", lambda: int), _n_(661055, "n_phrases", lambda: n_phrases)/_a_(661057, _n_(661056, "self", lambda: self), "top_fraction"))]
      _l_(661059)
      return aux
    else:
      aux = _c_(661068, _n_(661060, "map", lambda: map), lambda x: _n_(661061, "x", lambda: x)[0],
        _n_(661062, "sorted_phrase_scores", lambda: sorted_phrase_scores)[0:_c_(661067, _n_(661063, "int", lambda: int), _n_(661064, "n_phrases", lambda: n_phrases)/_a_(661066, _n_(661065, "self", lambda: self), "top_fraction"))])
      _l_(661069)
      return aux

def test():
  _l_(661088)

  search=_c_(661074, _n_(661073, "input", lambda: input), "Enter Text: ")
  _l_(661075)
  ke = _c_(661077, _n_(661076, "KeyExt", lambda: KeyExt))
  _l_(661078)
  keywords = _c_(661082, _a_(661080, _n_(661079, "ke", lambda: ke), "extract"), _n_(661081, "search", lambda: search), incl_scores=True)
  _l_(661083)
  _c_(661086, _n_(661084, "print", lambda: print), _n_(661085, "keywords", lambda: keywords))
  _l_(661087)

if _n_(661089, "__name__", lambda: __name__) == "__main__":
  _l_(661093)

  _c_(661091, _n_(661090, "test", lambda: test))
  _l_(661092)