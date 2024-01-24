# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63164902/getting-typeerror-expected-int32-got-none-of-type-nonetype-instead
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def preprocess_sentence(w):
  _l_(577477)

  # w = unicode_to_ascii(w.lower().strip())
  w = _c_(577457, _a_(577455, _n_(577454, "re", lambda: re), "sub"), r"([?.!,¿])", r" \1 ", _n_(577456, "w", lambda: w))
  _l_(577458)
  w = _c_(577462, _a_(577460, _n_(577459, "re", lambda: re), "sub"), r'[" "]+', " ", _n_(577461, "w", lambda: w))
  _l_(577463)
  w = _c_(577467, _a_(577465, _n_(577464, "re", lambda: re), "sub"), r"[^a-zA-Z?.!,¿]+", " ", _n_(577466, "w", lambda: w))
  _l_(577468)
  w = _c_(577471, _a_(577470, _n_(577469, "w", lambda: w), "strip"))
  _l_(577472)
  w = '<start> ' + _n_(577473, "w", lambda: w) + ' <end>'
  _l_(577474)
  aux = _n_(577475, "w", lambda: w)  
  _l_(577476)  
  return aux  
def create_dataset(path, num_examples):
  _l_(577506)

  lines = _c_(577487, _a_(577486, _c_(577485, _a_(577484, _c_(577483, _a_(577482, _c_(577481, _a_(577479, _n_(577478, "io", lambda: io), "open"), _n_(577480, "path", lambda: path), encoding='UTF-8'), "read")), "strip")), "split"), '\n')
  _l_(577488)
  # lines1 = lines[330000:]
  # lines = lines[0:323386]+lines1

  word_pairs = [[_c_(577491, _n_(577489, "preprocess_sentence", lambda: preprocess_sentence), _n_(577490, "w", lambda: w)) for w in _c_(577494, _a_(577493, _n_(577492, "l", lambda: l), "split"), '\t')]  for l in _n_(577495, "lines", lambda: lines)[:_n_(577496, "num_examples", lambda: num_examples)]]
  _l_(577497)
  word_pairs = [[_n_(577498, "i", lambda: i)[0],_n_(577499, "i", lambda: i)[1]] for i in _n_(577500, "word_pairs", lambda: word_pairs)]
  _l_(577501)
  aux = _c_(577504, _n_(577502, "zip", lambda: zip), *_n_(577503, "word_pairs", lambda: word_pairs))
  _l_(577505)
  return aux

def tokenize(lang):
  _l_(577535)

  lang_tokenizer = _c_(577512, _a_(577511, _a_(577510, _a_(577509, _a_(577508, _n_(577507, "tf", lambda: tf), "keras"), "preprocessing"), "text"), "Tokenizer"), filters='')
  _l_(577513)
  _c_(577517, _a_(577515, _n_(577514, "lang_tokenizer", lambda: lang_tokenizer), "fit_on_texts"), _n_(577516, "lang", lambda: lang))
  _l_(577518)

  tensor = _c_(577522, _a_(577520, _n_(577519, "lang_tokenizer", lambda: lang_tokenizer), "texts_to_sequences"), _n_(577521, "lang", lambda: lang))
  _l_(577523)

  tensor = _c_(577530, _a_(577528, _a_(577527, _a_(577526, _a_(577525, _n_(577524, "tf", lambda: tf), "keras"), "preprocessing"), "sequence"), "pad_sequences"), _n_(577529, "tensor", lambda: tensor),padding='post')
  _l_(577531)
  aux = _n_(577532, "tensor", lambda: tensor), _n_(577533, "lang_tokenizer", lambda: lang_tokenizer)
  _l_(577534)
  return aux

def load_dataset(path, num_examples=None):
  _l_(577556)

  # creating cleaned input, output pairs
  targ_lang, inp_lang = _c_(577539, _n_(577536, "create_dataset", lambda: create_dataset), _n_(577537, "path", lambda: path), _n_(577538, "num_examples", lambda: num_examples))
  _l_(577540)

  input_tensor, inp_lang_tokenizer = _c_(577543, _n_(577541, "tokenize", lambda: tokenize), _n_(577542, "inp_lang", lambda: inp_lang))
  _l_(577544)
  target_tensor, targ_lang_tokenizer = _c_(577547, _n_(577545, "tokenize", lambda: tokenize), _n_(577546, "targ_lang", lambda: targ_lang))
  _l_(577548)
  aux = _n_(577549, "input_tensor", lambda: input_tensor), _n_(577550, "target_tensor", lambda: target_tensor), _n_(577551, "inp_lang_tokenizer", lambda: inp_lang_tokenizer), _n_(577552, "targ_lang_tokenizer", lambda: targ_lang_tokenizer),_n_(577553, "targ_lang", lambda: targ_lang),_n_(577554, "inp_lang", lambda: inp_lang)
  _l_(577555)

  return aux

# Try experimenting with the size of that dataset
num_examples = None
_l_(577557)
input_tensor, target_tensor, inp_lang, targ_lang,targ_lang_text,inp_lang_text = _c_(577561, _n_(577558, "load_dataset", lambda: load_dataset), _n_(577559, "path", lambda: path), _n_(577560, "num_examples", lambda: num_examples))
_l_(577562)

# Calculate max_length of the target tensors
max_length_targ, max_length_inp = _a_(577564, _n_(577563, "target_tensor", lambda: target_tensor), "shape")[1], _a_(577566, _n_(577565, "input_tensor", lambda: input_tensor), "shape")[1]
_l_(577567)
_n_(577568, "max_length_targ", lambda: max_length_targ),_n_(577569, "max_length_inp", lambda: max_length_inp)
_l_(577570)

input_tensor_train, input_tensor_val, target_tensor_train, target_tensor_val = _c_(577574, _n_(577571, "train_test_split", lambda: train_test_split), _n_(577572, "input_tensor", lambda: input_tensor), _n_(577573, "target_tensor", lambda: target_tensor), test_size=0.2)
_l_(577575)