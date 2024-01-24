# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70621634/typeerror-forward-got-an-unexpected-keyword-argument-input-ids
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import torch.nn as nn
    _l_(385314)

except ImportError:
    pass
try:
    from transformers import AutoModel
    _l_(385316)

except ImportError:
    pass

class PosModel(_a_(385318, _n_(385317, "nn", lambda: nn), "Module")):
    _l_(385361)

    def __init__(self):
        _l_(385341)

        _c_(385323, _a_(385322, _n_(385319, "super", lambda: super)(_n_(385320, "PosModel", lambda: PosModel), _n_(385321, "self", lambda: self)), "__init__"))
        _l_(385324)
        
        _n_(385325, "self", lambda: self).base_model = _c_(385329, _a_(385328, _a_(385327, _n_(385326, "tr", lambda: tr), "RobertaForSequenceClassification"), "from_pretrained"), '/home/pc/unbiased_toxic_roberta')
        _l_(385330)
        _n_(385331, "self", lambda: self).dropout = _c_(385334, _a_(385333, _n_(385332, "nn", lambda: nn), "Dropout"), 0.5)
        _l_(385335)
        _n_(385336, "self", lambda: self).linear = _c_(385339, _a_(385338, _n_(385337, "nn", lambda: nn), "Linear"), 768, 2) # output features from bert is 768 and 2 is ur number of labels
        _l_(385340) # output features from bert is 768 and 2 is ur number of labels
    def forward(self, input_ids, attn_mask):
        _l_(385360)

        outputs = _c_(385346, _a_(385343, _n_(385342, "self", lambda: self), "base_model"), _n_(385344, "input_ids", lambda: input_ids), attention_mask=_n_(385345, "attn_mask", lambda: attn_mask))
        _l_(385347)
        # You write you new head here
        outputs = _c_(385351, _a_(385349, _n_(385348, "self", lambda: self), "dropout"), _n_(385350, "outputs", lambda: outputs)[0])
        _l_(385352)
        outputs = _c_(385356, _a_(385354, _n_(385353, "self", lambda: self), "linear"), _n_(385355, "outputs", lambda: outputs))
        _l_(385357)
        aux = _n_(385358, "outputs", lambda: outputs)
        _l_(385359)
        
        return aux

model = _c_(385363, _n_(385362, "PosModel", lambda: PosModel))
_l_(385364)

_c_(385367, _n_(385365, "print", lambda: print), _n_(385366, "model", lambda: model))
_l_(385368)