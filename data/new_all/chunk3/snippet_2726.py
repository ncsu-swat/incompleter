# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65366376/pytorch-typeerror-caught-typeerror-in-dataloader-worker-process-0
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
MAX_LEN = 160
_l_(553939)
class GPReviewDataset(_n_(553940, "Dataset", lambda: Dataset)):
  _l_(553993)

  def __init__(self, reviews, targets, tokenizer, max_len):
    _l_(553953)

    _n_(553941, "self", lambda: self).reviews = _n_(553942, "reviews", lambda: reviews)
    _l_(553943)
    _n_(553944, "self", lambda: self).targets = _n_(553945, "targets", lambda: targets)
    _l_(553946)
    _n_(553947, "self", lambda: self).tokenizer = _n_(553948, "tokenizer", lambda: tokenizer)
    _l_(553949)
    _n_(553950, "self", lambda: self).max_len = _n_(553951, "max_len", lambda: max_len)
    _l_(553952)
  def __len__(self):
    _l_(553959)

    aux = _c_(553957, _n_(553954, "len", lambda: len), _a_(553956, _n_(553955, "self", lambda: self), "reviews"))
    _l_(553958)
    return aux
  def __getitem__(self, item):
    _l_(553992)

    review = _c_(553964, _n_(553960, "str", lambda: str), _a_(553962, _n_(553961, "self", lambda: self), "reviews")[_n_(553963, "item", lambda: item)])
    _l_(553965)
    target = _a_(553967, _n_(553966, "self", lambda: self), "targets")[_n_(553968, "item", lambda: item)]
    _l_(553969)
    encoding = _c_(553976, _a_(553972, _a_(553971, _n_(553970, "self", lambda: self), "tokenizer"), "encode_plus"), _n_(553973, "review", lambda: review),
      add_special_tokens=True,
      max_length=_a_(553975, _n_(553974, "self", lambda: self), "max_len"),
      return_token_type_ids=False,
      pad_to_max_length=True,
      return_attention_mask=True,
      return_tensors='pt',
    )
    _l_(553977)
    aux = {
      'review_text': _n_(553978, "review", lambda: review),
      'input_ids': _c_(553981, _a_(553980, _n_(553979, "encoding", lambda: encoding)['input_ids'], "flatten")),
      'attention_mask': _c_(553984, _a_(553983, _n_(553982, "encoding", lambda: encoding)['attention_mask'], "flatten")),
      'targets': _c_(553990, _a_(553986, _n_(553985, "torch", lambda: torch), "tensor"), _n_(553987, "target", lambda: target), dtype=_a_(553989, _n_(553988, "torch", lambda: torch), "long"))
    }
    _l_(553991)
    return aux