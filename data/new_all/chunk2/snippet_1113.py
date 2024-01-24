# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65373407/fastai-text-nameerror-name-basetokenizer-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from fastai.text import *
    _l_(457993)

except ImportError:
    pass
try:
    from fastai.metrics import *
    _l_(457995)

except ImportError:
    pass
try:
    from transformers import RobertaTokenizer
    _l_(457997)

except ImportError:
    pass

class FastAiRobertaTokenizer(_n_(457998, "BaseTokenizer", lambda: BaseTokenizer)):
    _l_(458026)

    """Wrapper around RobertaTokenizer to be compatible with fastai"""
    def __init__(self, tokenizer: _n_(457999, "RobertaTokenizer", lambda: RobertaTokenizer), max_seq_len: _n_(458000, "int", lambda: int)=128, **kwargs):
        _l_(458007)

        _n_(458001, "self", lambda: self)._pretrained_tokenizer = _n_(458002, "tokenizer", lambda: tokenizer)
        _l_(458003)
        _n_(458004, "self", lambda: self).max_seq_len = _n_(458005, "max_seq_len", lambda: max_seq_len) 
        _l_(458006) 
    def __call__(self, *args, **kwargs):
        _l_(458010)

        aux = _n_(458008, "self", lambda: self) 
        _l_(458009) 
        return aux 
    def tokenizer(self, t:_n_(458011, "str", lambda: str)) -> List[_n_(458012, "str", lambda: str)]:
        _l_(458025)

        """Adds Roberta bos and eos tokens and limits the maximum sequence length""" 
        aux = [_a_(458014, _n_(458013, "config", lambda: config), "start_tok")] + _c_(458019, _a_(458017, _a_(458016, _n_(458015, "self", lambda: self), "_pretrained_tokenizer"), "tokenize"), _n_(458018, "t", lambda: t))[:_a_(458021, _n_(458020, "self", lambda: self), "max_seq_len") - 2] + [_a_(458023, _n_(458022, "config", lambda: config), "end_tok")]
        _l_(458024)
        return aux