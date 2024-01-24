# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61969056/i-want-to-solve-this-error-attributeerror-module-tokenization-has-no-attribut
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import tokenization
  _l_(692548)

except ImportError:
  pass
try:
  import codecs
  _l_(692550)

except ImportError:
  pass
try:
  import numpy as np
  _l_(692552)

except ImportError:
  pass

vocab_path = "./model_ch/vocab.txt"
_l_(692553)
max_seq_length = 128   
_l_(692554)   

file0 = "./task/message.tsv"
_l_(692555)
f0 = _c_(692559, _a_(692557, _n_(692556, "codecs", lambda: codecs), "open"), _n_(692558, "file0", lambda: file0), "r", "utf-8")
_l_(692560)
lines = _c_(692563, _a_(692562, _n_(692561, "f0", lambda: f0), "readlines"))
_l_(692564)
_c_(692567, _a_(692566, _n_(692565, "f0", lambda: f0), "close"))
_l_(692568)

len_file = _c_(692571, _n_(692569, "len", lambda: len), _n_(692570, "lines", lambda: lines))
_l_(692572)
count = _c_(692576, _a_(692574, _n_(692573, "np", lambda: np), "zeros"), [_n_(692575, "len_file", lambda: len_file)])
_l_(692577)
count0 = _c_(692581, _a_(692579, _n_(692578, "np", lambda: np), "zeros"), [_n_(692580, "len_file", lambda: len_file)])
_l_(692582)
my_tokenizer = _c_(692586, _a_(692584, _n_(692583, "tokenization", lambda: tokenization), "FullTokenizer"), vocab_file=_n_(692585, "vocab_path", lambda: vocab_path))
_l_(692587)

#file1 = "./task_data_ch/%s_count.tsv" % filename
file1 = "./task/message_count.tsv"
_l_(692588)
f1 = _c_(692592, _a_(692590, _n_(692589, "codecs", lambda: codecs), "open"), _n_(692591, "file1", lambda: file1), "w", "utf-8")
_l_(692593)
_c_(692596, _a_(692595, _n_(692594, "f1", lambda: f1), "write"), "%s\t%s\t%s\r\n" % ("label","count","count_truncated"))
_l_(692597)

for i in _c_(692600, _n_(692598, "range", lambda: range), 1,_n_(692599, "len_file", lambda: len_file)):
  _l_(692651)

  a = _n_(692601, "lines", lambda: lines)[_n_(692602, "i", lambda: i)]
  _l_(692603)
  a = _c_(692606, _a_(692605, _n_(692604, "a", lambda: a), "split"), "\t")
  _l_(692607)
  text = _n_(692608, "a", lambda: a)[1]
  _l_(692609)
  token = _c_(692613, _a_(692611, _n_(692610, "my_tokenizer", lambda: my_tokenizer), "tokenize"), _n_(692612, "text", lambda: text))
  _l_(692614)
  _c_(692617, _n_(692615, "print", lambda: print), _n_(692616, "token", lambda: token))
  _l_(692618)
  _n_(692619, "count", lambda: count)[_n_(692620, "i", lambda: i)] = _c_(692623, _n_(692621, "len", lambda: len), _n_(692622, "token", lambda: token)) + 2   # for [CLS] and [SEP]
  _l_(692624)   # for [CLS] and [SEP]
  if _n_(692625, "count", lambda: count)[_n_(692626, "i", lambda: i)] > _n_(692627, "max_seq_length", lambda: max_seq_length):
    _l_(692637)

    _n_(692628, "count0", lambda: count0)[_n_(692629, "i", lambda: i)] = _n_(692630, "max_seq_length", lambda: max_seq_length)
    _l_(692631)
  else:
    _n_(692632, "count0", lambda: count0)[_n_(692633, "i", lambda: i)] = _n_(692634, "count", lambda: count)[_n_(692635, "i", lambda: i)]
    _l_(692636)
  _c_(692649, _a_(692639, _n_(692638, "f1", lambda: f1), "write"), "%s\t%s\t%s\n" % (_n_(692640, "i", lambda: i)-1,_c_(692644, _n_(692641, "int", lambda: int), _n_(692642, "count", lambda: count)[_n_(692643, "i", lambda: i)]),_c_(692648, _n_(692645, "int", lambda: int), _n_(692646, "count0", lambda: count0)[_n_(692647, "i", lambda: i)])))
  _l_(692650)

sum0 = _c_(692657, _n_(692652, "int", lambda: int), _c_(692656, _a_(692654, _n_(692653, "np", lambda: np), "sum"), _n_(692655, "count0", lambda: count0)))
_l_(692658)
sum1 = _c_(692664, _n_(692659, "int", lambda: int), _c_(692663, _a_(692661, _n_(692660, "np", lambda: np), "sum"), _n_(692662, "count", lambda: count)))
_l_(692665)
_c_(692669, _n_(692666, "print", lambda: print), _n_(692667, "sum0", lambda: sum0), _n_(692668, "sum1", lambda: sum1))
_l_(692670)
_c_(692675, _n_(692671, "print", lambda: print), _c_(692674, _n_(692672, "int", lambda: int), _n_(692673, "len_file", lambda: len_file)-1))
_l_(692676)
_c_(692681, _a_(692678, _n_(692677, "f1", lambda: f1), "write"), "Total: %s, %s" % (_n_(692679, "sum1", lambda: sum1),_n_(692680, "sum0", lambda: sum0)))
_l_(692682)
_c_(692685, _a_(692684, _n_(692683, "f1", lambda: f1), "close"))
_l_(692686)